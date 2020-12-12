---
title: Hard | Course Schedule III 638	
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-07-21 22:37:50
---

There are `n` different online courses numbered from `1` to `n`. Each course has some duration(course length) `t` and closed on `dth` day. A course should be taken **continuously** for `t` days and must be finished before or on the `dth` day. You will start at the `1st` day.

Given `n` online courses represented by pairs `(t,d)`, your task is to find the maximal number of courses that can be taken.

[Leetcode](https://leetcode.com/problems/course-schedule-iii/)

<!--more-->

**Example:**

```
Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
```

**Note:**

1. The integer 1 <= d, t, n <= 10,000.
2. You can't take two courses simultaneously.

---

#### Standard solution  

When we finish a course, we must want to start a new course immediately without interval period.

If current course `A`'s duration plus total course time <= current `A`'s deadline, we could simply add this course.

Otherwise, we could swap current course `A` with the course `B` taken before with longest duration.

**How about the deadline if we choose to swap two courses? We could sort courses by deadline so that we don't need to worry about them.**

If course `B`'s length is longer than `A`, we could swap them. Because course `A` has later deadline and shorter duration.

If course `B`'s length is smaller then `A`, we don't add course `A`. Because for next course `C`, if we choose to swap them, course `C` will have more possibility to pass the deadline.

```java
class Solution {
    public int scheduleCourse(int[][] courses) {
        int n = courses.length;
        
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
        
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        int time = 0;
        for (int i = 0; i < n; i++) {
            if (time + courses[i][0] <= courses[i][1]) {
                time += courses[i][0];
                pq.add(courses[i][0]);
            } else if (!pq.isEmpty() && pq.peek() >= courses[i][0]) {
                time = time - pq.peek() + courses[i][0];
                pq.poll();
                pq.add(courses[i][0]);
            }
        }
        return pq.size();
    }
}
```

T: O(nlogn)			S: O(n)





