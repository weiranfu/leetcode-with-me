---
title: Medium | Non-overlapping Intervals 435
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-06-26 17:58:00
---

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

[Leetcode](https://leetcode.com/problems/non-overlapping-intervals/)

<!--more-->

**Example 1:**

```
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
```

**Example 2:**

```
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
```

**Example 3:**

```
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

**Note:**

1. You may assume the interval's end point is always bigger than its start point.
2. Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

---

#### Tricky 

This is a typical *Longest Increasing Subsequences* problem.

If we want to remove minimum intervals, we need to find the longest increasing intervals!

---

#### DP

Use `dp[i]` to store the number of increasing intervals.

```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals == null || intervals.length == 0) return 0;
        int n = intervals.length;
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        int[] dp = new int[n];
        dp[0] = 1;
        int res = 1;
        for (int i = 1; i < n; i++) {
            int max = 1;
            for (int j = 0; j < i; j++) {
                if (intervals[j][1] <= intervals[i][0]) {
                    max = Math.max(max, dp[j] + 1);
                }
            }
            dp[i] = max;
            res = Math.max(res, dp[i]);
        }
        return n - res;
    }
}
```

T: O(n^2)			S: O(n)

---

#### Greedy + Binary Search

[Longest Increasing Subsequences](https://aranne.github.io/2020/06/24/Longest-increasing-subsequences-300/)

If we only care about the tail number with same length of longest increasing subsequences, we could update the tail number to be smaller one (Greedy!)

Use Binary Search to find the right place to insert new tail.

When we find that place and update the tail in that length, we only update if end of interval becoming smaller.

```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals == null || intervals.length == 0) return 0;
        int n = intervals.length;
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        int[] tails = new int[n];         // store end of interval in different length
        int len = 0;
        for (int i = 0; i < n; i++) {
            int l = 0, r = len;
            while (l < r) {
                int mid = l + (r - l) / 2;
                if (tails[mid] <= intervals[i][0]) {
                    l = mid + 1;
                } else {
                    r = mid;
                }
            }
            if (tails[l] == 0) {
                tails[l] = intervals[i][1];
            } else {
                tails[l] = Math.min(tails[l], intervals[i][1]);//only update smaller end
            }
            if (l == len) {
                len++;
            }
        }
        return n - len;
    }
}
```

T: O(nlogn)			S: O(n)

---

#### Greedy

1. Sort intervals by end point.

2. If next interval intercect with current interval, `remove++`

   otherwise update `end = interval[i][1]`

```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals == null || intervals.length == 0) return 0;
        int n = intervals.length;
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        int end = Integer.MIN_VALUE;
        int remove = 0;
        for (int i = 0; i < n; i++) {
            if (intervals[i][0] >= end) {
                end = intervals[i][1];
            } else {
                remove++;
            }
        }
        return remove;
    }
}
```

T: O(nlogn)		S: O(1)

