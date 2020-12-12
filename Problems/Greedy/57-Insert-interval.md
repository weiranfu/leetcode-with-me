---
title: Medium | Insert Interval 57
tags:
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-05-13 19:15:21
---

Given a set of *non-overlapping* intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

[Leetcode](https://leetcode.com/problems/insert-interval/)

<!--more-->

**Example 1:**

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2:**

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

---

#### Tricky 

Extend the overlapping area as large as possible.

```java
start = Math.min(start, s);      // extend overlapping area
end = Math.max(end, e);
```

---

#### My thoughts 

Find the correct possition to merge the new interval.

---

#### First solution 

```java
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        if (intervals.length == 0) {
            int[][] res = new int[1][2];
            res[0] = newInterval;
            return res;
        }
        int n = intervals.length;
        List<int[]> list = new ArrayList<>();
        int start = newInterval[0];
        int end = newInterval[1];
        boolean added = false;
        for (int i = 0; i < n; i++) {
            int s = intervals[i][0];
            int e = intervals[i][1];
            if (start > e) {
                list.add(intervals[i]);
            } else if (end >= s) {
                start = Math.min(start, s);      // extend overlapping area
                end = Math.max(end, e);
            } else {
                if (!added) {
                    list.add(new int[]{start, end});
                    added = true;
                }
                list.add(intervals[i]);
            }
        }
        if (!added) {                          // add the last interval.
            list.add(new int[]{start, end});
            added = true;
        }
        int[][] res = new int[list.size()][2];
        for (int i = 0; i < list.size(); i++) {
            res[i] = list.get(i);
        }
        return res;
    }
}
```

T: O(n)		S: O(n)

---

#### Optimized

we could devide a for-loop into three parts to avoid check whether added the new interval.

Part 1 & 3 is to add non-overlapping intervals.

Part 2 is to merge intervals with new interval.

```java
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        if (intervals.length == 0) {
            int[][] res = new int[1][2];
            res[0] = newInterval;
            return res;
        }
        int n = intervals.length;
        List<int[]> list = new ArrayList<>();
        int start = newInterval[0];
        int end = newInterval[1];
        int i = 0;
        for (; i < n && intervals[i][1] < start; i++) {
            list.add(intervals[i]);
        }
        for (; i < n && intervals[i][0] <= end; i++) {
            start = Math.min(start, intervals[i][0]);
            end = Math.max(end, intervals[i][1]);
        }
        list.add(new int[]{start, end});
        for (; i < n; i++) {
            list.add(intervals[i]);
        }
        int[][] res = new int[list.size()][2];
        for (int j = 0; j < list.size(); j++) {
            res[j] = list.get(j);
        }
        return res;
    }
}
```

T: O(n)		S: O(n)