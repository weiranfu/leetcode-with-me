---
title: Medium | Design Tic-Tac-Toe 348
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Design
date: 2020-07-16 01:22:33
---

Design a Tic-tac-toe game that is played between two players on a *n* x *n* grid.

You may assume the following rules:

1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves is allowed.
3. A player who succeeds in placing *n* of their marks in a horizontal, vertical, or diagonal row wins the game.

Can you devise a solution with O(1) time complexity?

[Leetcode](https://leetcode.com/problems/design-tic-tac-toe/)

<!--more-->

**Example:**

```
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
```

**Follow up**

[Valid Tic-Tac-Toe State](https://leetcode.com/problems/valid-tic-tac-toe-state/)

---

#### Tricky 

1. Bitmask

   We can use `rows[]` and `cols[]` to represent the rows and cols selection by two players.

   And we only care about the right center two diagonals.

   So we use `diag1`  and `diag2`. 

   `n - row + col -1` is the index for `diag1`

   `row + col` is the index for `diag2`

   Check the value has its position with all `1`s

   ```java
   class TicTacToe {
       int[][] rows;
       int[][] cols;
       int[] diag1;  // n - row + col - 1
       int[] diag2;  // row + col
       int n;
   
       /** Initialize your data structure here. */
       public TicTacToe(int n) {
           this.n = n;
           rows = new int[n][2];
           cols = new int[n][2];
           diag1 = new int[2];
           diag2 = new int[2];
       }
       
       /** Player {player} makes a move at ({row}, {col}).
           @param row The row of the board.
           @param col The column of the board.
           @param player The player, can be either 1 or 2.
           @return The current winning condition, can be either:
                   0: No one wins.
                   1: Player 1 wins.
                   2: Player 2 wins. */
       public int move(int row, int col, int player) {
           rows[row][player - 1] |= 1 << col;
           cols[col][player - 1] |= 1 << row;
           if (n - row + col - 1 == n - 1) {
               diag1[player - 1] |= 1 << col;
           }
           if (row + col == n - 1) {
               diag2[player - 1] |= 1 << row;
           }
           if (rows[row][player - 1] == (1 << n) - 1 || cols[col][player - 1] == (1 << n) - 1
              || diag1[player - 1] == (1 << n) - 1
              || diag2[player - 1] == (1 << n) - 1) {
               return player;
           }
           return 0;
       }
   }
   ```

   T: O(1)			S: O(n)

2. Optimization

   Player1 place a move will add 1, and player2 place a move will reduce 1.

   We could plus all values in a same row to check whether the value is `n`.

   ```java
   class TicTacToe {
       int[] rows;
       int[] cols;
       int diag1;  // n - row + col - 1
       int diag2;  // row + col
       int n;
   
       /** Initialize your data structure here. */
       public TicTacToe(int n) {
           this.n = n;
           rows = new int[n];
           cols = new int[n];
       }
       
       /** Player {player} makes a move at ({row}, {col}).
           @param row The row of the board.
           @param col The column of the board.
           @param player The player, can be either 1 or 2.
           @return The current winning condition, can be either:
                   0: No one wins.
                   1: Player 1 wins.
                   2: Player 2 wins. */
       public int move(int row, int col, int player) {
           int add = player == 1 ? 1 : -1;
           rows[row] += add;
           cols[col] += add;
           if (n - row + col - 1 == n - 1) {
               diag1 += add;
           }
           if (row + col == n - 1) {
               diag2 += add;
           }
           if (Math.abs(rows[row]) == n || Math.abs(cols[col]) == n 
               || Math.abs(diag1) == n 
               || Math.abs(diag2) == n) {
               return player;
           }
           return 0;
       }
   }
   ```

   T: O(1)			S: O(n)