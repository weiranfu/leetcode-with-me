---
title: Hard | Regular Expression Matching 10
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - Design
date: 2020-01-22 20:36:26
---

Given an input string (`s`) and a pattern (`p`), implement regular expression matching with support for `'.'` and `'*'`.

```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
```

The matching should cover the **entire** input string (not partial).

**Note:**

- `s` could be empty and contains only lowercase letters `a-z`.
- `p` could be empty and contains only lowercase letters `a-z`, and characters like `.` or `*`.

[Leetcode](https://leetcode.com/problems/regular-expression-matching/)

<!--more-->

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
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

**Example 3:**

```
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

**Example 4:**

```
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
```

**Example 5:**

```
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
```

**Follow up:**

[Wildcard Matching](https://aranne.github.io/2020/01/19/44-Wildcard-matching/)

---

#### Tricky 

This problem is a typical two words matching problem.

Subproblems: s[i:] and p[j:]        # of subproblems is O(m*n)

Guess: 

* if `s[i] == p[j]` , we can pass these two chars, `dp[i][j] = dp[i - 1][j - 1]`

* if `p[j] == '.'`, we can pass two chars, `dp[i][j] = dp[i - 1][j - 1]`

* if `p[j] == '*'`, 

  * we can match one or more chars, and check preceding char to make sure 

    `p[j-1] == s[i] or p[j-1] == '.'`, then we can pass `s[i]`

    `dp[i][j] = dp[i - 1][j]`
  
  * we can match zero chars, we can pass preceding char and `*`:  
  
    `dp[i][j] = dp[i][j - 2]`

Base case:

`dp[0][0] = true`        match empty char in `s` and `p`

we can pass some leading `*` in pattern. 

```java
s = "aab"
p = "c*a*b"
```

`dp[0][2] = dp[0][0] = true`

```java
dp[0][0] = true;
for (int i = 2; i <= n; i++) {
	if (p.charAt(i - 1) == '*') {
		dp[0][i] = dp[0][i - 2];  // we can jump *
	}
}
```

#### Corner Case

We need to consider the situation that `.*`, which means the preceding char can match to any char.

---

#### DP

```java
class Solution {
    public boolean isMatch(String s, String p) {
        if (s == null || p == null) return false;
        int m = s.length();
        int n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;
        for (int i = 2; i <= n; i++) {
            if (p.charAt(i - 1) == '*') {
                dp[0][i] = dp[0][i - 2];  // we can jump *
            }
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == p.charAt(j - 1) || p.charAt(j - 1) == '.') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p.charAt(j - 1) == '*') {
                    if (j > 1 && (p.charAt(j - 2) == s.charAt(i - 1) 
                              		|| p.charAt(j - 2) == '.')) {
                        dp[i][j] = dp[i - 1][j];
                    }
                    dp[i][j] |= dp[i][j - 2];
                }
            }
        }
        return dp[m][n];
    }
}
```

T: O(mn)		S: O(mn)