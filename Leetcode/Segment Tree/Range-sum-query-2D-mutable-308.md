---
title: Hard | Range Sum Query 2D - Mutable 308
tags:
  - tricky
categories:
  - Leetcode
  - Segment Tree
date: 2020-06-18 08:50:38
---

Given a 2D matrix *matrix*, find the sum of the elements inside the rectangle defined by its upper left corner (*row*1, *col*1) and lower right corner (*row*2, *col*2).

![Range Sum Query 2D](https://leetcode.com/static/images/courses/range_sum_query_2d.png)
The above rectangle (with the red border) is defined by (row1, col1) = **(2, 1)** and (row2, col2) = **(4, 3)**, which contains sum = **8**.

[Leetcode](https://leetcode.com/problems/range-sum-query-2d-mutable/)

<!--more-->

**Example:**

```
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
```

**Note:**

1. The matrix is only modifiable by the *update* function.
2. You may assume the number of calls to *update* and *sumRegion* function is distributed evenly.
3. You may assume that *row*1 ≤ *row*2 and *col*1 ≤ *col*2.

**Follow up:** 

[Range Sum Query - Immutable](https://aranne.github.io/2020/06/18/Range-sum-query-immutable-303/#more)	

[Range Sum Query - Mutable](https://aranne.github.io/2020/06/18/Range-sum-query-mutable-307/#more)

[Range Sum Query 2D - Immutable](https://aranne.github.io/2020/06/18/Range-sum-query-2D-immutable/#more)

[Range Sum Query 2D - Mutable](https://aranne.github.io/2020/06/18/Range-sum-query-2D-mutable-308/#more)

---

#### Tricky 

* 2D Binary Index Tree
* Segment Tree

---

#### 2D Binary Index Tree

```java
class NumMatrix {
    
    int[][] sum;
    int[][] matrix;

    public NumMatrix(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return;
        this.matrix = matrix;
        int m = matrix.length;
        int n = matrix[0].length;
        sum = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                alter(i + 1, j + 1, matrix[i][j]);
            }
        }
    }
    
    private void alter(int row, int col, int delta) {
        for (; row < sum.length; row += lowbit(row)) {
            for (int j = col; j < sum[0].length; j += lowbit(j)) {
                sum[row][j] += delta;
            }
        }
    }
    
    private int query(int row, int col) {
        int res = 0;
        for (; row > 0; row -= lowbit(row)) {
            for (int j = col; j > 0; j -= lowbit(j)) {
                res += sum[row][j];
            }
        }
        return res;
    }
    
    public void update(int row, int col, int val) {
        int delta = val - matrix[row][col];
        matrix[row][col] = val;
        alter(row + 1, col + 1, delta);
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return query(row2 + 1, col2 + 1) - query(row2 + 1, col1) - query(row1, col2 + 1) + query(row1, col1);   
    }
    
    private int lowbit(int x) {
        return x & (-x);
    }
}
```

T: O(logm*logn)		S: O(mn)

---

#### Optimized



---

#### Standard solution  



---

#### Summary 

