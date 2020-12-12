---
title: Medium | Spiral Matrix 54
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-05-13 01:42:00
---

Given a matrix of *m* x *n* elements (*m* rows, *n* columns), return all elements of the matrix in spiral order.

[Leetcode](https://leetcode.com/problems/spiral-matrix/)

<!--more-->

**Example:**

```
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

---

#### Tricky 

How to control the direction when traversing the graph.

* One approach is to remember the current direction and try next direction with recursion.
* Another approach is to narrow the boundary and traverse four borders in order. 

---

#### My thoughts 

The first approach.

---

#### First solution 

Use `boolean[][] visited` to record the visited point.

```java
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
      	if (matrix.length == 0 || matrix[0].length == 0) return res;
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] direction = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        boolean[][] visited = new boolean[m][n];
        getNext(0, 0, 0, visited, direction, matrix, res);
        return res;
    }
    
    private void getNext(int i, int j, int next, boolean[][] visited, int[][] direction, int[][] matrix, List<Integer> res) {
        int m = matrix.length;
        int n = matrix[0].length;
        visited[i][j] = true;
        res.add(matrix[i][j]);
        for (int k = 0; k < 4; k++) {     // try four directions.
            int x = i + direction[next][0];
            int y = j + direction[next][1];
            if (x < 0 || x >= m || y < 0 || y >= n || visited[x][y]) {
                next++;
                if (next == 4) {
                    next = 0;
                }
            } else {
                getNext(x, y, next, visited, direction, matrix, res);
                break;       // Not need to try rest of directions.
            }
        }
    }
}
```

T: O(n^2)		S: O(n^2)  (recursion stack)

---

#### Narrow boundary

Try to narrow the boundary in four directions in order until `top == bottom || left == right`.

```java
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        if (matrix.length == 0 || matrix[0].length == 0) return res;
        int top = 0;
        int bottom = matrix.length;
        int left = 0;
        int right = matrix[0].length;
        while (top != bottom && left != right) {  // narrow the boundary
            for (int j = left; j < right; j++) {  // move right
                res.add(matrix[top][j]);
            }
            top++;
            if (top == bottom) break;
            for (int i = top; i < bottom; i++) {  // move down
                res.add(matrix[i][right - 1]);
            }
            right--;
            if (left == right) break;
            for (int j = right - 1; j >= left; j--) { // move left
                res.add(matrix[bottom - 1][j]);
            }
            bottom--;
            if (top == bottom) break;
            for (int i = bottom - 1; i >= top; i--) {
                res.add(matrix[i][left]);
            }
            left++;
        }
        return res;
    }
}
```

T: O(n^2)		S: O(1)

---

#### Summary 

In tricky.