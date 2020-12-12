---
title: Medium | Merge Intervals 56
tags:
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-05-13 17:50:58
---

Given a collection of intervals, merge all overlapping intervals.

[Leetcode](https://leetcode.com/problems/merge-intervals/)

<!--more-->

**Example 1:**

```
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2:**

```
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

---

#### Tricky 

How to merge intervals?

We only care about the `end` of this overlapping interval and the `start` of new overlapping interval.

* Sort intervals by the `start` time. Extend the overlapping area as large as possible.
* Extract `start` and `end` time as arrays, and sort them respectively. Only min start and max end matter and they are not impacted by how we pair starts and ends.

---

#### My thoughts 

Sort intervals by the `start` time. Extend `end` point.

`end = Math.max(end, interval[1])`

The condition that starting a new overlapping interval is `interval[0] > end`.

```java
class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> list = new ArrayList<>();
        if (intervals.length == 0) return new int[0][0];
        int n = intervals.length;
        
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        
        int start = Integer.MIN_VALUE, end = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            if (end < intervals[i][0]) {
                if (end != Integer.MIN_VALUE) {
                    list.add(new int[]{start, end});
                }
                start = intervals[i][0];
                end = intervals[i][1];
            } else {
                end = Math.max(end, intervals[i][1]);
            }
        }
        list.add(new int[]{start, end});     // add the last interval
        int[][] res = new int[list.size()][2];
        for (int i = 0; i < list.size(); i++) {
            res[i] = list.get(i);
        }
        return res;
    }
}
```

T: O(nlogn)		S: O(n)

---

#### Sort two arrays 

Sort `start` and `end` time arrays respectively.

Only min start and max end matter and they are not impacted by how we pair starts and ends.

Original intervals after sort drawn as lines:

```python
0----------10
   2-----8
       4-------------15  
             6 ------12
                                      17---------25
```

New intervals by using start[i]-end[i] pairs:

```python
0--------8
   2----------10
       4------------ 12
            6-------------15
                                           17----------25
```

Use `start` as pointer to the index of starting point.

```java
class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> list = new ArrayList<>();
        if (intervals.length <= 1) return intervals;
        int n = intervals.length;
        int[] starts = new int[n];
        int[] ends = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        } 
        Arrays.sort(starts);
        Arrays.sort(ends);
        int start = 0;                   // start index
        for (int i = 0; i < n; i++) {
            // i+1 level is not overlapped by i level.
            if (i == n - 1 || starts[i + 1] > ends[i]) {    
                list.add(new int[]{starts[start], ends[i]});
                start = i + 1;
            }
        }
        int[][] res = new int[list.size()][2];
        for (int i = 0; i < list.size(); i++) {
            res[i] = list.get(i);
        }
        return res;
    }
}
```

T: O(nlogn)			S: O(n)

---

#### Summary 

In tricky.