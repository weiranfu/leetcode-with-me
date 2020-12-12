---
title: Medium | Course Schedule IV 1462
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-21 22:57:54
---

There are a total of `n` courses you have to take, labeled from `0` to `n-1`.

Some courses may have direct prerequisites, for example, to take course 0 you have first to take course 1, which is expressed as a pair: `[1,0]`

Given the total number of courses `n`, a list of direct `prerequisite` **pairs** and a list of `queries` **pairs**.

You should answer for each `queries[i]` whether the course `queries[i][0]` is a prerequisite of the course `queries[i][1]` or not.

Return *a list of boolean*, the answers to the given `queries`.

Please note that if course **a** is a prerequisite of course **b** and course **b** is a prerequisite of course **c**, then, course **a** is a prerequisite of course **c**.

[Leetcode](https://leetcode.com/problems/course-schedule-iv/)

<!--more-->

**Example :**

![img](https://assets.leetcode.com/uploads/2020/04/17/graph-1.png)

```
Input: n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
```

**Constraints:**

- `2 <= n <= 100`
- `0 <= prerequisite.length <= (n * (n - 1) / 2)`
- `0 <= prerequisite[i][0], prerequisite[i][1] < n`
- `prerequisite[i][0] != prerequisite[i][1]`
- The prerequisites graph has no cycles.
- The prerequisites graph has no repeated edges.
- `1 <= queries.length <= 10^4`
- `queries[i][0] != queries[i][1]`

---

#### Brute Force 

We could do a DFS and save each node's path into a HashSet for quick look up.

```java
class Solution {
    int n;
    boolean[][] g;
    Set<Integer>[] path;
    
    public List<Boolean> checkIfPrerequisite(int n, int[][] prerequisites, int[][] queries) {
        this.n = n;
        g = new boolean[n][n];
        for (int[] pre : prerequisites) {
            int u = pre[0], v = pre[1];
            g[u][v] = true;
        }
        path = new Set[n];
        for (int i = 0; i < n; i++) path[i] = new HashSet<>();
        for (int i = 0; i < n; i++) {
            if (path[i].size() == 0) {				// haven't compute path
                dfs(i);
            }
        }
        
        List<Boolean> res = new ArrayList<>();
        for (int[] query : queries) {
            int u = query[0], v = query[1];
            res.add(path[u].contains(v));
        }
        return res;
    }
    private void dfs(int u) {
        path[u].add(u);
        for (int v = 0; v < n; v++) {
            if (g[u][v]) {
                if (path[v].size() == 0) {		// haven't compute path
                    dfs(v);
                }
                for (int w : path[v]) {
                    path[u].add(w);
                }
            }
        }
    }
}
```

T: O(n)			S: O(n^2)

---

#### Floyd

This is a connection problem between all pairs of nodes in the graph.

We could handle this kind of problem using *Floyd algorithm*

```java
class Solution {
    public List<Boolean> checkIfPrerequisite(int n, int[][] prerequisites, int[][] queries) {
        boolean[][] reach = new boolean[n][n];
        for (int[] pre : prerequisites) {
            int u = pre[0], v = pre[1];
            reach[u][v] = true;
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    reach[i][j] = reach[i][j] || reach[i][k] && reach[k][j];
                }
            }
        }
        
        List<Boolean> res = new ArrayList<>();
        for (int[] query : queries) {
            int u = query[0], v = query[1];
            res.add(reach[u][v]);
        }
        return res;
    }
}
```

T: O(n^3)			S: O(n^2)



