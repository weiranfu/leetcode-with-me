---
title: Hard | Unique Path III 980
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-20 15:48:47
---

On a 2-dimensional `grid`, there are 4 types of squares:

- `1` represents the starting square.  There is exactly one starting square.
- `2` represents the ending square.  There is exactly one ending square.
- `0` represents empty squares we can walk over.
- `-1` represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that **walk over every non-obstacle square exactly once**.

[Leetcode](https://leetcode.com/problems/unique-paths-iii/)

<!--more-->

**Example 1:**

```
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
```

**Example 2:**

```
Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
```

---

#### Backtracking

We try each possible move and if we can reach end point with visiting all other point exactly once, then `cnt++`

```java
class Solution {
    int[][] moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    int[][] grid;
    int m, n;
    int cnt;
    public int uniquePathsIII(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        this.grid = grid;
        m = grid.length; n = grid[0].length;
        int s1 = -1, s2 = -1;
        int total = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    s1 = i; s2 = j;
                } else if (grid[i][j] == 0) total++;
            }
        }
        cnt = 0;
        dfs(s1, s2, total);
        return cnt;
    }
    private void dfs(int i, int j, int total) {
        if (grid[i][j] == 2) {
            if (total == 0) {
                cnt++;
            }
            return;
        }
        for (int[] move : moves) {
            int x = i + move[0];
            int y = j + move[1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (grid[x][y] == 2) {
                dfs(x, y, total);
            } else if (grid[x][y] == 0) {
                grid[x][y] = -1;
                dfs(x, y, total - 1);
                grid[x][y] = 0;
            }
        }
    }
} 
```

T: O(4^(mn))			S: O(mn)