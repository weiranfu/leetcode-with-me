---
title: Hard | Stone Game IV 1510
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-15 22:07:21
---

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are `n` stones in a pile.  On each player's turn, that player makes a *move* consisting of removing **any** non-zero **square number** of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer `n`. Return `True` if and only if Alice wins the game otherwise return `False`, assuming both players play optimally.

[Leetcode](https://leetcode.com/problems/stone-game-iv/)

<!--more-->

**Example 1:**

```
Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
```

**Example 2:**

```
Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
```

**Follow up:** 

[Stone Game I](https://leetcode.com/problems/stone-game/)

[Stone Game II](https://leetcode.com/problems/stone-game-ii/)

[Stone Game III](https://leetcode.com/problems/stone-game-iii/)

[Stone Game IV](https://leetcode.com/problems/stone-game-iv/)

---

#### Tricky 

1. Sprague-Grundy Theorem

   ```java
   class Solution {
       public boolean winnerSquareGame(int n) {
           int[] dp = new int[n + 1];
           for (int i = 1; i <= n; i++) {
               Set<Integer> set = new HashSet<>();
               for (int j = 1; j * j <= i; j++) {
                   set.add(dp[i - j * j]);
               }
               for (int j = 0; ; j++) {
                   if (!set.contains(j)) {
                       dp[i] = j;
                       break;
                   }
               }
           }
           return dp[n] != 0;
       }
   }
   ```

   T: O(n\*√n)		S: O(n)

2. Optimization

   For all possible states we can go into, if we find a state that can make our opponent to lose, we win.

   Otherwise we lose.

   ```java
   class Solution {
       public boolean winnerSquareGame(int n) {
           int[] dp = new int[n + 1];
           Arrays.fill(dp, -1);
           dp[0] = 0;            // 0 means lose
           out:
           for (int i = 1; i <= n; i++) {
               for (int j = 1; j * j <= i; j++) {
                   if (dp[i - j * j] == 0) {     // find a state must lose
                       dp[i] = 1;
                       continue out;
                   }
               }
               dp[i] = 0;     // cannot find a state to lose
           }
           return dp[n] != 0;
       }
   }
   ```

   T: O(n\*√n)			S: O(n)