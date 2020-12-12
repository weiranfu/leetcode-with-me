---
title: Hard | Integer to English Words 273
tags:
  - common
  - tricky
  - corner case
categories:
  - Leetcode
  - String
date: 2020-06-27 17:41:53
---

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

[Leetcode](https://leetcode.com/problems/integer-to-english-words/)

<!--more-->

**Example 1:**

```
Input: 123
Output: "One Hundred Twenty Three"
```

**Example 2:**

```
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
```

**Example 3:**

```
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

**Example 4:**

```
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
```

---

#### Tricky 

We should convert Integer to English 3-digits by 3-digits.

For parsing 3 digits num, we could recursively parse it.

#### Corner Case

We should take care about the case that middle chunk is zero and should not be printed out? 

1000001

---

#### Standard solution  

```java
class Solution {
    
    String[] LESSTHAN20 = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten","Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    String[] TENS = {"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    String[] THOUSANDS = {"", "Thousand", "Million", "Billion"};
    
    public String numberToWords(int num) {
        if (num == 0) return "Zero";
        String res = "";
        int cnt = 0;
        while (num != 0) {
            if (num % 1000 != 0) {       // test for middle chunk
                res = parse3digits(num % 1000) + THOUSANDS[cnt] + " " + res;
            }
            cnt++;
            num = num / 1000;
        }
        return res.trim();
    }
    
    // parse 3 digits num followed by " "
    public String parse3digits(int num) {
        if (num == 0) return "";      // if num == 0, return ""
        else if (num < 20) {
            return LESSTHAN20[num] + " ";         
        } else if (num < 100) {
            return TENS[num / 10] + " " + parse3digits(num % 10);
        } else {
            return LESSTHAN20[num / 100] + " Hundred " + parse3digits(num % 100);
        }
    }
}
```

T: O(n)		S: O(1)
