---
title: Easy | Rotate String 796
tags:
  - common
  - tricky
categories:
  - Leetcode
  - KMP
date: 2020-08-25 12:41:41
---

We are given two strings, `A` and `B`.

A *shift on A* consists of taking string `A` and moving the leftmost character to the rightmost position. For example, if `A = 'abcde'`, then it will be `'bcdea'` after one shift on `A`. Return `True` if and only if `A` can become `B` after some number of shifts on `A`.

[Leetcode](https://leetcode.com/problems/rotate-string/)

<!--more-->

```
Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
```

---

#### First solution 

We can concatenate two `A` into a new String `s` and check whether `s` contains `B`.

```java
class Solution {
    public boolean rotateString(String A, String B) {
        return A.length() == B.length() && (A + A).contains(B);
    }
}
```

T: O(m\*n)			S: O(1)

---

#### KMP

```
class Solution {
    public boolean rotateString(String A, String B) {
        if (A.length() == 0 && B.length() == 0) return true;
        if (A.length() != B.length()) return false;
        String s = A + A;
        int m = s.length(), n = B.length();
        int[] next = new int[n + 1];
        for (int i = 1, j = 0; i < n; i++) {
            while (j > 0 && B.charAt(i) != B.charAt(j)) j = next[j];
            if (B.charAt(i) == B.charAt(j)) j++;
            next[i + 1] = j;
        }
        
        for (int i = 0, j = 0; i < m; i++) {
            while (j > 0 && s.charAt(i) != B.charAt(j)) j = next[j];
            if (s.charAt(i) == B.charAt(j)) j++;
            if (j == n) return true;
        }
        return false;
    }
}
```

T: O(m + n)			S: O(n)

