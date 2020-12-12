---
title: Medium | Stone Game II 1140
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-15 20:59:12
---

Alex and Lee continue their games with piles of stones.  There are a number of piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`.  The objective of the game is to end with the most stones. 

Alex and Lee take turns, with Alex starting first.  Initially, `M = 1`.

On each player's turn, that player can take **all the stones** in the **first** `X` remaining piles, where `1 <= X <= 2M`.  Then, we set `M = max(M, X)`.

The game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

[Leetcode](https://leetcode.com/problems/stone-game-ii/)

<!--more-->

**Example 1:**

```
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
```

**Constraints:**

- `1 <= piles.length <= 100`
- `1 <= piles[i] <= 10 ^ 4`

**Follow up: **

[Stone Game I](https://leetcode.com/problems/stone-game/)

[Stone Game II](https://leetcode.com/problems/stone-game-ii/)

[Stone Game III](https://leetcode.com/problems/stone-game-iii/)

[Stone Game IV](https://leetcode.com/problems/stone-game-iv/)

---

#### Tricky 

1. DP

   Since we can only take stones from one side. 1D array is enough for us to represent state.

   However we need to store the `M`, so 2D array is for us.

   `dp[i][j]` means the max stones we can get at `i`th item with `M = j`

   The possitive transition is much easier for us.

   If current `M == j`, we can choose to take away with `x in [1,2*j]` stones. Then the next `M` for the other one is `max(j, 2*x)`. The max `M` here is `len(array)`

   So we have `dp[i][j] = max{ sufixSum(i) - dp[i + x][max(j, 2*x)] for x in [1, 2*j]}`

   Since we need `dp[i+x]` before `dp[i]`, the topological order is from right to left.

   ```java
   class Solution {
       public int stoneGameII(int[] piles) {
           int n = piles.length;
           int[] sufSum = new int[n + 1];
           for (int i = n - 1; i >= 0; i--) {
               sufSum[i] = sufSum[i + 1] + piles[i];
           }
           int[][] dp = new int[n + 1][n + 1];
           for (int i = n - 1; i >= 0; i--) {  // from right to left
               for (int j = 1; j < n; j++) {   // max j is len
                   int max = 0;
                   for (int x = 1; x <= 2 * j && i + x <= n; x++) { // mind the bound
                       max = Math.max(max, sufSum[i] - dp[i + x][Math.max(j, x)]);
                   }
                   dp[i][j] = max;
               }
           }
           return dp[0][1];
       }
   }
   ```

   T: O(n^3)			S: O(n^2)

2. Recursion with Memorization

   Possitive transition is much easier for recursion with memorization.

   ```java
   class Solution {
       int n;
       int[][] dp;
       int[] sufSum;
       public int stoneGameII(int[] piles) {
           n = piles.length;
           sufSum = new int[n + 1];
           for (int i = n - 1; i >= 0; i--) {
               sufSum[i] = sufSum[i + 1] + piles[i];
           }
           dp = new int[n + 1][n + 1];
           for (int i = 0; i < n; i++) {
               Arrays.fill(dp[i], -1);
           }
           return dfs(0, 1);
       }
       private int dfs(int i, int j) {
         	if (i >= n) return 0;
           if (dp[i][j] != -1) return dp[i][j];
           int max = 0;
           for (int x = 1; x <= 2 * j && i + x <= n; x++) { // mind the bound
               max = Math.max(max, sufSum[i] - dfs(i + x, Math.max(j, x)));
           }
           dp[i][j] = max;
           return max;
       }
   }
   ```

   T: O(n^3)			S: O(n^2)