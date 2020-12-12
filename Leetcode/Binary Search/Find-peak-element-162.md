---
title: Medium | Find Peak Element 162
tags:
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-06-01 21:15:48
---

A peak element is an element that is greater than its neighbors.

Given an input array `nums`, where `nums[i] ≠ nums[i+1]`, find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that `nums[-1] = nums[n] = -∞`.

Your solution should be in logarithmic complexity.

[Leetcode](https://leetcode.com/problems/find-peak-element/)

<!--more-->

**Example:**

```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

---

#### Tricky 

How to use binary search to search a peak?

**We could assume that the a peak must exist, cause `nums[-1] = nums[n] = -∞`, so we could look at `nums[mid]` and `nums[mid + 1]` to figure out whether they're on rising slope or falling slope**

`if (nums[mid1] <= nums[mid + 1])`, we could assume `mid1` and `mid2` are on rising slope.

`if (nums[mid1] > nums[mid + 1])`, we could assume `mid1` and `mid2` are on falling slope.

---

#### Standard solution  

```java
class Solution {
    public int findPeakElement(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        int n = nums.length;
        int l = 0, r = n - 1;
        while (l < r) {
            int mid1 = l + (r - l) / 2;
            int mid2 = mid1 + 1;
            if (nums[mid1] >= nums[mid2]) { // falling slope
                r = mid1;
            } else {
                l = mid2;
            }
        }
        return l;
    }
}
```

T: O(logn)		S: O(1)

