---
title: Medium | Maximum Length of Subarray with Positive Product 1567
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-09-03 14:56:50
---

Given an array of integers `nums`, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return *the maximum length of a subarray with positive product*.

[Leetcode](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/)

<!--more-->

**Example 1:**

```
Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
```

**Example 2:**

```
Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
```

**Follow up**

[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

---

#### Record first occurrence

Consider all subarrays `a[:i]`

if there're even number of negatives, the valid length will be `i`

if there're odd number of negatives, the valid length will be `i - neg` (`neg` is the first occurrence of negative)

Then we can use `pos` to record the first occurrence of positive and `neg` to record the first occurrence of negative.

**Use `sign == 1` to detect the number of negatives**

```java
class Solution {
    public int getMaxLen(int[] nums) {
        int n = nums.length;
        int res = 0;
        int pos = -1, neg = n + 1;			// init for pos and neg
        int sign = 1;
        for (int i = 0; i < n; i++) {
            if (nums[i] < 0) {
                sign *= -1;
                if (neg == n + 1) neg = i;
            } else if (nums[i] == 0) {
                sign = 1;
                pos = i;
                neg = n + 1;
            }
            if (sign == 1) res = Math.max(res, i - pos); // even number of negatives
            else res = Math.max(res, i - neg); // odd number of negatives
        }
        return res;
    }
}
```

T: O(n)		S: O(1)

---

#### Count the number

Use `a` and `b` to count the length of positive subarray and negative subarray.

if we meet a negative number, if `b > 0`, `a = b + 1` else `a = 0`.

```java
class Solution {
    public int getMaxLen(int[] nums) {
        int n = nums.length;
        int res = 0;
        int a = 0, b = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) {
                a++;
                if (b > 0) b++;
            } else if (nums[i] < 0) {
                int tmp = a;
                if (b > 0) a = b + 1;	// concatenate a to b
                else a = 0;						// clear a
                b = tmp + 1;
            } else {
                a = b = 0;
            }
            res = Math.max(res, a);
        }
        return res;
    }
}
```

T: O(n)			S: O(1)



