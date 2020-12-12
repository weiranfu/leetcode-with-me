---
title: Medium | 01 Matrix 542
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-20 17:13:53
---

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

[Leetcode](https://leetcode.com/problems/01-matrix/)

<!--more-->

**Example:**

```
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
```

---

#### BFS

We add all `0` into queue, and change all original `1`s into `-1` to differentiate with distance `1`.

```java
class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) return matrix;
        int m = matrix.length, n = matrix[0].length;
        int[][] moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1) {
                    matrix[i][j] = -1;
                } else {
                    q.add(new int[]{i, j});
                }
            }
        }
        int steps = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            steps++;
            while (size-- != 0) {
                int[] info = q.poll();
                int i = info[0], j = info[1];
                for (int[] move : moves) {
                    int x = i + move[0];
                    int y = j + move[1];
                    if (x < 0 || x >= m || y < 0 || y >= n) continue;
                    if (matrix[x][y] == -1) {
                        matrix[x][y] = steps;
                        q.add(new int[]{x, y});
                    }
                }
            }
        }
        return matrix;
    }
}
```

T: O(mn)			S: O(mn)

