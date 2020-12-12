---
title: Medium | Parallel Courses 1136
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-22 11:46:39
---

There are `N` courses, labelled from 1 to `N`.

We are given `relations[i] = [X, Y]`, representing a prerequisite relationship between course `X` and course `Y`: course `X` has to be studied before course `Y`.

In one semester you can study any number of courses as long as you have studied all the prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses.  If there is no way to study all the courses, return `-1`.

[Leetcode](https://leetcode.com/problems/parallel-courses/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/04/20/1316_ex1.png)**

```
Input: N = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: 
In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2019/04/20/1316_ex2.png)**

```
Input: N = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: 
No course can be studied because they depend on each other.
```

**Note:**

1. `1 <= N <= 5000`
2. `1 <= relations.length <= 5000`
3. `relations[i][0] != relations[i][1]`
4. There are no repeated relations in the input.

**Follow up:** 

[Parallel Courses II](https://leetcode.com/problems/parallel-courses-ii/)

---

#### Topological Sort

Count the number of visiting nodes to detect cycle.

```java
class Solution {
    public int minNumberOfSemesters(int n, int[][] dependencies, int k) {
        List<Integer>[] graph = new List[n];
        int[] indegrees = new int[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] dependency : dependencies) {
            int u = dependency[0] - 1;
            int v = dependency[1] - 1;
            graph[u].add(v);
            indegrees[v]++;
        }
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegrees[i] == 0) {
                queue.add(i);
            }
        }
        
        int res = 0;
        int cnt = 0;
        while (!queue.isEmpty()) {
            int v = queue.poll();
            for (int w : graph[v]) {
                indegrees[w]--;
                if (indegrees[w] == 0) {
                    queue.add(w);
                }
            }
        }
        if (cnt != 0) {
            res++;
        }
        return res;
    }
}
```

T: O(V + E)			S: O(V)

---

#### DFS

Finding the min semesters we need to take all courses means we need to find the max depth in the graph.

We could use DFS with memorization to record each node's depth and compute the max depth.

Use `visited[]` to detect cycles. `visited -> 0: not visited yet, 1: visiting, 2: visited already`

```java
class Solution {
    List<Integer>[] g;
    int[] depth;
    int[] visited;  /* visited -> 0: not visited yet, 1: visiting, 2: visited already */
    int max;
    public int minimumSemesters(int N, int[][] relations) {
        g = new List[N];
        for (int i = 0; i < N; i++) g[i] = new ArrayList<>();
        depth = new int[N];
        visited = new int[N];
        for (int[] relation : relations) {
            int a = relation[0] - 1;
            int b = relation[1] - 1;
            g[a].add(b);
        }
        max = 0;
        for (int i = 0; i < N; i++) {
            if (visited[i] == 0) {
                if (!dfs(i)) {
                    return -1;
                }
            }
        }
        return max;
    }
    private boolean dfs(int u) {
        visited[u] = 1;
        for (int v : g[u]) {
            if (visited[v] == 0) {
                if (!dfs(v)) {
                    return false;
                }
            } else if (visited[v] == 1) {
                return false;
            }
            depth[u] = Math.max(depth[u], depth[v]);
        }
        depth[u]++;
        max = Math.max(max, depth[u]);
        visited[u] = 2;
        return true;
    }
}
```

T: O(V + E)		S: O(V)



