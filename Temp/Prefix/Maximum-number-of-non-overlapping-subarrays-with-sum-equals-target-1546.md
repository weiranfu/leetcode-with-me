---
title: Medium | Maximum Number of Non-Overlapping Subarrays with Sum Equals Target 1546
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Prefix	
date: 2020-08-21 15:17:45
---

Given an array `nums` and an integer `target`.

Return the maximum number of **non-empty** **non-overlapping** subarrays such that the sum of values in each subarray is equal to `target`.

[Leetcode](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)

<!--more-->

**Example 1:**

```
Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).
```

**Example 2:**

```
Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.
```

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `0 <= target <= 10^6`

---

#### Standard solution  

Prefix sum and use a map to record the max number of non-overlapping subarrays.

```java
class Solution {
    public int maxNonOverlapping(int[] nums, int target) {
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 0);
        int sum = 0, max = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            if (map.containsKey(sum - target)) {
                max = Math.max(max, map.get(sum - target) + 1);
            }
            map.put(sum, max);
        }
        return max;
    }
}
```

T: O(n)			S: O(n)

