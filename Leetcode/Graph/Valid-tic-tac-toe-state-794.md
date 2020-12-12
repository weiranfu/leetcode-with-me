---
title: Medium | Valid Tic-Tac-Toe State 794
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-16 02:18:14
---

A Tic-Tac-Toe board is given as a string array `board`. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The `board` is a 3 x 3 array, and consists of characters `" "`, `"X"`, and `"O"`.  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

- Players take turns placing characters into empty squares (" ").
- The first player always places "X" characters, while the second player always places "O" characters.
- "X" and "O" characters are always placed into empty squares, never filled ones.
- The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
- The game also ends if all squares are non-empty.
- No more moves can be played if the game is over.

[Leetcode](https://leetcode.com/problems/valid-tic-tac-toe-state/)

<!--more-->

```
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
```

**Follow up**

[Find Winner on a Tic-Tac-Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)

---

#### Tricky 

**When X wins, O cannot move anymore, so `turns` must be 1. When O wins, X cannot move anymore, so `turns` must be 0. Finally, when we return, `turns` must be either 0 or 1**

```java
class Solution {
    public boolean validTicTacToe(String[] board) {
        int n = board.length;
        int[] rows = new int[n];
        int[] cols = new int[n];
        int diag1 = 0, diag2 = 0;
        int cnt1 = 0, cnt2 = 0;   // count for 'X' and 'O'
        int win1 = 0, win2 = 0;   // count for win
        for (int i = 0; i < n; i++) {
            String row = board[i];
            for (int j = 0; j < n; j++) {
                char c = row.charAt(j);
                if (c != 'X' && c != 'O') continue;
                int add = c == 'X' ? 1 : -1;
                if (c == 'X') {
                    cnt1++;
                } else {
                    cnt2++;
                }
                rows[i] += add;
                cols[j] += add;
                if (n - i + j - 1 == n - 1) {
                    diag1 += add;
                } 
                if (i + j == n - 1) {
                    diag2 += add;
                }
                if (rows[i] == n || cols[j] == n || diag1 == n || diag2 == n) {
                    win1++;
                }
                if (rows[i] == -n || cols[j] == -n || diag1 == -n || diag2 == -n) {
                    win2++;
                }
            }
        }
        int more = cnt1 - cnt2; 
      	// X and O cannot win at same time
      	// X wins with more = 1 or O wins with more = 0
        if (win1 > 0 && more != 1 || win2 > 0 && more != 0) return false;
        return more == 0 || more == 1; // more can only 1 or 0
    }
}
```

T: O(n^2)			S: O(n)

