---
title: Medium | Maximum Side Length of a Square with Sum Less than Threshold 1292
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2019-12-15 00:17:58
---

Given a `m x n` matrix `mat` and an integer `threshold`. Return the maximum side-length of a square with a sum less than or equal to `threshold` or return **0** if there is no such square.

[Leetcode](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/12/05/e1.png)

```
Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
```

**Example 2:**

```
Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
```

**Example 3:**

```
Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output: 3
```

**Example 4:**

```
Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2
```

**Constraints:**

- `1 <= m, n <= 300`
- `m == mat.length`
- `n == mat[i].length`
- `0 <= mat[i][j] <= 10000`
- `0 <= threshold <= 10^5`

---

#### Tricky 

If we need to culculate sum of squares in a graph, we can store these sums in `prefixSum[i][j]`.

---

#### My thoughts 

PrefixSum `prefixsum[i+1][j+1]` is the sum of every element from `(0,0)` to `(i,j)`.

`sum = prefixSum[i + k][j + k] - prefixSum[i + k][j] - prefixSum[i][j + k] + prefixSum[i][j]`

```java
class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        int row = mat.length, col = mat[0].length;
        int[][] prefixSum = new int[row + 1][col + 1];
        // Move whole graph right and down one step, the orgin point is (1, 1)
        for (int i = 0; i < row; i += 1) {
            for (int j = 0; j < col; j += 1) {
                prefixSum[i + 1][j + 1] = prefixSum[i + 1][j] + prefixSum[i][j + 1] 
                    - prefixSum[i][j] + mat[i][j];
            }
        }
        int res = 0;
        for (int i = 0; i < row; i += 1) {
            for (int j = 0; j < col; j += 1) {
                for (int k = res + 1; k <= Math.min(row - i, col - j); k += 1) {
                    // prefixSum[i, j] represents sum from point(0, 0) to point(i-1, j-1)
                    int sum = prefixSum[i + k][j + k] - prefixSum[i + k][j] 
                        - prefixSum[i][j + k] + prefixSum[i][j];
                    if (sum <= threshold) {
                        res = Math.max(res, k);
                    } else {
                        break;
                    }
                }
            }
        }
        return res;
    }
}
```

T: O(mn*min(m, n)) S: O(mn)

---

#### Optimized 

Using binary search to find square length k.

```java
class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        int row = mat.length, col = mat[0].length;
        int[][] prefixSum = new int[row + 1][col + 1];
        // Move whole graph right and down one step, the orgin point is (1, 1)
        for (int i = 0; i < row; i += 1) {
            for (int j = 0; j < col; j += 1) {
                prefixSum[i + 1][j + 1] = prefixSum[i + 1][j] + prefixSum[i][j + 1] 
                    - prefixSum[i][j] + mat[i][j];
            }
        }
        int res = 0;
        int hi = Math.min(col, row);
        int lo = 0;
        while (lo <= hi) {
            int k = lo + (hi - lo) / 2;
            if (isValidSquare(k, prefixSum, threshold)) {
                res = Math.max(res, k);
                lo = k + 1;
            } else {
                hi = k - 1;
            }
        }
        return res;
    }
    public boolean isValidSquare(int k, int[][] prefixSum, int threshold) {
        int row = prefixSum.length - 1;
        int col = prefixSum[0].length - 1;
        // i and j should use <= rather than <
        for (int i = 0; i <= row - k; i += 1) {
            for (int j = 0; j <= col - k; j += 1) {
                int sum = prefixSum[i + k][j + k] - prefixSum[i + k][j] 
                    - prefixSum[i][j + k] + prefixSum[i][j];
                if (sum <= threshold) {
                    return true;
                }
            }
        }
        return false;
    }
    
}
```

T: O(mn* log(min(m, n))) S: O(mn)

---

#### Summary 

If we need to culculate sum of squares in a graph, we can store these sums in `prefixSum[i][j]`.

