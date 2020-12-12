---
title: Medium | Perfect Squares 279
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-04 19:08:51
---

Given a positive integer *n*, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to *n*.

[Leetcode](https://leetcode.com/problems/perfect-squares/)

<!--more-->

**Example 1:**

```
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
```

**Example 2:**

```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

---

#### Tricky 

1. DP

   **Complete Knapsack Problem!!**

   We can view the square number at items and the volume of knapsack is `n`

   Since the pack need to be filled up, we initialize `dp[i] = Integer.MAX_VALUE`

   ```java
class Solution {
       public int numSquares(int n) {
           if (n == 0) return 0;
           int[] dp = new int[n + 1];
           Arrays.fill(dp, Integer.MAX_VALUE);
           dp[0] = 0;
           for (int i = 1; i * i <= n; i++) {
               for (int j = i * i; j <= n; j++) {
                   if (dp[j - i * i] != Integer.MAX_VALUE) 
                       dp[j] = Math.min(dp[j], dp[j - i * i] + 1);  
               }
           }
           return dp[n];
       }
   }
   ```
   

T: O(n√n)			S: O(n)

---

   2. normal DP

   `dp[i]` stores the least number of perfect numbers to form `i`.

   Check all possible perfect number `dp[i] = dp[i - j * j] + 1 for j in [1, √n]`

   To avoid using `Math.sqrt()`, we could enumerate `j` from `1` to `j * j <= n`

   ```java
   class Solution {
       public int numSquares(int n) {
           if (n == 0) return 0;
           int[] dp = new int[n + 1];
           Arrays.fill(dp, Integer.MAX_VALUE);
           dp[0] = 0;
           for (int i = 1; i <= n; i++) {
               for (int j = 1; j * j <= i; j++) {
                   dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
               }
           }
           return dp[n];
       }
   }
   ```

   T: O(n√n)			S: O(n)