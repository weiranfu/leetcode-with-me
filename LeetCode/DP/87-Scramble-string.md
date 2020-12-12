---
title: Hard | Scramble String
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-05-19 22:13:38
---

Given a string *s1*, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of *s1* = `"great"`:

```
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
```

To scramble the string, we may choose any non-leaf node and swap its two children.

[Leetcode](https://leetcode.com/problems/scramble-string/)

<!--more-->

For example, if we choose the node `"gr"` and swap its two children, it produces a scrambled string `"rgeat"`.

```
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
```

We say that `"rgeat"` is a scrambled string of `"great"`.

Similarly, if we continue to swap the children of nodes `"eat"` and `"at"`, it produces a scrambled string `"rgtae"`.

```
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
```

We say that `"rgtae"` is a scrambled string of `"great"`.

Given two strings *s1* and *s2* of the same length, determine if *s2* is a scrambled string of *s1*.

**Example 1:**

```
Input: s1 = "great", s2 = "rgeat"
Output: true
```

**Example 2:**

```
Input: s1 = "abcde", s2 = "caebd"
Output: false
```

---

#### Tricky

My thoughts 

Use a map to store all possible scrambled strings produced by a substring `s1[i, j]`.

Use `i * n^2 + j` as the index into the map.

Save all possible strings as a set.

---

#### First solution: TLE!!!

```java
class Solution {
    public boolean isScramble(String s1, String s2) {
        if (s1 == null || s2 == null || s1.length() != s2.length()) return false;
        int n = s1.length();
        Map<Integer, Set<String>> map = new HashMap<>();
        getScramble(0, n, s1, map);
        Set<String> set = map.get(n);
        return set.contains(s2);
    }
    
    private void getScramble(int i, int j, String s1, Map<Integer, Set<String>> map) {
        int n = s1.length();
        Set<String> set = new HashSet<>();
        int idx = i * (n+1) * (n+1) + j;
        if (i == j) {
            map.put(idx, set);
        } else if (j - i == 1) {
            set.add(s1.substring(i, j));
            map.put(idx, set);
        } else {
            for (int k = i + 1; k < j; k++) {
                int idx1 = i * (n+1) * (n+1) + k;
                int idx2 = k * (n+1) * (n+1) + j;
                if (!map.containsKey(idx1)) getScramble(i, k, s1, map);
                if (!map.containsKey(idx2)) getScramble(k, j, s1, map);
                Set<String> left = map.get(idx1);
                Set<String> right = map.get(idx2);
                for (String l : left) {
                    for (String r : right) {
                        set.add(l + r);
                        set.add(r + l);
                    }
                }
                map.put(idx, set);
            }
        }
    }
}
```

T: O(n^3*m^2) 			S: O(n^2)

---

#### Optimized

Why TLE error in above code? because we try to get all possible scrambles then check `set.contains(s2)`.

So we could check whether a substring of s1 is a scrambled string of a substring of s2 during DP.

We can divide s1(s2) into two substrings with length `k` and `len-k` and check if the two substrings 

`s1[0, k-1]` and `s1[k, len-1]` are the scrambles of `s2[0, k-1]` and `s2[k,len-1]` or `s2[len-k, len-1]` and `s2[0, len-k-1]`

So this is a interval DP and there're two strings to store, so we need 4D array to maintain.

Because substring's length in two strings are same, so we only need 3D array to maintain.

`dp[len][i][j]` means `s1[i, i+len]` and `s2[j, j + len]` is scrambled.

\# of subproblems: O(n^3)

time/subproblem: O(n)

total time: O(n^4)

```java
class Solution {
    public boolean isScramble(String s1, String s2) {
        if (s1 == null || s2 == null) return true;
        if (s1.length() != s2.length()) return false;
        int n = s1.length();
        boolean[][][] dp = new boolean[n + 1][n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                dp[1][i][j] = s1.charAt(i - 1) == s2.charAt(j - 1);
            }
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 1, j = len; j <= n; i++, j++) {
                for (int u = 1, v = len; v <= n; u++, v++) {
                    for (int k = 1; k < len; k++) {
                        if (dp[k][i][u] && dp[len-k][i+k][u+k]
                            || (dp[k][i][v-k+1] && dp[len-k][j-(len-k)+1][u])) {
                            dp[len][i][u] = true;
                            break;
                        }
                    }
                }
            }
        }
        return dp[n][1][1];
    }
}
```

T: O(n^4)		S: O(n^3)

