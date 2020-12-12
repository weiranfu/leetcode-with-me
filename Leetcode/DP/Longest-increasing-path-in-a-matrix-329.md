---
title: Hard | Longest Increasing Path in a Matrix 329
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-16 03:02:34
---

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

[Leetcode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)

<!--more-->

**Example 1:**

```
Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
```

---

#### Tricky 

This is a typical problem using recursion with memorization instead of bottom-up DP.

We can record the max path starting from each point in `dp[i][j]`

```java
class Solution {
    int[][] matrix;
    int m, n;
    int[][] dp;
    int[][] dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    int max;
    public int longestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;
        this.matrix = matrix;
        m = matrix.length;
        n = matrix[0].length;
        dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = -1;
            }
        }
        max = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j] == -1) {
                    dfs(i, j);
                }
            }
        }
        return max;
    }
    private int dfs(int i, int j) {
        if (dp[i][j] != -1) return dp[i][j];
        int res = 1;
        for (int[] dir : dirs) {
            int x = i + dir[0];
            int y = j + dir[1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (matrix[i][j] < matrix[x][y]) {
                res = Math.max(res, 1 + dfs(x, y));
            }
        }
        dp[i][j] = res;
        max = Math.max(max, res);
        return res;
    }
}
```

T: O(n^2)			S: O(n^2)