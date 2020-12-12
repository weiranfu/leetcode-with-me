---
title: Hard | Kth Smallest Number in Multiplication Table 668
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-06-28 16:03:53
---

Nearly every one have used the [Multiplication Table](https://en.wikipedia.org/wiki/Multiplication_table). But could you find out the `k-th` smallest number quickly from the multiplication table?

Given the height `m` and the length `n` of a `m * n` Multiplication Table, and a positive integer `k`, you need to return the `k-th` smallest number in this table.

[Leetcode](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/)

<!--more-->

**Example 1:**

```
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
```

**Example 2:**

```
Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
```

---

#### Tricky 

1. Priority Queue + merge K sorted list.    (LTE!!!!)

   ```java
   class Solution {
       public int findKthNumber(int m, int n, int k) {
           PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] * a[1] - b[0] * b[1]);
           for (int i = 1; i <= Math.min(m, k); i++) {
               pq.add(new int[]{i, 1});
           }
           while (!pq.isEmpty()) {
               int[] info = pq.poll();
               int i = info[0];
               int j = info[1];
               k--;
               if (k == 0) return i * j;
               if (j + 1 <= n) pq.add(new int[]{i, j + 1});
           }
           return -1;
       }
   }
   ```

   T: O(klog(Min(m, k)))			S: O(Min(m, k))

2. Binary Search

   Since we can easily count how many numbers in table that no more than `val`.

   We could use binary search to find `kth` number, because the monotonic relationship between number of valid numbers in table and max value.

   We could binary search the value range of number.

   We will return the `lower` and `upper` during binary search.

   ```java
   class Solution {
       public int findKthNumber(int m, int n, int k) {
           int l = 1 * 1, r = m * n + 1;
           while (l < r) {
               int mid = l + (r - l) / 2;
               int[] info = count(m, n, mid);
               if (info[0] >= k) {
                   r = info[1];
               } else {
                   l = info[2];
               }
           }
           return l;
       }
       
       private int[] count(int m, int n, int val) {
           int[] res = new int[3];
           int i = m, j = 1;
           int lower = 1, upper = m * n;
           int cnt = 0;
           while (i >= 1 && j <= n) {
               if (i * j <= val) {
                   lower = Math.max(lower, i * j);
                   cnt += i;
                   j++;
               } else {
                   upper = Math.min(upper, i * j);
                   i--;
               }
           }
           res[0] = cnt;
           res[1] = lower;
           res[2] = upper;
           return res;
       }
   }
   ```

   T: O((m + n) * logMax)		S: O(1)

