---
title: Hard | N-Queens 51
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-05-12 20:34:24
---

The *n*-queens puzzle is the problem of placing *n* queens on an *n*×*n* chessboard such that no two queens attack each other.

![img](https://assets.leetcode.com/uploads/2018/10/12/8-queens.png)

Given an integer *n*, return all distinct solutions to the *n*-queens puzzle.

Each solution contains a distinct board configuration of the *n*-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space respectively.

[Leetcode](https://leetcode.com/problems/n-queens/)

<!--more-->

**Example:**

```
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
```

---

#### Tricky 

The key is how to record previous state of board when putting queen at row `i`.

We could use three arrays to record columns, 45-degrees & 134-degrees diagonals.

There're `n` columns, `2n - 1`  45-degrees diagonals, `2n - 1` 135-degrees diagonals.

If we put a queen at `board[row][col]`, then we need to check `cols[col]`, `diag1[col + n - row - 1]` and `diag2[2n - row - col - 2]` to see whether there exists a queen.

---

#### My thoughts 

Use backtracking to search all possible solutions.

---

#### Use arrays to record the board

There're `n` columns, `2n - 1`  45-degrees diagonals, `2n - 1` 135-degrees diagonals.

If we put a queen at `board[row][col]`, then we need to check `cols[col]`, `diag1[n - row + col - 1]` and `diag2[row + col]`.

```java
class Solution {
    char[][] board;
    boolean[] cols;
    boolean[] diag1;   // n - row + col - 1
    boolean[] diag2;   // row + col
    int n;
    
    public List<List<String>> solveNQueens(int n) {
        this.n = n;
        board = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = '.';
            }
        }
        List<List<String>> res = new ArrayList<>();
        cols = new boolean[n];
        diag1 = new boolean[2 * n - 1];
        diag2 = new boolean[2 * n - 1];
        solve(new ArrayList<>(), res);
        return res;
    }
    
    private void solve(List<String> curr, List<List<String>> res) {
        int row = curr.size();
        if (row == n) {
            res.add(new ArrayList<>(curr));
            return;
        }
        for (int col = 0; col < n; col++) {
            if (!cols[col] && !diag1[n - row + col - 1] && !diag2[row + col]) {
                cols[col] = true;
                diag1[n - row + col - 1] = true;
                diag2[row + col] = true;
                board[row][col] = 'Q';
                curr.add(new String(board[row]));
                solve(curr, res);
                curr.remove(curr.size() - 1);
                board[row][col] = '.';
                cols[col] = false;
                diag1[n - row + col - 1] = false;
                diag2[row + col] = false;
            }
        }
    }
}
```

T: O(n!)		S: O(n^2)

---

#### Bitmask

We can use `l`, `mid`, `r` to record the invalid position on current row. 

`l` means positions invalid by upper right queen, `mid` means positions invalid by upper queen, `r` means positions invalid by upper left queen.

How to invalid positions on next row if we put on `[row, col]` with current `l`, `mid`, `r`.

1. invalid the pos below current pos, `mid | pick`
2. invalid the pos at bottom left, `(l | pick) << 1`
3. invalid the pos at bottom right, `(r | pick) >> 1`

Use `int mask = ~(l | mid | r) & ((1 << n) - 1)`  to get all valid pos for current row.

Use `int pick = mask & (-mask)` to get the lowbit of mask.

Use `mask = mask & (mask - 1)` to flip the last one of mask.

```java
class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<>();
        if (n == 0) return res;
        List<String> list = new ArrayList<>();
        dfs(0, 0, 0, 0, n, list, res);
        return res;
    }
    
    private void dfs(int row, int l, int mid, int r, int n, List<String> list, List<List<String>> res) {
        if (row == n) {
            res.add(new ArrayList<>(list));
            return;
        }
        int mask = ~(l | mid | r) & ((1 << n) - 1); // valid bits
        while (mask > 0) {
            int pick = mask & (-mask);              // lowbit
            list.add(getLine(pick, n));
            dfs(row + 1, (l | pick) << 1, mid | pick, (r | pick) >> 1, n, list, res);
            list.remove(list.size() - 1);
            mask = mask & (mask - 1);               // flip the last one of mask
        }
    }
    
    private String getLine(int pick, int n) {
        char[] row = new char[n];
        int i = n - 1;
        while (i >= 0) {
            if ((pick & 1) == 1) {
                row[i] = 'Q';
            } else {
                row[i] = '.';
            }
            if (pick != 0) pick >>= 1;
            i--;
        }
        return new String(row);
    }
}
```

T: O(N!)			S: O(n)