---
title: Hard | Minimum Distance to Type a Word Using Two Fingers 1320
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-01-13 11:44:47
---

![img](https://assets.leetcode.com/uploads/2020/01/02/leetcode_keyboard.png)

You have a keyboard layout as shown above in the XY plane, where each English uppercase letter is located at some coordinate, for example, the letter **A** is located at coordinate **(0,0)**, the letter **B** is located at coordinate **(0,1)**, the letter **P** is located at coordinate **(2,3)**and the letter **Z** is located at coordinate **(4,1)**.

Given the string `word`, return the minimum total distance to type such string using only two fingers. The distance between coordinates **(x1,y1)** and **(x2,y2)** is **|x1 - x2| + |y1 - y2|**. 

[Leetcode](https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/)

<!--more-->

Note that the initial positions of your two fingers are considered free so don't count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.

**Example 1:**

```
Input: word = "CAKE"
Output: 3
Explanation: 
Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -> cost = 0 
Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -> cost = 0 
Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3
```

**Example 2:**

```
Input: word = "HAPPY"
Output: 6
Explanation: 
Using two fingers, one optimal way to type "HAPPY" is:
Finger 1 on letter 'H' -> cost = 0
Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
Finger 2 on letter 'P' -> cost = 0
Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
Total distance = 6
```

**Constraints:**

- `2 <= word.length <= 300`
- Each `word[i]` is an English uppercase letter.

---

#### Tricky 

This is a DP question. We need to consider type a char using left hand or right hand.

Not finished yet.

---

#### My thoughts 

Failed to solve.

---

#### First solution 

```java
class Solution {
    public int minimumDistance(String word) {
        int n = word.length();
        char[] cs = word.toCharArray();
        int[][] cost = new int[26][26];
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                int x1 = i / 6, y1 = i % 6;
                int x2 = j / 6, y2 = j % 6;
                cost[i][j] = Math.abs(x1 - x2) + Math.abs(y1 - y2);
            }
        }
        // Left hand starts at 0, right hand starts at i.
        int best = Integer.MAX_VALUE;
        int[][] dp = new int[n + 1][n + 1];
        for (int[] info : dp) {
            Arrays.fill(info, -1);
        }
        for (int i = 1; i < n; i++) {
            int sum = 0;
            for (int j = 1; j < i; j++) {
                int prev = cs[j - 1] - 'A';
                int point = cs[j] - 'A';
                sum += cost[prev][point];
            }
            best = Math.min(best, sum + findCost(i - 1, i, dp, cost, cs));
        }
        return best;
    }
    // Left hand starts at x, right hand starts at y.
    private int findCost(int x, int y, int[][] dp, int[][] cost, char[] cs) {
        if (dp[x][y] >= 0) return dp[x][y];
        int pos = Math.max(x, y) + 1;
        if (pos == cs.length) return 0;
        int costX = cost[cs[x] - 'A'][cs[pos] - 'A'] + findCost(pos, y, dp, cost, cs);
        int costY = cost[cs[y] - 'A'][cs[pos] - 'A'] + findCost(x, pos, dp, cost, cs);
        dp[x][y] = Math.min(costX, costY);
        return dp[x][y];
    }
}
```

T: O(n^2) 				S: O(n^2)

---

#### Standard solution 

Haven't done with this problem.

---

#### Optimized 



---

#### Summary 

