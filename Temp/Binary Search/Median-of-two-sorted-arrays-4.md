---
title: Hard | Median of Two Sorted Arrays 4
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-07-30 18:23:58
---

There are two sorted arrays **nums1** and **nums2** of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume **nums1** and **nums2** cannot be both empty.

[Leetcode](https://leetcode.com/problems/median-of-two-sorted-arrays/)

<!--more-->

**Example 1:**

```
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

**Example 2:**

```
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

---

首先，我们理解什么中位数：指的是该数左右个数相等。

`odd : [1,| 2 |,3]`，`2` 就是这个数组的中位数，左右两边都只要 1 位；

`even: [1,| 2, 3 |,4]`，`2`,`3` 就是这个数组的中位数，左右两边 1 位；

`median1 = (m + n) / 2`

`median2 = (m + n + 1) / 2`

那么，现在我们有两个数组：

`num1: [a1,a2,a3,…an]`

`nums2: [b1,b2,b3,…bn]`

`[nums1[:m1],nums2[:n1] | nums1[m1:], nums2[n1:]]`

只要保证左右两边 个数 相同，中位数就在 | 这个边界旁边产生。

**How to get `median1` and `median2`?**

**`median1 = max(nums1[m1-1], nums2[n1-1]) `**

**`median2 = min(nums1[m1], nums2[n1])`**

1. Brute Force

   We keep two pointers `a` and `b` to traverse two arrays like merge sort.

   They can devide two arrays into 4 parts. `nums1[] -> m == m1 + m2`  `nums2[] -> n == n1 + n2`

   `if (m1 + m2) == (m + n + 1) / 2`, it means we find the median.

   Why we use `(m + n + 1) / 2` here? 这样保证个数为奇数时中位数一定落在左边

   ```java
   class Solution {
       public double findMedianSortedArrays(int[] nums1, int[] nums2) {
           int m = nums1.length, n = nums2.length;
           int a = 0, b = 0;
           while (a < m || b < n) {
               if (a + b == (m + n + 1) / 2) break;
               int x = a < m ? nums1[a] : Integer.MAX_VALUE;
               int y = b < n ? nums2[b] : Integer.MAX_VALUE;
               if (x <= y) a++; 
               else b++;
           }
           int median1 = Math.max(a > 0 ? nums1[a - 1] : Integer.MIN_VALUE, 
                                  b > 0 ? nums2[b - 1] : Integer.MIN_VALUE);
           if ((m + n) % 2 != 0) return (double)median1;
           int median2 = Math.min(a < m ? nums1[a] : Integer.MAX_VALUE, 
                                  b < n ? nums2[b] : Integer.MAX_VALUE);
           return (median1 + median2) * 0.5;
       }
   }
   ```

   T: O(m + n)		S: O(1)

2. Binary Search

   We could use binary Search to divide two arrays.

   Because `m1 + n1 == (m + n + 1) / 2`, if we have determined `m1`, we could get `n1` by `n1 = (m + n + 1) / 2 - m1`.

   So we could perform binary search to find `m1`.

   Always make sure that `m` array's length is smaller than `n` array's length, so that we will never overflow the boundary when computing `n1 = (m + n + 1) / 2 - m1`

   当 `[ [a1],[b1,b2,b3] | [a2,..an],[b4,...bn] ]`

   **How to determine such a divide is a valid divide?**

   We need to make sure `a1 < a2 && a1 < b4` and `b3 < a2 && b3 < b4`

   即 `L1 <= R2 && L2 <= R1`, if we find this condition is satisfied, we can return the division.

   if `L1 > R2`, `L1` is too large, `r = mid - 1`

   if `l2 > R2`, `L2` is too large, `l = mid + 1`

   ```java
   class Solution {
       public double findMedianSortedArrays(int[] nums1, int[] nums2) {
           int m = nums1.length, n = nums2.length;
           if (m > n) return findMedianSortedArrays(nums2, nums1); // make sure m > n
           
           int l = 0, r = m - 1;
           int target = (m + n + 1) / 2;
           while (l <= m) {
               int m1 = l + (r - l) / 2;
               int m2 = target - m1;
               int L1 = m1 > 0 ? nums1[m1 - 1] : Integer.MIN_VALUE;
               int L2 = m2 > 0 ? nums2[m2 - 1] : Integer.MIN_VALUE;
               int R1 = m1 < m ? nums1[m1] : Integer.MAX_VALUE;
               int R2 = m2 < n ? nums2[m2] : Integer.MAX_VALUE;
               if (L1 <= R2 && L2 <= R1) {
                   if ((m + n) % 2 == 1) {
                       return (double)Math.max(L1, L2);
                   } else {
                       return (Math.max(L1, L2) + Math.min(R1, R2)) * 0.5;
                   }
               } else if (L1 > R2) {
                   r = m1 - 1;
               } else { // L2 > R1
                   l = m1 + 1; 
               }
           }
           return -1;
       }
   }
   ```

   T: O(log(m + n))				S: O(1)

   

