---
title: Hard | Paint House III 1473
tags:
  - tricky
  - Oh-no
categories:
  - Leetcode
  - DP
date: 2020-06-08 16:13:49
---

There is a row of `m` houses in a small city, each house must be painted with one of the `n` colors (labeled from 1 to `n`), some houses that has been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color. (For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods  [{1}, {2,2}, {3,3}, {2}, {1,1}]).

Given an array `houses`, an `m * n` matrix `cost` and an integer `target` where:

- `houses[i]`: is the color of the house `i`, **0** if the house is not painted yet.
- `cost[i][j]`: is the cost of paint the house `i` with the color `j+1`.

Return the minimum cost of painting all the remaining houses in such a way that there are exactly `target` neighborhoods, if not possible return **-1**.

[Leetcode](https://leetcode.com/problems/paint-house-iii/)

<!--more-->

**Example 1:**

```
Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
```

**Example 2:**

```
Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.
```

**Example 3:**

```
Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
Output: 5
```

**Example 4:**

```
Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.
```

**Constraints:**

- `m == houses.length == cost.length`
- `n == cost[i].length`
- `1 <= m <= 100`
- `1 <= n <= 20`
- `1 <= target <= m`
- `0 <= houses[i] <= n`
- `1 <= cost[i][j] <= 10^4`

---

#### Tricky 

We need to store 3D info in DP: `neighborhoods`, `curr index`, `color`. `dp[k][i][c]`

When we are considering `houses[i]`, two possible situations:

* house has been painted: cost must be zero
* house hasn't been painted: cost equals to `cost[i][c]`

When we look at its previous `houses[i - 1]`,

* If their color are same, `neighborhoods` keeps. `dp[k][i][c] = dp[k][i - 1][c]`
* If their color are not same, `neighborhoods` will increase. `dp[k][i][c] = min {dp[k-1][i-1][c1]}`

For base case:

**dp[k] depends on dp[k-1], dp[i] depends on dp[i-1], so we only need to initialize dp\[0]\[0][c]**

**Cause we are finding min value, dp\[0]\[0]\[c] = 0, other dp\[k]\[i]\[c] = Integer.MAX_VALUE**

If we cannot find a valid solution, `dp[target][m][c] == Integer.MAX_VALUE`

#### Oh-no

Casue we initialize `dp\[k]\[i]\[c] = Integer.MAX_VALUE`, we need to mind overflow in transition function.

---

#### Standard solution  

We could do a small pruning when we iterate `houses i`. We could start with `i = k`.

```java
for (int k = 1; k <= target; k++) {
	for (int i = k; i <= m; i++) {        // pruning
	
	}
}
```

**Because we don't need to consider cases that target number of neighborhoods is greater than number of houses.**

```java
class Solution {
    public int minCost(int[] houses, int[][] cost, int m, int n, int target) {
        int[][][] dp = new int[target + 1][m + 1][n + 1];
        for (int i = 0; i <= target; i++) {
            for (int j = 0; j <= m; j++) {
                for (int k = 1; k <= n; k++) {
                    if (i == 0 && j == 0) {
                        dp[i][j][k] = 0;                  // base case
                    } else {
                        dp[i][j][k] = Integer.MAX_VALUE;
                    }
                }
            }
        }
        for (int k = 1; k <= target; k++) {
            for (int i = k; i <= m; i++) {    // pruning
                if (houses[i - 1] != 0) {     // has been painted
                    int color = houses[i - 1];
                    int min = dp[k][i - 1][color];       // prev house with same color
                    for (int c1 = 1; c1 <= n; c1++) {
                        if (c1 == color) continue;
                        min = Math.min(min, dp[k - 1][i - 1][c1]);  // different color
                    }
                    dp[k][i][color] = min;
                } else { 												// hasn't been paited
                    for (int c = 1; c <= n; c++) {
                        int min = dp[k][i - 1][c];
                        for (int c1 = 1; c1 <= n; c1++) {
                            if (c == c1) continue;
                            min = Math.min(min, dp[k - 1][i - 1][c1]);
                        }
                        if (min != Integer.MAX_VALUE) {             // avoid overflow
                            dp[k][i][c] = min + cost[i - 1][c - 1];
                        }
                    }
                }
            }
        }
        int res = Integer.MAX_VALUE;             
        for (int c = 1; c <= n; c++) {
            res = Math.min(res, dp[target][m][c]);
        }
        return res != Integer.MAX_VALUE ? res : -1;       // cannot find solution
    }
}
```

O(k\*m\*n\*n)			S: O(k\*m\*n)