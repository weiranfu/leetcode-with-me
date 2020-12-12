---
title: Easy | Longest common prefix 14
tags:
  - common
  - corner case
categories:
  - Leetcode
  - String
date: 2019-07-26 23:42:51
---

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

[Leetcode](https://leetcode.com/problems/longest-common-prefix/)

<!--more-->

**Example 1:**

```
Input: ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**

```
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Note:**

All given inputs are in lowercase letters `a-z`.

---

#### Corner Case

Mind that the input `strs[]` could be null. 

---

#### My thoughts 

If there exist a prefix, it must belong to every string.

`prefix = strs[0]`.

Then check every string with this `prefix`, if `prefix` is not in the string,

`prefix = prefix.substring(0, prefix.length() - 1)`. 

---

#### First solution 

We use `prefix.equals(strs[i].substring(0, prefix.length()))` to indicate whether the `prefix` exist in this `strs[i]`. And we need to consider two cases when use `.substring()` method:

1. `prefix.length() <= strs[i].length()`
2. `prefix.length() > strs[i].length()`

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        String prefix = strs[0];
        for (int i = 0; i < strs.length; i += 1) {
            if (prefix.length() <= strs[i].length()) {
                while (!prefix.equals(strs[i].substring(0, prefix.length()))) {
                    prefix = prefix.substring(0, prefix.length() - 1);
                }
            } else {
                String temp = prefix;
                prefix = strs[i];
                strs[i] = temp;
                i -= 1;
            }
        }
        return prefix;
    }
}
```

T: O(m*n) (maybe?)

S: O(1)

---

#### Optimized 

1. However, if we use `.indexOf` method, we don't need to consider the length of `prefix` and `strs[i]`.

   Use `strs[i].indexOf(prefix)` to indicate whether `strs[i]` has an `prefix`.

   If `prefix` doesn't exist in `strs[i]` or `prefix.length() > strs[i].length()`

   `.indexOf()` method will return `-1`.

2. If `prefix.isEmpty() `, the `while` loop ends. 

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        String prefix = strs[0];
        for (int i = 0; i < strs.length; i += 1) {
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) {
                    return prefix;
                } 
            }
        }
        return prefix;
    }
}
```

---

#### Summary 

`indexOf() == 0` means a `prefix`.