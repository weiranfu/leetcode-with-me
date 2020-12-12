---
title: Easy | Meeting Rooms
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-07-21 20:18:05
---

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` (si < ei), determine if a person could attend all meetings.

[Leetcode](https://leetcode.com/problems/meeting-rooms/)

<!--more-->

**Example 1:**

```
Input: [[0,30],[5,10],[15,20]]
Output: false
```

**Example 2:**

```
Input: [[7,10],[2,4]]
Output: true
```

**Follow up:** 

[Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

---

#### Standard solution  

This is a typical *Greedy* problem about **Interval grouping**

```java
class Solution {
    public boolean canAttendMeetings(int[][] ranges) {
        if (ranges == null || ranges.length == 0) return true;
        int n = ranges.length;
        
        Arrays.sort(ranges, (a, b) -> a[0] - b[0]);
        
        int end = -1;
        for (int i = 0; i < n; i++) {
            if (end == -1 || end <= ranges[i][0]) {
                end = ranges[i][1];
            } else {
                return false;
            }
        }
        return true;
    }
}
```

T: O(nlong)		S: O(1)

