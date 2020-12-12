---
title: Hard | Best Time to Buy and Sell Stock III 123
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-05-25 22:00:12
---

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete at most *two* transactions.

**Note:** You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

[Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

<!--more-->

**Example 1:**

```
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```

**Example 2:**

```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

**Example 3:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

**Follow up:** [Best Time to Buy and Sell Stock IV](https://aranne.github.io/2020/06/05/188-Best-time-to-buy-and-sell-stock-IV/#more)

---

#### Tricky

It's not difficult to get the DP recursive formula:

```
dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]), j=[0..i-1]
```

For k transactions, on i-th day,
if we don't trade then the profit is same as previous day dp[k, i-1];
and if we bought the share on j-th day where j=[0..i-1], then sell the share on i-th day then the profit is prices[i] - prices[j] + dp[k-1, j-1] .
**Actually j can be i as well. When j is i, the one more extra item prices[i] - prices[j] + dp[k-1, j] = dp[k-1, i] looks like we just lose one chance of transaction.**

I see someone else use the formula dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j]), where the last one is dp[k-1, j] instead of dp[k-1, j-1]. It's not the direct sense, as if the share was bought on j-th day, then the total profit of previous transactions should be done on (j-1)th day. However, the result based on that formula is also correct, because if the share was sold on j-th day and then bought again, it is the same if we didn't trade on that day.

1. **So the straigtforward implementation is:**

   ```java
           public int MaxProfitDp(int[] prices) {
               if (prices.Length == 0) return 0;
               var dp = new int[3, prices.Length];
               for (int k = 1; k <= 2; k++)  {
                   for (int i = 1; i < prices.Length; i++) {
                       int min = prices[0];
                       for (int j = 1; j <= i; j++)
                           min = Math.Min(min, prices[j] - dp[k-1, j-1]);
                       dp[k, i] = Math.Max(dp[k, i-1], prices[i] - min);
                   }
               }
   
               return dp[2, prices.Length - 1];
           }
   ```

   T: O(kn^2), 			S: O(kn).

2. **In the above code, min is repeated calculated. It can be easily improved as:**

   ```java
           public int MaxProfitDpCompact1(int[] prices) {
               if (prices.Length == 0) return 0;
               var dp = new int[3, prices.Length];
               for (int k = 1; k <= 2; k++) {
                   int min = prices[0];
                   for (int i = 1; i < prices.Length; i++) {
                       min = Math.Min(min, prices[i] - dp[k-1, i-1]);
                       dp[k, i] = Math.Max(dp[k, i-1], prices[i] - min);
                   }
               }
   
               return dp[2, prices.Length - 1];
           }
   ```

   T: O(kn)				S: O(kn)

3. **If we slight swap the two 'for' loops in order to compact `i` dimension :**

   We need to save min for each transaction, so there are k 'min'.

   ```java
           public int MaxProfitDpCompact1T(int[] prices) {
               if (prices.Length == 0) return 0;
               var dp = new int[3, prices.Length];
               var min = new int[3];
               Arrays.fill(min, prices[0]);
               for (int i = 1; i < prices.Length; i++) {
                   for (int k = 1; k <= 2; k++) {
                       min[k] = Math.Min(min[k], prices[i] - dp[k-1, i-1]);
                       dp[k, i] = Math.Max(dp[k, i-1], prices[i] - min[k]);
                   }
               }
   
               return dp[2, prices.Length - 1];
           }
   ```

   T: O(kn)			S: O(kn)

4. **Compact `i` dimention**

   We can find the second dimension (variable i) is only dependent on the previous one (i-1), so we can compact this dimension. (We can choose the first dimension (variable k) as well since it is also only dependent on its previous one k-1, but can't compact both.)

   ```java
           public int MaxProfitDpCompact2(int[] prices) {
               if (prices.Length == 0) return 0;
               var dp = new int[3];
               var min = new int[3];
               Array.Fill(min, prices[0]);
               for (int i = 1; i < prices.Length; i++)  {
                   for (int k = 1; k <= 2; k++) {
                       min[k] = Math.Min(min[k], prices[i] - dp[k-1]);
                       dp[k] = Math.Max(dp[k], prices[i] - min[k]);
                   }
               }
   
               return dp[2];
           }
   ```

   T: O(kn)		S:  O(k)

5. **In this case, K is 2. We can expand the array to all named variables**

   ```java
           public int MaxProfitDpCompactFinal(int[] prices)  {
               int buy1 = int.MaxValue, buy2 = int.MaxValue;
               int sell1 = 0, sell2 = 0;
   
               for (int i = 0; i < prices.Length; i++) {
                   buy1 = Math.Min(buy1, prices[i]);
                   sell1 = Math.Max(sell1, prices[i] - buy1);
                   buy2 = Math.Min(buy2, prices[i] - sell1);
                   sell2 = Math.Max(sell2, prices[i] - buy2);
               }
   
               return sell2;
           }
   ```

   T: O(n)		S: O(1)

   We can also explain the above codes in other words. On every day, we buy the share with the price as low as we can, and sell the share with price as high as we can. For the second transaction, we integrate the profit of first transaction into the cost of the second buy, then the profit of the second sell will be the total profit of two transactions.

