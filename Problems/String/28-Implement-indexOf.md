---
title: Easy | Implement indexOf 28
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - String
date: 2019-07-26 22:07:16
---

Implement [indexOf()](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)).

Return the index of the first occurrence of needle in haystack, or **-1** if needle is not part of haystack.

[Leetcode](https://leetcode.com/problems/implement-strstr/)

<!--more-->

**Example 1:**

```
Input: haystack = "hello", needle = "ll"
Output: 2
```

**Example 2:**

```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

**Clarification:**

What should we return when `needle` is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when `needle` is an empty string. This is consistent to C's [strstr()](http://www.cplusplus.com/reference/cstring/strstr/) and Java's [indexOf()](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)).

---

#### Tricky 

[KMP method](https://aranne.github.io/2019/07/26/KMP-method/)

#### Corner Case

When we use `s.substring(startIndex, endIndex)`, 

the range of substring is `[startIndex, endIndex)`.

So in loop below: we need to use `<=` in `i <= haystack.length()`.

```java
        for (int i = 0; i <= haystack.length() - length; i += 1) {
            if (haystack.substring(i, i + length).equals(needle)) {
                return i;
            }
        }
```

---

#### My thoughts 

Check all the substrings whose length is `needle.length()`.

---

#### First solution 

```java
class Solution {
    public int strStr(String haystack, String needle) {
        int length = needle.length();
        if (length == 0) {
            return 0;
        }
        for (int i = 0; i <= haystack.length() - length; i += 1) {
            if (haystack.substring(i, i + length).equals(needle)) {
                return i;
            }
        }
        return -1;
    }
}
```

T: O(n) S: O(1)

---

#### Optimized 

We could not use `substring()` method.

we could use [KMP method](https://aranne.github.io/2019/07/26/KMP-method/) to find substring in a string.

```java
class Solution {
     public int strStr(String haystack, String needle) {
         if (needle.equals("")) {
             return 0;
         }
         int[] next = getNext(needle);
         int i = 0;
         int j = 0;
         while (i < haystack.length() && j < needle.length()) {
             if (j == -1 || haystack.charAt(i) == needle.charAt(j)) {
                 i += 1;
                 j += 1;
             } else {
                 j = next[j];
             }
         }
         if (j == needle.length()) {
             return i - needle.length();
         } else {
             return -1;
         }
     }


     private static int[] getNext(String nee) {
         int[] next = new int[nee.length()];
         next[0] = -1;
         int j = next[0];
         int i = 1;
         while (i < next.length) {
             if (j == -1 || nee.charAt(i - 1) == nee.charAt(j)) {
                 next[i] = j + 1; // j stores next[i - 1]
                 j = next[i];    // j stores next[i], then i++
                 i += 1;
             } else {
                 j = next[j];
             }
         }
         return next;
     }
}
```

T: O(n), S: O(n)

---

#### Summary 

KMP method is an important method to find substring.