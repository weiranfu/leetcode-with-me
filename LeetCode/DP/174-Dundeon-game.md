---
title: Hard | Dungeon Game 174
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-06-04 16:22:00
---

The demons had captured the princess (**P**) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (**K**) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (*negative* integers) upon entering these rooms; other rooms are either empty (*0's*) or contain magic orbs that increase the knight's health (*positive* integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

**Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.**

[Leetcode](https://leetcode.com/problems/dungeon-game/)

<!--more-->

For example, given the dungeon below, the initial health of the knight must be at least **7** if he follows the optimal path `RIGHT-> RIGHT -> DOWN -> DOWN`.

| -2 (K) | -3   | 3      |
| ------ | ---- | ------ |
| -5     | -10  | 1      |
| 10     | 30   | -5 (P) |

**Note:**

- The knight's health has no upper bound.
- Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

---

#### Tricky 

The intuition is that to determine the minimum health the knight needed, we need to calculate from bottom-right to top-left.

We could store the minimum health the knight needed in the DP. 

For a cell `dp[i][j]`, we need to consider its down and right cells, `dp[i + 1][j]` and `dp[i][j + 1]`.

We choose the min health of them, and reduce current value at `dungeon[i][j]`.

If the `health <= 0`, which means we just need 1 initial health.

`dp[i][j] = Math.max(1, Math.min(dp[i+1][j], d[i][j+1]) - dungeon[i][j])`.

---

#### Standard solution  

```java
class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        if (dungeon == null || dungeon.length == 0 || dungeon[0].length == 0) return -1;
        int m = dungeon.length;
        int n = dungeon[0].length;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) {
            dp[i][n] = Integer.MAX_VALUE;
        }
        for (int j = 0; j <= n; j++) {
            dp[m][j] = Integer.MAX_VALUE;
        }
        dp[m - 1][n] = 1;
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int min = Math.min(dp[i + 1][j], dp[i][j + 1]);
                dp[i][j] = Math.max(min - dungeon[i][j], 1);
            }
        }
        return dp[0][0];
    }
}
```

T: O(mn)		S: O(mn)



