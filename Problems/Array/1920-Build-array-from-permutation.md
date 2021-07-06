---
title: Easy | 1920 Build Array From Permutation
categories:
  - LeetCode
  - Array
date: 2021-07-06 02:26:00
---

# 1920 Build Array From Permutation

Given a **zero-based permutation** `nums` (**0-indexed**), build an array `ans` of the **same length** where `ans[i] = nums[nums[i]]` for each `0 <= i < nums.length` and return it.

A **zero-based permutation** `nums` is an array of **distinct** integers from `0` to `nums.length - 1` (**inclusive**).

[Leetcode](https://leetcode.com/problems/build-array-from-permutation/)

<!--more-->

**Follow up:** come up a solution with O(1) space complexity.

---

#### Standard Solution

We need to record the previous value while updating new value.

Since all numbers are smaller than *n*, we can save value in format **a + nb**, **a** means previous value, **b** means new value.

```java
class Solution {
    public int[] buildArray(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            // save value in format of a + nb
            nums[i] = nums[i] + (nums[nums[i]] % n) * n;
        }
        for (int i = 0; i < n; i++) {
            nums[i] = nums[i] / n;
        }
        return nums;
    }
}
```

T: O(n)		S: O(1)

