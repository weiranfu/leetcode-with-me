---
title: Hard | Stone Game III 1406
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-15 21:34:58
---

Alice and Bob continue their games with piles of stones. There are several stones **arranged in a row**, and each stone has an associated value which is an integer given in the array `stoneValue`.

Alice and Bob take turns, with **Alice** starting first. On each player's turn, that player can take **1, 2 or 3 stones** from the **first** remaining stones in the row.

The score of each player is the sum of values of the stones taken. The score of each player is **0** initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob **play optimally**.

Return *"Alice"* if Alice will win, *"Bob"* if Bob will win or *"Tie"* if they end the game with the same score.

[Leetcode](https://leetcode.com/problems/stone-game-iii/)

<!--more-->

**Example 1:**

```
Input: values = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
```

**Example 2:**

```
Input: values = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. The next move Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. The next move Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.
```

**Follow up:** 

[Stone Game I](https://leetcode.com/problems/stone-game/)

[Stone Game II](https://leetcode.com/problems/stone-game-ii/)

[Stone Game III](https://leetcode.com/problems/stone-game-iii/)

[Stone Game IV](https://leetcode.com/problems/stone-game-iv/)

---

#### Tricky 

1. Recursion with Memorization

   Since we take stones only at left of array, we only need 1D dp to store states.

   How to represent the max value Alice can get?

   `dp[i] = max{ sufixSum(i) - dp[i + x] for x in [1, 3]}`

   `dp[i + x]` means the max value Bob can get.

   So this is a impartial game.

   ```java
   class Solution {
       int[] sufSum;
       int[] dp;
       int INF = 0x3f3f3f3f;
       int n;
       public String stoneGameIII(int[] stones) {
           n = stones.length;
           sufSum = new int[n + 1];
           for (int i = n - 1; i >= 0; i--) {
               sufSum[i] = sufSum[i + 1] + stones[i];
           }
           dp = new int[n];
           Arrays.fill(dp, -INF);
           int Alice = search(0);
           int Bob = sufSum[0] - Alice;
           if (Alice > Bob) {
               return "Alice";
           } else if (Alice < Bob) {
               return "Bob";
           } else {
               return "Tie";
           }
       }
       private int search(int i) {
           if (i >= n) return 0;
           if (dp[i] != -INF) return dp[i];
           int max = -INF;
           for (int x = 1; x <= 3 && i + x <= n; x++) {
               max = Math.max(max, sufSum[i] - search(i + x));
           }
           dp[i] = max;
           return max;
       }
   }
   ```

   T: O(n^2)		S: O(n)

2. DP

   We can `dp[i]` means the max value we can get at index `i`.

   `dp[i] = max{ sufixSum[i] - dp[i + x] for x in [1, 3] }`

   Since we need `dp[i + x]` before `dp[i]`, the topological order is from right to left.

   ```java
   class Solution {
       public String stoneGameIII(int[] stones) {
           int n = stones.length;
           int INF = 0x3f3f3f3f;
           int[] sufSum = new int[n + 1];
           for (int i = n - 1; i >= 0; i--) {
               sufSum[i] = sufSum[i + 1] + stones[i];
           }
           int[] dp = new int[n];
           Arrays.fill(dp, -INF);
           for (int i = n - 1; i >= 0; i--) {
               int max = -INF;
               for (int x = 1; x <= 3 && i + x <= n; x++) {
                   max = Math.max(max, sufSum[i] - (i + x < n ? dp[i + x] : 0));
               }
               dp[i] = max;
           }
           int Alice = dp[0];
           int Bob = sufSum[0] - Alice;
           if (Alice > Bob) {
               return "Alice";
           } else if (Alice < Bob) {
               return "Bob";
           } else {
               return "Tie";
           }
       }
   }
   ```

   T: O(n^2)			S: O(n)