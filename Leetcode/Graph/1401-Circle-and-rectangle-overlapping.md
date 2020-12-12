---
title: Medium | Circle and Rectangle Overlapping
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-05-18 00:12:49
---

Given a circle represented as (`radius`, `x_center`, `y_center`) and an axis-aligned rectangle represented as (`x1`, `y1`, `x2`, `y2`), where (`x1`, `y1`) are the coordinates of the bottom-left corner, and (`x2`, `y2`) are the coordinates of the top-right corner of the rectangle.

Return True if the circle and rectangle are overlapped otherwise return False.

In other words, check if there are **any** point (xi, yi) such that belongs to the circle and the rectangle at the same time.

[Leetcode](https://leetcode.com/problems/circle-and-rectangle-overlapping/)

<!--more-->

**Example:**

![img](https://assets.leetcode.com/uploads/2020/02/20/sample_4_1728.png)

```
Input: radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0) 
```

---

#### Tricky 

How to calculate the minimum distance between a rectangle and a point.

We could get the closest point in rectangle in x-axis and y-axis respectively.

**Get the closet point to x_center within the range of [x1, x2]** .

```java
private int getClosest(int val, int min, int max) {
  return Math.max(min, Math.min(max, val));
}
```

---

#### My thoughts 

Try all possible directions of circle center (x, y).

---

#### First solution 

```java
class Solution {
    public boolean checkOverlap(int radius, int x, int y, int x1, int y1, int x2, int y2) {
        int dis;
        if (x > x2 && y > y2) {
            dis = distance(x, y, x2, y2);
        } else if (x > x2 && y < y1) {
            dis = distance(x, y, x2, y1);
        } else if (x > x2) {
            dis = (x - x2) * (x - x2);
        } else if (x < x1 && y > y2) {
            dis = distance(x, y, x1, y2);
        } else if (x < x1 && y < y1) {
            dis = distance(x, y, x1, y1);
        } else if (x < x1) {
            dis = (x1 - x) * (x1 - x);
        } else if (y > y2) {
            dis = (y - y2) * (y - y2);
        } else if (y < y1) {
            dis = (y1 - y) * (y1 - y);
        } else {
            return true;
        }
        return dis <= radius * radius;
    }
    
    private int distance(int x1, int y1, int x2, int y2) {
        return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
    }
}
```

T: O(1)			S: O(1)

---

#### Optimized

Get closest point in rectangle in x-axis and y-axis respectively.

```java
class Solution {
    public boolean checkOverlap(int radius, int x, int y, int x1, int y1, int x2, int y2) {
        int closestX = getClosest(x, x1, x2);
        int closestY = getClosest(y, y1, y2);
        return distance(x, y, closestX, closestY) <= radius * radius;
    }
    
    private int distance(int x1, int y1, int x2, int y2) {
        return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
    }
    
    private int getClosest(int val, int min, int max) {
        return Math.max(min, Math.min(max, val));
    }
}
```

T:  O(1)			S: O(1)