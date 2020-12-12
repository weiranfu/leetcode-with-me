---
title: Medium | Course Schedule II 210
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-06-08 21:11:09
---

There are a total of *n* courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs**, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

[Leetcode](https://leetcode.com/problems/course-schedule-ii/)

<!--more-->

**Example 1:**

```
Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
```

**Example 2:**

```
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
```

[Course Schedule I](https://leetcode.com/problems/course-schedule/)

[Course Schedule II](https://aranne.github.io/2020/06/08/210-Course-schedule-II/#more)

[Course Schedule III](https://leetcode.com/problems/course-schedule-iii/)

[Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/)

---

#### Tricky 

* To detect cycle: **DFS Tarjan's algorithm** OR **BFS topological sort**
* To get the topological order list, using topological sort.

---

#### Tarjan Algorithm

```java
class Solution {
    int n;
    List<Integer>[] g;
    int[] visited;
    int[] res;
    int p;
    
    public int[] findOrder(int n, int[][] prerequisites) {
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
        res = new int[n]; p = n - 1;
        for (int i = 0; i < n; i++) {
            if (visited[i] == 0) {
                if (!dfs(i)) {
                    return new int[0];
                }
            }
        }
        return res;
    }
    private boolean dfs(int u) {
        
        visited[u] = 1;                 // visiting
        
        for (int v : g[u]) {
            if (visited[v] == 0) {
                if (!dfs(v)) {
                    return false;
                }
            }
            if (visited[v] == 1) return false;
        }
        
        visited[u] = 2;                 // visited
        res[p--] = u;
        return true;
    }
}
```

T: O(V + E)		S: O(V)

---

#### BFS Topological sort

If there's cycle, the indegrees of nodes on cycle cannot be 0 after topological sort. (*Just like dead lock*). These nodes will remain unmarked after BFS.

So If there exist cycle, the topological sort won't collect the nodes on cycle.

```java
class Solution {
    public int[] findOrder(int n, int[][] prerequisites) {
        if (n == 0) return new int[0];
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        int[] indegrees = new int[n];
        for (int[] pre : prerequisites) {
            int from = pre[1];
            int to = pre[0];
            graph[from].add(to);
            indegrees[to]++;                 // add indegrees
        }
        
        Queue<Integer> start = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegrees[i] == 0) {
                start.add(i);
            }
        }
        int[] topo = new int[n];
        int p = 0;
        while (!start.isEmpty()) {
            int v = start.poll();
            topo[p++] = v;
            for (int w : graph[v]) {
                indegrees[w]--;
                if (indegrees[w] == 0) {
                    start.add(w);
                }
            }
        }
        if (p != n) return new int[0]; // has cycle
        return topo;
    }
}
```

T: O(V + E)		S: O(V)



