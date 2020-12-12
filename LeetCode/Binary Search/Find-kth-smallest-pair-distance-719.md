---
title: Hard | Find Kth Smallest Pair Distance 719
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-06-27 20:01:18
---

Given an integer array, return the k-th smallest **distance** among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

[Leetcode](https://leetcode.com/problems/find-k-th-smallest-pair-distance/)

<!--more-->

**Example 1:**

```
Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
```

---

#### Tricky 

The brute force solution is to enumerate all pairs and find the kth smallest one. It will take O(n^2) (LTE!)

If we sort the array, then we can easily count the numbers of pairs whose distance is smaller than a number. (Only takes O(n))

**The number of valid pairs and `max` distance hava a monotonic relationship.**

If distance `max` is small, the valid pairs will be small. If distance `max` is large, all pairs will be valid.

Then we could use binary search! 

For a given `max`, count the number of valid pairs.

If `num >= k`, we could decrease `max` value. If `num < k` , we must increase `max` value.

---

#### Standard solution  

```java
class Solution {
    public int smallestDistancePair(int[] nums, int k) {
        if (nums == null || nums.length == 0) return -1;
        int n = nums.length;
        Arrays.sort(nums);                  // sort array nums
        
        int l = 0, r = nums[n - 1] - nums[0];
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (count(nums, mid) >= k) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
    
  	// takes O(n)
    private int count(int[] nums, int max) {
        int res = 0;
        int n = nums.length;
        int j = 1;
        for (int i = 0; i < n; i++) {
            while (j < n && nums[j] - nums[i] <= max) {
                j++;
            }
            res += j - i - 1;
        }
        return res;
    }
}
```

T: O(log(max) \* n)

T: O(1)

