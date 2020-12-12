---
title: Hard | Strobogrammatic Number III 248
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-06-24 14:17:46
---

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

[Leetcode](https://leetcode.com/problems/strobogrammatic-number-iii/)

<!--more-->

**Example:**

```
Input: low = "50", high = "100"
Output: 3 
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
```

**Note:**
Because the range might be a large number, the *low* and *high* numbers are represented as string.

---

#### Tricky 

* How to generate strobogrammatic number?

  There're five pairs `00, 11, 88, 69, 96`. We could generate it as concatenating pairs.

  If the length of strobogrammatic number is odd, the char at center position cannot be `6` or `9`

  If the length of strobogrammatic length is greater than 1, there cannot exist any leading 0

* How to generate strobogrammatic number between a range `[low, high]`

  Since we could generate this number of a certain length, we could generate different length strobogrammic numbers with `low.length() <= len <= high.length()`

* How to compare number represented as string.

  Since number might be very large, we can't convert it into an integer.

  We can compare them in String format if their length are same.

  For example, `"88".compareTo("50") >= 0` `"88".compareTo("100") >= 0`

  `"88"` and `"100"` are in different length so we cannot compare them directly.

  However if `s1.length() < s2.length()`, `s1` must be smaller than `s2`.

  So we just need to make sure to compare the num at the same length with `low` and `high`

  ```java
  String s = new String(c);
  if (s.length() == low.length() && s.compareTo(low) < 0
      || (s.length() == high.length() && s.compareTo(high) > 0)) {
    return 0;
  } else {
    return 1;
  }
  ```

---

#### Standard solution  

```java
class Solution {
    
    char[][] pairs = {{'0', '0'}, {'1', '1'}, {'8', '8'}, {'6', '9'}, {'9', '6'}};
    
    public int strobogrammaticInRange(String low, String high) {
        int n = low.length();
        int m = high.length();
        int res = 0;
        for (int len = n; len <= m; len++) {        // generate in different length
            char[] c = new char[len];
            res += dfs(c, 0, len - 1, low, high);
        }
        return res;
    }
    
    private int dfs(char[] c, int left, int right, String low, String high) {
        if (left > right) {
            String s = new String(c);             // compare two string
            if (s.length() == low.length() && s.compareTo(low) < 0
               || (s.length() == high.length() && s.compareTo(high) > 0)) {
                return 0;
            } else {
                return 1;
            }
        }
        int res = 0;
        for (char[] pair : pairs) {
            c[left] = pair[0];
            c[right] = pair[1];
            if (c.length > 1 && c[0] == '0') continue;         // not leading 0
            if (left == right && pair[0] != pair[1]) continue; // odd length c
            res += dfs(c, left + 1, right - 1, low, high);
        }
        return res;
    }
}
```

T: O((high - low)^2)				S: O(high - low)