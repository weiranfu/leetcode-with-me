---
title: Hard | Minimum Insertion Steps to Make a String Palindrome 1312
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-01-05 17:03:04
---

Given a string `s`. In one step you can insert any character at any index of the string.

Return *the minimum number of steps* to make `s` palindrome.

A **Palindrome String** is one that reads the same backward as well as forward.

[Leetcode](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)

<!--more-->

**Example 1:**

```
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we don't need any insertions.
```

**Example 2:**

```
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
```

**Example 3:**

```
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
```

**Example 4:**

```
Input: s = "g"
Output: 0
```

**Example 5:**

```
Input: s = "no"
Output: 1
```

**Constraints:**

- `1 <= s.length <= 500`
- All characters of `s` are lower case English letters.

---

#### Tricky 

This is a common Paranthesization DP problem.  

The subproblem is to check substring s[i, j] whether a palindrome.

The # of subproblems is O(n^2)

Recurrence is : `dp[i][j] = Math.min(1 + dp[i][j-1], 1 + dp[i+1][j])`

The topological order is: from small pairs to large pairs.

The overall runtime is: # of subproblems * time/subproblem = O(n^2) * O(1) = O(n^2)

---

#### DP: Bottom-up 

```java
class Solution {
    public int minInsertions(String s) {
        char[] cs = s.toCharArray();
        int n = s.length();
        int[][] dp = new int[n][n];
        for (int interval = 0; interval < n; interval++) {
            for (int i = 0; i < n - interval; i++) {
                if (interval == 0) {
                    dp[i][i] = 0;
                } else if (cs[i] == cs[i+interval]) {
                    dp[i][i+interval] = dp[i+1][i+interval-1];
                } else {
                    dp[i][i+interval] = 
                      Math.min(1 + dp[i+1][i+interval], 1 + dp[i][i+interval-1]);
                }
            }
        }
        return dp[0][n - 1];
    }
}
```

T: O(n^2)		S: O(n^2)

---

#### Memorization

```java
class Solution {
    public int minInsertions(String s) {
        char[] cs = s.toCharArray();
        int n = s.length();
        int[][] memo = new int[n][n];
        for (int[] a : memo) {
            Arrays.fill(a, -1);
        }
        return steps(0, n-1, cs, memo);
    }
    
    public int steps(int i, int j, char[] cs, int[][] memo) {
        if (i >= j) return 0;
        if (memo[i][j] != -1) {
            return memo[i][j];
        }
        if (cs[i] == cs[j]) {
            memo[i][j] = steps(i+1, j-1, cs, memo);
        } else {
            memo[i][j] = Math.min(1 + steps(i+1, j, cs, memo), 1 + steps(i, j-1, cs, memo));
        }
        return memo[i][j];
    }
}
```

T: O(n^2)			S: O(n^2)

---

#### Summary 

In Tricky.