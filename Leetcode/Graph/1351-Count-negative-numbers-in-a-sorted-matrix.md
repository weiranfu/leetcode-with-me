---
title: Easy | Count Negative Numbers in a Sorted Matrix
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-03-06 23:44:27
---

Given a `m * n` matrix `grid` which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of **negative** numbers in `grid`.

[Leetcode](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)

<!--more-->

**Example 1:**

```
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
```

**Example 2:**

```
Input: grid = [[3,2],[1,0]]
Output: 0
```

**Example 3:**

```
Input: grid = [[1,-1],[-1,-1]]
Output: 3
```

**Example 4:**

```
Input: grid = [[-1]]
Output: 1
```

---

#### Tricky 

This sorted matrix can be viewed as a tree.

The root node is at the up-right corner.

```java
class Solution {
    public int countNegatives(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        if (m == 0 || grid == null) return 0;
        int i = 0;
        int j = n - 1;
        int cnt = 0;
        while (i < m && j >= 0) {
            if (grid[i][j] < 0) {
                cnt += m - i;
                j--;
            } else {
                i++;
            }
        }
        return cnt;
    }
}
```

T: O(m + n)

S: O(1)

---

#### Summary 

View sorted matrix as a tree!