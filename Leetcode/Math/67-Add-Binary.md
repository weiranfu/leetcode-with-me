---
title: Easy | Add Binary 67
tags:
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-05-15 00:06:38
---

Given two binary strings, return their sum (also a binary string).

The input strings are both **non-empty** and contains only characters `1` or `0`.

[Leetcode](https://leetcode.com/problems/add-binary/)

<!--more-->

**Example 1:**

```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**

```
Input: a = "1010", b = "1011"
Output: "10101"
```

---

#### Tricky 

We only consern about the sum `sum = a.charAt(i) + b.charAt(j) + carry`.

If string a or b is exhausted, we don't add it. So we could optimize the code as:

```java
int sum = carry;
if (a.hasLen()) sum += a.charAt(i)
if (b.hasLen()) sum += b.charAt(j)
```

---

#### First solution 

```java
class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        int total;
        while (i >= 0 && j >= 0) {
            int n1 = a.charAt(i--) - '0';
            int n2 = b.charAt(j--) - '0';
            total = n1 + n2 + carry;
            carry = total / 2;
            total = total % 2;
            sb.append(total);
        }
        while (i >= 0) {
            total = carry + (a.charAt(i--) - '0');
            carry = total / 2;
            total = total % 2;
            sb.append(total);
        }
        while (j >= 0) {
            total = carry + (b.charAt(j--) - '0');
            carry = total / 2;
            total = total % 2;
            sb.append(total);
        }
        if (carry == 1) {
            sb.append(1);
        }
        return sb.reverse().toString();
    }
}
```

T: O(n)		S: O(n)

---

#### Optimized

```java
class Solution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        int total;
        while (i >= 0 || j >= 0) {
            total = carry;
            if (i >= 0) total += a.charAt(i--) - '0';
            if (j >= 0) total += b.charAt(j--) - '0';
            carry = total / 2;
            total = total % 2;
            sb.append(total);
        }
        if (carry == 1) {
            sb.append(1);
        }
        return sb.reverse().toString();
    }
}
```

T: O(n)		S: O(n)

---

#### Summary 

`sb.append(int)` means StringBuilder appends a char representation of int.

`sb.reverse().toString()` avoids `sb.insert(0, int)`.