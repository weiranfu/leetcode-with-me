---
title: Medium | String to Integer (atoi) 8
tags:
  - common
  - tricky
  - corner case
categories:
  - Leetcode
  - Math
date: 2019-11-27 01:14:00
---

Implement `atoi` which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

[Leetcode](https://leetcode.com/problems/string-to-integer-atoi/)

<!--more-->

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

**Note:**

- Only the space character `' '` is considered as whitespace character.
- Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

**Example 1:**

```
Input: "42"
Output: 42
```

**Example 2:**

```
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
```

**Example 3:**

```
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
```

**Example 4:**

```
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
```

**Example 5:**

```
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
```

---

#### Trick 

We can not use `(int) res == res` to check if overflow.(if res is a long type.)

because long type can also cause overflow.

if `long a = Long.MAX_VALUE * 10`, then a is overflow and`a = -10` actually.

so in this case, `(int a) == a` is true.

So we need to use `a > Integer.MAX_VALUE` to detect overflow for Integer. 

#### Corner Case

* We can only skip space shows up before sign and digit.
* We can only have a sign showing up before any digit.
* We can only have one sign.

---

#### My thoughts 

count how many times sign or digit shows up.

---

#### First solution 

```java
class Solution {
    public int myAtoi(String str) {
        char sign = '+';
        int countSign = 0; // count how many times sing shows up. Sign can only show up twice.
        int countNum = 0;  // count how many times digit shows up.
        long res = 0;
        for (char c : str.toCharArray()) {
            if (c == ' ' && countSign == 0 && countNum == 0) {  // only sikp ' ' before sign '+'/'-'
                continue;
            } else if (c == '+' && countNum == 0) {
                countSign += 1;
                if (countSign > 1) {
                    return 0;
                }
                continue;
            } else if (c == '-' && countNum == 0) {
                countSign += 1;
                if (countSign > 1) {
                    return 0;
                }
                sign = '-';
            } else if (c >= '0' && c <= '9') {
                countNum += 1;
                // change char to String then to int.
                int tail = Integer.parseInt(c + "");  
                res = res * 10 + tail;
       // Check for overflow.  cannot use ((int) res == res) to check whether overflow. 
                if (res > Integer.MAX_VALUE) {   
                    return sign == '+' ? Integer.MAX_VALUE : Integer.MIN_VALUE;
                }
            } else {
                break;
            }
        }
        return sign == '+' ? (int) res : (int) -res;
    }
}
```

T: O(n) S: O(1)

---

#### Optimized 

* We can use `int tmp = str.charAt(i) - '0'` to get the integer of a char.

* If there's no digit, only space in string. We should move `str.length() == 0` after `str = str.trim()`

  in order to handle `" "` corner case.

```java
class Solution {
    public int myAtoi(String str) {
        if (str == null) return 0;
        str = str.trim();
        if (str.length() == 0) return 0;  // We should check length after str.trim()
        int sign = 1, start = 0; 
        long base = 0;
        char firstChar = str.charAt(start);
        if (firstChar == '+' || firstChar == '-') {
            sign = firstChar == '+' ? 1 : -1;
            start += 1;
        } 
        for (; start < str.length(); start += 1) {
            int digit = str.charAt(start) - '0';  // Change char to integer.
            if (digit >= 0 && digit <= 9) {
                base = base * 10 + digit;
                if (base > Integer.MAX_VALUE) {
                    return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
                }
            } else {
                return (int) base * sign;
            }
        }
        return (int) base * sign;
    }
}
```

T: O(n) S: O(1)

---

#### Summary 

We can use `int tmp = str.charAt(i) - '0'` to get the integer of a char.