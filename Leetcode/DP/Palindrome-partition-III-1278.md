---
title: Hard | Palindrome Partition III 1278
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-07 21:52:27
---

You are given a string `s` containing lowercase letters and an integer `k`. You need to :

- First, change some characters of `s` to other lowercase English letters.
- Then divide `s` into `k` non-empty disjoint substrings such that each substring is palindrome.

Return the minimal number of characters that you need to change to divide the string.

[Leetcode](https://leetcode.com/problems/palindrome-partitioning-iii/)

<!--more-->

**Example 1:**

```
Input: s = "abc", k = 2
Output: 1
Explanation: You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.
```

**Example 2:**

```
Input: s = "aabbc", k = 3
Output: 0
Explanation: You can split the string into "aa", "bb" and "c", all of them are palindrome.
```

**Example 3:**

```
Input: s = "leetcode", k = 8
Output: 0
```

---

#### Tricky 

This is a follow up to [Palindrome II](https://leetcode.com/problems/palindrome-partitioning-ii/).

In *Palindrome II*, we use `isPalin[j][i]` to determine whether a substring is a palindrome.

Here we use `minCost[j][i]` to represent the min cost to convert a substring to a palindrome.

`minCost[j][i] = (s[j] == s[i] ? 0 : 1) + minCost[j + 1][i - 1]`

Then we use `dp[k][i]` to represent partition `s[:i]` into `k` parts.

**Mind the initialization:** 

`k == 1` we need initialize. And `i` must be greater than or equal to `k`: `i >= k`

```java
for (int i = 1; i <= n; i++) {
  dp[1][i] = minCost[1][i];       // initialize
}        

for (int k = 2; k <= K; k++) {
  for (int i = k; i <= n; i++) {  // i must >= k
    int min = Integer.MAX_VALUE;
    for (int j = 1; j < i; j++) {
      min = Math.min(min, dp[k - 1][j] + minCost[j + 1][i]);
    }
    dp[k][i] = min;
  }
}
```

```java
class Solution {
    public int palindromePartition(String s, int K) {
        if (s == null || s.length() == 0) return 0;
        int n = s.length();
        int[][] dp = new int[K + 1][n + 1];
        int[][] minCost = new int[n + 1][n + 1];  // determine minCost to convert a string to palindrome
        
        for (int len = 2; len <= n; len++) {
            for (int i = 1, j = len; j <= n; i++, j++) {
                if (s.charAt(i - 1) == s.charAt(j - 1)) {
                    minCost[i][j] = j - i < 3 ? 0 : minCost[i + 1][j - 1];
                } else {
                    minCost[i][j] = j - i < 3 ? 1 : minCost[i + 1][j - 1] + 1;
                }
            }
        }
        
        for (int i = 1; i <= n; i++) {
            dp[1][i] = minCost[1][i];       // initialize
        }        
        
        for (int k = 2; k <= K; k++) {
            for (int i = k; i <= n; i++) {  // i must >= k
                int min = Integer.MAX_VALUE;
                for (int j = 1; j < i; j++) {
                    min = Math.min(min, dp[k - 1][j] + minCost[j + 1][i]);
                }
                dp[k][i] = min;
            }
        }
        
        return dp[K][n];
    }
}
```

T: O(n^2\*k)			S: O(n^2)