---
title: Medium | Flip Game II 294
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-15 12:46:25
---

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: `+` and `-`, you and your friend take turns to flip two **consecutive** `"++"` into `"--"`. The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

[Leetcode](https://leetcode.com/problems/flip-game-ii/)

<!--more-->

**Example:**

```
Input: s = "++++"
Output: true 
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
```

---

#### Tricky 

#### Backtracking

```java
class Solution {
    public boolean canWin(String s) {
        if (s == null || s.length() <= 1) return false;
        char[] cs = s.toCharArray();
        return canWinHelper(cs);
    }
    public boolean canWinHelper(char[] cs) {
        for (int i = 0; i < cs.length - 1; i++) {
            if (cs[i] == '+' && cs[i + 1] == '+') {
                cs[i] = '-';
                cs[i + 1] = '-';
                if (!canWinHelper(cs)) {
                    cs[i] = '+';
                    cs[i + 1] = '+';
                    return true;
                }
                cs[i] = '+';
                cs[i + 1] = '+';
            }
        }
        return false;
    }
}
```

T: O(n!)			S: O(2^n)

let's say the length of the input string `s` is `n`, there are at most `n - 1` ways to replace `"++"` to `"--"` (imagine `s` is all `"+++..."`), once we replace one `"++"`, there are at most `(n - 2) - 1` ways to do the replacement, it's a little bit like solving the N-Queens problem, the time complexity is `(n - 1) x (n - 3) x (n - 5) x ...`, so it's `O(n!!)`, [double factorial](https://en.wikipedia.org/wiki/Double_factorial).

2. Optimized with memorization

   We can store the `boolean` value for each `string` into a Map.

   ```java
   class Solution {
       Map<String, Boolean> map;
       public boolean canWin(String s) {
           if (s == null || s.length() <= 1) return false;
           map = new HashMap<>();
           return canWinHelper(s);
       }
       public boolean canWinHelper(String s) {
           if (map.containsKey(s)) return map.get(s);
           for (int i = 0; i < s.length() - 1; i++) {
               if (s.startsWith("++", i)) {
                   String str = s.substring(0, i) + "--" + s.substring(i + 2);
                   if (!canWinHelper(str)) {
                       map.put(s, true);
                       return true;
                   }
               }
           }
           map.put(s, false);
           return false;
       }
   }
   ```

   T: O(n\*2^n)			S: O(2^n)

#### Game theory and Strague-Grundy Theorem.

1. Use `long state` bitmask to represent the occurrences of `+`.

   For a contiguous `+`, we could view them as a indepent DAG game.

   For example, `++--+-+++` has three independ DAG game. `110000000`, `000010000` and `000000111`

   Since we use `long` as state, we cannot use `int[] dp` to store state's SG value. We need to use Map to store them.

   Since we use `long` as state, we need to use `(long)1 << i` to set a flag.

   ```java
   class Solution {
       int n;
       Map<Long, Integer> dp;
       public boolean canWin(String s) {
           n = s.length();
           long state = 0;
           for (int i = 0; i < n; i++) {
               if (s.charAt(i) == '+') {
                   state |= (long)1 << i;
               }
           }
           dp = new HashMap<>();
           int res = 0;
           int i, j;
           long st = 0;
           for (i = 0, j = -1; i < n; i++) {
               if ((state >> i & 1) == 0 && st != 0) {
                   res ^= sg(st);
                   st = 0;
               } else if ((state >> i & 1) == 1) {
                   st |= (long)1 << i;             // collect 1
               }
           }
           if (st != 0) {
               res ^= sg(st);
           }
           return res != 0;
       }
       private int sg(long state) {
           if (dp.containsKey(state)) return dp.get(state);
           Set<Integer> set = new HashSet<>();
           for (int i = 0; i < n - 1; i++) {
               if ((state >> i & 1) == 1 && (state >> (i+1) & 1) == 1) {   // two contigous +
                   long s = state ^ (((long)1 << i) | ((long)1 << (i+1)));  // remove 1
                   set.add(sg(s));
               }
           }
           for (int i = 0; ; i++) {
               if (!set.contains(i)) {
                   dp.put(state, i);
                   return i;
               }
           }
       }
   }
   ```

   T: O(n\* 2^n)			S: O(2^n)

2. However, sometimes the String can be longer than `64`, which cannot be represented by bitmask.

   Here we find that the game only need the number of contigous `+`, so we can only represent game state using number of contiguous `+`.

   `++--+--+++` will be represented as `(2, 1, 3)`

   How to choose two `+` from a game?

   `+++++` will be divided into `(0,3)`, `(1,2)`. Mind that `(2, 1)` and `(3, 0)` is duplicate game.

   ```java
   class Solution {
       public boolean canWin(String s) {
           int n = s.length();
           List<Integer> states = new ArrayList<>();
           int max = 0, len = 0;
           for (int i = 0; i < n; i++) {
               if (s.charAt(i) == '+') {
                   len++;
               } 
               if (i + 1 == n || s.charAt(i) == '-') { // collect len
                   if (len >= 2) states.add(len);
                   max = Math.max(max, len);
                   len = 0;
               }
           }
           int[] dp = new int[max + 1];
           for (int i = 2; i <= max; i++) {        
               Set<Integer> set = new HashSet<>();
               for (int j = 0; j <= (i - 2) / 2; j++) {// all possible substates
                   set.add(dp[j] ^ dp[i - j - 2]);     // SG theorem
               }
               for (int j = 0; ; j++) {
                   if (!set.contains(j)) {    // find SG value
                       dp[i] = j;
                       break;
                   }
               }
           }
           int res = 0;
           for (int state : states) {
               res ^= dp[state];
           }
           return res != 0;
       }
   }
   ```

   T: O(n^2)			S: O(n)