---
title: Hard | Paint House II 265
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-02 22:52:22
---

There are a row of *n* houses, each house can be painted with one of the *k* colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a `*n* x *k*` cost matrix. For example, `costs[0][0]` is the cost of painting house 0 with color 0; `costs[1][2]` is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note: Could you devise a O(nk) solution?

[Leetcode](https://leetcode.com/problems/paint-house-ii/)

<!--more-->

**Example:**

```
Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
```

**Follow up:** 

[Paint House III](https://leetcode.com/problems/paint-house-iii/)

---

#### Tricky 

DP

`dp[i][k]` means paint `i`th house using `k` color.

To compute `dp[i][j]`, we need to find out the minimum cost of previous house using different color.

* O(n \* k^2) 

  Iterate all possible color of previous house except the color of current house to find min cost.

* O(n \* k) 

  Use `preMin`, `preSecMin`, `preMinColor` to store the min cost, second min cost, min cost color of previous house using different colors.

  If current house's color is same as `minColor`, we choose `preSecMin`. Otherwise we choose `preMin`

---

#### DP

```java
class Solution {
    public int minCostII(int[][] costs) {
        if (costs == null || costs.length == 0 || costs[0].length == 0) return 0;
        int m = costs.length;
        int n = costs[0].length;
        int[][] dp = new int[m + 1][n];
        for (int i = 1; i <= m; i++) {
            for (int j = 0; j < n; j++) {
                int min = Integer.MAX_VALUE;
                for (int k = 0; k < n; k++) {
                    if (k == j) continue;
                    min = Math.min(min, dp[i - 1][k]);
                }
                dp[i][j] = (min == Integer.MAX_VALUE ? 0 : min) + costs[i - 1][j];
            }
        }
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            res = Math.min(res, dp[m][i]);
        }
        return res;
    }
}
```

T: O(n \* k^2)			S: O(nk)

---

#### Optimized

```java
class Solution {
    public int minCostII(int[][] costs) {
        if (costs == null || costs.length == 0 || costs[0].length == 0) return 0;
        int m = costs.length;
        int n = costs[0].length;
        int[][] dp = new int[m + 1][n];
        int preMin = Integer.MAX_VALUE, preMinColor = -1, preSecMin = Integer.MAX_VALUE;
        for (int i = 1; i <= m; i++) {
            int min = Integer.MAX_VALUE, minColor = -1, secMin = Integer.MAX_VALUE;
            for (int j = 0; j < n; j++) {
                int preCost = (j != preMinColor) ? preMin : preSecMin;
                dp[i][j] = (preCost == Integer.MAX_VALUE ? 0 : preCost) + costs[i - 1][j];
                if (dp[i][j] < min) {            // update min
                    secMin = min;
                    min = dp[i][j];
                    minColor = j;
                } else if (dp[i][j] < secMin) {  // update seconde min
                    secMin = dp[i][j];
                }
            }
            preMin = min;
            preMinColor = minColor;
            preSecMin = secMin;
        }
        return preMin;
    }
}
```

T: O(n \* k)				S: O(nk)

