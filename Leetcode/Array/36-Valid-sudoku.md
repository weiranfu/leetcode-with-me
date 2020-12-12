---
title: Medium | Valid Sudoku 36
tags:
  - common
categories:
  - Leetcode
  - Array
date: 2020-01-30 13:34:29
---

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the 9 `3x3` sub-boxes of the grid must contain the digits `1-9` without repetition.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

[Leetcode](https://leetcode.com/problems/valid-sudoku/)

<!--more-->

The Sudoku board could be partially filled, where empty cells are filled with the character `'.'`.

**Example 1:**

```
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
```

**Example 2:**

```
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

**Note:**

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
- The given board contain only digits `1-9` and the character `'.'`.
- The given board size is always `9x9`.

---

#### My thoughts 

Use three 2D array to store columns, rows and cells number of integer.

```java
int[][] box = new int[n][n+1];
int[][] row = new int[n][n+1];
int[][] col = new int[n][n+1];
```

How to compute cell's index?

```java
int colNum = j / 3;
int rowNum = i / 3;
int bucket = rowNum * 3 + colNum;
```

---

#### Standard solution  

```java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        int n = board.length;
        int[][] box = new int[n][n+1];
        int[][] row = new int[n][n+1];
        int[][] col = new int[n][n+1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '.') continue;
                int value = board[i][j] - '0';
                int colNum = j / 3;
                int rowNum = i / 3;
                int bucket = rowNum * 3 + colNum;
                box[bucket][value]++;
                if (box[bucket][value] > 1) return false;
                col[j][value]++;
                if (col[j][value] > 1) return false;
                row[i][value]++;
                if (row[i][value] > 1) return false;
            }
        }
        return true;
    }
}
```

T: O(mn) 			S: O(mn)