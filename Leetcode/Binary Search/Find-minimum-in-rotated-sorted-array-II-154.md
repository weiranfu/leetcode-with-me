---
title: Medium | Find Minimum in Rotated Sorted Array II 154
tags:
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-06-24 19:55:59
---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).

Find the minimum element.

The array may contain duplicates.

[Leetcode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

<!--more-->

**Example 1:**

```
Input: [1,3,5]
Output: 1
```

**Example 2:**

```
Input: [2,2,2,0,1]
Output: 0
```

---

#### Tricky 

We need to remove duplicates at two ends of array.

---

#### Standard solution  

```java
class Solution {
    public int findMin(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        int n = nums.length;
        while (n > 0 && nums[n - 1] == nums[0]) n--;		// remove duplicates
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[n - 1]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return nums[l];
    }
}
```

T: O(logn)		worst case: O(n).  when all in array are duplicates.

S: O(1)

