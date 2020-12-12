---
title: Easy | Unique Path 62
tags:
  - common
categories:
  - Leetcode
  - Graph
date: 2020-05-14 16:18:19
---

A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

[Leetcode](https://leetcode.com/problems/unique-paths/)

<!--more-->

![img](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)
Above is a 7 x 3 grid. How many possible unique paths are there?

**Example 1:**

```
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
```

---

#### My thoughts 

`dp[i][j] = dp[i - 1][j] + dp[i][j - 1]`

---

#### First solution 

Note that we use `row[0] and col[0]` as the starting lines for dp computing.

```java
class Solution {
    public int uniquePaths(int m, int n) {
        if (m == 0 || n == 0) return 0;
        int[][] dp = new int[m + 1][n + 1];  // two extra lines.
        dp[0][1] = 1;
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m][n];
    }
}
```

T: O(mn)		S: O(mn)

---

#### Optimized

Only use O(n) space for dp.

`dp[i] = dp[i] + dp[i - 1]`

```java
class Solution {
    public int uniquePaths(int m, int n) {
        if (m == 0 || n == 0) return 0;
        int[] dp = new int[n + 1];
        dp[1] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 1; j < n + 1; j++) {
                dp[j] = dp[j] + dp[j - 1];
            }
        }
        return dp[n];
    }
}
```

T: O(mn)		S: O(n)

