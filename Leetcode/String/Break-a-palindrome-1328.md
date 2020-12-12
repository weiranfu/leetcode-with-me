---
title: Medium | Break a Palindrome 1328
tags:
  - common
  - tricky
categories:
  - Leetcode
  - String
date: 2020-09-21 11:39:05
---

Given a palindromic string `palindrome`, replace **exactly one** character by any lowercase English letter so that the string becomes the lexicographically smallest possible string that **isn't** a palindrome.

After doing so, return the final string.  If there is no way to do so, return the empty string.

[Leetcode](https://leetcode.com/problems/break-a-palindrome/)

<!--more-->

**Example 1:**

```
Input: palindrome = "abccba"
Output: "aaccba"
```

**Example 2:**

```
Input: palindrome = "a"
Output: ""
```

**Constraints:**

- `palindrome` consists of only lowercase English letters.

---

#### Standard solution  

We search half string for `a`, if we find a `non-'a'` char, we replace it with `a`.

If all chars in `palindrome` is `a`, we replace the last char with `b`.

Corner case: if `palindrome`'s length is `1`, we cannot break it, return `""`.

```java
class Solution {
    public String breakPalindrome(String s) {
        if (s.length() == 1) return "";
        int n = s.length();
        char[] cs = s.toCharArray();
        for (int i = 0; i < n / 2; i++) {
            if (cs[i] != 'a') {
                cs[i] = 'a';
                return String.valueOf(cs);
            }
        }
        cs[n - 1] = 'b';
        return String.valueOf(cs);
    }
}
```

T: O(n)			S: O(n)

