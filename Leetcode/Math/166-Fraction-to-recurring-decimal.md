---
title: Medium | Fraction to Recurring Decimal 166
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - Math
date: 2020-06-03 21:38:01
---

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

[Leetcode](https://leetcode.com/problems/fraction-to-recurring-decimal/)

<!--more-->

**Example 1:**

```
Input: numerator = 1, denominator = 2
Output: "0.5"
```

**Example 2:**

```
Input: numerator = 2, denominator = 1
Output: "2"
```

**Example 3:**

```
Input: numerator = 2, denominator = 3
Output: "0.(6)"
```

---

#### Tricky 

How to get the recurring decimal?

We could use a map to record the remainder and associated index in StringBuilder.

When a same remainder comes up, we find the recurring decimal.

#### Corner Case

When we use `Math.abs()`, there could be overflow!!

So we chose `long`: `long num = Math.abs((long) numerator)`.

---

#### Standard solution  

```java
class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        StringBuilder sb = new StringBuilder();
        // sign part
        sb.append(((numerator >= 0) ^ (denominator >= 0)) ? "-" : "");  
        
        long num = Math.abs((long)numerator);     // overflow
        long den = Math.abs((long)denominator);
        // integer part
        sb.append(num / den);                                      
        if (num % den == 0) {
            return sb.toString();
        }
        num %= den;
        sb.append(".");
        // fraction part
        Map<Long, Integer> map = new HashMap<>();
        map.put(num, sb.length());
        while (num != 0) {
            num *= 10;
            sb.append(num / den);
            num %= den;
            if (map.containsKey(num)) {
                int index = map.get(num);   // get recurring index
                sb.insert(index, "(");
                sb.append(")");
                break;
            } else {
                map.put(num, sb.length());
            }
        }
        return sb.toString();
    }
}
```

T: O(n)		S: O(1)

