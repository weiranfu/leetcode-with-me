---
title: Hard | Best Time to Buy and Sell Stock IV 188
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-06-05 15:48:32
---

Say you have an array for which the *i-*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete at most **k** transactions.

**Note:**
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

[Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

<!--more-->

**Example 1:**

```
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
```

**Example 2:**

```
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
```

**Follow up**

[Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

---

#### Tricky 

* There could be *Memory Limit Error* cause by huge array input. The tricky part to solve it is that:

   When `k >= len / 2`, we could make as many transactions as we want.

* We store the `k` transaction as a dimention of DP. `dp[k][i]` means we perform at most k transactions from `day 0` to `day i`.

  There're two cases in `day i`.

  * Do nothing: `dp[k][i] = dp[k][i - 1]`

  * Sell stock at `day i`: we need to find when we buy the stock and achieve the max profit.

    `dp[k][i] = max { dp[k - 1][j - 1] + prices[i] - prices[j] } for j in [1, i)`

    Note: j could not be i.

* We could simplify O(kn^2) DP to O(kn), cause we could find the `max` result during DP.

---

#### First solution 

```java
class Solution {
    public int maxProfit(int K, int[] prices) {
        if (K == 0 || prices.length <= 1) return 0;
        int n = prices.length;
        
        if (K >= n / 2) return quickSolve(prices);
        
        int[][] dp = new int[K + 1][n];
        for (int k = 1; k <= K; k++) {
            for (int i = 1; i < n; i++) {
                int max = prices[i] - prices[0];    // find max if we sell on day i
                for (int j = 1; j < i; j++) {
                    max = Math.max(max, dp[k - 1][j - 1] + prices[i] - prices[j]);
                }
                dp[k][i] = Math.max(dp[k][i - 1], max);//compare with do nothing on dayi
            }
        }
        return dp[K][n - 1];
    }
    
    private int quickSolve(int[] prices) {
        int res = 0;
        int n = prices.length;
        for (int i = 1; i < n; i++) {
            res += Math.max(0, prices[i] - prices[i - 1]);
        }
        return res;
    }
}
```

T: O(kn^2)		S: O(nk)

---

#### Calculate max along with DP

We could calculate max during DP process. So we could simplify the code as below.

```java
class Solution {
    public int maxProfit(int K, int[] prices) {
        if (K == 0 || prices.length <= 1) return 0;
        int n = prices.length;
        
        if (K >= n / 2) return quickSolve(prices);
        
        int[][] dp = new int[K + 1][n];
        for (int k = 1; k <= K; k++) {
            int max = -prices[0];   // initial max
            for (int i = 1; i < n; i++) {
                if (i > 1) {        // find max from [1, i] during DP
                    max = Math.max(max, dp[k - 1][i - 2] - prices[i - 1]);
                }
                dp[k][i] = Math.max(dp[k][i - 1], prices[i] + max);
            }
        }
        return dp[K][n - 1];
    }
    
    private int quickSolve(int[] prices) {
        int res = 0;
        int n = prices.length;
        for (int i = 1; i < n; i++) {
            res += Math.max(0, prices[i] - prices[i - 1]);
        }
        return res;
    }
}
```

T: O(kn)		S: O(nk)

---

#### Calculate max after we get dp

Since we need to find max value from `[1, i]` exclusive `i`, we could update the max value after we get `dp[k][i]`.

So we could exchange code at line 13 with line 15

```java
class Solution {
    public int maxProfit(int K, int[] prices) {
        if (K == 0 || prices.length <= 1) return 0;
        int n = prices.length;
        
        if (K >= n / 2) return quickSolve(prices);
        
        int[][] dp = new int[K + 1][n];
        for (int k = 1; k <= K; k++) {
            int max = -prices[0];
            for (int i = 1; i < n; i++) {
                dp[k][i] = Math.max(dp[k][i - 1], prices[i] + max);
                max = Math.max(max, dp[k - 1][i - 1] - prices[i]);// update max
            }
        }
        return dp[K][n - 1];
    }
    
    private int quickSolve(int[] prices) {
        int res = 0;
        int n = prices.length;
        for (int i = 1; i < n; i++) {
            res += Math.max(0, prices[i] - prices[i - 1]);
        }
        return res;
    }
}
```

T: O(kn)		S: O(nk)

---

#### Compact DP array into 1D

Since we find `dp[k][i]` only depend on `dp[k][i - 1]` or `dp[k - 1][i - 1]`, we could compact DP into 1D.

The first thing is that we need to swap two `for` loops to compact on `i` dimention.

**We need `max[k]` to store the max with different k value.** 

```java
class Solution {
    public int maxProfit(int K, int[] prices) {
        if (K == 0 || prices.length <= 1) return 0;
        int n = prices.length;
        
        if (K >= n / 2) return quickSolve(prices);
        
        int[][] dp = new int[K + 1][n];
        int[] max = new int[K + 1];         // to store max with different k
        Arrays.fill(max, -prices[0]);
        for (int i = 1; i < n; i++) {
            for (int k = 1; k <= K; k++) {
                dp[k][i] = Math.max(dp[k][i - 1], prices[i] + max[k]);
                max[k] = Math.max(max[k], dp[k - 1][i - 1] - prices[i]);
            }
        }
        return dp[K][n - 1];
    }
    
    private int quickSolve(int[] prices) {
        int res = 0;
        int n = prices.length;
        for (int i = 1; i < n; i++) {
            res += Math.max(0, prices[i] - prices[i - 1]);
        }
        return res;
    }
}
```

Then we could compact `dp[k][n]` into `dp[k]`.

```java
class Solution {
    public int maxProfit(int K, int[] prices) {
        if (K == 0 || prices.length <= 1) return 0;
        int n = prices.length;
        
        if (K >= n / 2) return quickSolve(prices);
        
        int[] dp = new int[K + 1];
        int[] max = new int[K + 1];
        Arrays.fill(max, -prices[0]);
        for (int i = 1; i < n; i++) {
            for (int k = 1; k <= K; k++) {
                dp[k] = Math.max(dp[k], prices[i] + max[k]);
                max[k] = Math.max(max[k], dp[k - 1] - prices[i]);
            }
        }
        return dp[K];
    }
    
    private int quickSolve(int[] prices) {
        int res = 0;
        int n = prices.length;
        for (int i = 1; i < n; i++) {
            res += Math.max(0, prices[i] - prices[i - 1]);
        }
        return res;
    }
}
```

T: O(kn)		S: O(k)