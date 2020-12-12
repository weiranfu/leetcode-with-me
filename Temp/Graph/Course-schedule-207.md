---
title: Medium | Course Schedule 207
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-06-07 18:15:24
---

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs**, is it possible for you to finish all courses?

[Leetcode](https://leetcode.com/problems/course-schedule/)

<!--more-->

**Example 1:**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```

**Example 2:**

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
```

**Follow up:** 

[Course Schedule I](https://leetcode.com/problems/course-schedule/)

[Course Schedule II](https://aranne.github.io/2020/06/08/210-Course-schedule-II/#more)

[Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)

[Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/)

---

#### Tricky 

We need to take course in topological order. 

**To determine whether we can finish all courses is to detect whether there exists cycle in this directed graph.**

* DFS: Tarjan's Algorithm. Keep a stack to dfs all nodes, we when meet a node which is on Stack, then we find a cycle.
* BFS: Topological sort. We could do a BFS topological sort. If there's no cycle, we will end up visiting all nodes. If there's a cycle, the nodes in the cycle all have 1 indegree edge left. (*Just like dead lock*).

---

#### DFS 

[Tarjan's Algorithm]([https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm](https://en.wikipedia.org/wiki/Tarjan's_strongly_connected_components_algorithm))

```javascript
L ← Empty list that will contain the sorted nodes
while there are unmarked nodes do
    select an unmarked node n
    visit(n)

function visit(node n)
    if n has a permanent mark then return
    if n has a temporary mark then stop   (not a DAG)
    mark n temporarily
    for each node m with an edge from n to m do
        visit(m)
    mark n permanently
    add n to head of L
```

```java
class Solution {
    List<Integer>[] g;
    int n;
    int[] visited;   /* 0: not visted, 1: visiting, 2: visited */
    
    public boolean canFinish(int n, int[][] prerequisites) {
        this.n = n;
        g = new List[n];
        for (int i = 0; i < n; i++) {
            g[i] = new ArrayList<>();
        }
        for (int[] prerequisite : prerequisites) {
            int u = prerequisite[1];
            int v = prerequisite[0];
            g[u].add(v);
        }
        visited = new int[n];
        for (int i = 0; i < n; i++) {
            if (visited[i] == 0) {
                if (!dfs(i)) {
                    return false;
                }
            }
        }
        return true;
    }
    private boolean dfs(int u) {
        visited[u] = 1;
        for (int v : g[u]) {
            if (visited[v] == 0) {
                if (!dfs(v)) {
                    return false;   // cylce exists
                }
            }
            if (visited[v] == 1) return false;
        }
        visited[u] = 2;
        return true;
    }
}
```

T: O(V + E)		S: O(V)

---

#### BFS

We could do a BFS topological sort. If there's no cycle, we will end up visiting all nodes. If there's a cycle, the nodes in the cycle all have 1 indegree edge left. (*Just like dead lock*).

```java
class Solution {
    public boolean canFinish(int n, int[][] prerequisites) {
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        int[] indegrees = new int[n];
        for (int[] prerequisite : prerequisites) {
            int v = prerequisite[1];
            int w = prerequisite[0];
            graph[v].add(w);
            indegrees[w]++;
        }
        Queue<Integer> start = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegrees[i] == 0) {
                start.add(i);
            }
        }
        while (!start.isEmpty()) {
            int v = start.poll();
            for (int w : graph[v]) {
                indegrees[w]--;
                if (indegrees[w] == 0) {
                    start.add(w);
                }
            }
        }
        // check whether there exist a cycle.
        for (int i = 0; i < n; i++) {   
            if (indegrees[i] > 0) {
                return false;
            }
        }
        return true;
    }
}
```

T: O(V + E)			S: O(V)



