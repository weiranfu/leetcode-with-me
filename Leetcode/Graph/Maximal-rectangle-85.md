---
title: Hard | Maximal Rectangle 85
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-05-19 07:15:50
---

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

[Leetcode](https://leetcode.com/problems/maximal-rectangle/)

<!--more-->

**Example:**

```
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
```

**Follow up:** [Maximal Square](https://aranne.github.io/2020/06/19/Maximal-Square-221/#more)

---

#### Tricky 

1. This question is similar as [[Largest Rectangle in Histogram\]](http://oj.leetcode.com/problems/largest-rectangle-in-histogram/):

   You can maintain a row length of Integer array H recorded its height of '1's, and scan and update row by row to find out the largest rectangle of each row.

   For each row, if `matrix[row][i] == '1'`. `H[i] +=1`, or reset the `H[i] = 0`.
   and accroding the algorithm of [Largest Rectangle in Histogram](http://oj.leetcode.com/problems/largest-rectangle-in-histogram/), to update the maximum area.

   #### Stack 

   ```java
   class Solution {
       public int maximalRectangle(char[][] matrix) {
           if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;
           int m = matrix.length, n = matrix[0].length;
           int[] heights = new int[n + 1];
           
           int max = 0;
           Stack<Integer> stack = new Stack<>();
           for (int i = 0; i < m; i++) {
               stack.clear();
               for (int j = 0; j <= n; j++) {
                   if (j < n) {
                       if (matrix[i][j] == '1') {
                           heights[j]++;
                       } else {
                           heights[j] = 0;
                       }
                   }
                   while (!stack.isEmpty() && heights[stack.peek()] > heights[j]) {
                       int H = heights[stack.pop()];
                       int idx = stack.isEmpty() ? -1 : stack.peek();
                       max = Math.max(max, H * (j - idx - 1));
                   }
                   stack.push(j);
               }
           }
           return max;
       }
   }
   ```

   T: O(n^2)			S: O(n)

2. Save the number of contiguous `1` for each point in every col as `height[j]`. For example, 

   ```java
   col 1					height[]     1
       0											 0
       1                      1
       1                      2
       1                      3
   ```
   
   `height[j] = height[j] + 1 if matrix[i][j] == '1'`
   
   Since we get the max height every point in curr row, we could compute the area a point can form.
   
   We can scan from curr point to left most and keep tracking the min height. (Since ractangle is stricted by min height) `minH = Math.min(minH, height[k])`
   
   ```
     1 1 1								
     0 1 1											
   1 1 1 1(curr)						height   1 1 3 3
   ```
   
   `area = minH * (j - k + 1)`
   
   #### Hight Array + Brute Force
   
   ```java
   class Solution {
       public int maximalRectangle(char[][] matrix) {
           if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;
           int m = matrix.length;
           int n = matrix[0].length;
           int[] height = new int[n];
           
           int max = 0;
           for (int i = 0; i < m; i++) {
               for (int j = 0; j < n; j++) {
                   if (matrix[i][j] == '0') {
                       height[j] = 0;
                   } else {
                       height[j]++;
                   }
                   int minH = height[j];
                   for (int k = j; k >= 0; k--) {        // search left bound
                       minH = Math.min(minH, height[k]);
                       if (minH == 0) break;
                       max = Math.max(max, minH * (j - k + 1));
                   }
               }
           }
           return max;
       }
   }
   ```
   
   T: O(m\*n^2)			S: O(mn)
   
3. Brute force

   We iterate `up` and `down` rows to fix the upper bound and lower bound of matrix. Then we check each column whether it has all `1`s. Count contiguous such column.

   ```java
   class Solution {
       public int maximalRectangle(char[][] matrix) {
           if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;
           int m = matrix.length;
           int n = matrix[0].length;
           int[] sum = new int[n];
           
           int max = 0;
           for (int i = 0; i < m; i++) {     // down row
               Arrays.fill(sum, 0);          // clear sum
               for (int j = i; j < m; j++) { // up row
                   for (int k = 0; k < n; k++) {
                       sum[k] += matrix[j][k] - '0';
                   }
                   int curr = j - i + 1;     // current height
                   int cnt = 0;
                   for (int k = 0; k < n; k++) {
                       if (sum[k] == curr) { // column has all 1s
                           cnt++;
                           max = Math.max(max, curr * (cnt));
                       } else {
                           cnt = 0;
                       }
                   }
               }
           }
           return max;
       }
   }
   ```

   T: O(m\*m\*n)				S: O(n)

4. We can store the max height of each point in every row can span.

   And store the max left width's index and right width's index it can span at this height.

   Height:

   This one is easy. `h` is defined as the number of continuous ones in a line from our point.

   ```java
   new_height[j] = old_height[j] + 1 if row[j] == '1' else 0
   ```

   Left:

   Consider what causes changes to the left bound of our rectangle. Since all instances of zeros occurring in the row above the current one have already been factored into the current version of `left`, the only thing that affects our `left` is if we encounter a zero in our current row.

   As a result we can define:

   ```java
   new_left[j] = max(old_left[j], cur_left)
   ```

   `cur_left` is one greater than rightmost occurrence of zero we have encountered. When we "expand" the rectangle to the left, we know it can't expand past that point, otherwise it'll run into the zero.

   Right:

   Here we can reuse our reasoning in `left` and define:

   ```
   new_right[j] = min(old_right[j], cur_right)
   ```

   `cur_right` is the leftmost occurrence of zero we have encountered. For the sake of simplicity, we don't decrement `cur_right` by one (like how we increment `cur_left`) so we can compute the area of the rectangle with `height[j] * (right[j] - left[j])` instead of `height[j] * (right[j] + 1 - left[j])`.

   #### Height, Left, Right

   ```java
   class Solution {
       public int maximalRectangle(char[][] matrix) {
           if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return 0;
           int m = matrix.length;
           int n = matrix[0].length;
           int[] height = new int[n];
           int[] left = new int[n];
           int[] right = new int[n];
           
           Arrays.fill(right, n);// initialize right as the rightmost boundary possible
           
           int max = 0;
           for (int i = 0; i < m; i++) {
               for (int j = 0; j < n; j++) {
                   if (matrix[i][j] == '0') {
                       height[j] = 0;
                   } else {
                       height[j]++;
                   }
               }
               int curr_left = 0;    // track 0's index
               for (int j = 0; j < n; j++) { // scan from left to right
                   if (matrix[i][j] == '0') {
                       left[j] = 0;         // reset to left most
                       curr_left = j + 1;
                   } else {
                       left[j] = Math.max(left[j], curr_left);
                   }
               }
               int curr_right = n;  // track 0's index 
               for (int j = n - 1; j >= 0; j--) {
                   if (matrix[i][j] == '0') {
                       right[j] = n;       // reset to right most
                       curr_right = j;
                   } else {
                       right[j] = Math.min(right[j], curr_right);
                   }
               }
               for (int j = 0; j < n; j++) {
                   max = Math.max(max, height[j] * (right[j] - left[j]));
               }
           }
           return max;
       }
   }
   ```

   T: O(mn)			S: O(n)



