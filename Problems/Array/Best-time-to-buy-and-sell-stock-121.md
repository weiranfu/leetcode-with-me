---
title: Easy | Best Time to Buy and Sell Stock 121
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-05-25 02:02:45
---

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

[Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

<!--more-->

**Example 1:**

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

**Example 2:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

**Follow up:** [Best Time to Buy and Sell Stock II](https://aranne.github.io/2020/05/25/122-Best-time-to-buy-and-sell-stock-II/#more)

---

#### Tricky 

We could see this problem as a [Maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem), because if we want to get the best time to buy  and sell stock, which means we need to get the maximum sequentially subarray sums of `prices[i] - prices[i - 1]`. If `sum < 0`, we choose not to buy stock.

---

#### My thoughts 

Keep a `min` to maintain the lowest price, and find best time to sell it. 

Keep updating `min` when `prices[i] < min`.

---

#### First solution 

```java
class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        if (prices == null || prices.length == 0) return res;
        int n = prices.length;
        int min = prices[0];
        for (int i = 0; i < n; i++) {
            if (prices[i] > min) {
                res = Math.max(res, prices[i] - min);
            } else if (prices[i] < min) {
                min = prices[i];
            }
        }
        return res;
    }
}
```

T: O(n)		S: O(1)

---

#### Optimized

**Maximum subarray problem**

```java
class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        if (prices == null || prices.length == 0) return res;
        int n = prices.length;
        int currSum = 0;                 // maintain current sum of subarray.
        for (int i = 1; i < n; i++) {
            currSum = Math.max(0, currSum) + prices[i] - prices[i - 1];
            res = Math.max(res, currSum);
        }
        return res;
    }
}
```

T: O(n)		S: O(1)

---

#### Summary 

**Best time to buy and sell stock problem is a typical maximum subarray problem.**

