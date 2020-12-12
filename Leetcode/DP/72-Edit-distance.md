---
title: Hard | Edit Distance 72
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-05-15 17:51:41
---

Given two words *word1* and *word2*, find the minimum number of operations required to convert *word1* to *word2*.

You have the following 3 operations permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

[Leetcode](https://leetcode.com/problems/edit-distance/)

<!--more-->

**Example 1:**

```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

**Example 2:**

```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

---

#### Tricky 

There're three operations when `word1[i] != word2[j]`

* Insert `word2[j]` into `word1` or delete `word2[j]` in `word2`, 

  then pass `word2[j]`:   `dp[i][j] = dp[i][j - 1] + 1`

* delete `word1[i]` in `word1` or insert `word1[i]` in `word2`, 

  then pass `word1[i]`:  `dp[i][j] = dp[i - 1][j] + 1`

* replace `word1[i]` with `word2[j]`, then pass `word1[i]` and `word2[j]`,`dp[i][j] = dp[i-1][j-1] + 1`

---

#### Standard solution  

```java
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        if (m == 0) return n;
        if (n == 0) return m;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i < m + 1; i++) {
            dp[i][0] = i;
        }
        for (int j = 1; j < n + 1; j++) {
            dp[0][j] = j;
        }
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                char c1 = word1.charAt(i - 1);
                char c2 = word2.charAt(j - 1);
                if (c1 == c2) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.min(dp[i][j - 1] + 1, Math.min(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1));
                }
            }
        }
        return dp[m][n];
    }
}
```

T: O(mn)		S: O(mn)