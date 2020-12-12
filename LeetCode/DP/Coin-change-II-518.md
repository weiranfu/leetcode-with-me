---
title: Medium | Coin Change II 518
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-06 14:55:15
---

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

[Leetcode](https://leetcode.com/problems/coin-change-2/)

<!--more-->

**Example 1:**

```
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

**Example 2:**

```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

**Example 3:**

```
Input: amount = 10, coins = [10] 
Output: 1
```

---

#### Tricky 

This is a typical **complete knapsack** problem.

For each coin(*item*), we can add more than once.

So for each coin, `dp[i]` means the amount we can form using coins.

```java
class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, Integer.MIN_VALUE);
        dp[0] = 0;
        int[] cnt = new int[amount + 1];
        cnt[0] = 1;
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                int t = Math.max(dp[i], dp[i - coin] + coin);
                int s = 0;
                if (t == dp[i]) s += cnt[i];
                if (t == dp[i - coin] + coin) s += cnt[i - coin];
                dp[i] = t;
                cnt[i] = s;
            }
        }
        return cnt[amount];
    }
}
```

T: O(mn)			S: O(n)

However, `dp[i] == dp[i - coin] + coin`

So we can just use `dp[i]` to store the number of conbinations to make up `amount`.

And `dp[i]`always fill up the amount, so we don't need to initial `dp` with `Integer.MIN_VALUE`

```java
class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];
            }
        }
        return dp[amount];
    }
}
```

T: O(mn)		S: O(n)

