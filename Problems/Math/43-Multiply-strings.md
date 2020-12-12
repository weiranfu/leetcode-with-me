---
title: Medium | Multiply Strings 43
tags:
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-01-31 15:31:50
---

Given two non-negative integers `num1` and `num2`represented as strings, return the product of `num1` and `num2`, also represented as a string.

[Leetcode](https://leetcode.com/problems/multiply-strings/)

<!--more-->

**Example 1:**

```
Input: num1 = "2", num2 = "3"
Output: "6"
```

**Example 2:**

```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

**Note:**

1. The length of both `num1` and `num2` is < 110.
2. Both `num1` and `num2` contain only digits `0-9`.
3. Both `num1` and `num2` do not contain any leading zero, except the number 0 itself.
4. You **must not use any built-in BigInteger library** or **convert the inputs to integer** directly.

---

#### Tricky 

Create an array to store product digits. The max length of product will be `num1.length + num2.length`

`num1[i] * num2[j]`, its product will falls on `product[i + j + 1]`.

Iterate all digits in num2 to mutiply with num1. 

Use carry bit to represent carry info.

Remember to move forward the last multiply's carry at `product[i]`.

---

#### First solution 

```java
class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) return "0";
        char[] cs1 = num1.toCharArray();
        char[] cs2 = num2.toCharArray();
        int[] product = new int[cs1.length  + cs2.length];
        for (int i = cs2.length - 1; i >= 0; i--) {
            int carry = 0;
            for (int j = cs1.length - 1; j >= 0; j--) {
                int mul = (cs1[j] - '0') * (cs2[i] - '0');
                int tmp = product[i + j + 1] + mul + carry;
                product[i + j + 1] = tmp % 10;
                carry = tmp / 10;
            }
            product[i] += carry; // move forward the last multiply's carry
        }
        int i = 0;
        while (i < product.length && product[i] == 0) { // Remove head '0's
            i++;
        }
        StringBuilder sb = new StringBuilder();
        for (; i < product.length; i++) {
            sb.append((char) (product[i] + '0'));
        }
        return sb.toString();
    }
}
```

T: O(mn)			S: O(m + n)

---

#### Summary 

In tricky.