---
title: Medium | Word Search I 79
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-06-09 16:29:11
---

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

[Leetcode](https://leetcode.com/problems/word-search/)

<!--more-->

**Example:**

```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```

**Follow up:** [Word Search II](https://aranne.github.io/2020/06/09/Word-search-II-212/#more)

---

#### Tricky 

Try all possible start point and perform backtracking search.

---

#### Standard solution  

```java
class Solution {
    public boolean exist(char[][] board, String word) {
        if (board == null || board.length == 0 || board[0].length == 0 || word == null || word.equals("")) {
            return false;
        }
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int m = board.length;
        int n = board[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word.charAt(0)) {  // starts searching
                    if (search(i, j, 1, board, word, directions)) { // next word
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    private boolean search(int i, int j, int next, char[][] board, String word, int[][] directions) {
        if (next == word.length()) return true;
        board[i][j] = '$';                                  // visit (i, j)
        int m = board.length;
        int n = board[0].length;
        char c = word.charAt(next);
        for (int[] direction : directions) {
            int x = i + direction[0];
            int y = j + direction[1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (board[x][y] == word.charAt(next)) {
                if (search(x, y, next + 1, board, word, directions)) {
                  	board[i][j] = word.charAt(next - 1);   // reset board
                    return true;
                }
            }
        }
        board[i][j] = word.charAt(next - 1);              // reset board.
        return false;
    }
}
```

T: O(mn*depth)			S: O(mn)

