---
title: Medium | Longest Palindromic Substirng 5
tags:
  - tricky
  - implement
categories:
  - Leetcode
  - String
date: 2019-11-25 21:40:00
---

Given a string **s**, find the longest palindromic substring in **s**. You may assume that the maximum length of **s** is 1000.

[Leetcode](https://leetcode.com/problems/longest-palindromic-substring/)

<!--more-->

**Example 1:**

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

**Example 2:**

```
Input: "cbbd"
Output: "bb"
```

---

#### Tricky 

#### DP

`isPalind[i][j] = charAt(i) == charAt(j) && isPalind[i+1][j-1]`

so we need `isPalind[i+1][j-1]` before `isPalind[i][j]`

the topological order is: `i` from n to 0, `j` from `i` to n.

```java
class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        boolean[][] isPalind = new boolean[n][n];
        int maxLen = 0, left = 0, right = 0;
      	// Because we need isPalind[i+1][j-1] to get isPalind[i][j]
        for (int i = n - 1; i >= 0; i--) {   
            for (int j = i; j < n; j++) {
                isPalind[i][j] = s.charAt(i) == s.charAt(j) 
                  								&& (j - i < 3 || isPalind[i+1][j-1]);
                if (isPalind[i][j] && maxLen < j - i + 1) {
                    maxLen = j - i + 1;
                    left = i;
                    right = j + 1;
                }
            }
        }
        return s.substring(left, right);
    }
}	
```

T: O(n^2) S: O(n^2)

---

#### Brute Force (Optimized)

Enumerate the center of palindrome and try to extend the palindrome to the longest.

Palindrome could be even or odd chars, so we need to extend it in two ways. 

Use `index` pointer to store intermediate result.

```java
class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) return s;
        int n = s.length();
        char[] cs = s.toCharArray();
        int[] res = {0, 0};
        for (int i = 0; i < n; i++) {
            extend(i, i, cs, res);                   // extend odd palindrome
            if (i > 0) extend(i - 1, i, cs, res);    // extend even palindrome
        }
        return s.substring(res[0], res[1]);
    }
    private void extend(int l, int r, char[] cs, int[] res) {
        int n = cs.length;
        while (l >= 0 && r < n && cs[l] == cs[r]) {
            l--;
            r++;
        }
        if (res[1] - res[0] < r - l - 1) {
            res[0] = l + 1;
            res[1] = r;
        }
    }
}
```

T: O(n^2) S: O(n)

---

#### Manacher

To Do

 