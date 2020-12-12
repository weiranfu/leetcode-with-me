---
title: Medium | Search in Rotated Sorted Array II
tags:
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-05-17 00:23:03
---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,0,1,2,2,5,6]` might become `[2,5,6,0,0,1,2]`).

You are given a target value to search. If found in the array return `true`, otherwise return `false`.

There may be duplicate integers in the array.

[Leetcode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

<!--more-->

**Example 1:**

```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

**Example 2:**

```
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```

**Follow up:** 

[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

---

#### Tricky 

The tricky is when the head and tail are same, how to determine whether the target / mid falls in left part or right part.

For example `nums = [1, 3, 1, 1, 1], target = 3`. The `mid = 1`, `nums[head] == nums[tail] == 1`. mid could be in left part and right part.

The solution is to shrink the tail until tail value is not equal to head value.

---

#### First solution 

```java
class Solution {
    public boolean search(int[] nums, int target) {
        if (nums == null || nums.length == 0) return false;
        int n = nums.length;
        while (n > 0 && nums[n - 1] == nums[0]) n--; // remove duplicates
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return true;
            if (nums[mid] > nums[n - 1]) {
                if (target > nums[n - 1]) {
                    if (nums[mid] > target) {
                        r = mid - 1;
                    } else {
                        l = mid + 1;
                    }
                } else {
                    l = mid + 1;
                }
            } else {
                if (target > nums[n - 1]) {
                    r = mid - 1;
                } else {
                    if (nums[mid] > target) {
                        r = mid - 1;
                    } else {
                        l = mid + 1;
                    }
                }
            }
        }
        return nums[l] == target ? true : false;
    }
}
```

T: O(logn)		worst case: O(n) when all elements are same

S: O(1)