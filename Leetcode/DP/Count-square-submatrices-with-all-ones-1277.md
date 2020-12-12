---
title: Medium | Count Square Submatrices with All Ones 1277
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-02 21:00:33
---

Given a `m * n` matrix of ones and zeros, return how many **square** submatrices have all ones.

[Leetcode](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

<!--more-->

**Example:**

```
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
```

**Follow up:** 

[Maximal Square](https://leetcode.com/problems/maximal-square/)

---

#### Tricky 

This is a follow up to *Maximal Square* problem. We use DP to compute the maximum length of square at each point. Then the number of square formed at that point is `max length`.

---

#### Standard solution  

```java
class Solution {
    public int countSquares(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dp = new int[m + 1][n + 1];
        int res = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (matrix[i - 1][j - 1] == 0) {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1])) + 1;
                    res += dp[i][j];
                }
            }
        }
        return res;
    }
}
```

T: O(mn)		S: O(mn)