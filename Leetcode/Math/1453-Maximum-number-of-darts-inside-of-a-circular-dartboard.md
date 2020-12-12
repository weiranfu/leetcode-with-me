---
title: Hard | Maximum Number of Darts Inside of a Circular Dartboard
tags:
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-05-18 16:59:34
---

You have a very large square wall and a circular dartboard placed on the wall. You have been challenged to throw darts into the board blindfolded. Darts thrown at the wall are represented as an array of `points` on a 2D plane. 

Return the maximum number of points that are within or lie on **any** circular dartboard of radius `r`.

[Leetcode](https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/)

<!--more-->

**Example:**

**![img](https://assets.leetcode.com/uploads/2020/04/29/sample_2_1806.png)**

```
Input: points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
Output: 5
Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all points except the point (7,8).
```

---

#### Tricky 

* Enumerate all combinations of 2 points, find the circle going through them with radius = r.

  Use this circumcenter as the center of circle, and count how many points inside.

* When comparing two double values, `float * float` will be slightly(like 0.00000000001) greater than its real value(There is no effect if the actuall value is smaller at this circumstance), so adding `0.00001` on the right to avoid these rounding error when the left is greater slightly.

  `double * double <= r * r + 0.00001`

---

#### Standard solution  

```java
class Solution {
    public int numPoints(int[][] points, int r) {
        if (points == null || points.length == 0 || points[0].length == 0 || r == 0) return 0;
        int n = points.length;
        int res = 1;                         // at least 1.
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int x1 = points[i][0], y1 = points[i][1];
                int x2 = points[j][0], y2 = points[j][1];
                double d = Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
                if (d > 2 * r) continue;
                double x0 = (x1 + x2) / 2.0 + (y2 - y1) * Math.sqrt(r * r - d * d / 4) / d;  // center of circle.
                double y0 = (y1 + y2) / 2.0 - (x2 - x1) * Math.sqrt(r * r - d * d / 4) / d;
                int cnt = 0;
                for (int[] point : points) {
                    int x = point[0], y = point[1];
                    if ((x - x0) * (x - x0) + (y - y0) * (y - y0) <= r * r + 0.00001) {   // floating error
                        cnt++;
                    }
                }
                res = Math.max(res, cnt);
            }
        }
        return res;
    }
}
```

T: O(n^3) 			S: O(1)