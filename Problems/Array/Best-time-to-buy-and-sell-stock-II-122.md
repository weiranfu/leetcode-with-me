---
title: Easy | Best Time to Buy and Sell Stock II 122
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-05-25 02:23:23
---

Say you have an array `prices` for which the *i*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

**Note:** You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

[Leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

<!--more-->

**Example 1:**

```
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
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

We could buy a stock multiple times.

This is still a [maximum subarray problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem), we could to convert this array to increasing array `prices[i] - prices[i - 1]`. If `prices[i] - prices[i - 1] > 0`, we add it to `currSum`, `currSum += prices[i] - prices[i - 1]`. If we want to achieve hightest profit, we need to get the total sum of `currSum` for multiple transactions.

---

#### First solution

```java
class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        if (prices == null || prices.length == 0) return res;
        int n = prices.length;
        int currSum = 0;
        for (int i = 1; i < n; i++) {
            if (prices[i] > prices[i - 1]) {             // if increasing
                currSum += prices[i] - prices[i - 1];   // sum of subarray
            } else {
                res += currSum;                       // multiple transaction
                currSum = 0;
            }
        }
        res += currSum;
        return res;
    }
}
```

T: O(n)		S: O(1)

---

#### Optimize  

We don't need `currSum`, we could directly add positive `prices[i] - price[i - 1]` into `res` result.

```java
class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        if (prices == null || prices.length == 0) return res;
        int n = prices.length;
        for (int i = 1; i < n; i++) {
            if (prices[i] > prices[i - 1]) {
                res += prices[i] - prices[i - 1]; 
            }
        }
        return res;
    }
}
```

T: O(n)		S: O(1)

