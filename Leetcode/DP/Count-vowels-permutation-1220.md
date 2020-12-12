---
title: Hard | Count Vowels Permutation 1220
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-02 16:38:52
---

Given an integer `n`, your task is to count how many strings of length `n` can be formed under the following rules:

- Each character is a lower case vowel (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`)
- Each vowel `'a'` may only be followed by an `'e'`.
- Each vowel `'e'` may only be followed by an `'a'` or an `'i'`.
- Each vowel `'i'` **may not** be followed by another `'i'`.
- Each vowel `'o'` may only be followed by an `'i'` or a `'u'`.
- Each vowel `'u'` may only be followed by an `'a'.`

Since the answer may be too large, return it modulo `10^9 + 7.`

[Leetcode](https://leetcode.com/problems/count-vowels-permutation/)

<!--more-->

---

#### Tricky 

* We need to store previous ending char in `dp`. So `dp[i][j]` means length is `i + 1` ending with `char j` 

  So we can easily find the transition function.

* How to solve `too large` answer?

  We need to use `long` instead of `int` in `dp[]` array. We need to `mod` intermediate result.

---

#### Standard solution  

```java
class Solution {
    /*
    a: 0, e: 1, i: 2, o:3, u:4
    */
    public int countVowelPermutation(int n) {
        if (n == 0) return 0;
        int mod = (int)1e9 + 7;
        long[][] dp = new long[n][5];
        for (int i = 0; i < 5; i++) {
            dp[0][i] = 1;
        }
        for (int i = 0; i < n - 1; i++) {
            dp[i + 1][0] = (dp[i][1] + dp[i][2] + dp[i][4]) % mod;
            
            dp[i + 1][1] = (dp[i][0] + dp[i][2]) % mod;
            
            dp[i + 1][2] = (dp[i][1] + dp[i][3]) % mod;
            
            dp[i + 1][3] = dp[i][2] % mod;
            
            dp[i + 1][4] = (dp[i][2] + dp[i][3]) % mod;
        }
        long res = 0;
        for (int i = 0; i < 5; i++) {
            res = (res + dp[n - 1][i]) % mod;       // DON'T use res += dp[n-1][i] % mod
        }
        return (int)res;
    }
}
```

T: O(n)		S: O(n)