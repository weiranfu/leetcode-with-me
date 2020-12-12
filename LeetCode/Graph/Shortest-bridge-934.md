---
title: Medium | Shortest Bridge 934
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-08-01 13:01:39
---

In a given 2D binary array `A`, there are two islands.  (An island is a 4-directionally connected group of `1`s not connected to any other 1s.)

Now, we may change `0`s to `1`s so as to connect the two islands together to form 1 island.

Return the smallest number of `0`s that must be flipped.  (It is guaranteed that the answer is at least 1.)

[Leetcode](https://leetcode.com/problems/shortest-bridge/)

<!--more-->

**Example 1:**

```
Input: A = [[0,1],[1,0]]
Output: 1
```

**Example 2:**

```
Input: A = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
```

**Example 3:**

```
Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
```

---

#### DFS + BFS

Use DFS to search the first island.

Use BFS to expand the island until we find the second island.

```java
class Solution {
    
    int[][] A;
    int m, n;
    int[][] moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    public int shortestBridge(int[][] A) {
        this.A = A;
        m = A.length; n = A[0].length;
        Queue<int[]> q = new LinkedList<>();
        outer:
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (A[i][j] == 1) {
                    A[i][j] = -1;
                    q.add(new int[]{i, j});
                    dfs(i, j, q);
                    break outer;
                }
            }
        }
        int steps = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- != 0) {
                int[] info = q.poll();
                int i = info[0], j = info[1];
                for (int[] move : moves) {
                    int x = i + move[0];
                    int y = j + move[1];
                    if (x < 0 || x >= m || y < 0 || y >= n) continue;
                    if (A[x][y] == 0) {
                        A[x][y] = -1;
                        q.add(new int[]{x, y});
                    } else if (A[x][y] == 1) {
                        return steps;
                    }
                }
            }
            steps++;
        }
        return -1;
    }
    private void dfs(int i, int j, Queue<int[]> q) {
        for (int[] move : moves) {
            int x = i + move[0];
            int y = j + move[1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (A[x][y] == 1) {
                A[x][y] = -1;
                q.add(new int[]{x, y});
                dfs(x, y, q);
            }
        }
    }
}
```

T: O(m\*n)			S: O(m\*n)

