---
title: Medium | Graph Valid Tree 261
tags:
  - common
categories:
  - Leetcode
  - Graph
date: 2020-08-19 09:48:37
---

Given `n` nodes labeled from `0` to `n-1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

[Leetcode](https://leetcode.com/problems/graph-valid-tree/)

<!--more-->

**Example 1:**

```
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
```

**Example 2:**

```
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
```

---

#### Standard solution  

**A graph can be a tree if and only if all nodes are connected and there doesn't exist a circle.**

```java
class Solution {
    List<Integer>[] g;
    int[] visited;
    int cnt;
    
    public boolean validTree(int n, int[][] edges) {
        g = new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        visited = new int[n];
        cnt = 0;
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            g[u].add(v);
            g[v].add(u);
        }
        return dfs(0, -1) && cnt == n;
    }
    private boolean dfs(int u, int p) {
        visited[u] = 1;
        for (int v : g[u]) {
            if (v == p) continue;
            if (visited[v] == 0) {
                if (!dfs(v, u)) {
                    return false;
                }
            } else if (visited[v] == 1) return false;
        }
        visited[u] = 2;
        cnt++;
        return true;
    }
}
```

T: O(V + E)		S: O(V)

#### Union Find

Use union find to connect two nodes of an edge, if it is already connected, which means there exists a circle, return false.

To check all nodes are fully connected, `edges.length == n - 1`

```java
class Solution {
    int[] uf;
    
    public boolean validTree(int n, int[][] edges) {
        uf = new int[n];
        for (int i = 0; i < n; i++) uf[i] = i;
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            int x = find(u), y = find(v);
            if (x == y) return false;
            uf[x] = y;
        }
        return edges.length == n - 1;
    }
    
    private int find(int x) {
        if (uf[x] != x) {
            uf[x] = find(uf[x]);
        }
        return uf[x];
    }
}
```

T: O(V)			S: O(V)