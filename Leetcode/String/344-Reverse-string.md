---
title: Easy | Reverse string 344
tags:
  - common
categories:
  - Leetcode
  - String
date: 2019-07-28 21:36:16
---

Write a function that reverses a string. The input string is given as an array of characters `char[]`.

Do not allocate extra space for another array, you must do this by **modifying the input array in-place**with O(1) extra memory.

You may assume all the characters consist of [printable ascii characters](https://en.wikipedia.org/wiki/ASCII#Printable_characters).

[Leetcode](https://leetcode.com/problems/reverse-string/)

<!--more-->

**Example 1:**

```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Example 2:**

```
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

---

#### My thoughts 

Two pointers to swap.

---

#### First solution 

```java
class Solution {
    public void reverseString(char[] s) {
        int first = 0;
        int last = s.length - 1;
        if (s.length == 0) {
            return;
        }
        while (first <= last) {
            char temp = s[first];
            s[first] = s[last];
            s[last] = temp;
            first += 1;
            last -= 1;
        }
    }
}
```

T: O(n), S: O(1)

---

#### Summary 

Swap to reverse.