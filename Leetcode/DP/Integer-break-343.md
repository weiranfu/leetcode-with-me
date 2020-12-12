---
title: Medium | Integer Break 343
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-05 22:41:48
---

Given a positive integer *n*, break it into the sum of **at least** two positive integers and maximize the product of those integers. Return the maximum product you can get.

[Leetcode](https://leetcode.com/problems/integer-break/)

<!--more-->

**Example 1:**

```
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
```

**Example 2:**

```
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
```

**Note**: You may assume that *n* is not less than 2 and not larger than 58.

---

#### Tricky 

This is a **complete knapsack** problem.

The key is that we need to use at least 2 elements in our knapsack.

So the items we can choose is from 1 to n - 1.

```java
class Solution {
    public int integerBreak(int n) {
        if (n == 0) return 0;
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i < n; i++) {         // items we choose from 1 to n - 1
            for (int j = i; j <= n; j++) {
                dp[j] = Math.max(dp[j], dp[j - i] * i);
            }
        }
        return dp[n];
    }
}
```

T: O(n ^ 2)			S: O(n)