---
title: Medium | Minimum Size Subarray Sum 209	
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-07-25 16:52:06
---

Given an array of **n** positive integers and a positive integer **s**, find the minimal length of a **contiguous** subarray of which the sum ≥ **s**. If there isn't one, return 0 instead.

[Leetcode](https://leetcode.com/problems/minimum-size-subarray-sum/)

<!--more-->

**Example:** 

```
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```

**Follow up:** 

[Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)

---

#### Two Pointers

Since the given array contains only positive integers, the subarray sum can only increase by including more elements. Therefore, you don't have to include more elements once the current subarray already has a sum large enough. This gives the linear time complexity solution by maintaining a minimum window with a two indices.

```java
class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        int sum = 0;
        int res = n + 1;
        for (int i = 0, j = 0; i < n; i++) {
            sum += nums[i];
            while (j <= i && sum >= s) {
                res = Math.min(res, i - j + 1);
                sum -= nums[j];
                j++;
            }
        }
        return res == n + 1 ? 0 : res;
    }
}
```

T: O(n)			S: O(1)

---

#### Binary search

Since all elements are positive, the cumulative sum must be strictly increasing. Then, a subarray sum can expressed as the difference between two cumulative sum. Hence, given a start index for the cumulative sum array, the other end index can be searched using binary search.

```java
class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        int[] preSum = new int[n + 1];
        for (int i = 1; i <= n; i++) preSum[i] = preSum[i - 1] + nums[i - 1];
        int res = n + 1;
        for (int i = 0; i < n; i++) {
          // preSum[i] for i in [0, n-1], preSum[j] for j in [i+1, n]
            int j = binarySearch(i + 1, n + 1, preSum, s + preSum[i]);
            if (j != -1) {
                res = Math.min(res, j - i);
            }
        }
        return res == n + 1 ? 0 : res;
    }
    private int binarySearch(int low, int high, int[] preSum, int key) {
        int l = low, r = high;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (preSum[mid] >= key) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l == high ? -1 : l;
    }
}
```

T: O(nlogn)			S: O(n)

