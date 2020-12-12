---
title: Medium | Reverse Word in a String II 186
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-06-04 21:30:54
---

Given an input string , reverse the string word by word. Could you solve it *in-place* without allocating extra space?

[Leetcode](https://leetcode.com/problems/reverse-words-in-a-string-ii/)

<!--more-->

**Example:**

```
Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
```

**Note:** 

- A word is defined as a sequence of non-space characters.
- The input string does not contain leading or trailing spaces.
- The words are always separated by a single space.

---

#### Tricky 

Reverse the whole line, and then reverse word by word.

---

#### My thoughts 

Using extra space to reverse word by word.

---

#### First solution 

```java
class Solution {
    public void reverseWords(char[] s) {
        int n = s.length;
        char[] tmp = new char[n];
        int p = 0;
        for (int i = n - 1; i >= 0; i--) {
            int j = i;
            while (j >= 0 && s[j] != ' ') {
                j--;
            }
            for (int k = j + 1; k <= i; k++) {
                tmp[p++] = s[k];
            }
            if (p != n) tmp[p++] = ' ';
            i = j;
        }
        for (int i = 0; i < n; i++) {
            s[i] = tmp[i];
        }
    }
}
```

T: O(n)		S: O(n)

---

#### Optimized

Reverse the whole line and then reverse word by word.

```java
class Solution {
    public void reverseWords(char[] s) {
        int n = s.length;
        reverse(s, 0, n - 1);
        for (int i = n - 1; i >= 0; i--) {
            int j = i; 
            while (j >= 0 && s[j] != ' ') {
                j--;
            }
            reverse(s, j + 1, i);
            i = j;
        }
    }
    
    private void reverse(char[] s, int start, int end) {
        while (start < end) {
            char tmp = s[start];
            s[start] = s[end];
            s[end] = tmp;
            start++;
            end--;
        }
    }
}
```

T: O(n)			S: O(1)



