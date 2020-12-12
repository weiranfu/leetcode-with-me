---
title: Easy | Nim Game 292
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-15 15:31:41
---

You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

[Leetcode](https://leetcode.com/problems/nim-game/)

<!--more-->

**Example:**

```
Input: 4
Output: false 
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be 
             removed by your friend.
```

---

#### Tricky 

1. SG Theorem. (**LTE**)

   Since a state with `n` stones can only transit to `n - 1`, `n - 2` and `n - 3` states, we can use 

   `int[] dp = new int[3]` to store the states' SG value.

   ```java
   class Solution {
       public boolean canWinNim(int n) {
           int[] dp = new int[3];
           for (int i = 1; i <= n; i++) {
               Set<Integer> set = new HashSet<>();
               for (int j = 1; j <= 3; j++) {
                   if (i - j >= 0) {
                       set.add(dp[(i - j) % 3]);
                   }
               }
               for (int j = 0; ; j++) {
                   if (!set.contains(j)) {
                       dp[i % 3] = j;
                       break;
                   }
               }
           }
           return dp[n % 3] != 0;
       }
   }
   ```

   T：O(n)		S: O(1)

2. Find the Theorem: The first one who got the number that is multiple of 4 (i.e. n % 4 == 0) will lost, otherwise he/she will win.

   The SG value of number of stones is 

   stones:		0    1   2   3  4   5  6  7  8

   SG:			   0    1   2   3  0   1  2  3  0

   ```java
   class Solution {
       public boolean canWinNim(int n) {
           return n % 4 != 0;
       }
   }
   ```

   T: O(1)			S: O(1)