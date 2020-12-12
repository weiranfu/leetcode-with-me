---
title: Medium | Find Eventual Safe States 802
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-17 19:41:21
---

In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is *eventually safe* if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number `K` so that for any choice of where to walk, we must have stopped at a terminal node in less than `K` steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has `N` nodes with labels `0, 1, ..., N-1`, where `N` is the length of `graph`.  The graph is given in the following form: `graph[i]` is a list of labels `j` such that `(i, j)` is a directed edge of the graph.

[Leetcode](https://leetcode.com/problems/find-eventual-safe-states/)

<!--more-->

```
Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.
```

![Illustration of graph](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png)

---

#### Tricky 

1. Topo + DFS

   We can use dfs topological sort to detect cycle.

   And we use `visited[v]` to represent the states of each nodes.

   `0` means not visited yet.

   `1` means visiting now. (If there's a cycle, the `visited[v]` will remain `1`)

   `2` means visited already.

   Finally, we will collect all nodes with `visited[v] == 2`.

   ```java
   class Solution {
       int[] visited;
       int[][] g;
       public List<Integer> eventualSafeNodes(int[][] graph) {
           int n = graph.length;
           g = graph;
           visited = new int[n];
           List<Integer> res = new ArrayList<>();
           for (int i = 0; i < n; i++) {
               if (visited[i] == 0) {				// not visited
                   if (dfs(i)) {
                       res.add(i);
                   }
               } else if (visited[i] == 2) { // visited
                   res.add(i);
               }
           }
           return res;
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
           }
           visited[u] = 2;
           return true;
       }
   }
   ```

   T: O(V + E)		S: O(V)

2. Topo + BFS with outdegree + reverse graph

   Since we need to find the safe nodes without cycles, we cannot perform BFS according to its indegree.
   We need to BFS backward according to node's outdegree.
   However we cannot find the neighbors of node if we perform BFS backward, we decide to reverse the graph and perform BFS.

   ```java
   class Solution {
       public List<Integer> eventualSafeNodes(int[][] graph) {
           int n = graph.length;
           List<Integer>[] g = new List[n];
           for (int i = 0; i < n; i++) {
               g[i] = new ArrayList<>();
           }
           int[] indegree = new int[n];
           for (int u = 0; u < n; u++) {
               for (int v : graph[u]) {
                   g[v].add(u);						// reverse graph
                   indegree[u]++;
               }
           }
           Queue<Integer> queue = new LinkedList<>();
           for (int i = 0; i < n; i++) {
               if (indegree[i] == 0) {
                   queue.add(i);
               }
           }
           List<Integer> res = new ArrayList<>();
           while (!queue.isEmpty()) {
               int u = queue.poll();
               res.add(u);
               for (int v : g[u]) {
                   indegree[v]--;
                   if (indegree[v] == 0) {
                       queue.add(v);
                   }
               }
           }
           Collections.sort(res);
           return res;
       }
   }
   ```

   T: O(V + E)			S: O(V)			