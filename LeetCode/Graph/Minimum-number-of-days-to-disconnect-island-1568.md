---
title: Hard | Minimum Number of Days to Disconnect Island 1568
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-09-05 10:27:05
---

Given a 2D `grid` consisting of `1`s (land) and `0`s (water).  An *island* is a maximal 4-directionally (horizontal or vertical) connected group of `1`s.

The grid is said to be **connected** if we have **exactly one island**, otherwise is said **disconnected**.

In one day, we are allowed to change **any** single land cell `(1)` into a water cell `(0)`.

Return *the minimum number of days* to disconnect the grid.

[Leetcode](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2020/08/13/1926_island.png)**

```
Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
```

**Example 2:**

```
Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
```

**Example 3:**

```
Input: grid = [[1,0,1,0]]
Output: 0
```

**Example 4:**

```
Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,0,1,1]]
Output: 1
```

**Example 5:**

```
Input: grid = [[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,1,1,1]]
Output: 2
```

**Constraints:**

- `1 <= grid.length, grid[i].length <= 30`
- `grid[i][j]` is `0` or `1`.

---

#### Standard solution  

Observation

**ans <= 2**

ans is always less-equal to 2

**why?**

for any island we can remove the two blocks around the bottom right corner to make it disconnected

```
x x x
x x x
x x x
```

can be changed to

```
x x x
x x .
x . x
```

```java
class Solution {
    int[][] grid;
    int m, n;
    boolean[][] visited;
    int[][] moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    public int minDays(int[][] grid) {
        this.grid = grid;
        m = grid.length; n = grid[0].length;
        if (check()) return 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    grid[i][j] = 0;
                    if (check()) return 1;
                    grid[i][j] = 1;
                }
            }
        }
        return 2;
    }
    private boolean check() {
        int cnt = 0;
        visited = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    cnt++;
                    dfs(i, j);
                }
            }
        }
        return cnt >= 2 || cnt == 0;
    }
    private void dfs(int i, int j) {
        visited[i][j] = true;
        for (int[] move : moves) {
            int x = i + move[0];
            int y = j + move[1];
            if (x < 0 || x >= m || y < 0 || y >= n || visited[x][y]) continue;
            if (grid[x][y] == 1) {
                dfs(x, y);
            }
        }
    }
}
```

T: O(m^2\*n^2)			S: O(mn)