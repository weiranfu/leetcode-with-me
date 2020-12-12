---
title: Medium | Unique Paths II 63
tags:
  - corner case
categories:
  - Leetcode
  - Graph	
date: 2019-11-26 14:10:11
---

A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

[Leetcode](https://leetcode.com/problems/unique-paths-ii/)

<!--more-->

![img](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

An obstacle and empty space is marked as `1` and `0` respectively in the grid.

**Note:** *m* and *n* will be at most 100.

**Example 1:**

```
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```

**Follow up**

[Unique Path III](https://leetcode.com/problems/unique-paths-iii/)

---

#### Tricky

```java
class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] dp = new int[m + 1][n + 1];
        dp[0][1] = 1;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (grid[i - 1][j - 1] != 1) {
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                }
            }
        }
        return dp[m][n];
    }
}
```

T: O(mn)			S: O(mn)

---

#### 1D DP

Mind the initialization of 1D version

We need to set `dp[0] = 0` and `dp[1] = 1` for initialization.

```java
class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] dp = new int[n + 1];
        dp[1] = 1;													// initialize
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (grid[i - 1][j - 1] != 1) {
                    dp[j] = dp[j] + dp[j - 1];
                } else {
                    dp[j] = 0;
                }
            }
        }
        return dp[n];
    }
}
```

T: O(mn)  S: O(n)
