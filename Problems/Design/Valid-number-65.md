---
title: Hard | Valid Number 65
tags:
  - tricky
categories:
  - Leetcode
  - Design
date: 2020-05-14 17:20:56
---

Validate if a given string can be interpreted as a decimal number.

[Leetcode](https://leetcode.com/problems/valid-number/)

<!--more-->

Some examples:

```javascript
"0" => true
"   " => false
"20e+9" => true
"  0.1" => true
"abc" => false
"1  a" => false
"2e10" =>ture
"  -90e3" => true
"  1e" => false
"e3" => false
"-.3" => true
" 6e-1" => true
"  99e2.5" => false    !!!!
"  0e2"  => true
"53.5e93" => true
" --6" => false
"-+5" => false
"."  => false         !!!!
"3." => true          !!!!
".e5" => false        !!!!
"0.e5" => true        !!!!
".3e3" => true        !!!!
"6+1" => false
"5.1+1" => false
"46.e3" => true       !!!!
"46.+e3" => false
"34.e+3" => true
```

**Note:** It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

- Numbers 0-9
- Exponent - "e"
- Positive/negative sign - "+"/"-"
- Decimal point - "."

---

#### Tricky 

Use `hasNum` flag to indicate whether there exist numbers.

`return hasNum;` 

---

#### Standard solution  

```java
class Solution {
    public boolean isNumber(String s) {
        s = s.trim();
        boolean dot = false;
        boolean exp = false;
        boolean hasNum = false;
        for (int i = 0; i < s.length(); i++) {
            if (Character.isDigit(s.charAt(i))) {
                hasNum = true;
            } else if (s.charAt(i) == '.') {
                if (exp || dot) {
                    return false;
                }
                dot = true;
            } else if (s.charAt(i) == 'e') {
                if (exp || !hasNum) {
                    return false;
                }
                exp = true;
                hasNum = false;          // clear hasNum
            } else if (s.charAt(i) == '+' || s.charAt(i) == '-') {
                if (i != 0 && s.charAt(i - 1) != 'e') { // sign must at beginning of num
                    return false;
                }
            } else {
                return false;
            }
        }
        return hasNum;     // must have seen numbers.
    }
}
```

T: O(n)		S: O(1)

---

#### DFA

We need to draw a graph of DFA.

Nine States: 

`Start, StartSign, Integer, Decimal, No_Num_Decimal, Exp, ExpSign, ExpInt, Error.`

The `No_Num_Decimal` state means there's no number before the `.`, such as `.` , `+.`

The `ExpSign` state represents `e+`

The `ExpInt` state represents `e23`

The end  state is `Integer || Decimal || ExpInt`. Note that `No_Num_Decimal` and `Exp` state cannot be final state.

![](https://cdn.jsdelivr.net/gh/weiranfu/image-hosting@main/img/leetcode/valid-number-65.jpg)

```java
class Solution {
    final int START = 0;
    final int STARTSIGN = 1;
    final int INTEGER = 2;
    final int DECIMAL = 3;
    final int NONUMDEC = 4;
    final int EXP = 5;
    final int EXPSIGN = 6;
    final int EXPINT = 7;
    final int ERROR = 8;
    int state;
    
    public boolean isNumber(String s) {
        s = s.trim();
        state = START;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (isError()) {
                return false;
            }
            if (Character.isDigit(c)) onDigit();
            else if (c == '.') onDot();
            else if (c == 'e') onExp();
            else if (c == '+' || c == '-') onSign();
            else return false;
        }
        return isEnd();
    }
    
    public void onDigit() {
        if (state == START) {
            state = INTEGER;
        } else if (state == EXP) {
            state = EXPINT;
        } else if (state == STARTSIGN) {
            state = INTEGER;
        } else if (state == EXPSIGN) {
            state = EXPINT;
        } else if (state == NONUMDEC) {
            state = DECIMAL;
        }
    }
    
    public void onSign() {
        if (state == START) {
            state = STARTSIGN;
        } else if (state == EXP) {
            state = EXPSIGN;
        } else {
            state = ERROR;
        }
    }
    
    public void onDot() {
        if (state == START) {
            state = NONUMDEC;
        } else if (state == STARTSIGN) {
            state = NONUMDEC;
        } else if (state == INTEGER) {
            state = DECIMAL;
        } else {
            state = ERROR;
        }
    }
    
    public void onExp() {
        if (state == INTEGER) {
            state = EXP;
        } else if (state == DECIMAL) {
            state = EXP;
        } else {
            state = ERROR;
        }
    }
    
    public boolean isError() {
        return state == ERROR;
    }
    
    public boolean isEnd() {
        return state == INTEGER || state == DECIMAL || state == EXPINT;
    }
}
```

T: O(n)		S: O(1)

