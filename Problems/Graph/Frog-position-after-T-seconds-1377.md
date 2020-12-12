---
title: Hard | Frog Position after T Seconds 1377
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-21 01:05:16
---

Given an undirected tree consisting of `n` vertices numbered from 1 to `n`. A frog starts jumping from the **vertex 1**. In one second, the frog jumps from its current vertex to another **unvisited** vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices it jumps randomly to one of them with the same probability, otherwise, when the frog can not jump to any unvisited vertex it jumps forever on the same vertex. 

The edges of the undirected tree are given in the array `edges`, where `edges[i] = [fromi, toi]` means that exists an edge connecting directly the vertices `fromi` and `toi`.

*Return the probability that after t seconds the frog is on the vertex target.*

[Leetcode](https://leetcode.com/problems/frog-position-after-t-seconds/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/02/20/frog_2.png)

```
Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666 
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2020/02/20/frog_3.png)**

```
Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 100, target = 7
Output: 0.3333333333333333
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. And it will stay on 7 forever. 
```

---

#### BFS

Edge cases:

1. Time is up and we didn't reach our target, return `0`
2. Current node is our target, time is just up or can't jump to any unvisitied node, return probability `p`
3. Current node is our target, time is not up and there are unvisitied nodes to jump to, return `0`

```java
class Solution {
    public double frogPosition(int n, int[][] edges, int t, int target) {
        List<Integer>[] g = new List[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();
        for (int[] edge : edges) {
            int a = edge[0], b = edge[1];
            g[a].add(b);
            g[b].add(a);
        }
        double[] prob = new double[n + 1];
        prob[1] = 1;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{1, -1});
        int time = 0;
        while (time != t && !q.isEmpty()) {
            time++;
            int size = q.size();
            while (size-- != 0) {
                int[] info = q.poll();
                int u = info[0], p = info[1];
                int divide = (u == 1 ? g[u].size() : g[u].size() - 1);
                for (int v : g[u]) {
                    if (v == p) continue;
                    prob[v] = prob[u] / divide;
                    q.add(new int[]{v, u});
                }
                if (divide != 0) prob[u] = 0; // frog don't stay vertex u, 
            }                                 // he keeps going to the next vertex
        }
        return prob[target];
    }
}
```

T: O(n)			S: O(n)

---

#### DFS

Search target nodes with `time` as depth

When from a vertex `u` there are `v` vertices which can be visited, so the probability of choosing a vertex is `1/v`, followed by the product with the sum of probabilities of every neighbor.

```java
class Solution {
    List<Integer> g[];
    public double frogPosition(int n, int[][] edges, int t, int target) {
        if (n == 1) return 1.0;
        g = new List[n + 1];
        for(int i = 1; i <= n ; i++) g[i] = new LinkedList<>();
        for (int[] edge : edges) {
            int a = edge[0], b = edge[1];
            g[a].add(b);
            g[b].add(a);
        }
        return dfs(1, t, target, -1);
    }

    private double dfs(int u, int t, int target, int p) {
        if (u != 1 && g[u].size() == 1 || t == 0) {
            if (u == target)
                return 1;       // find target return 1
            else return 0;
        }
        double res = 0.0;
        for (int v : g[u]) {
            if (v == p) continue; // skip parent
            res += dfs(v, t - 1, target, u);
        }
        if (u != 1)
            return res * 1.0 / (g[u].size() - 1);
        else
            return res * 1.0 / (g[u].size());
    }
}
```

T: O(n)		S: O(n)