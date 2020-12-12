---
title: Easy | Ransom note 383
tags:
  - common
categories:
  - Leetcode
  - String
date: 2019-07-28 16:39:46
---

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false. 

Each letter in the magazine string can only be used once in your ransom note.

**Note:**
You may assume that both strings contain only lowercase letters.

[Leetcode](https://leetcode.com/problems/ransom-note/)

<!--more-->

```
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
```

---

#### My thoughts 

Using a dictionary of 26 characters to store the usage of `magazine` string.

---

#### First solution 

```java
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() == 0) {
            return true;
        } else if (magazine.length() == 0) {
            return false;
        }
        int[] dic = new int[26];
        for (int i = 0; i < magazine.length(); i += 1) {
            dic[magazine.charAt(i) - 'a'] += 1;
        }
        for (int i = 0; i < ransomNote.length(); i += 1) {
            if (dic[ransomNote.charAt(i) - 'a'] == 0) {
                return false;
            }
            dic[ransomNote.charAt(i) - 'a'] -= 1;
        }
        return true;
    }
}
```

T: O(n), S: O(1)

---

#### Standard solution 

Maybe `s.toCharArray()` is faster than `s.charAt(i)`.

```java
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() == 0) {
            return true;
        } else if (magazine.length() == 0) {
            return false;
        }
        int[] table = new int[26];
        for (char c : magazine.toCharArray()) {
            table[c - 'a'] += 1;
        }
        for (char c : ransomNote.toCharArray()) {
            table[c - 'a'] -= 1;
            if (table[c - 'a'] < 0) {
                return false;
            }
        }
        return true;
    }
}
```

T: O(N), S: O(1)

---

#### Summary 

I don't know `s.toCharArray()` and `s.charAt(i)` which is faster,

**Since the String is implemented with an array, the `charAt()` method is a constant time operation.**

