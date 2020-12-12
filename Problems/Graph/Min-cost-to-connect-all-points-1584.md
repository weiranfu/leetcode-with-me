---
title: Medium | Min Cost to Connect All Points 1584
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-09-27 16:53:51
---

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **manhattan distance** between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return *the minimum cost to make all points connected.* All points are connected if there is **exactly one** simple path between any two points.

[Leetcode](https://leetcode.com/problems/min-cost-to-connect-all-points/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/08/26/d.png)

![](https://assets.leetcode.com/uploads/2020/08/26/c.png)

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

---

#### Standard solution  

**This is a dense graph, we need to use Prim algorithm instead of Kruskal algorithm**

**How to represent a point with two dimention (x, y)?**

We could use the original index in `points` to represent a point with two dimention.

`point[i]` means a point with `[x1, y1]` as its coordination.

Then a distance between two points `a` and `b` can be represented as `g[a][b] = |x1-x2|+|y1-y2|`

`a` and `b` is the original index in `points`.

```java
class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        int MAX = 0x3f3f3f3f;
        boolean[] visited = new boolean[n];
        int[][] g = new int[n][n];
        int[] dist = new int[n];
        Arrays.fill(dist, MAX);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                g[i][j] = MAX;
            }
        }
        for (int i = 0; i < n; i++) {
            int a = points[i][0], b = points[i][1];
            for (int j = 0; j < n; j++) {
                int x = points[j][0], y = points[j][1];
                if (a == x && b == y) continue;
                int d = Math.abs(a - x) + Math.abs(b - y);
                g[i][j] = d;						// original index i and j
                g[j][i] = d;
            }
        }
        int cost = 0;
        for (int i = 0; i < n; i++) {
            int u = -1;
            for (int v = 0; v < n; v++) {
                if (!visited[v] && (u == -1 || dist[v] < dist[u])) u = v;
            }
            visited[u] = true;
            if (i != 0) cost += dist[u];
            for (int v = 0; v < n; v++) {
                dist[v] = Math.min(dist[v], g[u][v]);
            }
        }
        return cost;
    }
}
```

T: O(n^2)			S: O(n^2)

