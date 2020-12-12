---
title: Medium | Set Matrix Zeroes
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-05-15 20:01:35
---

Given a *m* x *n* matrix, if an element is 0, set its entire row and column to 0. Do it [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm).

[Leetcode](https://leetcode.com/problems/set-matrix-zeroes/)

<!--more-->

**Example:**

```
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
```

**Follow up:** Could you devise a constant space solution?

---

#### Tricky 

When we encounter a zero, we cannot set the row & column to be zeroes immediately, because this will affect the rest of graph for indicating zero.

* A straight forward way is to use O(mn) space to set all zeroes.

* A simple improvement uses O(m + n) (two arrays to store states of each row & col) to set all zeroes.

* Best solution is to use the space of first row and column to store states instead of allocating two arrays.

  **In the first phase, use matrix elements to set states in a top-down way. In the second phase, use states to set matrix elements in a bottom-up way to avoid affecting the rest of graph for indicating zeroes.**

---

#### My thoughts 

Second approach, space complexity: O(m + n)

---

#### First solution 

```java
class Solution {
    public void setZeroes(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return;
        int m = matrix.length;
        int n = matrix[0].length;
        boolean[] rows = new boolean[m];
        boolean[] cols = new boolean[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    if (!rows[i]) {
                        rows[i] = true;
                    }
                    if (!cols[j]) {
                        cols[j] = true;
                    }
                }
            }
        }
        for (int row = 0; row < m; row++) {
            if (rows[row]) {
                for (int col = 0; col < n; col++) {
                    matrix[row][col] = 0;
                }
            }
        }
        for (int col = 0; col < n; col++) {
            if (cols[col]) {
                for (int row = 0; row < m; row++) {
                    matrix[row][col] = 0;
                }
            }
        }
    }
}
```

T: O(mn)		S: O(m + n)

---

#### Optimized: 

**Use the space of first row & col instead of allocating two arrays.**

Store states of each row in the first of that row, and store states of each column in the first of that column. Because the state of row0 and the state of column0 would occupy the same cell, I let it be the state of row0, and use another variable "col0" for column0. 

**In the first phase, use matrix elements to set states in a top-down way. In the second phase, use states to set matrix elements in a bottom-up way**

```java
class Solution {
    public void setZeroes(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return;
        int m = matrix.length;
        int n = matrix[0].length;
        int col0 = 1;
        for (int i = 0; i < m; i++) {            // top-bottom
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    if (j == 0) {
                        col0 = 0;
                    } else {
                        matrix[i][0] = 0;
                        matrix[0][j] = 0;
                    }
                }
            }
        }
        for (int i = m - 1; i >= 0; i--) {         // bottom-up
            for (int j = n - 1; j >= 0; j--) {
                if (j == 0) {
                    if (col0 == 0) {
                        matrix[i][j] = 0;
                    }
                } else if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}
```

T: O(mn)		S: O(1)

---

#### Summary 

In tricky.