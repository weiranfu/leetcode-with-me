---
title: Medium | Find Minimum in Rotated Sorted Array 153
tags:
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-05-31 20:42:43
---

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).

Find the minimum element.

You may assume no duplicate exists in the array.

[Leetcode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

<!--more-->

**Example 1:**

```
Input: [3,4,5,1,2] 
Output: 1
```

**Example 2:**

```
Input: [4,5,6,7,0,1,2]
Output: 0
```

**Follow up:**

[Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

---

#### Binary Search

**Use `nums[n - 1]` as a pivot rather than `nums[0]`**

Because in example `[1,2,3,4]`, we cannot use `nums[0]` as a pivot, otherwise we will get the wrong answer `4` instead of `1`.

```java
class Solution {
    public int findMin(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        int n = nums.length;
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[n - 1]) {		// use nums[n - 1] as a pivot
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return nums[l];
    }
}
```

T: O(logn)		S: O(1)

2. If we still want to use `nums[0]` as a pivot, we need to check the special case

```java
class Solution {
    public int findMin(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        int n = nums.length;
        if (nums[0] <= nums[n - 1]) return nums[0];		// check special case
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] >= nums[0]) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return nums[l];
    }
}
```

T: O(logn)			S: O(1)