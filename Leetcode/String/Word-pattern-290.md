---
title: Easy | Word Pattern 290
tags:
  - common
  - tricky
categories:
  - Leetcode
  - String
date: 2020-07-04 18:42:09
---

Given a `pattern` and a string `str`, find if `str` follows the same pattern.

Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `str`.

[Leetcode](https://leetcode.com/problems/word-pattern/)

<!--more-->

**Example 1:**

```
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
```

**Example 2:**

```
Input:pattern = "abba", str = "dog cat cat fish"
Output: false
```

**Example 3:**

```
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
```

**Example 4:**

```
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
```

**Notes:**
You may assume `pattern` contains only lowercase letters, and `str` contains lowercase letters that may be separated by a single space.

---

#### Tricky 

[Bijection](https://en.wikipedia.org/wiki/Bijection)

Use a map to record the 1-to-1 mapping relationship.

---

#### First solution 

Use two maps to record the 1-to-1 mapping.

```java
class Solution {
    public boolean wordPattern(String pattern, String str) {
        Map<Character, String> map1 = new HashMap<>();
        Map<String, Character> map2 = new HashMap<>();
        String[] strs = str.split(" ");
        if (pattern.length() != strs.length) return false;
        int n = strs.length;
        for (int i = 0; i < n; i++) {
            char c = pattern.charAt(i);
            String s = strs[i];
            if (!map1.containsKey(c) && !map2.containsKey(s)) {
                map1.put(c, s);
                map2.put(s, c);
            } else if (!s.equals(map1.get(c)) || map2.get(s) != c) {
                return false;
            }
        }
        return true;
    }
}
```

T: O(n)		S: O(n)

---

#### Optimized

Use one map to record 1-to-1 mapping.

Use `map.containsValue()` to check the value.

```java
class Solution {
    public boolean wordPattern(String pattern, String str) {
        Map<Character, String> map = new HashMap<>();
        String[] strs = str.split(" ");
        if (pattern.length() != strs.length) return false;
        int n = strs.length;
        for (int i = 0; i < n; i++) {
            char c = pattern.charAt(i);
            String s = strs[i];
            if (map.containsKey(c)) {
                if (!map.get(c).equals(s)) {
                    return false;
                }
            } else {
                if (map.containsValue(s)) {
                    return false;
                }
                map.put(c, s);
            }
        }
        return true;
    }
}
```

T: O(n)			S: O(n)