---
title: Hard | Best Position for a Service Centre 1515
tags:
  - tricky
categories:
  - Leetcode
  - Geometry
date: 2020-07-12 00:30:30
---

A delivery company wants to build a new service centre in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new centre in a position such that **the sum of the euclidean distances to all customers is minimum**.

Given an array `positions` where `positions[i] = [xi, yi]` is the position of the `ith` customer on the map, return *the minimum sum of the euclidean distances* to all customers.

In other words, you need to choose the position of the service centre `[xcentre, ycentre]` such that the following formula is minimized:

![img](https://assets.leetcode.com/uploads/2020/06/25/q4_edited.jpg)

Answers within `10^-5` of the actual value will be accepted.

[Leetcode](https://leetcode.com/problems/best-position-for-a-service-centre/)

<!--more-->

**Example:**

![img](https://assets.leetcode.com/uploads/2020/06/25/q4_e1.jpg)

```
Input: positions = [[0,1],[1,0],[1,2],[2,1]]
Output: 4.00000
Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1] will make the distance to each customer = 1, the sum of all distances is 4 which is the minimum possible we can achieve.
```

**Constraints:**

- `1 <= positions.length <= 50`
- `positions[i].length == 2`
- `0 <= positions[i][0], positions[i][1] <= 100`

---

#### Tricky 

**Simulated Annealing** (模拟退火算法)

Starting from a random point (here I use `(0, 0)`). We move around in 4 directions with some initial `step` (I used `50`).

If we can find smaller total distance, we move to that point.

Otherwise, we set `step /= 2`.

We keep this iteration until the `step` is smaller than `1e-6`.

```java
class Solution {
    int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public double getMinDistSum(int[][] pos) {
        int n = pos.length;
        double esp = 1e-6;
        double x = 0, y = 0;
        double step = 50;
        double min = sum(x, y, pos);
        while (step > esp) {
            boolean find = false;
            for (int[] dir : dirs) {         // looking around for a better point
                double x1 = x + step * dir[0];
                double y1 = y + step * dir[1];
                double d = sum(x1, y1, pos);
                if (min > d) {
                    x = x1;
                    y = y1;
                    min = d;
                    find = true;
                }
            }
            if (!find) step /= 2;
        }
        return min;
    }
    private double dist(double x1, double y1, double x2, double y2) {
        return Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
    }
    private double sum(double x, double y, int[][] pos) {
        double s = 0;
        for (int[] p : pos) {
            s += dist(x, y, p[0], p[1]);
        }
        return s;
    }
}
```

T: O(nlogn)