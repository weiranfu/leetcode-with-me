---
title: Hard | Longest Chunked Palindrome Decomposition 1147
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-02 00:17:03
---

Return the largest possible `k` such that there exists `a_1, a_2, ..., a_k` such that:

- Each `a_i` is a non-empty string;
- Their concatenation `a_1 + a_2 + ... + a_k` is equal to `text`;
- For all `1 <= i <= k`,  `a_i = a_{k+1 - i}`.

[Leetcode](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/)

<!--more-->

**Example 1:**

```
Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
```

**Example 2:**

```
Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".
```

**Example 3:**

```
Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
```

**Example 4:**

```
Input: text = "aaa"
Output: 3
Explanation: We can split the string on "(a)(a)(a)".
```

---

#### Tricky 

* DP

  `dp[i]` means the longest decomposition of substring end with `i`.

  So we search `j ~ i` to find a `dp[j] != -1` and check `substring(j, i) == substring(n-i, n-j)`

  Then update  `dp[i] = Math.max(dp[i], dp[j] + 1)`

  ```java
  class Solution {
      public int longestDecomposition(String text) {
          if (text == null || text.length() == 0) return 0;
          int n = text.length();
          int[] dp = new int[n / 2 + 1];
          Arrays.fill(dp, -1);
          dp[0] = 0;
          int res = 0;
          for (int i = 1; i <= n / 2; i++) {
              for (int j = 0; j < i; j++) {
                  if (dp[j] != -1) {
                      if (text.substring(j, i).equals(text.substring(n - i, n - j))) {
                          dp[i] = Math.max(dp[i], dp[j] + 1);
                          res = Math.max(res, dp[i] * 2);
                      }  
                  }
              }
          }
          return (n % 2 == 0 && dp[n / 2] != -1) ? res : res + 1;
      }
  }
  ```

  T: *O(n^2) O(substring_match) = O(n^3)*   		S: O(n)

* Greedy

  Actually we can match as many substrings at the head or tail as possible.

  Give a quick prove here.
  If we have long prefix matched and a shorter prefix matched at the same time.
  The longer prefix can always be divided in to smaller part.

  ![image](https://assets.leetcode.com/users/lee215/image_1564892108.png)

  Assume we have a longer blue matched and a shorter red matched.
  As definition of the statement, we have `B1 = B2, R1 = R4`.

  Because `B1 = B2`,
  the end part of `B1` = the end part of `B2`,
  equal to `R2 = R4`,
  So we have `R1 = R4 = R2`.

  `B` is in a pattern of `R` + middle part + `R`.
  Instead take a longer `B` with 1 point,
  we can cut it in to 3 parts to gain more points.

  This proves that greedily take shorter matched it right.
  Note that the above diagram shows cases when `shorter length <= longer length/ 2`
  When `shorter length > longer length/ 2`, this conclusion is still correct.

  ```java
  class Solution {
      public int longestDecomposition(String text) {
          if (text == null || text.length() == 0) return 0;
          int n = text.length();
          String l = "", r = "";
          int res = 0;
          for (int i = 0; i < n / 2; i++) {
              l = l + text.charAt(i);
              r = text.charAt(n - 1 - i) + r;
              if (r.equals(l)) {
                  res += 2;
                  l = "";
                  r = "";
              }
          }
          return (n % 2 == 0 && l.length() == 0) ? res : res + 1;
      }
  }
  ```

  T: O(n *match) = O(n^2)			S: O(1)