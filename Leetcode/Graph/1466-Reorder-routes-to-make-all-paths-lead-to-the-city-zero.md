---
title: Medium | Reorder Routes to Make All Paths Lead to the City Zero 1466
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-05-31 17:24:33
---

There are `n` cities numbered from `0` to `n-1` and `n-1` roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by `connections` where `connections[i] = [a, b]` represents a road from city `a` to `b`.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the **minimum** number of edges changed.

It's **guaranteed** that each city can reach the city 0 after reorder.

[Leetcode](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2020/05/13/sample_1_1819.png)**

```
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2020/05/13/sample_2_1819.png)**

```
Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
```

---

#### Tricky 

The key is how to store the path in wrond direction.

If we store the directed path in graph, then we could not perform DFS/BFS, cause we could not connect all nodes from City 0.

So there're two approach:

1. Store directed path is both `from` and `to` nodes. So we could count how many path are in wrong direction.
2. Store undirected path in nodes with different weight. `from->to` path counts 1 and `to->from` path counts 0.

---

#### My thoughts 

Approach two.

---

#### First solution 

BFS with two direction paths.

```java
class Solution {
    class Node {
        List<Integer> to;            // store to nodes
        List<Integer> from;          // store from nodes
        public Node(List<Integer> to, List<Integer> from) {
            this.to = to;
            this.from = from;
        }
    }
    public int minReorder(int n, int[][] connections) {
        Node[] graph = new Node[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new Node(new ArrayList<>(), new ArrayList<>());
        }
        for (int[] connection : connections) {
            int from = connection[0];
            int to = connection[1];
            graph[from].to.add(to);
            graph[to].from.add(from);
        }
        int res = 0;
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n];
        queue.add(0);
        while (!queue.isEmpty()) {
            int idx = queue.poll();
            visited[idx] = true;
            Node node = graph[idx];
            for (int i : node.from) {
                if (!visited[i]) {
                    queue.add(i);
                }
            }
            for (int i : node.to) {
                if (!visited[i]) {
                    res++;               // wrong direction
                    queue.add(i);
                }
            }
        }
        return res;
    }
}
```

T: O(n)			S: O(n)

---

#### Optimized

DFS with weighted undirected path.

When we doing DFS, we store `parent` node during recursion.

```java
class Solution {
    class Pair {
        int node;
        int value;
        public Pair(int node, int value) {
            this.node = node;
            this.value = value;
        }
    }
    
    int res;
    List<Pair>[] graph;
    
    public int minReorder(int n, int[][] connections) {
        graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] connection : connections) {
            int from = connection[0];
            int to = connection[1];
            graph[from].add(new Pair(to, 1));    // DFS direction value is 1.
            graph[to].add(new Pair(from, 0));    // opposite direction value is 0.
        }
        res = 0;
        dfs(0, -1);
        return res;
    }
    
    private void dfs(int n, int parent) {         // save parent.
        for (Pair p : graph[n]) {
            if (p.node == parent) continue;
            res += p.value;                    // sum up path value.
            dfs(p.node, n);
        }
    }
}
```

T: O(n)		S: O(n)



