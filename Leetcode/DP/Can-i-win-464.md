---
title: Medium | Can I Win 464
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-15 23:15:31
---

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer `maxChoosableInteger` and another integer `desiredTotal`, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that `maxChoosableInteger` will not be larger than 20 and `desiredTotal` will not be larger than 300.

[Leetcode](https://leetcode.com/problems/can-i-win/)

<!--more-->

**Example**

```
Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
```

---

#### Tricky 

1. Bottom-up DP 		**LTE**

   Use `dp[i][s]` to represent whether I can win with `sum = i` and `state = s`

   `dp[desiredTotal][s] = false` Anyone move to this stage cannot make a move, so he will lose.

   ```java
   class Solution {
       public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
           if (desiredTotal == 0) return true;
           int[][] dp = new int[desiredTotal + 1][1 << maxChoosableInteger];
           for (int i = 0; i <= desiredTotal; i++) {
               Arrays.fill(dp[i], -1);
           }
           Arrays.fill(dp[desiredTotal], 0);
           for (int i = desiredTotal - 1; i >= 0; i--) {
               out:
               for (int s = 0; s < 1 << maxChoosableInteger; s++) {// all state.
                   for (int j = 0; j < maxChoosableInteger; j++) {
                       if ((s & 1 << j) == 0) {
                           int state = s | 1 << j;
                         	// if sum > desiredTotal, which means opponent will lose
                           if (i + j + 1 > desiredTotal || dp[i + j + 1][state] == 0) {
                               dp[i][s] = 1;
                               continue out;
                           }
                       }
                   }
                   dp[i][s] = 0;
               }
           }
           
           return dp[0][0] == 1;
       }
   }
   ```

   Why **LTE** happens?

   **Because we compute many `state` which is indeed invalid and will never visit.**

   **And only 1D dp[] array is enough, because if we know which number has been selected, we already know the current sum.**

   So we can try recursion with memorization and only check valid state.

2. 1D DP

   Use `dp[state]` to store the states of selected number.

   **Corner case: **

   If the total number cannot reach the desired total, nobody can win.

   ```java
   class Solution {
       /*
       dp[i]
       -1: not visited
       1:  win
       0:  lose
       */
       int[] dp;
       int max;
       int total;
       public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
           max = maxChoosableInteger;
           total = desiredTotal;
           if (total == 0) return true;
           int sum = 0;
           for (int i = 1; i <= max; i++) {
               sum += i;
           }
           if (sum < total) return false;    // nobody can win
           dp = new int[1 << max];
           Arrays.fill(dp, -1);
           return dfs(0, 0) == 1;
       }
       private int dfs(int i, int state) {
           if (i >= total) return 0;     // cannot make a move, so lose
           if (dp[state] != -1) return dp[state];
           for (int j = 0; j < max; j++) {
               if ((state >> j & 1) == 0) {
                   int s = state | 1 << j;
                   if (dfs(i + j + 1, s) == 0) { // find a lose state, so win
                       dp[state] = 1;
                       return 1;
                   }
               }
           }
           dp[state] = 0; // cannot find lose state, so lose
           return 0;
       }
   }
   ```

   T: O(n\*2^n)			S: O(2^n)