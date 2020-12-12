---
title: Hard | Minimum Cost to Make at Least One Valid Path in a Grid 1368
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-18 00:50:23
---

Given a *m* x *n* `grid`. Each cell of the `grid` has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of `grid[i][j]` can be:

- **1** which means go to the cell to the right. (i.e go from `grid[i][j]` to `grid[i][j + 1]`)
- **2** which means go to the cell to the left. (i.e go from `grid[i][j]` to `grid[i][j - 1]`)
- **3** which means go to the lower cell. (i.e go from `grid[i][j]` to `grid[i + 1][j]`)
- **4** which means go to the upper cell. (i.e go from `grid[i][j]` to `grid[i - 1][j]`)

Notice that there could be some **invalid signs** on the cells of the `grid` which points outside the `grid`.

You will initially start at the upper left cell `(0,0)`. A valid path in the grid is a path which starts from the upper left cell `(0,0)` and ends at the bottom-right cell `(m - 1, n - 1)` following the signs on the grid. The valid path **doesn't have to be the shortest**.

You can modify the sign on a cell with `cost = 1`. You can modify the sign on a cell **one time only**.

Return *the minimum cost* to make the grid have at least one valid path.

[Leetcode](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/02/13/grid1.png)

```
Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.
```

**Follow up**

[Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/)

---

#### Tricky 

How to decide whether to change the direction?

We can view this situation as you must pay at different cost to go to next point.

If you go next point following the sign, you pay `0`, otherwise you need to pay `1`.

So we convert problem to a **Shortest Path with Cost** problem.

#### Dijkstra in Sparse Graph

We don't need to build a new graph, and we can calculate the cost with `int cost = grid[i][j] == k + 1 ? 0 : 1;`

This is a **Sparse Graph** because E = m\*n, V = m\*n.

```java
/* 0: right, 1: left, 2: down, 3: up */
int[][] moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
```

```java
class Solution {
    public int minCost(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int INF = 0x3f3f3f3f;
        /* 0: right, 1: left, 2: down, 3: up */
        int[][] moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++) {
            Arrays.fill(dist[i], INF);
        }
        boolean[][] visited = new boolean[m][n];
        
        dist[0][0] = 0;
        /* pq: int[]{ distance, x, y} */
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.add(new int[]{0, 0, 0});
        while (!pq.isEmpty()) {
            int[] info = pq.poll();
            int i = info[1], j = info[2];
            if (visited[i][j]) continue;
            visited[i][j] = true;
            for (int k = 0; k < 4; k++) {
                int x = i + moves[k][0];
                int y = j + moves[k][1];
                if (x < 0 || x >= m || y < 0 || y >= n) continue;
                int cost = grid[i][j] == k + 1 ? 0 : 1;
                if (dist[x][y] > dist[i][j] + cost) {
                    dist[x][y] = dist[i][j] + cost;
                    pq.add(new int[]{dist[x][y], x, y});
                }
            }
        }
        return dist[m - 1][n - 1] == INF ? -1 : dist[m - 1][n - 1];
    }
}
```

T: O(ElogV)			S: O(V)