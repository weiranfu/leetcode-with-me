---
title: Medium | 3Sum Closest 16
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-07-06 19:28:46
---

Given an array `nums` of *n* integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

[Leetcode](https://leetcode.com/problems/3sum-closest/)

<!--more-->

**Example 1:**

```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

---

#### Tricky 

Sort the array. Fix the first number and use two pointers to check the `sum = nums[i] + nums[l] + nums[r]` with `target`.

---

#### Standard solution  

```java
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        Arrays.sort(nums);
        int diff = Integer.MAX_VALUE;
        int res = 0;
        for (int i = 0; i < n; i++) {
            int l = i + 1, r = n - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == target) {
                    return target;
                }
                if (Math.abs(target - sum) < Math.abs(diff)) {
                    diff = Math.abs(target - sum);
                    res = sum;
                }
                if (sum < target) {
                    l++;
                } else {
                    r--;
                }
            }
        }
        return res;
    }
}
```

T: O(n^2)			S: O(1)