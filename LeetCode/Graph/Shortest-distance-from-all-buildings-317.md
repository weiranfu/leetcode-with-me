---
title: Hard | Shortest Distance from All Buildings 317
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-21 00:20:00
---

You want to build a house on an *empty* land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values **0**, **1** or **2**, where:

- Each **0** marks an empty land which you can pass by freely.
- Each **1** marks a building which you cannot pass through.
- Each **2** marks an obstacle which you cannot pass through.

There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

[Leetcode](https://leetcode.com/problems/shortest-distance-from-all-buildings/)

<!--more-->

**Example:**

```
Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
```

---

#### BFS  

bfs each `1` to find out min distance to each `0`, **accumulate this distances to each 0 location**: distance\[]\[], finally find out min value from distance\[]\[]
- In the case of cannot reach all house: 

  not all `0`s can reach each house: reachCount\[]\[] to count the # of house each 0 can reach, only >= houseCount is valid

- [improve speed]：during BFS we could check whether all houses are reachable from each other.

  if count reachable house < houseCount, return `-1` directly!!!

```java
class Solution {
    int[][] moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int[][] grid;
    int m, n;
    int[][] dist;                   // accumulated distance from each house
    int[][] cnt;                    // cnt reachable house for each 0
    int total;                      // total house
    public int shortestDistance(int[][] grid) {
        m = grid.length; n = grid[0].length;
        this.grid = grid;
        dist = new int[m][n];
        cnt = new int[m][n];
        total = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    total++;
                }
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {           
                    if (!bfs(i, j)) { // houses is not reachable each other
                        return -1;
                    }
                }
            }
        }
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 && cnt[i][j] == total) {
                    min = Math.min(min, dist[i][j]);
                }
            }
        }
        return min == Integer.MAX_VALUE ? -1 : min;
    } 
    private boolean bfs(int ii, int jj) {
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[m][n];
        q.add(new int[]{ii, jj});
        int steps = 0;
        int count = 1;      // count reachable for other houses
        visited[ii][jj] = true;
        while (!q.isEmpty()) {
            steps++;
            int size = q.size();
            while (size-- != 0) {
                int[] info = q.poll();
                int i = info[0], j = info[1];
                for (int[] move : moves) {
                    int x = i + move[0];
                    int y = j + move[1];
                    if (x < 0 || x >= m || y < 0 || y >= n) continue;
                    if (grid[x][y] == 0 && !visited[x][y]) {
                        visited[x][y] = true;
                        dist[x][y] += steps;
                        cnt[x][y]++;
                        q.add(new int[]{x, y});
                    } else if (grid[x][y] == 1 && !visited[x][y]) {
                        visited[x][y] = true;
                        count++;
                    }
                }
            }
        }
        return count == total;
    }
}
```

T: O(m^2\*n^2)		S: O(mn)

