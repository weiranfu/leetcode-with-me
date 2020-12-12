---
title: Medium | Search in Rotated Sorted Array 33
tags:
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-01-29 22:56:55
---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

You are given a target value to search. If found in the array return its index, otherwise return `-1`.

[Leetcode](https://leetcode.com/problems/search-in-rotated-sorted-array/)

<!--more-->

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of *O*(log *n*).

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Follow up**

[Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)

---

#### Tricky 

How to deal with a rotated array? Rotated array has two seperated parts. Each part is in ascending order.

Note that the 1st item is greater than the last item in rotated array.

So we should consider multiple situations according to the repectively possitions of `target` and `mid` in two parts.

---

#### My thoughts 

Consider the respective possition of `target` and `mid` in two parts array.

```java
class Solution {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length == 0) return -1; 
        int n = nums.length;
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] > nums[n - 1]) {			// mid is in left part
                if (target > nums[n - 1]) {			// target is in left part
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
        return nums[l] == target ? l : -1;
    }
}
```

O(logN)			S: O(1)

---

#### Summary 

Need to know which part the mid and target fall into before performing binary search.