---
title: Easy | Repeated Substring Pattern 459
tags:
  - common
  - tricky
categories:
  - Leetcode
  - KMP
date: 2020-09-20 22:49:43
---

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

[Leetcode](https://leetcode.com/problems/repeated-substring-pattern/)

<!--more-->

**Example 1:**

```
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
```

**Example 2:**

```
Input: "aba"
Output: False
```

**Example 3:**

```
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
```

---

#### Brute Force

Check each possible substrings with length in `[1, n / 2]`

Keep a sliding window of size `len`, and check each char at `cs[i + j]` with the char in the first block `cs[j]`.

```java
class Solution {
    public boolean repeatedSubstringPattern(String s) {
        if (s == null || s.length() == 0) return false;
        int n = s.length();
        char[] cs = s.toCharArray();
        for (int len = 1; len <= n / 2; len++) {
            if (n % len != 0) continue;
            boolean check = true;
            outer:
            for (int i = len; i < n; i += len) {  // sliding window
                for (int j = 0; j < len; j++) {
                    if (cs[j] != cs[i + j]) {
                        check = false;
                        break outer;
                    }
                }
            }
            if (check) return true;
        }
        return false;
    }
}
```

T: O(n^2)			S: O(n)

---

#### KMP

1. Roughly speaking, next[i+1] stores the maximum number of characters that the string is repeating itself up to position i.
2. Therefore, if a string repeats a length 5 substring 4 times, then the last entry would be of value 15.
3. To check if the string is repeating itself, we just need the last entry to be non-zero and str.size() is divisible by `str.size()-last entry`.

```java
class Solution {
    public boolean repeatedSubstringPattern(String s) {
        if (s == null || s.length() == 0) return false;
        int n = s.length();
        int[] next = new int[n + 1];
        for (int i = 1, j = 0; i < n; i++) {
            while (j != 0 && s.charAt(i) != s.charAt(j)) j = next[j];
            if (s.charAt(i) == s.charAt(j)) j++;
            next[i + 1] = j;
        }
        return next[n] != 0 && next[n] % (n - next[n]) == 0;
    }
}
```

T:  O(n)		S: O(n)

