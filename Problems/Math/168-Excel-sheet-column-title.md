---
title: Easy | Excel Sheet Column Title 168	
tags:
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-06-04 00:11:05
---

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

```
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
```

[Leetcode](https://leetcode.com/problems/excel-sheet-column-title/)

<!--more-->

**Example 1:**

```
Input: 1
Output: "A"
```

**Example 2:**

```
Input: 28
Output: "AB"
```

**Example 3:**

```
Input: 701
Output: "ZY"
```

---

#### Tricky 

1. This is base-26 number system. However we need to view it starting from 0.

   0 - 'A', 1 -  'B', … 25 - 'Z'

   So we need to decrease 1 when get remainder.

2. `StringBuilder.insert(0, char)` is not effient, and it takes O(n).

   We could use `StringBuilder.append()` and then `StringBuilder.reverse()` instead.

---

#### Standard solution  

```java
class Solution {
    public String convertToTitle(int n) {
        StringBuilder sb = new StringBuilder();
        while (n != 0) {
            n--;
            int remainder = n % 26;
            sb.append((char)('A' + remainder));
            n /= 26;
        }
        return sb.reverse().toString();
    }
}
```

T: O(n)		S: O(1)

---

#### Summary 

`StringBuilder.insert(0, char)` is not effient, and it takes O(n).

We could use `StringBuilder.append()` and then `StringBuilder.reverse()` instead.