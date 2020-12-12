---
title: Hard | Sudoku Solver 37
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-01-30 20:48:13
---

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

Empty cells are indicated by the character `'.'`.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)
A sudoku puzzle...

[Leetcode](https://leetcode.com/problems/sudoku-solver/)

<!--more-->

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)
...and its solution numbers marked in red.

**Note:**

- The given board contain only digits `1-9` and the character `'.'`.
- You may assume that the given Sudoku puzzle will have a single unique solution.
- The given board size is always `9x9`.

---

#### Tricky 

How to solve a problem with so many possibilities?

The difficulty is that if we put a num at a wrong place, how can we backtrack to previous state?

Use DFS + backtracking to go back.

```java
put(num)   // put an integer here
if (solve()) {
   return true;
} else {
   remove(num)  // go back
}
```

---

#### My thoughts

There are two programming conceptions here which could help.

> The first one is called *constrained programming*.

That basically means to put restrictions after each number placement. One puts a number on the board and that immediately excludes this number from further usage in the current *row*, *column* and *sub-box*. That propagates *constraints* and helps to reduce the number of combinations to consider.

![bla](https://leetcode.com/problems/sudoku-solver/Figures/37/37_const3.png)

> The second one called *backtracking*.

Let's imagine that one has already managed to put several numbers on the board. But the combination chosen is not the optimal one and there is no way to place the further numbers. What to do? *To backtrack*. That means to come back, to change the previously placed number and try to proceed again. If that would not work either, *backtrack* again.

![bla](https://leetcode.com/problems/sudoku-solver/Figures/37/37_backtrack2.png)

------

#### First solution  

Use `cell[][] row[] and col[]` array to record constraints on each point.

Once a num is put, the constraint will be updated.

Use backtracking to go back to previous state.

```java
class Solution {
    public void solveSudoku(char[][] board) {
        int n = board.length;
        boolean[][] cell = new boolean[n][n+1];
        boolean[][] row = new boolean[n][n+1];
        boolean[][] col = new boolean[n][n+1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                char c = board[i][j];
                if (c == '.') continue;
                int value = c - '0';
                row[i][value] = true;
                col[j][value] = true;
                cell[getCell(i, j)][value] = true;
            }
        }
        solve(0, board, cell, row, col);
    }
    private boolean solve(int k, char[][] board, boolean[][] cell, boolean[][] row, boolean[][] col) {
        int n = board.length;
        if (k == n * n) return true;
        int i = k / n;
        int j = k % n;
        if (board[i][j] != '.') return solve(k + 1, board, cell, row, col);
        for (int v = 1; v <= 9; v++) {
            if (cell[getCell(i, j)][v] || row[i][v] || col[j][v]) continue;
            board[i][j] = (char) ('0' + v);
            cell[getCell(i, j)][v] = true;
            row[i][v] = true;
            col[j][v] = true;
            if (solve(k + 1, board, cell, row, col)) {  // DFS to solve it
                return true;
            } else {                                   // starts backtracking to previous state.
                board[i][j] = '.';
                cell[getCell(i, j)][v] = false;
                row[i][v] = false;
                col[j][v] = false;
            }
        }
        return false;
    }
    private int getCell(int i, int j) {
        int row = i / 3;
        int col = j / 3;
        return row * 3 + col;
    }
}
```

T: O((9!)^9)			For each row, no more than 9! possibilities. So totally is O((9!)^9)

S: O(81)

---

#### Summary 

Use DFS + backtracking + constrained programming to try all the possible tries.