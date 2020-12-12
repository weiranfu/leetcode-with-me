---
title: Medium | Minimum Path Sum 64
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2019-11-24 22:55:14
---

Given a *m* x *n* grid filled with non-negative numbers, find a path from top left to bottom right which *minimizes* the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

[Leetcode](https://leetcode.com/problems/minimum-path-sum/)

<!--more-->

**Example:**

```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```

---

#### Tricky 

We can only move right or down, so we can use dp to determine the distence to a point.



---

#### My thoughts 

DFS: relax neighbors of each node.

---

#### First solution 

```java
class Solution {
    public int minPathSum(int[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        int[][] path = new int[r][c];
        for (int i = 0; i < r; i += 1) {
            for (int j = 0; j < c; j += 1) {
                path[i][j] = Integer.MAX_VALUE;
            }
        }
        int i = 0, j = 0;
        path[i][j] = grid[i][j];
        relax(i, j, path, grid);
        return path[r-1][c-1];
    }
    
    private void relax(int i, int j, int[][] path, int[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        if (j + 1 < c && path[i][j+1] > path[i][j] + grid[i][j+1]) {
            path[i][j+1] = path[i][j] + grid[i][j+1];
            relax(i, j+1, path, grid);
        } 
        if (i + 1 < r && path[i+1][j] > path[i][j] + grid[i+1][j]) {
            path[i+1][j] = path[i][j] + grid[i+1][j];
            relax(i+1, j, path, grid);
        }
    } 
}
```



---

#### Standard solution: DP 

There're two possible path for a point, from top or from left.

`grid[i][j] = grid[i][j] + Math.min(grid[i-1][j], grid[i][j-1]);`

```java
class Solution {
    public int minPathSum(int[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        for (int i = 1; i < c; i += 1) {
            grid[0][i] = grid[0][i] + grid[0][i-1];
        }
        for (int i = 1; i < r; i += 1) {
            grid[i][0] = grid[i][0] + grid[i-1][0];
        }
        for (int i = 1; i < r; i += 1) {
            for (int j = 1; j < c; j += 1) {
                grid[i][j] = grid[i][j] + Math.min(grid[i-1][j], grid[i][j-1]);
            }
        }
        return grid[r-1][c-1];
    }
}
```

T: O(n^2), S: O(n^2)

---

#### Summary 

We can use DP to solve path problem where we can only move right or down.