---
title: Hard | Interleaving String
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-05-20 22:13:57
---

Given *s1*, *s2*, *s3*, find whether *s3* is formed by the interleaving of *s1* and *s2*.

[Leetcode](https://leetcode.com/problems/interleaving-string/)

<!--more-->

**Example 1:**

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
```

**Example 2:**

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
```

---

#### Tricky 

How to store the intermediate result when we use up `i` letters in `s1` and `j` letters in `s2`.

**One observation: `len(s1) + len(s2) == len(s3)`, so the next char need to compare is at `i + j - 1` in `s3`**.

So we maintain a `dp[n1][n2]`.

`char target = s3.charAt(i + j - 1)`

`if (s1.charAt(i - 1) == target) dp[i][j] = dp[i - 1][j]`

`if (s2.charAt(j - 1) == target) dp[i][j] = dp[i][j - 1]`

---

#### My thoughts 

I firstly maintain a 3D DP table to cache the intermediate result when we use up `i` letters in `s1` and `j` letters in `s2` and next char is at `k` in `s3`.

---

#### First solution 

```java
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int n1 = s1.length();
        int n2 = s2.length();
        int n3 = s3.length();
        boolean[][][] dp = new boolean[n1+1][n2+1][n3+1];
        dp[0][0][0] = true;
        for (int i = 0; i < n1 + 1; i++) {
            for (int j = 0; j < n2 + 1; j++) {
                for (int k = 1; k < n3 + 1; k++) {
                    if (i == 0 && j == 0) continue;
                    char target = s3.charAt(k - 1);
                    boolean res = false;
                    if (i != 0 && target == s1.charAt(i - 1)) {
                        res = res || dp[i-1][j][k-1];
                    }
                    if (j != 0 && target == s2.charAt(j - 1)) {
                        res = res || dp[i][j-1][k-1];
                    }
                    dp[i][j][k] = res;
                }
            }
        }
        return dp[n1][n2][n3];
    }
}
```

T: O(n^3)			S: O(n^3)

---

#### Optimized

**One observation: `len(s1) + len(s2) == len(s3)`**

Actually, if we use up `i` letters in `s1` and `j`  letters in `s2`, then the next target char in `s3` will be at position `i + j - 1`.

So we just need a 2D DP table to save intermediate result.

```java
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int n1 = s1.length();
        int n2 = s2.length();
        int n3 = s3.length();
        if (n1 + n2 != n3) return false;
        boolean[][] dp = new boolean[n1 + 1][n2 + 1];
        dp[0][0] = true;
        for (int i = 0; i < n1 + 1; i++) {
            for (int j = 0; j < n2 + 1; j++) {
                if (i == 0 && j == 0) continue;
                char target = s3.charAt(i + j - 1);
                boolean res = false;
                if (i != 0 && s1.charAt(i - 1) == target) {
                    res = res || dp[i - 1][j];
                }
                if (j != 0 && s2.charAt(j - 1) == target) {
                    res = res || dp[i][j - 1];
                }
                dp[i][j] = res;
            }
        }
        return dp[n1][n2];
    }
}
```

T: O(n^2)		S: O(n^2)

---

#### Summary 

In tricky.