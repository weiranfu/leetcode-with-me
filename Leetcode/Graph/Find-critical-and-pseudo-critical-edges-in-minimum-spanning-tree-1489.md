---
title: Hard | Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree 1489
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-06-22 14:30:54
---

Given a weighted undirected connected graph with `n` vertices numbered from `0` to `n-1`, and an array `edges` where `edges[i] = [fromi, toi, weighti]` represents a bidirectional and weighted edge between nodes `fromi` and `toi`. A minimum spanning tree (MST) is a subset of the edges of the graph that connects all vertices without cycles and with the minimum possible total edge weight.

Find *all the critical and pseudo-critical edges in the minimum spanning tree (MST) of the given graph*. An MST edge whose deletion from the graph would cause the MST weight to increase is called a *critical edge*. A *pseudo-critical edge*, on the other hand, is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

[Leetcode](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/06/04/ex1.png)

```
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:
```

![](https://assets.leetcode.com/uploads/2020/06/04/msts.png)

```
Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
```

---

#### Tricky 

How to determine an edge is a critical edge?

**If we remove it, the weight of MST will increase or we cannot form MST**

How to determine an edge is pseudo-critical edge?

**If force add it, then the weight of MST will still stay the same**

---

#### My thoughts 

Use kruskal algorithm with Union Find.

If we want to remove an edge, we just don't consider it when we meet it.

If we want to force add an edge, `uf[from] = uf[to]. weight = e.weigth`

As we need to sort all edges, we define a class `Edge` to store the id.

---

#### Standard solution  

```java
class Solution {
    class Edge {
        int from;
        int to;
        int weight;
        int id;
        public Edge(int from, int to, int weight, int id) {
            this.from = from; this.to = to; this.weight = weight; this.id = id;
        }
    }
    
    int[] uf;
    
    public List<List<Integer>> findCriticalAndPseudoCriticalEdges(int n, int[][] edgesArray) {
        List<List<Integer>> res = new ArrayList<>();
        int E = edgesArray.length;
        Edge[] edges = new Edge[E];
        for (int i = 0; i < E; i++) {
            int[] edge = edgesArray[i];
            edges[i] = new Edge(edge[0], edge[1], edge[2], i);
        }
      	uf = new int[n];
        
        Arrays.sort(edges, (a, b) -> a.weight - b.weight);  // sort edges
        
        initUF();
        int weight = mst(edges, n, 0, -1);
        List<Integer> critical = new ArrayList<>();
        List<Integer> pseudo = new ArrayList<>();
        
        for (int i = 0; i < E; i++) {
            int id = edges[i].id;
            int to = edges[i].to;
            int from = edges[i].from;
            
            initUF();
            int removeWeight = mst(edges, n, 0, id);
            if (removeWeight != weight) {    // mst weight could increase or decrease
                critical.add(id);
                continue;
            }
            
            initUF();
            uf[to] = from;
            int addWeight = edges[i].weight + mst(edges, n, 1, -1);
            if (addWeight == weight) {      // mst still has same weight
                pseudo.add(id);
            }
        }
        res.add(critical);
        res.add(pseudo);
        return res;
    }
    
    // cnt number of edges in MST. 
    // id is the removed edge's id.
    private int mst(Edge[] edges, int n, int cnt, int id) {
        int weight = 0;
        for (Edge e : edges) {
            if (cnt == n - 1) break;
            if (e.id == id) continue;
            int from = e.from;
            int to = e.to;
            int p = find(from), q = find(to);
            if (p != q) {
                uf[p] = q;
                weight += e.weight;
                cnt++;
            }
        }
        return weight;
    }
    
    private int find(int v) {
        if (uf[v] != v) {
            uf[v] = find(uf[v]);
        }
        return uf[v];
    }
    
    private void initUF() {
        for (int i = 0; i < uf.length; i++) {
            uf[i] = i;
        }
    }
}
```

T: O(E \* ElogE)				S: O(E)