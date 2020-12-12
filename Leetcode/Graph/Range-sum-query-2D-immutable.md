---
title: Medium | Range Sum Query 2D - Immutable 304
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-06-18 08:26:42
---

Given a 2D matrix *matrix*, find the sum of the elements inside the rectangle defined by its upper left corner (*row*1, *col*1) and lower right corner (*row*2, *col*2).

![Range Sum Query 2D](https://leetcode.com/static/images/courses/range_sum_query_2d.png)
The above rectangle (with the red border) is defined by (row1, col1) = **(2, 1)** and (row2, col2) = **(4, 3)**, which contains sum = **8**.

[Leetcode](https://leetcode.com/problems/range-sum-query-2d-immutable/)

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
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
```

**Note:**

1. You may assume that the matrix does not change.
2. There are many calls to *sumRegion* function.
3. You may assume that *row*1 ≤ *row*2 and *col*1 ≤ *col*2.

**Follow up:** 

[Range Sum Query - Immutable](https://aranne.github.io/2020/06/18/Range-sum-query-immutable-303/#more)	

[Range Sum Query - Mutable](https://aranne.github.io/2020/06/18/Range-sum-query-mutable-307/#more)

[Range Sum Query 2D - Immutable](https://aranne.github.io/2020/06/18/Range-sum-query-2D-immutable/#more)

[Range Sum Query 2D - Mutable](https://aranne.github.io/2020/06/18/Range-sum-query-2D-mutable-308/#more)

---

#### Tricky 

Store `preSum` into 2d array.

![Sum OD](https://leetcode.com/static/images/courses/sum_od.png)

`Sum(ABCD) = preSum(OD) - preSum(OC) - preSum(OB) + preSum(OA)`

---

#### Standard solution  

```java
class NumMatrix {
    
    int[][] preSum;

    public NumMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        preSum = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                preSum[i][j] = preSum[i][j - 1] + preSum[i - 1][j] - preSum[i - 1][j - 1] + matrix[i - 1][j - 1];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return preSum[row2 + 1][col2 + 1] - preSum[row2 + 1][col1] - preSum[row1][col2 + 1] + preSum[row1][col1];
    }
}

```

Time complexity:

initialize: 				 O(mn)			

sumRegion query: O(1)

