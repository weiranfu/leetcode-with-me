---
title: Medium | Rotate Image 48
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-05-09 23:22:39
---

You are given an *n* x *n* 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

**Note:**

You have to rotate the image [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm), which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

[Leetcode](https://leetcode.com/problems/rotate-image/)

<!--more-->

**Example 1:**

```
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

**Example 2:**

```
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

---

#### Tricky 

* clockwise rotate:

  first reverse up to down, then swap the symmetry 

  ```
  1 2 3     7 8 9     7 4 1
  4 5 6  => 4 5 6  => 8 5 2
  7 8 9     1 2 3     9 6 3
  ```

* anticlockwise rotate:

  first reverse left to right, then swap the symmetry

  ```
  1 2 3     3 2 1     3 6 9
  4 5 6  => 6 5 4  => 2 5 8
  7 8 9     9 8 7     1 4 7
  ```

---

#### My thoughts 

Rotate the matrix layer by layer.

---

#### First solution 

```java
class Solution {
    public void rotate(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        if (m == 0 || m != n) return;
        for (int k = 0; k < n / 2; k++) {
            rotateLayer(matrix, k);
        }
    }
    
    private void rotateLayer(int[][] matrix, int layer) {
        int m = matrix.length;
        int tmp;
        // layer_length = m - layer * 2
        // rotate_length = layer_length - 1.
        for (int i = 0; i < m - layer * 2 - 1; i++) {
            tmp = matrix[layer][layer + i];
            matrix[layer][layer + i] = matrix[m - 1 - layer - i][layer];
            matrix[m - 1 - layer - i][layer] = matrix[m - 1 - layer][m - 1 - layer - i];
            matrix[m - 1 - layer][m - 1 - layer - i] = matrix[layer + i][m - 1 - layer];
            matrix[layer + i][m - 1 - layer] = tmp;
        }
    }
}
```

T: O(n^2) 		S: O(1)

---

#### Optimized

Reverse up to down, then swap the symmetry.

```java
class Solution {
    public void rotate(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        if (m == 0 || m != n) return;
        for (int i = 0; i < n / 2; i++) {
            int[] tmp = matrix[i];
            matrix[i] = matrix[m - 1 - i];
            matrix[m - 1 - i] = tmp;
        }
        for (int i = 0; i < m; i++) {
            for (int j = i + 1; j < n; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = tmp;
            }
        }
    }
}
```

T: O(n^2)		S: O(1)

---

#### Summary 

In tricky.