---
title: Medium | Best Time to Buy and Sell Stock with Cooldown 309
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-02 23:39:59
---

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

[Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

<!--more-->

**Example:**

```
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

**Follow up:** 

[Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

---

#### Tricky 

* DP

  Use `dp[i]` means max profit we can get at index `i`.

  * Don't sell stock.  `dp[i] = dp[i - 1]`
  * Sell stock. Find the max profit: `max{ prices[i] - prices[j] + dp[j - 2] for j in [0, i)}`

  ```java
  class Solution {
      public int maxProfit(int[] prices) {
          if (prices == null || prices.length == 0) return 0;
          int n = prices.length;
          int[] dp = new int[n];
          dp[0] = 0;
          for (int i = 1; i < n; i++) {
              int max = Integer.MIN_VALUE;
              for (int j = 0; j < i; j++) {
                  max = Math.max(max, prices[i] - prices[j] + (j >= 2 ? dp[j - 2] : 0));
              } 
              dp[i] = Math.max(dp[i - 1], max);
          }
          return dp[n - 1];
      }
  }
  ```

  T: O(n^2)		S: O(n)

* DP

  `dp[i][k][0]` means we are at sell state(has 0 stocks at hand) with at most k transactions.

  `dp[i][k][1]` means we are at buy state(has 1 stocks at hand) with at most k transactions.

  More details are in this [Post](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75924/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems)

  Use `preSecSell` to store the `dp[i - 2][k][0]`.

  ```java
  class Solution {
      public int maxProfit(int[] prices) {
          if (prices == null || prices.length == 0) return 0;
          int n = prices.length;
          int buy = Integer.MIN_VALUE;
          int sell = 0;
          int preSecSell = 0;
          for (int price : prices) {
              int preBuy = buy;
              buy = Math.max(buy, preSecSell - price);
              preSecSell = sell;
              sell = Math.max(sell, preBuy + price);
          }
          return sell;
      }
  }
  ```

  T: O(n)		S: O(1)

