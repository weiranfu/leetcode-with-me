---
title: Hard | Sliding Window Maximum 239
tags:
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-06-23 16:06:42
---

Given an array *nums*, there is a sliding window of size *k* which is moving from the very left of the array to the very right. You can only see the *k* numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

[Leetcode](https://leetcode.com/problems/sliding-window-maximum/)

<!--more-->

**Example:**

```
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

---

#### Tricky 

This is a typical monotonic queue problem.

We use a Deque to implement a monotonic queue. We only store nums that could affect the max value in the queue and pop out the smaller one.

To control the left boundary of queue, we store the index of each item in the queue. 

If we want to pop out an element from queue, we need to check the index. If `index <= left`, we pop out it.

```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums == null || nums.length == 0) return new int[0];
        int n = nums.length;
        int[] res = new int[n - k + 1];
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0, j = 0; i < n; i++) {  // poll out invalid max value
            while (!q.isEmpty() && q.peekFirst() < i - k + 1) q.pollFirst();
            while (!q.isEmpty() && nums[q.peekLast()] <= nums[i]) q.pollLast();
            q.addLast(i);
            if (i >= k - 1) res[i - k + 1] = nums[q.peekFirst()];	// get max value
        }
        return res;
    }
}
```

T: O(n)			S: O(n)