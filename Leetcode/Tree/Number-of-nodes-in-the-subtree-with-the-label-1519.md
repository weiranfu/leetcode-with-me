---
title: Medium | Number of Nodes in the Subtree With the Same Label 1519
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-07-19 13:22:25
---

Given a tree (i.e. a connected, undirected graph that has no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` `edges`. The **root** of the tree is the node `0`, and each node of the tree has **a label** which is a lower-case character given in the string `labels` (i.e. The node with the number `i` has the label `labels[i]`).

The `edges` array is given on the form `edges[i] = [ai, bi]`, which means there is an edge between nodes `ai` and `bi` in the tree.

Return *an array of size n* where `ans[i]` is the number of nodes in the subtree of the `ith` node which have the same label as node `i`.

A subtree of a tree `T` is the tree consisting of a node in `T` and all of its descendant nodes.

[Leetcode](https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/)

<!--more-->

**Example :**

![img](https://assets.leetcode.com/uploads/2020/07/01/q3e3.jpg)

```
Input: n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
Output: [3,2,1,1,1]
```

---

#### Tricky 

Use `cnt[n][26]` to store the number of colors for each node and perform DFS.

```java
class Solution {
    List<Integer>[] g;
    int[] res;
    String labels;
    int[][] cnt;
    public int[] countSubTrees(int n, int[][] edges, String labels) {
        this.labels = labels;
        g = new List[n];
        for (int i = 0; i < n; i++)  g[i] = new ArrayList<>();
        for (int[] e : edges) {
            int a = e[0], b = e[1];
            g[a].add(b);
            g[b].add(a);
        }
        cnt = new int[n][26];
        res = new int[n];
        dfs(0, -1);
        return res;
    }
    private void dfs(int u, int p) {
        char c = labels.charAt(u);
        cnt[u][c - 'a']++;
        for (int v : g[u]) {
            if (v == p) continue;
            dfs(v, u);
            for (int i = 0; i < 26; i++) {
                cnt[u][i] += cnt[v][i];
            }
        }
        res[u] = cnt[u][c - 'a'];
    }
}
```

T: O(V)			S: O(V)