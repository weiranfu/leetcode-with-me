---
title: Medium | Is Subsequence 392
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-09-10 20:28:26
---

Given a string **s** and a string **t**, check if **s** is subsequence of **t**.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

**Follow up:**
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

[Leetcode](https://leetcode.com/problems/is-subsequence/)

<!--more-->

**Example 1:**

```
Input: s = "abc", t = "ahbgdc"
Output: true
```

**Example 2:**

```
Input: s = "axc", t = "ahbgdc"
Output: false
```

**Constraints:**

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- Both strings consists only of lowercase characters.

---

#### Brute Force DP

Use `dp[i][j]` to store whether `t[j]` contains `s[i]`.

```java
class Solution {
    public boolean isSubsequence(String s, String t) {
        int m = s.length(), n = t.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        Arrays.fill(dp[0], true);
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if ((s.charAt(i - 1) == t.charAt(j - 1) && dp[i - 1][j - 1]) || dp[i][j - 1]) {
                    dp[i][j] = true;
                }
            }
        }
        return dp[m][n];
    }
}
```

T: O(m\*n)			S: O(m\*n)

---

#### Greedy

**If a char at `s[i]` appears in two positions of `t`, `t1` and `t2`, we always choose the previous one `t1`.**

So we always choose the previous char in `t` to match with same char in `s`.

```java
class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.length() == 0) return true;
        int m = s.length(), n = t.length();
        for (int i = 0, j = 0; j < n; j++) {
            if (t.charAt(j) == s.charAt(i)) {
                i++;
                if (i == m) return true;
            }
        }
        return false;
    }
}
```

T: O(n)			S: O(1)

---

#### Follow up: Multiple s  

If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

If we still match each `Sk` with `t`, it will take O(kn), which is inefficient.

We need to abstract a data structure to store all info of `t` and check with each `Sk`.

**We could use a `List<Integer>[] idx` to store each chars' indices in `t`, then only search the first occurrence of char after a certain position.**

**Since indices are sorted, we could use a binary search to achieve that!**

```java
class Solution {
    public List<Boolean> isSubsequence(List<String> strs, String t) {
        int n = t.length();
        List<Integer>[] indices = new List[26];
        for (int i = 0; i < 26; i++) {
            indices[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            indices[t.charAt(i) - 'a'].add(i);
        }
        List<Boolean> res = new ArrayList<>();
        outer:
        for (String s : strs) {
            if (s.length() == 0) {
                res.add(true);
                continue;
            }
            int m = s.length();
            int prev = -1;
            for (int i = 0; i < m; i++) {
                char c = s.charAt(i);
                if (indices[c - 'a'].size() == 0) {
                    res.add(false);
                    continue outer;
                }
                int p = binarySearch(indices[c - 'a'], prev);
                if (p == -1) {
                    res.add(false);
                    continue outer;
                }
                prev = p;
            }
            res.add(true);
        }
    }
    private int binarySearch(List<Integer> list, int prev) {
        int l = 0, r = list.size();
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (list.get(mid) > prev) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l == list.size() ? -1 : list.get(l);
    }
}
```

T: O(k\*m\*logL)			S: O(n)