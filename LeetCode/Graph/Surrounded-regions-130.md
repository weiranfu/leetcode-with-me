---
title: Medium | Surrounded Regions 130
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-05-27 08:23:33
---

Given a 2D board containing `'X'` and `'O'` (**the letter O**), capture all regions surrounded by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.

[Leetcode](https://leetcode.com/problems/surrounded-regions/)

<!--more-->

**Example:**

```
X X X X
X O O X
X X O X
X O X X
```

After running your function, the board should be:

```
X X X X
X X X X
X X X X
X O X X
```

**Explanation:**

Surrounded regions shouldn’t be on the border, which means that any `'O'` on the border of the board are not flipped to `'X'`. Any `'O'` that is not on the border and it is not connected to an `'O'` on the border will be flipped to `'X'`. Two cells are connected if they are adjacent cells connected horizontally or vertically.

---

#### Tricky 

We can return `true` during dfs if the `O`s do not connect to the boundary.

If the `O` is not connected to the boundary `O`, then it should be changed to `X`.

We could use DFS the `O` on the boundary to get all `O` nodes connected boundary.

How to mark them? 

* Use `boolean[][] visited` to mark boundary `O`.
* Change `board[i] = '*'`, after altering all `O` to `X`, change `*` back to `O`.

---

Change `board[i] = '*'` to mark boundary `O`.

1. change all `O` connected to boundary into `*`.
2. Scan the board change `O` into `X` and `*` into `O`.

```java
class Solution {
    int[][] moves = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    char[][] board;
    int m, n;
    
    public void solve(char[][] board) {
        if (board == null || board.length == 0 || board[0].length == 0) return;
        this.board = board;
        m = board.length; n = board[0].length;
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') fill(i, 0, '*');
            if (board[i][n - 1] == 'O') fill(i, n - 1, '*');
        }
        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O') fill(0, j, '*');
            if (board[m - 1][j] == 'O') fill(m - 1, j, '*');
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'X') continue;
                else if (board[i][j] == 'O') board[i][j] = 'X';
                else if (board[i][j] == '*') board[i][j] = 'O';
            }
        }
    }
    private void fill(int i, int j, char c) {
        board[i][j] = c;
        for (int[] move : moves) {
            int x = i + move[0];
            int y = j + move[1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (board[x][y] == 'O') {
                board[x][y] = c;
                fill(x, y, c);
            }
        }
    }
}
```

T: O(mn)		S: O(mn) (recursion stack)

