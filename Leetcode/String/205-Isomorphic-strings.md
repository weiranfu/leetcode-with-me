---
title: Easy | Isomorphic Strings 205
tags:
  - tricky
categories:
  - Leetcode
  - String
date: 2019-08-06 20:24:45
---

Given two strings **s** and **t**, determine if they are isomorphic.

Two strings are isomorphic if the characters in **s** can be replaced to get **t**.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters in a string may map to the same character but a character may map to itself.

[Leetcode](https://leetcode.com/problems/isomorphic-strings/)

<!--more-->

**Example 1:**

```
Input: s = "egg", t = "add"
Output: true
```

**Example 2:**

```
Input: s = "foo", t = "bar"
Output: false
```

**Example 3:**

```
Input: s = "paper", t = "title"
Output: true
```

**Note:**
You may assume both **s** and **t** have the same length.

---

#### Tricky 

How to use one map to track two mapping relationship. 

`if (map.containsKey(a)) && map.get(a) != b`  return false.

`if (!map.containsKey(a) && map.containsValue(b))` return false. 

---

#### My thoughts 

Using two maps to track mapping.

---

#### First solution 

`tableS` and `tableT` are used to record mapping relationship.

```java
class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] tableS = new int[256];
        int[] tableT = new int[256];
        for (int i = 0; i < s.length(); i += 1) {
            int indexS = (int) s.charAt(i);
            int indexT = (int) t.charAt(i);
            if (tableS[indexS] == 0 && tableT[indexT] == 0) {
                tableS[indexS] = indexT;
                tableT[indexT] = indexS;
            } else if (tableS[indexS] != indexT || tableT[indexT] != indexS) {
                return false;
            }
        }
        return true;
   
```

T: O(n), S: O(1)

---

#### Second solution 

If we just use one map, store two characters in a map.

```java
class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> map = new HashMap<>();
        for (int i = 0; i < s.length(); i += 1) {
            char cs = s.charAt(i);
            char ct = t.charAt(i);
            if (map.containsKey(cs)) {
                if (map.get(cs) != ct) {
                    return false;
                }
            } else if (map.containsValue(ct)) {
                return false;
            }
            map.put(cs, ct);
        }
        return true;
    }
}
```

T: O(n) S: O(n)

---

#### Summary 

Using map to store mapping relationship.