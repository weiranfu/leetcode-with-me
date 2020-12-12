---
title: Hard | Shortest Palindrome 214
tags:
  - tricky
categories:
  - Leetcode
  - KMP
date: 2020-06-09 22:14:47
---

Given a string ***s***, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

[Leetcode](https://leetcode.com/problems/shortest-palindrome/)

<!--more-->

**Example 1:**

```
Input: "aacecaaa"
Output: "aaacecaaa"
```

**Example 2:**

```
Input: "abcd"
Output: "dcbabcd"
```

---

#### Tricky 

The problem can be converted to "find the longest palindrome substring starts from index 0."

**This means the longest palindrome is also a prefix.** We could try to solve it with KMP.

Note that in KMP, we use `next[]` to find longest common prefix and suffix.

The reversed palindrome is same as itself, so we could reverse the `s` and append it to original `s` to find the longest common prefix and suffix.

`s + reverse(s)`

`new = abbac + cabba`    ==> longest common prefix and suffix is `abba`, which is longest palindrome.

Now the problem is that the new combined string could produce wrong `next[]` table.

Let's look at `s = aaa`

`new = aaa + aaa`                     The next table is `[0, 0, 1, 2, 3, 4, 5]`

We cannot have the longest common prefix and suffix which length is greater than the original string.

We could simply add a delimiter between two string to avoid this problem.

`new = aaa + '#' + aaa`         The next table is `[0, 0, 1, 2, 0, 1, 2, 3]` 

The `next[#]` is 0 and `x` will be reset to the start of the table.

---

#### My thoughts 

Use DP to find all palindromes. Then to find the longest palindrome starts with 0.

However this method takes O(n^2) and will cause LTE!

---

#### First solution 

DP

```java
class Solution {
    public String shortestPalindrome(String s) {
        if (s == null || s.length() == 0) return s;
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }
        int max = 0;
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                dp[i][i + len - 1] = (s.charAt(i) == s.charAt(i + len - 1) && (len < 3 || dp[i + 1][i + len - 2]));
                if (i == 0 && dp[i][i + len - 1]) {
                    max = Math.max(max, i + len - 1);
                }
            }
        }
        StringBuilder res = new StringBuilder();
        res.append(s.substring(max + 1, n));
        return res.reverse().append(s).toString();
    }
}
```

T: O(n^2)			S: O(n^2)

---

#### KMP

Find longest palindrome starts with 0  in `s`

==> find longest prefix and suffix in `s + '#' + reverse(s)`

```java
class Solution {
    public String shortestPalindrome(String s) {
        if (s == null || s.length() == 0) return s;
        int n = s.length();
        String reverse = new StringBuilder(s).reverse().toString();
        String pattern = s + '#' + reverse;
        
        int len = pattern.length();
        int[] next = new int[len + 1];
        int i = 1, x = 0;
        while (i < len) {
            if (pattern.charAt(i) == pattern.charAt(x)) {
                next[i + 1] = x + 1;
                i++;
                x++;
            } else {
                if (x == 0) {
                    next[i + 1] = 0;
                    i++;
                } else {
                    x = next[x];
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(s.substring(next[len], n));      // longest common prefix and suffix
        return sb.reverse().append(s).toString();
    }
}
```

T: O(n)			S: O(n)



