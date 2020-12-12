---
title: Medium | Find First and Last Position of Element in Sorted Array 34
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - Binary Search
date: 2020-01-29 23:36:00
---

Given an array of integers `nums` sorted in ascending order, find the starting and ending position of a given `target` value.

Your algorithm's runtime complexity must be in the order of *O*(log *n*).

If the target is not found in the array, return `[-1, -1]`.

[Leetcode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

<!--more-->

**Example 1:**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

**Example 2:**

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

---

#### Binary Search

Find lower bound firstly, if we can't find it, just return [-1, -1]

```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums == null || nums.length == 0) return new int[]{-1, -1};
        int n = nums.length;
        int[] res = new int[]{-1, -1};
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] >= target) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        if (nums[l] != target) return res;		// find lower bound first
        res[0] = l;
        l = 0; r = n - 1;
        while (l < r) {
            int mid = l + (r - l + 1) / 2;
            if (nums[mid] <= target) {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        res[1] = l;
        return res;
    }
}
```

T: O(logn)		S: O(1)

---

#### lower_bound function

There're two common function in binary search.

lower_bound(): find the first item in sorted array that is **greater than or equal to** target value.

upper_bound(): find the first item in sorted array that is **greater than** target value.

Actually, we can only use lower_bound() function to find all targets.

`upper_bound(target) == lower_bound(target + 1) - 1`.

```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int n = nums.length;
        if (n == 0) return new int[]{-1, -1};
        int[] res = new int[]{-1, -1};
        int lower = lowerBound(nums, 0, n, target);
	      // Corner case: high == n, don't find value
        if (lower == n || nums[lower] != target) {      
            return res;
        } else {
            res[0] = lower;
        }
        int upper = lowerBound(nums, 0, n, target + 1);
        res[1] = upper - 1;
        return res;
    }
    private int lowerBound(int[] nums, int low, int high, int target) {
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] < target) {      // if smaller, then move forward.         
                low = mid + 1;
            } else {
                high = mid;              
            }
        }
        return high;       
    }
}
```

T: O(logn)		S: O(1)