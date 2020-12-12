---
title: Medium | Stone Game 877
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-08 22:37:09
---

Alex and Lee play a game with piles of stones.  There are an even number of piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`.

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return `True` if and only if Alex wins the game.

[Leetcode](https://leetcode.com/problems/stone-game/)

<!--more-->

**Example 1:**

```
Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
```

**Note:**

1. `2 <= piles.length <= 500`
2. `piles.length` is even.
3. `1 <= piles[i] <= 500`
4. `sum(piles)` is odd.

**Follow up**

[Stone Game I](https://leetcode.com/problems/stone-game/)

[Stone Game II](https://leetcode.com/problems/stone-game-ii/)

[Stone Game III](https://leetcode.com/problems/stone-game-iii/)

[Stone Game IV](https://leetcode.com/problems/stone-game-iv/)

---

#### Tricky 

We can use `dp[i][j][0]` to represent the max stones Alex can get from `[i, j]`

Cause Alex choose optimally, he can choose either `piles[i]` or `piles[j]`

So `dp[i][j][0] = max{ Sum(i, j) - dp[i+1][j][1], Sum(i, j) - dp[i][j - 1][1] }`

```java
class Solution {
    public boolean stoneGame(int[] piles) {
        if (piles == null || piles.length == 0) return true;
        int n = piles.length;
        int[][][] dp = new int[n][n][2];
        int[] preSum = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            preSum[i] = preSum[i - 1] + piles[i - 1];
        }
        for (int i = 0; i < n; i++) {
            dp[i][i][0] = piles[i];
            dp[i][i][1] = piles[i];
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0, j = len - 1; j < n; i++, j++) {
                int right0 = preSum[j] - preSum[i] - dp[i][j - 1][1] + piles[j];
                int right1 = preSum[j] - preSum[i] - dp[i][j - 1][0] + piles[j];
                int left0 = preSum[j + 1] - preSum[i + 1] - dp[i + 1][j][1] + piles[i];
                int left1 = preSum[j + 1] - preSum[i + 1] - dp[i + 1][j][0] + piles[i];
                dp[i][j][0] = Math.max(left0, right0);
                dp[i][j][1] = Math.max(left1, right1);
            }
        }
        return 2 * dp[0][n - 1][0] > preSum[n];
    }
}
```

T: O(n^2)		S: O(n^2)

---

#### Just return true

Alex is first to pick pile.
`piles.length` is even, and this lead to an interesting fact:
Alex can always pick odd piles or always pick even piles!

For example,
If Alex wants to pick even indexed piles `piles[0], piles[2], ....., piles[n-2]`,
he picks first `piles[0]`, then Lee can pick either `piles[1]` or `piles[n - 1]`.
Every turn, Alex can always pick even indexed piles and Lee can only pick odd indexed piles.

In the description, we know that `sum(piles)` is odd.
If `sum(piles[even]) > sum(piles[odd])`, Alex just picks all evens and wins.
If `sum(piles[even]) < sum(piles[odd])`, Alex just picks all odds and wins.

So, Alex always defeats Lee in this game.

```java
class Solution {
    public boolean stoneGame(int[] piles) {
        return true;
    }
}
```

---

#### DP

It's tricky when we have even number of piles of stones. You may not have this condition in an interview.

**Follow-up:**

What if piles.length can be odd?
What if we want to know exactly the diffenerce of score?
Then we need to solve it with DP.

`dp[i][j]` means the biggest number of stones you can get more than opponent picking piles in `[i,j]`
You can first pick `piles[i]` or `piles[j]`.

1. If you pick `piles[i]`, your result will be `piles[i] - dp[i + 1][j]`
2. If you pick `piles[j]`, your result will be `piles[j] - dp[i][j - 1]`

So we get:
`dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])`
We start from smaller subarray and then we use that to calculate bigger subarray.

Note that take evens or take odds, it's just an easy strategy to win when the number of stones is even.

```java
class Solution {
    public boolean stoneGame(int[] piles) {
        if (piles == null || piles.length == 0) return true;
        int n = piles.length;
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = piles[i];
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0, j = len - 1; j < n; i++, j++) {
                dp[i][j] = Math.max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1]);
            }
        }
        return dp[0][n - 1] > 0;
    }
}
```

T: O(n^2)			S: O(n^2)

---

#### DP — 1D

`j = i + len - 1`

`dp[i][i+len-1] = max(p[i] - dp[i+1][i+len-1], p[i+len-1] - dp[i][i+len-2])`

滚动数组

`dp[i] = max(p[i] - dp[i+1], p[i+len-1] - dp[i])`

update from right to left

```java
class Solution {
    public boolean stoneGame(int[] piles) {
        if (piles == null || piles.length == 0) return true;
        int n = piles.length;
        int[] dp = new int[n + 1];
        for (int len = 1; len <= n; len++) {
            for (int i = n - len; i >= 0; i--) {
                dp[i] = Math.max(piles[i] - dp[i+1], piles[i+len-1] - dp[i]);
            }
        }
        return dp[n-1] > 0;
    }
}
```

T: O(n^2)			S: O(n)