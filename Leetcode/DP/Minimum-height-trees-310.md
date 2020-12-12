---
title: Medium | Minimum Height Trees 310
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-13 11:35:42
---

For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

[Leetcode](https://leetcode.com/problems/minimum-height-trees/)

<!--more-->

**Example :**

```
Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
```

---

#### Tricky 

1. 树形DP

   ```java
   class Solution {
       List<Integer>[] g;
       int[][] dpdown;
       int[] dpup;
       List<Integer> res;
       int min;
       
       public List<Integer> findMinHeightTrees(int n, int[][] edges) {
           g = new List[n];
           for (int i = 0; i < n; i++) {
               g[i] = new ArrayList<>();
           }
           for (int[] edge : edges) {
               int a = edge[0];
               int b = edge[1];
               g[a].add(b);
               g[b].add(a);
           }    
           dpdown = new int[n][2];
           dpup = new int[n];
           min = n;
           dfsDown(0, -1);
           dfs(0, -1);
           return res;
       }
       private void dfsDown(int v, int p) {
           for (int w : g[v]) {
               if (w == p) continue;
               dfsDown(w, v);
               if (dpdown[v][0] < dpdown[w][0] + 1) {
                   dpdown[v][1] = dpdown[v][0];
                   dpdown[v][0] = dpdown[w][0] + 1;
               } else if (dpdown[v][1] < dpdown[w][0] + 1) {
                   dpdown[v][1] = dpdown[w][0] + 1;
               }
           }
       }
       private void dfs(int v, int p) {
           if (p != -1) {
               int up = dpup[p] + 1;                   // dpup[p] + 1
               if (dpdown[v][0] + 1 == dpdown[p][0]) { // 判断u 是否在 dpdown[p] 上
                   up = Math.max(up, dpdown[p][1] + 1);
               } else {
                   up = Math.max(up, dpdown[p][0] + 1);
               }
               dpup[v] = up;
           }
           int max = Math.max(dpdown[v][0], dpup[v]); // 最长链
           if (min > max) {
               min = max;
               res = new ArrayList<>();
               res.add(v);
           } else if (min == max) {
               res.add(v);
           }
           for (int w : g[v]) {
               if (w == p) continue;
               dfs(w, v);
           }
       }
   }
   ```

   T: O(n)			S: O(n)

   ---

   #### DFS to find Diameter

   Since the point must be at the centre of diameter, we could find the diameter path using DFS

   If diameter size is even, the two items in the center are result, else the just one at center is result.

   ```java
   class Solution {
       List<Integer>[] g;
       int[] edgeTo;
       int max;
       int node;
       
       public List<Integer> findMinHeightTrees(int n, int[][] edges) {
           List<Integer> res = new ArrayList<>();
           g = new List[n];
           edgeTo = new int[n];
           for (int i = 0; i < n; i++) {
               g[i] = new ArrayList<>();
           }
           for (int[] edge : edges) {
               int a = edge[0];
               int b = edge[1];
               g[a].add(b);
               g[b].add(a);
           }    
           max = 0;
           dfs(0, -1, 0);
           max = 0;
           edgeTo[node] = -1;
           dfs(node, -1, 0);
           
           List<Integer> diameter = new ArrayList<Integer>();
           int curr = node;
           while (curr != -1) {
               diameter.add(curr);
               curr = edgeTo[curr];
           }
           int size = diameter.size();
           if (size % 2 == 0) {
               res.add(diameter.get(size / 2));
               res.add(diameter.get(size / 2 - 1));
           } else {
               res.add(diameter.get(size / 2));
           }
           return res;
       }
       private void dfs(int v, int p, int len) {
           if (len > max) {
               max = len;
               node = v;
           }
           edgeTo[v] = p;
           for (int w : g[v]) {
               if (w == p) continue;
               dfs(w, v, len + 1);
           }
       }
   }
   ```

   T: O(n)		S: O(n)