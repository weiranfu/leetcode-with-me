---
title: Medium | Count Submatrices with All Ones 1504
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-05 15:53:10
---

Given a `rows * columns` matrix `mat` of ones and zeros, return how many **submatrices** have all ones.

[Leetcode](https://leetcode.com/problems/count-submatrices-with-all-ones/)

<!--more-->

**Example 1:**

```
Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
```

**Example 2:**

```
Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
```

**Follow up:** 

[Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

---

#### Tricky 

* Use `height[]` to store the contiguous 1 in a column.

  Then we iterate each row, and check the max height of each collumn to collect result.

  ```java
  class Solution {
      public int numSubmat(int[][] mat) {
          if (mat == null || mat.length == 0 || mat[0].length == 0) return 0;
          int m = mat.length;
          int n = mat[0].length;
          int[] height = new int[n];
          int res = 0;
          for (int i = 0; i < m; i++) {
              for (int j = 0; j < n; j++) {
                  if (mat[i][j] == 0) {
                      height[j] = 0;
                  } else {
                      height[j]++;
                  }
                  if (mat[i][j] == 1) {
                      int k = j;
                      int h = height[j];
                      while (k >= 0) {
                          h = Math.min(h, height[k]);
                          if (h == 0) break;
                          res += h;                   // collect result
                          k--;
                      }
                  }
              }
          }
          return res;
      }
  }
  ```

  T: O(m\*n\*n)			S: O(n)

* Brute force

  We iterate `up` and `down` rows to fix the upper bound and lower bound of a matrix. Then we need to check if column between `up` and `down` rows has all `1`s. Count contiguous such columns `cnt`.

  If there exist such a column, `res += cnt`

  ```java
  class Solution {
      public int numSubmat(int[][] mat) {
          if (mat == null || mat.length == 0 || mat[0].length == 0) return 0;
          int m = mat.length;
          int n = mat[0].length;
          int[] sum = new int[n];
          int res = 0;
          for (int i = 0; i < m; i++) {     // down row
              Arrays.fill(sum, 0);          // clear sum
              for (int j = i; j < m; j++) { // up row
                  for (int k = 0; k < n; k++) {
                      sum[k] += mat[j][k];
                  }
                  int curr = j - i + 1;    // curr height between up and down
                  int cnt = 0;
                  for (int k = 0; k < n; k++) {
                      if (curr == sum[k]) { // column has all 1s
                          cnt++;
                          res += cnt;     // collect result
                      } else {
                          cnt = 0;
                      }
                  }
              }
          }
          return res;
      }
  }
  ```

  T: O(m\*m\*n)			S: O(n)

* Stack optimization

  When we get all `height` at `i` point, we enumerate `j` to find `min{height[j], height[i]}`.

  If we find a `height[j] > height[i]`, `res += height[i]`.

  If we find a `height[j] < height[i]`, `res += height[j]`.

  We can use `sum[i]` to store all sum at each point, when we find `height[j] < height[i]`, we can just retrieve the store value `res += sum[j]`, because all `j` before it must smaller than `height[i]`.

  **Right now, we want to find the max value smaller current point' height, we can use monotonic stack.**

  Monotonic increasing stack to keep track of index of each point.
  
  We can store `index` and `sum` into stack.
  
  ```java
  class Solution {
      public int numSubmat(int[][] mat) {
          if (mat == null || mat.length == 0 || mat[0].length == 0) return 0;
          int m = mat.length;
          int n = mat[0].length;
          int[] height = new int[n];
          int res = 0;
          for (int i = 0; i < m; i++) {
              Stack<int[]> stack = new Stack<>();
              for (int j = 0; j < n; j++) {
                  if (mat[i][j] == 0) {
                      height[j] = 0;
                  } else {
                      height[j]++;
                  }
                  while (!stack.isEmpty() && height[stack.peek()[0]] >= height[j]) {
                      stack.pop();
                  }
                  int s = 0;
                  if (stack.isEmpty()) {
                      s += height[j] * (j + 1);
                  } else {
                      s += height[j] * (j - stack.peek()[0]);
                      s += stack.peek()[1];
                }
                  stack.push(new int[]{j, s});
                res += s;
              }
          }
          return res;
      }
  }
  ```
  
  T: O(mn)		S: O(n)
  
  