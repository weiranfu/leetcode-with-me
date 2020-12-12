---
title: Medium | Decode Ways
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-05-20 00:13:15
---

A message containing letters from `A-Z` is being encoded to numbers using the following mapping:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

Given a **non-empty** string containing only digits, determine the total number of ways to decode it.

[Leetcode](https://leetcode.com/problems/decode-ways/)

<!--more-->

**Example 1:**

```
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
```

**Example 2:**

```
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

**Follow up**

[Decode ways II](https://leetcode.com/problems/decode-ways-ii/)

---

#### Tricky 

There're two possible situations when decoding the code.

If the current code `curr > 0` , then `dp[i] += dp[i - 1]`.

If the current code `curr` and previous code `prev`

`prev != 0 && prev * 10 + curr <= 26 `, then `dp[i] += dp[i - 2]`

---

#### First solution 

`dp[i]` means # of ways to decode code `s[:i]`.

```java
class Solution {
    public int numDecodings(String s) {
        int res = 0;
        if (s == null || s.length() == 0) return res;
        int n = s.length();
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i < n + 1; i++) {
            int curr;
            if (i == 1) {
                curr = s.charAt(i - 1) - '0';
            } else {
                int prev = s.charAt(i - 2) - '0';
                curr = s.charAt(i - 1) - '0';
                if (prev != 0 && prev * 10 + curr <= 26) {
                    dp[i] += dp[i - 2];
                }
            }
            if (curr > 0) {			// 0 can't be decoded alone
               dp[i] += dp[i - 1]; 
            }
        }
        return dp[n];
    }
}
```

T: O(n)		S: O(n)



