---
title: Medium | Path with Maximum Minimum Value 1102
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-18 10:45:44
---

Given a matrix of integers `A` with R rows and C columns, find the **maximum** score of a path starting at `[0,0]` and ending at `[R-1,C-1]`.

The *score* of a path is the **minimum** value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A *path* moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

[Leetcode](https://leetcode.com/problems/path-with-maximum-minimum-value/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/04/23/1313_ex1.JPG)**

```
Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: 
The path with the maximum score is highlighted in yellow. 
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2019/04/23/1313_ex2.JPG)**

```
Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
```

---

#### Tricky 

1. Dijkstra with max value path.

   the distance between two points is `int d = Math.min(dist[i][j], A[x][y]);`

   If we can increase the distance if `dist[x][y] < d`, add into priority queue.

   ```java
   class Solution {
       public int maximumMinimumPath(int[][] A) {
           int m = A.length, n = A[0].length;
           int INF = 0x3f3f3f3f;
           int[][] moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
           int[][] dist = new int[m][n];
           boolean[][] visited = new boolean[m][n];
           /* max heap pq: int[]{ distance, x, y } */
           PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[0] - a[0]);
           dist[0][0] = A[0][0];
           pq.add(new int[]{dist[0][0], 0, 0});
           while (!pq.isEmpty()) {
               int[] info = pq.poll();
               int i = info[1], j = info[2];
               if (visited[i][j]) continue;
               visited[i][j] = true;
               for (int[] move : moves) {
                   int x = i + move[0];
                   int y = j + move[1];
                   if (x < 0 || x >= m || y < 0 || y >= n) continue;
                   int d = Math.min(dist[i][j], A[x][y]);  // distance of next point
                   if (dist[x][y] < d) {            // if we can increase the distance
                       dist[x][y] = d; 
                       pq.add(new int[]{d, x, y});
                   }
               }
           }
           return dist[m - 1][n - 1];
       }
   }
   ```

   T: O(mnlogmn)			S: O(mn)

2. Dijkstra + BFS

   We keep tracking the min value of a path and extend the max value path.

   Use Dijkstra to find the max value path.

   ```java
   class Solution {
       public int maximumMinimumPath(int[][] A) {
           int m = A.length, n = A[0].length;
           int[][] moves = {{0,1},{1,0},{0,-1},{-1,0}};
           PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[0] - a[0]);
           pq.add(new int[] {A[0][0], 0, 0});
           boolean[][] visited = new boolean[m][n];
           visited[0][0] = true;
           int maxscore = A[0][0];
           while(!pq.isEmpty()) {
               int[] info = pq.poll();
               int i = info[1], j = info[2];
               maxscore = Math.min(maxscore, info[0]);
               if(i == m - 1 && j == n - 1) return maxscore;  // find max score
               for(int[] move : moves) {
                   int x = move[0] + i, y = move[1] + j;
                   if (x < 0 || x >= m || y < 0 || y >= n) continue;
                   if (visited[x][y]) continue;
                   visited[x][y] = true;
                   pq.add(new int[]{A[x][y], x, y});
               }
           }
           return -1;
       }
   }
   ```

   T: O(mnlogmn)		S: O(mn)