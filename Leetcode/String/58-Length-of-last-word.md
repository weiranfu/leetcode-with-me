---
title: Easy | Length of last word 58
tags:
  - common
  - corner case
  - Oh-shit
categories:
  - Leetcode
  - String
date: 2019-07-27 10:22:23
---

Given a string *s* consists of upper/lower-case alphabets and empty space characters `' '`, return the length of last word in the string.

If the last word does not exist, return 0.

**Note:** A word is defined as a character sequence consists of non-space characters only.

[Leetcode](https://leetcode.com/problems/length-of-last-word/)

<!--more-->

**Example:**

```
Input: "Hello World"
Output: 5
```

---

#### Corner Case

1. `string` is an empty string.   e.g. `""`.
2. the last item of `string` is `' '`, `' '` cannot be counted into last word. e.g. `"a "`.
3.  Index `i` should always be `i >= 0`.     e.g. `"a"` or `" "`.

#### Oh-Shit 

When we determine the condition in a `loop`, we determine the left condition first.

e.g. use  `while (i >= 0 && s.charAt(i))` instead of `while (s.charAt(i) && i >= 0)`.

The seconde one will failed if `i < 0`, because we first look at `s.charAt(i)` and then `i >= 0`.

---

#### My thoughts 

Loop from the back of string to the front.

---

#### First solution 

```java
class Solution {
    public int lengthOfLastWord(String s) {
        if (s.isEmpty()) {
            return 0;
        }
        int length = 0;
        int i = s.length() - 1;
        char c = s.charAt(i);
        while (c == ' ') {
            i -= 1;
            if (i < 0) {
                break;
            }
            c = s.charAt(i);
        }
        while (c != ' ') {
            i -= 1;
            length += 1;
            if (i < 0) {
                break;
            }
            c = s.charAt(i);
        }
        return length;
    }
}
```

T: O(n), S: O(1)

---

#### Optimized 

Move `c = s.charAt(i)` into the loop, and move `i < 0` condition into the loop.

Mind that `i >= 0` should place left to `c = s.charAt(i)`.

```java
class Solution {
    public int lengthOfLastWord(String s) {
        if (s.isEmpty()) {
            return 0;
        }
        int length = 0;
        int i = s.length() - 1;
        while (i >= 0 && s.charAt(i) == ' ') {
            i -= 1;
        }
        while (i >= 0 && s.charAt(i) != ' ') {
            i -= 1;
            length += 1;
        }
        return length;
    }
}
```

T: O(n), S: O(1)

---

#### Second Solution

Use `.trim()` method to remove all the " " at both sides of string`.

But it will be slower because `.trim()` will return a copy of string omitted whitespace.

```java
class Solution {
    public int lengthOfLastWord(String s) {
        if (s.isEmpty()) {
            return 0;
        }
        int length = 0;
        int i = s.trim().length() - 1;
        while (i >= 0 && s.trim().charAt(i) != ' ') {
            i -= 1;
            length += 1;
        }
        return length;
    }
}
```

T: O(n), S: O(1)

---

#### Third Solution

Use `.trim()` and `.lastIndexOf()` method.

```java
class Solution {
    public int lengthOfLastWord(String s) {
        int i = s.trim().length() - 1;
        return i - s.trim().lastIndexOf(' ');
    }
}
```

If `s == ""`, `i` will be ` -1`, `s.trim().lastIndexOf()` will be `-1`, return 0.

If `s == " "`, `i` will be `-1`, `s.trim().lastIndexOf()` will be `-1`, return 0.

If `s == "a "`, `i` will be `0`, `s.trim().lastIndexOf()` will be `-1`, return 1.

---

#### Summary 

A string can be empty, can have `" "` at both sides of the string.