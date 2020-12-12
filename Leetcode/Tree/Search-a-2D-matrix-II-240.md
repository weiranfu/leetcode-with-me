---
title: Medium | Search a 2D Matrix II 240
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2019-12-15 16:54:38
---

Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

[Leetcode](https://leetcode.com/problems/search-a-2d-matrix-ii/)

<!--more-->

**Example:**

Consider the following matrix:

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

Given target = `5`, return `true`.

Given target = `20`, return `false`.

---

#### Tricky 

This graph is acually a tree. The root is at top-right corner.

So we could search from root just like search in a binary tree.

---

#### My thoughts 

Using binary search in for each valid row.

---

#### First solution 

Using binary search in every row's first value to find the last row that satisify `row[0] < target`.

Then for these valid rows, use binary search to find target in each row. 

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) return false;
        int m = matrix.length, n = matrix[0].length;
        int x_lo = 0, x_hi = m;
        while (x_lo < x_hi) {
            int mid = x_lo + (x_hi - x_lo) / 2;
            if (matrix[mid][0] == target) {
                return true;
            } else if (matrix[mid][0] < target) {
                x_lo = mid + 1;
            } else {
                x_hi = mid;
            }
        }
        for (int i = 0; i < x_hi; i += 1) {
            int[] row = matrix[i];
            int y_lo = 0, y_hi = n;
            while (y_lo < y_hi) {
                int mid = y_lo + (y_hi - y_lo) / 2;
                if (row[mid] == target) {
                    return true;
                } else if (row[mid] < target) {
                    y_lo = mid + 1;
                } else {
                    y_hi = mid;
                }
            }
        }
        return false;
    }
}
```

T: O(n*log(m)) S: O(m)

---

#### Standard solution 

Viewing this graph as a tree rooted at right-top corner.

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0 || matrix[0].length == 0) return false;
        int m = matrix.length, n = matrix[0].length;
        int i = 0, j = n - 1;
        while (i < m && j >= 0) {
            if (matrix[i][j] == target) {
                return true;
            } else if (matrix[i][j] < target) {
                i += 1;
            } else {
                j -= 1;
            }
        }
        return false;
    }
}
```

T: O(m + n) S: O(1)

---

#### Summary 

Ascending graph in 2 directions can be seen as a tree rooted at top-right corner.