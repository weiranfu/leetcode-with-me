---
title: Hard | Strange Printer 664
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-09 23:18:53
---

There is a strange printer with the following two special requirements:

1. The printer can only print a sequence of the same character each time.
2. At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.

Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

[Leetcode](https://leetcode.com/problems/strange-printer/)

<!--more-->

**Example 1:**

```
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
```

**Example 2:**

```
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
```

**Hint**: Length of the given string will not exceed 100.

**Follow up:** 

[Remove Boxes](https://leetcode.com/problems/remove-boxes/)

[Palindrome Removal](https://leetcode.com/problems/palindrome-removal/)

---

#### Tricky 

1. DP

   `dp[i][j]` means min cost for an interval.

   we can just print `i`, `dp[i][j] = dp[i + 1][j] + 1`

   Or we can try to find same color `char[k] == char[i]`

   `dp[i][j] = min(dp[i][k] + dp[k + 1][j])`

   ```java
   class Solution {
       public int strangePrinter(String s) {
           if (s == null || s.length() == 0) return 0;
           int n = s.length();
           int[][] dp = new int[n + 1][n + 1];
           for (int i = 1; i <= n; i++) {
               dp[i][i] = 1;
           }
           for (int len = 2; len <= n; len++) {
               for (int i = 1, j = len; j <= n; i++, j++) {
                   int min = dp[i + 1][j] + 1;
                   for (int k = i + 1; k <= j; k++) {
                       if (s.charAt(k - 1) == s.charAt(i - 1)) {
                           min = Math.min(min, dp[i + 1][k] + (k + 1 > j ? 0 : dp[k + 1][j]));
                       }
                   }
                   dp[i][j] = min;
               }
           }
           return dp[1][n];
       }
   }
   ```

   T: O(n^3)			S: O(n^2)

2. DFS with memorization

   ```java
   class Solution {
       public int strangePrinter(String s) {
           if (s == null || s.length() == 0) return 0;
           int n = s.length();
           int[][] dp = new int[n + 1][n + 1];
           return dfs(1, n, dp, s);
       }
       
       private int dfs(int l, int r, int[][] dp, String s) {
           if (l > r) return 0;
           
           if (dp[l][r] > 0) return dp[l][r];
           
           int min = dfs(l + 1, r, dp, s) + 1;
           for (int k = l + 1; k <= r; k++) {
               if (s.charAt(l - 1) == s.charAt(k - 1)) {
                   min = Math.min(min, dfs(l + 1, k, dp, s) + (k + 1 > r ? 0 : dfs(k + 1, r, dp, s)));
               }
           }
           dp[l][r] = min;
           return min;
       }
   }
   ```

   T: O(n^3)		S: O(n^3)