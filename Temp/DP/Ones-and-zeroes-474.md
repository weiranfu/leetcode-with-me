---
title: Medium | Ones and Zeroes 474
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-10 01:59:24
---

Given an array, `strs`, with strings consisting of only `0s` and `1s`. Also two integers `m` and `n`.

Now your task is to find the maximum number of strings that you can form with given **m** `0s` and **n** `1s`. Each `0` and `1` can be used at most **once**.

[Leetcode](https://leetcode.com/problems/ones-and-zeroes/)

<!--more-->

**Example 1:**

```
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0".
```

**Example 2:**

```
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
```

---

#### Tricky 

This is a typical 2D 0-1 knapsack problem.

The volume is number of `1`s, the weight is number of `0`s, and we want to achieve max value(number) of all `strs`.

```java
class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        if (strs == null || strs.length == 0) return 0;
        int N = strs.length;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i < N; i++) {
            int zero = 0;
            int one = 0;
            String s = strs[i];
            for (char c : s.toCharArray()) {
                if (c == '1') one++;
                else zero++;
            }
            for (int j = m; j >= zero; j--) {
                for (int k = n; k >= one; k--) {
                    dp[j][k] = Math.max(dp[j][k], dp[j - zero][k - one] + 1);
                }
            }
        }
        return dp[m][n];
    }
}
```

T: O(N\*m\*n)			S: O(m\*n)