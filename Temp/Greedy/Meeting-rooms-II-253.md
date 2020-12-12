---
title: Medium | Meeting Rooms II 253
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-07-21 20:25:59
---

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` (si < ei), find the minimum number of conference rooms required.

[Leetcode](https://leetcode.com/problems/meeting-rooms-ii/)

<!--more-->

**Example 1:**

```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
```

**Example 2:**

```
Input: [[7,10],[2,4]]
Output: 1
```

---

#### Standard solution  

This is a typical *Greedy* problem about **Interval Grouping**.

1. Sort ranges based on `begin time`

2. Each time we consider an interval, we check whether the min end time of existing ranges > current begin time, `min(end time) > begin time`. We use Priority queue to maintain the min time of existing ranges.

   If it is, we need to open a new room and add current `end time` into priority queue.

   Otherwise, we remove the min end time one, and add current `end time` into priority queue.

```java
class Solution {
    public int minMeetingRooms(int[][] ranges) {
        if (ranges == null || ranges.length == 0) return 0;
        int n = ranges.length;
        
        Arrays.sort(ranges, (a, b) -> a[0] - b[0]);
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            if (pq.isEmpty() || pq.peek() > ranges[i][0]) {
                pq.add(ranges[i][1]);
            } else {
                pq.poll();
                pq.add(ranges[i][1]);
            }
        }
        return pq.size();
    }
}
```

T: O(nlogn)			S: O(n)

---

#### 差分数组

Since the`max - min + 1` could be vary large, the actual run time could be very large.

```java
class Solution {
    public int minMeetingRooms(int[][] ranges) {
        if (ranges == null || ranges.length == 0) return 0;
        int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
        //Find max/min meeting time
        for (int i = 0; i < ranges.length; i++) {
            max = Math.max(max, ranges[i][1]);
            min = Math.min(min, ranges[i][0]);
        }
        int[] A = new int[max - min + 1];
        for (int[] meet : ranges) {
            A[meet[0] - min]++;
            A[meet[1] - min]--;
        }
        int res = A[0];
        for (int i = 1; i < B.length; i++) {
            A[i] += A[i - 1];
            res = Math.max(res, A[i]);
        }
        return res;
    }
}
```

T: O(n)			S: O(n)

---

#### Chronological Ordering

Inspired by previous solution, we can view each meeting event as two events: entering event and leaving event.

Sort all these event and calculate the number of event being held at the same time.

**Note that we process leaving event before entering event if two events happens at the same time.**

```java
class Solution {
    public int minMeetingRooms(int[][] ranges) {
        if (ranges == null || ranges.length == 0) return 0;
        int n = ranges.length;
        int[][] events = new int[2 * n][2];
        for (int i = 0; i < n; i++) {
            events[2 * i] = new int[]{ranges[i][0], 1};
            events[2 * i + 1] = new int[]{ranges[i][1], -1};
        }
        // if time is same, process leaving event before entering event. 
        Arrays.sort(events, (a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            else return a[1] - b[1];
        });
        int res = 0, cnt = 0;
        for (int[] event : events) {
            cnt += event[1];
            res = Math.max(res, cnt);
        }
        return res;
    }
}
```

T: O(nlogn)			S: O(nlogn)

