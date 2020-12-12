---
title: Easy | Print Words Vertically 1324
tags:
  - implement
categories:
  - Leetcode
  - String
date: 2020-01-19 10:37:50
---

Given a string `s`. Return all the words vertically in the same order in which they appear in `s`.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

[Leetcode](https://leetcode.com/problems/print-words-vertically/)

<!--more-->

**Example 1:**

```
Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"
```

**Example 2:**

```
Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
```

**Example 3:**

```
Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
```

---

#### Implement

How to removing trailing spaces at the end of String?

We could to use `StringBuilder sb = new StringBuilder()`. 

```java
while (i >= 0 && sb.charAt(i) == ' ') {
    sb.deleteCharAt(i);
    i--;
}
```

---

#### Standard solution  

```java
class Solution {
    public List<String> printVertically(String str) {
        String[] ss = str.split(" ");
        List<String> res = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        int max = 0;
        for (String s : ss) {
            max = Math.max(max, s.length());
        }
        for (int i = 0; i < max; i++) {
            sb = new StringBuilder();
            for (String s : ss) {
                if (i >= s.length()) {
                    sb.append(" ");
                } else {
                    sb.append(s.charAt(i));
                }
            }
            int j = sb.length() - 1;
            while (sb.charAt(j) == ' ') {
                sb.deleteCharAt(j);
                j--;
            }
            res.add(sb.toString());
        }
        return res;
    }
}
```

T: O(n*len). 			S: O(n)

---

#### Summary 

In Implement.