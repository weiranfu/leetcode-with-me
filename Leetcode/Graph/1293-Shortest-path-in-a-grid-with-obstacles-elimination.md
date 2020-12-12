---
title: Hard | Shortest Path in a Grid with Obstacles Elimination 1293
tags:
  - tricky
  - implement
categories:
  - Leetcode
  - Graph
date: 2019-12-15 15:39:47
---

Given a `m * n` grid, where each cell is either `0` (empty) or `1` (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner `(0, 0)` to the lower right corner `(m-1, n-1)`given that you can eliminate **at most** `k` obstacles. If it is not possible to find such walk return -1.

[Leetcode](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

<!--more-->

**Example 1:**

```
Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
```

**Example 2:**

```
Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
```

**Constraints:**

- `grid.length == m`
- `grid[0].length == n`
- `1 <= m, n <= 40`
- `1 <= k <= m*n`
- `grid[i][j] == 0 **or** 1`
- `grid[0][0] == grid[m-1][n-1] == 0`

---

#### Tricky 

Using 3D array to store point with k obstacles state.

Using BFS to traverse all nodes in steps ascending order. 

#### Imeplement

How to store a point with k state in a queue?

`Queue<int[]> queue = new ArrayDeque<>();`

Store: `queue.add(new int[]{0, 0, k});`

Retrive: `int[] info = queue.poll(); int i = info[0], j = info[1], k = info[2];`

---

#### My thoughts 

Failed to solve

---

#### Standard solution 

```java
class Solution {
    public int shortestPath(int[][] grid, int k) {
        int row = grid.length, col = grid[0].length;
        int[][] moves = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        int[][][] dp = new int[row][col][k + 1];
        for (int[][] g : dp) {
            for (int[] h : g) {
                Arrays.fill(h, -1);
            }
        }
        dp[0][0][k] = 0;
        Queue<int[]> queue = new ArrayDeque<>();  // Store a point with k state.
        queue.add(new int[]{0, 0, k});
        while (!queue.isEmpty()) {
            int[] info = queue.poll();
            int i = info[0], j = info[1], p = info[2];
            if (i == row - 1 && j == col - 1) return dp[i][j][p];
            for (int[] move : moves) {
                int x = i + move[0];
                int y = j + move[1];
                if (x < 0 || x >= row || y < 0 || y >= col) continue;
                int p_left = p - grid[x][y];
                if (p_left < 0) continue; // Can't eliminate this obstacle.
                // Don't consider same k state with more steps.
                if (dp[x][y][p_left] >= 0) continue;  
                dp[x][y][p_left] = dp[i][j][p] + 1;
                queue.add(new int[]{x, y, p_left});//Store this point with p_left state.
            }
        }
        return -1;
    }
}
```

T: O(mn*k) S: O(mnk)

---

#### BFS with 2D array to store k state

Use BFS to search possible ways to the target with k state stored in a 2D array.

If the next step's k state < 0, then cannot go to this point.

If we come to a point we have visited before, which means we use more steps to reach here, so the accepted situation is that we came here with more availiable k state and also more steps.

```java
class Solution {
    public int shortestPath(int[][] grid, int k) {
        int row = grid.length, col = grid[0].length;
        int[][] moves = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        int[][] state = new int[row][col];
        for (int[] s : state) {
            Arrays.fill(s, -1);
        }
        state[0][0] = k;
        int steps = 0;
        Queue<int[]> queue = new LinkedList<>();  // Store a point with k state.
        queue.offer(new int[]{0, 0});
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int s = 0; s < size; s += 1) {
                int[] info = queue.poll();
                int i = info[0], j = info[1];
                if (i == row - 1 && j == col - 1) return steps;
                for (int[] move : moves) {
                    int x = i + move[0];
                    int y = j + move[1];
                    if (x < 0 || x >= row || y < 0 || y >= col) continue;
                    int left = state[i][j] - grid[x][y];
                    // Moving to same point(x, y) with more steps and less k is useless
                    // Or left obstacles is less than 0.
                    if (left < 0 || state[x][y] >= left) continue;
                    state[x][y] = left;
                    queue.offer(new int[]{x, y});
                }
            }
            steps += 1;
        }
        return -1;
    }
}


```

T: O(mn*K) S: O(mn)

---

#### Summary 

Using 3D array to store point with k obstacles state.