---
title: Medium | Integer to Roman 12
tags:
  - tricky
categories:
  - Leetcode
  - Math
date: 2019-11-27 21:48:20
---

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

[Leetcode](https://leetcode.com/problems/integer-to-roman/)

<!--more-->

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, two is written as `II` in Roman numeral, just two one's added together. Twelve is written as, `XII`, which is simply `X` + `II`. The number twenty seven is written as `XXVII`, which is `XX` + `V` + `II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

**Example 1:**

```
Input: 3
Output: "III"
```

**Example 2:**

```
Input: 4
Output: "IV"
```

**Example 3:**

```
Input: 9
Output: "IX"
```

**Example 4:**

```
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```

**Example 5:**

```
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

##### Follow up: 

[13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

---

#### Tricky 

There're only `int[] values = new int[]{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}`

possibilities to represent in Roman.

So we can check the num with these value, if `num > values[i]`, then `num = num - values[i]` and add corresponding Roman symbol to String.

---

#### My thoughts 

Build a map to stole the relation of Roman symbol to integer value.

---

#### First solution 

```java
class Solution {
    public String intToRoman(int num) {
        StringBuilder sb = new StringBuilder();
        Map<Integer, Character> map = new HashMap<>();
        map.put(1, 'I'); map.put(5, 'V');
        map.put(10, 'X'); map.put(50, 'L');
        map.put(100, 'C'); map.put(500, 'D');
        map.put(1000, 'M');
        int base = 1;
        while (num != 0) {
            int digit = num % 10;
            if (digit > 0 && digit < 4) {
                for (int i = 0; i < digit; i += 1) {
                    sb.insert(0, map.get(1 * base));
                }
            } else if (digit == 4) {
                sb.insert(0, map.get(5 * base));
                sb.insert(0, map.get(1 * base));
            } else if (digit == 5) {
                sb.insert(0, map.get(5 * base));
            } else if (digit > 5 && digit < 9) {
                for (int i = 5; i < digit; i += 1) {
                    sb.insert(0, map.get(1 * base));
                }
                sb.insert(0, map.get(5 * base));
            } else if (digit == 9) {
                sb.insert(0, map.get(10 * base));
                sb.insert(0, map.get(1 * base));
            }
            base = base * 10;
            num = num / 10;
        }
        return sb.toString();
    }
    
}
```

T: O(n) S: O(n)

---

#### 10 Base to Roman Base

Construct Roman Base according to 10 Base.

```java
class Solution {
    public String intToRoman(int num) {
        String[] Ibase = new String[]{"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        String[] Xbase = new String[]{"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        String[] Cbase = new String[]{"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        String[] Mbase = new String[]{"", "M", "MM", "MMM"};
        
        return Mbase[num / 1000] + Cbase[(num / 100) % 10] + Xbase[(num / 10) % 10] + Ibase[num % 10];
    }
    
}
```

T: O(1), S: O(1)

---

#### Count Values 

See in the Tricky. Just like count RMB

```java
class Solution {
    public String intToRoman(int num) {
        String[] roman = new String[]{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] values = new int[]{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        
        StringBuilder sb = new StringBuilder();
        int start = 0;
        while (num > 0) {
            if (num >= values[start]) {
                sb.append(roman[start]);
                num -= values[start];
            } else {
                start += 1;
            }
        }
        return sb.toString();
    }   
}
```

T: O(n) S: O(n)

---

#### Summary 

We can count RMB like this. If RMB is great than a kind of cash, then add that cash to result and subtract the value of cash with RMB.