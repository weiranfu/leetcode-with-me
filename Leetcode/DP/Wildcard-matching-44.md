---
title: Hard | Wildcard Matching 44
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - DP
date: 2020-01-19 10:01:35
---

Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` and `'*'`.

```
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
```

The matching should cover the **entire** input string (not partial).

[Leetcode](https://leetcode.com/problems/wildcard-matching/)

<!--more-->

**Note:**

- `s` could be empty and contains only lowercase letters `a-z`.
- `p` could be empty and contains only lowercase letters `a-z`, and characters like `?` or `*`.

**Example 1:**

```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2:**

```
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
```

**Example 3:**

```
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
```

**Example 4:**

```
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
```

**Example 5:**

```
Input:
s = "acdcb"
p = "a*c?b"
Output: false
```

---

#### Tricky 

This is a DP problem.

1. subproblem: 

   dp[:i] [:j] is match or not

   num of subproblems are O(n* m)

2. guess:

   * if `s[i] == p[j]`, pass s[i] and p[j]. `dp[i][j] = dp[i - 1][j - 1]`
* if `p[j] == '?'`, pass s[i] and p[j]. `dp[i][j] = dp[i - 1][j - 1]`
   * if `p[j] == '*'`,
* match more chars: pass s[i] `dp[i][j] = dp[i - 1][j]`
     * match zero char: pass p[j]. `dp[i][j] = dp[i][j - 1]`

3. Base case:

   `dp[0][0] = true`     match empty char in `s` and `p`.
   
   If `p` start with `*`, we can just pass them. `if (p[j]=='*') dp[0][j] = dp[0][j - 1]`

#### Corner Case

Mind the base case, there could be leading `*` in pattern string, and we could pass them!

---

#### Standard solution 

```java
class Solution {
    public boolean isMatch(String s, String p) {
        if (s == null || p == null) {
            return false;
        }
        boolean[][] dp = new boolean[s.length() + 1][p.length() + 1];
        dp[0][0] = true;
        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '*') {
                dp[0][i + 1] = dp[0][i];
            }
        }
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < p.length(); j++) {
                if (s.charAt(i) == p.charAt(j) || p.charAt(j) == '?') {
                    dp[i + 1][j + 1] = dp[i][j];
                } else if (p.charAt(j) == '*') {
                    dp[i + 1][j + 1] = dp[i][j + 1] || dp[i + 1][j];
                }
            }
        }
        return dp[s.length()][p.length()];
    }
}
```

T: O(m* n)			S: O(m* n)
