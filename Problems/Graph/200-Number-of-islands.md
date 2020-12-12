---
title: Medium | Number of Islands 200
tags:
  - tricky
  - implement
categories:
  - Leetcode
  - Graph
date: 2019-12-14 20:58:58
---

Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

[Leetcode](https://leetcode.com/problems/number-of-islands/)

<!--more-->

**Example 1:**

```
Input:
11110
11010
11000
00000

Output: 1
```

**Example 2:**

```
Input:
11000
11000
00100
00011

Output: 3
```

---

#### Tricky 

#### 1. DFS to find Connected Component

When we find a `1`, start a DFS and mark it as visited (**We can modify grid\[]\[] directly**).

```java
class Solution {
    int[][] moves = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    int m, n;
    
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        int res = 0;
        m = grid.length;
        n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                  	res++;
                    dfs(i, j, grid);
                }
            }
        }
        return res;
    }
    private void dfs(int i, int j, char[][] grid) {
        grid[i][j] = '0';                 // mark as visited
        for (int[] move : moves) {
            int x = i + move[0];
            int y = j + move[1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (grid[x][y] == '1') {
                dfs(x, y, grid);
            }
        }
    }
}
```

T: O(m\*n)		S: O(m\*n) call stack

#### 2. Union Find

**Union Find solution can determine the size of each union quickly and it can also check whether two islands are connected quickly.**

We can connect two points using `union(p1, p2)`

However we need to map `(x, y)` into `id` (2D -> 1D) for union.

```java
id = x * n + y;
x = id / n;
y = id % n;
int[] uf = new int[m * n]      // max mapping value is (mn-1)
```

How to count the number of unions? Count the number of unions which is `uf[x] = x`

```java
class Solution {
    int[][] moves = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    int m, n;
    int[] uf;
    
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        m = grid.length;
        n = grid[0].length;
        uf = new int[m * n]; // max value is (mn-1)
        for (int i = 0; i < m * n; i++) {
            uf[i] = i;                          // initialize
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '0') continue;
                int id = i * n + j;   // mapping
                for (int[] move : moves) {
                    int x = i + move[0];
                    int y = j + move[1];
                    if (x < 0 || x >= m || y < 0 || y >= n) continue;
                    if (grid[x][y] == '0') continue;
                    int id2 = x * n + y;
                    uf[find(id)] = find(id2);
                }
            }
        }
        int res = 0;
        for (int i = 0; i < m * n; i++) {
            int x = i / n, y = i % n;         // mapping back
            if (grid[x][y] == '1' && uf[i] == i) {
                res++;
            }
        }
        return res;
    }
    private int find(int x) {
        if (uf[x] != x) {
            uf[x] = find(uf[x]);
        }
        return uf[x];
    }
}
```

T: O(mn\*logmn)			S: O(mn)