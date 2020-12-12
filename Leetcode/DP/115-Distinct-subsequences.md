---
title: Hard | Distinct Subsequences 115
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-05-24 01:59:25
---

Given a string **S** and a string **T**, count the number of distinct subsequences of **S** which equals **T**.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, `"ACE"` is a subsequence of `"ABCDE"`while `"AEC"` is not).

It's guaranteed the answer fits on a 32-bit signed integer.

[Leetcode](https://leetcode.com/problems/distinct-subsequences/)

<!--more-->

**Example:**

```
Input: S = "babgbag", T = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
```

---

#### Tricky 

DP problem.

1. Subproblems: prefix:

    `s[:i] t[:j]` means `the number of subsequences s[:i] contains t[:j]`. 

   \# of subproblems: O(m * n)

2. Guess: 

   If `s[i] != t[j]`, we could ignore `s[i]` and align substring `s[i - 1]` contains `t[j]`, `dp[i][j] = dp[i-1][j]`.

   If `s[i] == t[j]`, there're two possible cases: one is subsequences contains `t[j]`, one does not.

   So the one contains `t[j]` is `dp[i - 1][j - 1]`, the one does not is `dp[i - 1][j]`.

   `dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]`.

3. Recurrence: 

   ```java
   if (s[i] == t[j]) {
   	dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
   } else {
   	dp[i][j] = dp[i - 1][j]
   }
   ```

   time/subproblem: O(1)

4. Topological order: 

   from top to down, from left to right

   Total time: O(m * n)

5. Original problem

   `dp[m][n]`

   Initial status: `dp[i][0] == 1` means all substrings contains `""` as subsequences.

---

#### Standard solution  

```java
class Solution {
    public int numDistinct(String s, String t) {
        if (s == null || t == null || (s.length() == 0 && t.length() != 0)) return 0;
        if (t.length() == 0) return 1;
        int m = s.length();
        int n = t.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i < m + 1; i++) {
            dp[i][0] = 1;                      // ininital status
        }
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        return dp[m][n];
    }
}
```

T: O(mn)		S: O(mn)

