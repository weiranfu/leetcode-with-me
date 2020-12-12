---
title: Medium | Rotting Oranges 994
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - Graph
date: 2019-12-16 16:10:39
---

In a given grid, each cell can have one of three values:

- the value `0` representing an empty cell;
- the value `1` representing a fresh orange;
- the value `2` representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return `-1`instead.

[Leetcode](https://leetcode.com/problems/rotting-oranges/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)**

```
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2:**

```
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

**Example 3:**

```
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
```

**Note:**

1. `1 <= grid.length <= 10`
2. `1 <= grid[0].length <= 10`
3. `grid[i][j]` is only `0`, `1`, or `2`.

---

#### Tricky 

#### Corner Case

What if there's not any fresh orange, so steps will be 0.

---

#### My thoughts 

**To find how many steps we need to make all oranges rotten is same as to find the maximum smallest steps for each fresh orange to reach a rotten orange.**

However, thinking this way will be difficult to implement. We need to set all rotten oranges as targets, then for each fresh orange to find smallest steps to reach these targets.

That will be very inefficient, because there're multiple targets for each node. Although we could use A* algorithm, it still can be inefficient.

---

#### Standard solution 

**Using BFS. For each level, all rotten oranges change its fresh neighbors into rotten, and add then into next level for traversal.**

Instead of using `boolean[][] visited` to record which oranges has been changed, we could just change `grid[i][j] == 1` to `grid[i][j] == 2` 

```java
class Solution {
    public int orangesRotting(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) return -1;
        int[][] moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int m =  grid.length, n = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        int total = 0;
        int cnt = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    cnt++;
                    total++;
                    q.add(new int[]{i, j});
                } else if (grid[i][j] == 1) total++;
            }
        }
        int time = 0;
        if (cnt == total) return time;              // corner case
        while (!q.isEmpty()) {
            time++;
            int size = q.size();
            while (size-- != 0) {
                int[] info = q.poll();
                int i = info[0], j = info[1];
                for (int[] move : moves) {
                    int x = i + move[0];
                    int y = j + move[1];
                    if (x < 0 || x >= m || y < 0 || y >= n) continue;
                    if (grid[x][y] != 1) continue;  // find fresh orange
                    grid[x][y] = 2;                 // rotten
                    cnt++;
                    q.add(new int[]{x, y});
                }
            }
            if (cnt == total) return time;
        }
        return -1;
    }
}
```

T: O(mn) S: O(mn)

---

#### Summary 

We can control the traversal of BFS level by level. By using `int size = queue.size()`, we can get the number of this level's nodes.