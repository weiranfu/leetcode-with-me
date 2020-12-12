---
title: Easy | Range Sum Query - Immutable 303
tags:
  - common
categories:
  - Leetcode
  - Array
date: 2020-06-18 04:52:48
---

Given an integer array *nums*, find the sum of the elements between indices *i* and *j* (*i* ≤ *j*), inclusive.

[Leetcode](https://leetcode.com/problems/range-sum-query-immutable/)

<!--more-->

**Example:**

```
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

**Note:**

1. You may assume that the array does not change.
2. There are many calls to *sumRange* function.

**Follow up:** 

[Range Sum Query - Immutable](https://aranne.github.io/2020/06/18/Range-sum-query-immutable-303/#more)	

[Range Sum Query - Mutable](https://aranne.github.io/2020/06/18/Range-sum-query-mutable-307/#more)

[Range Sum Query 2D - Immutable](https://aranne.github.io/2020/06/18/Range-sum-query-2D-immutable/#more)

[Range Sum Query 2D - Mutable](https://aranne.github.io/2020/06/18/Range-sum-query-2D-mutable-308/#more)

---

#### Standard solution  

Use `preSum` to store the sum of subarrays.

```java
class NumArray {
    
    int[] preSum;

    public NumArray(int[] nums) {
        if (nums == null || nums.length == 0) return;
        int n = nums.length;
        preSum = new int[n];
        preSum[0] = nums[0];
        for (int i = 1; i < n; i++) {
            preSum[i] = preSum[i - 1] + nums[i];
        }
    }
    
    public int sumRange(int i, int j) {
        if (i == 0) return preSum[j];
        else return preSum[j] - preSum[i - 1];
    }
}
```

T: O(1)			S: O(n)

