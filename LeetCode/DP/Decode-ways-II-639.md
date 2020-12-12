---
title: Hard | Decode Ways II 639
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-09-26 11:34:12
---

A message containing letters from `A-Z` is being encoded to numbers using the following mapping way:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

[Leetcode](https://leetcode.com/problems/decode-ways-ii/)

<!--more-->

**Example 1:**

```
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
```

**Example 2:**

```
Input: "1*"
Output: 9 + 9 = 18
```

**Note:**

1. The length of the input string will fit in range [1, 105].
2. The input string will only contain the character '*' and digits '0' - '9'.

---

#### Standard solution  

We can decode in two ways: 

	1. a single digit
 	2. two digits together

Considering `*` and `0`, we need to handle some edge cases.

```java
class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0) return 0;
        int mod = (int)1e9 + 7;
        int n = s.length();
        char[] cs = s.toCharArray();
        long[] dp = new long[n + 1];
        if (cs[0] == '0') return 0;         // cannot decode
        dp[0] = 1;
        dp[1] = countOne(cs[0]);
        for (int i = 2; i <= n; i++) {
            int one = countOne(cs[i - 1]);
            int two = countTwo(cs[i - 2], cs[i - 1]);
            dp[i] = one * dp[i - 1] + two * dp[i - 2];
        }
        return (int)(dp[n] % mod);
    }
    
    private int countOne(char curr) {
        if (curr == '*') return 9;
        else if (curr == '0') return 0;     // cannot decode a single 0
        else return 1;
    }
    
    private int countTwo(char prev, char curr) {
        if (prev == '*' && curr == '*') { // can only represents 10~26 except 10 and 20
            return 15;
        } else if (curr == '*') {
            if (prev == '1') return 9;
            else if (prev == '2') return 6;
            else return 0;
        } else if (prev == '*') {
            if (curr >= '0' && curr <= '6') return 2;
            else return 1;
        } else {  // prev != '*', curr != '*'
            if (prev == '0') return 0;
            int num = (prev - '0') * 10 + (curr - '0');
            if (num <= 26) return 1;
            else return 0;
        }
    }
}
```

T: O(n)			S: O(n)