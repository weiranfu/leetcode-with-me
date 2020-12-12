---
title: Medium | Number of Operations to Make Network Connected 1319
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-01-12 12:57:18
---

There are `n` computers numbered from `0` to `n-1` connected by ethernet cables `connections` forming a network where `connections[i] = [a, b]` represents a connection between computers `a` and `b`. Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network `connections`. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected. Return the *minimum number of times* you need to do this in order to make all the computers connected. If it's not possible, return -1. 

[Leetcode](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2020/01/02/sample_1_1677.png)**

```
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2020/01/02/sample_2_1677.png)**

```
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
```

**Constraints:**

- `1 <= n <= 10^5`
- `1 <= connections.length <= min(n*(n-1)/2, 10^5)`
- `connections[i].length == 2`
- `0 <= connections[i][0], connections[i][1] < n`
- `connections[i][0] != connections[i][1]`
- There are no repeated connections.
- No two computers are connected by more than one cable.

---

#### Tricky 

 

---

#### My thoughts 

Use UnionFind to connect servers, and get number of extra path to connect left servers.

---

#### Union Find

If there's not enough number connections, we cannot connect all servers.

`if (connections.length < n - 1) return -1`

```java
class Solution {
    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) return -1;// NOT enough path to connect servers
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        for (int[] connection : connections) {
            int a = connection[0];
            int b = connection[1];
            int p1 = find(a, parent);
            int p2 = find(b, parent);
            if (p1 != p2) {
                parent[p1] = p2;
            }
        }
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (parent[i] == i) {          // Find number of unions.
                cnt++;
            }
        }
        return cnt - 1;
    }
    private int find(int i, int[] parent) { // NO path compression here.
        while (i != parent[i]) {
            i = parent[i];
        }
        return i;
    }
}
```

T: (n^2) 			S: O(n)

---

#### Union Find with path compression 

```java
class Solution {
    class UnionFind {
        int[] parent;
        public UnionFind(int n) {
            parent = new int[n];
            Arrays.fill(parent, -1);
        }
        public int find(int a) {
            int root = a;
            while (parent[root] >= 0) {
                root = parent[root];
            }
            while (a != root) {
                int tmp = parent[a];
                parent[a] = root;
                a = tmp;
            }
            return root;
        }
        public boolean isConnected(int a, int b) {
            return find(a) == find(b);
        }
        public void connect(int a, int b) {
            if (-parent[find(a)] > -parent[find(b)]) {
                parent[find(a)] += parent[find(b)];
                parent[find(b)] = find(a);
            } else {
                parent[find(b)] += parent[find(a)];
                parent[find(a)] = find(b);
            }
        }
    }
    public int makeConnected(int n, int[][] connections) {
        int path = 0;
        int left = n;
        UnionFind uf = new UnionFind(n);
        for (int[] connection : connections) {
            int a = connection[0];
            int b = connection[1];
            if (uf.isConnected(a, b)) {
                path++;
            } else {
                uf.connect(a, b);
                left--;
            }
        }
        if (path >= left - 1) {
            return left - 1;
        } else {
            return -1;
        }
    }
}
```

T: O(n + m) 			S: O(n)

---

#### DFS

If number of path is smaller than n-1, then we don't have enough path to connect all server.

Find all components in graph. Use DFS to mark all neighbors as visited, then create a new component.

```java
class Solution {
    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) return -1;
        List<Integer>[] graph = (List<Integer>[]) new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<Integer>();
        }
        for (int[] connection : connections) {
            int a = connection[0];
            int b = connection[1];
            graph[a].add(b);
            graph[b].add(a);
        }
        boolean[] visited = new boolean[n];
        int components = 0;
        for (int i = 0; i < n; i++) {
            components += findComponents(i, visited, graph);
        }
        return components - 1;
    }
    private int findComponents(int i, boolean[] visited, List<Integer>[] graph) {
        if (visited[i]) return 0;
        visited[i] = true;
        for (int j : graph[i]) {
            findComponents(j, visited, graph); // mark all neighbors as visited.
        }
        return 1;  // Create a new components.
    }
}
```

T: O(n + m) 			S: O(n) 			

---

#### Summary 

Union Find and DFS can used to find all components in a graph.

