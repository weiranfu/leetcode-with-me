---
title: Medium | Maximal Square 221
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-06-19 16:54:55
---

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

[Leetcode](https://leetcode.com/problems/maximal-square/)

<!--more-->

**Example:**

```javascript
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```

**Follow up**

[Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/)

---

#### Tricky 

1. Brute Force:

   Save the number of contiguous `1` at each point in every row into `width`

   For example, in row `1 0 1 1 1`, the contiguous `1` is `1 0 1 2 3`, so we can easily get the maximum possible width of each square.

   Then start search upwards at each point to find possible squares.

   When we search upwards, the width is stricted by `minWidth`. 

   `minWidth = min(minWidth, width[k][j])`

2. DP

   We can save the max length of square each point can form in `dp[i][j]`

   At point `(i, j)`, 

   ```
      _______________
    __|_____________|
   |  |          |  |
   |  |          |  |
   |  |          |  |
   |  |__________|__|(i-1, j)
   |__|__________|__|(i, j)
   						 (i,j-1)
   ```

   We have to look up three points, `(i-1, j)`, `(i, j-1)` and `(i-1, j-1)`

   `dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`

---

#### Brute Force 

```java
class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] width = new int[m + 1][n + 1];
        int max = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (matrix[i - 1][j - 1] == '0') {
                    width[i][j] = 0;
                } else {
                    width[i][j] = width[i][j - 1] + 1;
                }
                int minW = width[i][j];
                for (int w = 1; w <= width[i][j]; w++) { // searching upward
                    int index = i - w + 1;
                    if (index < 1) break;
                    minW = Math.min(minW, width[index][j]);
                    if (minW < w) break;  // cannot form square any more
                    max = Math.max(max, w * w);   // square with width w
                }
            }
        }
        return max;
    }
}
```

T: O(m\*n^2)			S: O(mn)

---

#### DP

```java
class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] dp = new int[m + 1][n + 1];
        int max = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (matrix[i - 1][j - 1] == '0') {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i][j - 1], dp[i - 1][j])) + 1;
                }
                max = Math.max(max, dp[i][j] * dp[i][j]);
            }
        }
        return max;
    }
}
```

T: O(mn)		S: O(mn)



