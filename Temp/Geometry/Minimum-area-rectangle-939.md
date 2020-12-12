---
title: Medium | Minimum Area Rectangle 939
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Geometry
date: 2020-09-29 01:01:38
---

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

[Leetcode](https://leetcode.com/problems/minimum-area-rectangle/)

<!--more-->

**Example 1:**

```
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
```

**Example 2:**

```
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
```

**Note**:

1. `1 <= points.length <= 500`
2. `0 <= points[i][0] <= 40000`
3. `0 <= points[i][1] <= 40000`
4. All points are distinct.

**Follow up:** 

[Minimum Area Rectangle II](https://leetcode.com/problems/minimum-area-rectangle-ii/)

---

#### Brute Force

How to define a rectangle?

**We only need two points on the diagonal!!!**

So iterate two points as diagonal and check for the existance of another two points.

Use a map to store mapping of `y` to `x`. `Map<Integer, Set<Integer>> yMap`

```java
class Solution {
    public int minAreaRect(int[][] points) {
        // stores y according to x
        Map<Integer, Set<Integer>> yMap = new HashMap<>();
        for (int[] point : points) {
            int x = point[0], y = point[1];
            yMap.putIfAbsent(x, new HashSet<>());
            yMap.get(x).add(y);
        }
        int min = Integer.MAX_VALUE;
        for (int[] p1 : points) {
            int x1 = p1[0], y1 = p1[1];
            for (int[] p2 : points) {
                int x2 = p2[0], y2 = p2[1];
                // find two points at diagonal
                if (x1 == x2 || y1 == y2) continue; 
                // cannot find another two points
                if (!yMap.get(x1).contains(y2) || !yMap.get(x2).contains(y1)) continue;
                min = Math.min(min, Math.abs(x1 - x2) * Math.abs(y1 - y2));
            }
        }
        return min == Integer.MAX_VALUE ? 0 : min;
    }
}
```

T: O(n^2)			S: O(n)