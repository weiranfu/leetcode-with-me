---
title: Medium | Construct K Palindrome Strings
tags:
  - tricky
categories:
  - Leetcode
  - String
date: 2020-05-17 23:29:00
---

Given a string `s` and an integer `k`. You should construct `k` non-empty **palindrome** strings using **all the characters** in `s`. All characters are lower-case English letters.

Return ***True*** if you can use all the characters in `s` to construct `k` palindrome strings or ***False*** otherwise.

[Leetcode](https://leetcode.com/problems/construct-k-palindrome-strings/)

<!--more-->

**Example 1:**

```
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
```

**Example 2:**

```
Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
```

**Example 3:**

```
Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
```

**Example 4:**

```
Input: s = "yzyzyzyzyzyzyzy", k = 2
Output: true
Explanation: Simply you can put all z's in one string and all y's in the other string. Both strings will be palindrome.
```

**Example 5:**

```
Input: s = "cr", k = 7
Output: false
Explanation: We don't have enough characters in s to construct 7 palindromes.
```

---

#### Tricky 

The are two conditions:

* `odd characters <= k`
  Count the occurrences of all characters. If one character has odd times occurrences, there must be at least one palindrome, with odd length and this character in the middle.
  So we count the characters that appear odd times, the number of odd character should not be bigger than `k`.
* `k <= s.length()`
  Also, if we have one character in each palindrome, we will have at most `s.length()` palindromes,
  so we need `k <= s.length()`.

So we return `odd <= k <= n`

---

#### First solution 

```java
class Solution {
    public boolean canConstruct(String s, int k) {
        if (s == null || s.length() == 0 || k == 0) return false;
        int n = s.length();
        int[] map = new int[26];
        for (char c : s.toCharArray()) {
            map[c - 'a']++;
        }
        int odd = 0;
        for (int i = 0; i < 26; i++) {
            if (map[i] % 2 == 1) {
                odd++;
            }
        }
        return odd <= k && k <= n;
    }
}
```

T: O(n)		S: O(1)

---

#### Optimized

We only store the status(odd / even) of each char of string in map.

**1 means odd, 0 means even.**

`map[c] ^= 1` will change odd to even or even to odd.

 ```java
class Solution {
    public boolean canConstruct(String s, int k) {
        if (s == null || s.length() == 0 || k == 0) return false;
        int n = s.length();
        int[] map = new int[26];
        int odd = 0;
        for (char c : s.toCharArray()) {
            map[c - 'a'] ^= 1;
            odd += map[c - 'a'] == 1 ? 1 : -1;
        }
        return odd <= k && k <= n;
    }
}
 ```

T: O(n)			S: O(1)

---

#### Summary 

We only store the status(odd / even) of each char of string in map.

1 means odd, 0 means even.

`map[c] ^= 1` will change odd to even or even to odd.