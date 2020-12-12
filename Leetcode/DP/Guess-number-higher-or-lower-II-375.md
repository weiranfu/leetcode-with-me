---
title: Medium | Guess Number Higher or Lower II 375
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-08 16:54:36
---

We are playing the Guess Game. The game is as follows:

I pick a number from **1** to **n**. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay **$x**. You win the game when you guess the number I picked.

[Leetcode](https://leetcode.com/problems/guess-number-higher-or-lower-ii/)

<!--more-->

**Example:**

```
n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
```

Given a particular **n ≥ 1**, find out how much money you need to have to guarantee a **win**.

**Follow up:** 

**[Super Egg Drop](https://leetcode.com/problems/super-egg-drop/)**

---

#### Tricky 

This is a typical interval DP.

`dp[l][r]`: consider interval `[l, r]`, the min cost we need to pay.

When we choose `x`, we need to pay the higher cost of `dp[l][x-1]` and `dp[x+1][r]` to ensure the correctness with certainty

`dp[l][r] = min{ max{ dp[l][k-1], dp[k+1][r] } for k in [l, r-1] }`

Base case:

`dp[i][i] = 0` If there are only one number left, we don't need to guess and pay.

```java
class Solution {
    public int getMoneyAmount(int n) {
        int[][] dp = new int[n + 1][n + 1];
        
        for (int len = 2; len <= n; len++) {
            for (int i = 1, j = len; j <= n; i++, j++) {
                int min = Integer.MAX_VALUE;
                for (int k = i; k < j; k++) {
                    int max = (k == i ? dp[k + 1][j] : Math.max(dp[i][k - 1], dp[k + 1][j]));
                    min = Math.min(min, max + k);
                }
                dp[i][j] = min;
            }
        }
        return dp[1][n];
    }
}
```
T: O(n ^ 2)			S: O(n ^ 2)