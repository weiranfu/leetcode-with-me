---
title: Medium | Minimum Deletions to Make String Balanced 1653
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-11-14 16:36:11
---

You are given a string `s` consisting only of characters `'a'` and `'b'`.

You can delete any number of characters in `s` to make `s` **balanced**. `s` is **balanced** if there is no pair of indices `(i,j)` such that `i < j` and `s[i] = 'b'` and `s[j]= 'a'`.

Return *the **minimum** number of deletions needed to make* `s` ***balanced***.

[Leetcode](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/)

<!--more-->

**Example 1:**

```
Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
```

**Example 2:**

```
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
```

**Constraints:**

- `1 <= s.length <= 105`
- `s[i]` is `'a'` or `'b'`.

---

#### DP 

We can use `dp[i][0]` to store number of deletions to make `s` ending with `a`.

`dp[i][1]` to store number of deletions to make `s` ending with `b`.

When we meet a `a`, we can choose to end with `a`: `dp[i][0] = dp[i-1][0]` 

or end with `b`: `dp[i][1] = dp[i-1][1] + 1`

When we meet a `b`, we can choose to end with `a`: `dp[i][0] = dp[i-1][0] + 1`

or end with `b`: `dp[i][1] = Math.min(dp[i-1][0], dp[i-1][1])`

```java
class Solution {
    public int minimumDeletions(String s) {
        int n = s.length();
        int[][] cnt = new int[n + 1][2];
        for (int i = 1; i <= n; i++) {
            if (s.charAt(i - 1) == 'a') {
                cnt[i][0] = cnt[i - 1][0];
                cnt[i][1] = cnt[i - 1][1] + 1;
            } else {
                cnt[i][0] = cnt[i - 1][0] + 1;
                cnt[i][1] = Math.min(cnt[i - 1][1], cnt[i - 1][0]);
            }
        }
        return Math.min(cnt[n][0], cnt[n][1]);
    }
}
```

T: O(n)		S: O(n)

---

#### Optimized

Space complexity: O(n) —> O(1)

```java
class Solution {
    public int minimumDeletions(String s) {
        int n = s.length();
        /* cnt[i][0] means ending with a,  
           cnt[i][1] means ending with b
        */
        int a = 0, b = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == 'a') {
                b++;
            } else {
                b = Math.min(a, b);
                a++;
            }
        }
        return Math.min(a, b);
    }
}
```

T:  O(n)		S: O(1)

---

#### Track number of B

We can keep track of how many `b` have already come along --> that is the maximum cost you have to pay to make the string balanced. Concretely: you will only have to delete all previous `b` if at least as many `a` come along.

```java
class Solution {
    public int minimumDeletions(String s) {
        int n = s.length();
        int res = 0, cntB = 0;
        for (int i = 1; i <= n; i++) {
            if (s.charAt(i - 1) == 'b') {
                cntB++;
            } else if (cntB > 0) {
                res++;
                cntB--;
            }
        }
        return res;
    }
}
```

T: O(n)		S: O(1)

