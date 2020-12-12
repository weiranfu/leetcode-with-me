---
title: Hard | Last Substring in Lexicographical Order 1163
tags:
  - common
  - tricky
categories:
  - Leetcode
  - KMP
date: 2020-08-26 10:17:45
---

Given a string `s`, return the last substring of `s` in lexicographical order.

[Leetcode](https://leetcode.com/problems/last-substring-in-lexicographical-order/)

<!--more-->

**Example 1:**

```
Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
```

**Example 2:**

```
Input: "leetcode"
Output: "tcode"
```

**Note:**

1. `1 <= s.length <= 4 * 10^5`
2. s contains only lowercase English letters.

---

#### Standard solution  

The solution must be in one of those n suffix candidates, and **the main idea here is to eliminate those candidates we are certain not the solution, at last, the only one left is our solution**.

Think of two sequences matching k characters so far and only differ at `s[i+k] > s[j+k]`
i ... i+k
j ... j+k

Regardless of j relative position to i, we could set j to j+k+1. This is because for any j2 (j<j2<j+k); and i2 (i<i2<j+k), i+k-i2 = j+k-j2, substring `[j2, j+k]` is still smaller than `[i2, i+k]` (these two still only differ at `s[i+k] > s[j+k])`.

Reversely and similarly, if s[i+k] < s[j+k], then set i to i+k+1

at last to break tie, when i==j, set j=j+1; (**We assume s[i:] is the final anwser**)

**The idea is similar with KMP**

```java
class Solution {
    public String lastSubstring(String s) {
        int n = s.length();
        int i = 0, j = 1, len = 1;
        while (j + len - 1 < n) {
            char a = s.charAt(i + len - 1);
            char b = s.charAt(j + len - 1);
            if (a == b) {
                len++;
                continue;
            } else if (a < b) {
                i = i + len;
            } else {
                j = j + len;
            }
            if (i == j) j++;
            len = 1;
        }
        return s.substring(i);
    }
}
```

T: O(n)			S: O(1)