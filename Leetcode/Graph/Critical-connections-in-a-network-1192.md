---
title: Hard | Critical Connections in a Network 1192
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2019-12-02 15:20:08
---

There are `n` servers numbered from `0` to `n-1` connected by undirected server-to-server `connections` forming a network where `connections[i] = [a, b]` represents a connection between servers `a` and `b`. Any server can reach any other server directly or indirectly through the network.

A *critical connection* is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

[Leetcode](https://leetcode.com/problems/critical-connections-in-a-network/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/09/03/1537_ex1_2.png)**

```
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
```

**Constraints:**

- `1 <= n <= 10^5`
- `n-1 <= connections.length <= 10^5`
- `connections[i][0] != connections[i][1]`
- There are no repeated connections.

---

#### Tarjan's Algorithm

Use Tarjan's Algorithm to find all SCC.

找环，并将环上的所有点合并成一个，即缩点，并取环上id最小的那个点的id作为整个环的id，并记录到`low[]`

**但是low的value跟dfs的顺序有关。**

![](https://raw.githubusercontent.com/aranne/aranne.github.io/master/images/IMG_1192.png)

如果我们先访问6 —> 7 —> 5 —> 8 —> 9, 最后所有点的low value都会变成 6 的low value。

但是如果我们访问 6 —> 7 —> 8 —> 9 —> 5, 最后8，9两个点的 low value 将会和其他点的不一样。

所以必须在更新low的时候就判断critical connection，不能等到所有low都更新完了才判断。

如果一个点的`low[u] == id[u]`, 则 `parent -> u `是一个critical connection

```java
class Solution {
    
    List<Integer>[] g;
    int n;
    int id;
    int[] ids, low;
    boolean[] onStack;
    List<List<Integer>> res;
    
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        this.n = n;
        g = new List[n];
        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();
        id = 1;
        ids = new int[n];
        low = new int[n];
        onStack = new boolean[n];
        
        for (List<Integer> edge : connections) {
            int a = edge.get(0), b = edge.get(1);
            g[a].add(b);
            g[b].add(a);
        }
        res = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            if (ids[i] == 0) {
                dfs(i, -1);
            }
        }
        return res;
    }
    private void dfs(int u, int p) {
        ids[u] = low[u] = id++;
        onStack[u] = true;
        for (int v : g[u]) {
            if (v == p) continue;
            if (ids[v] == 0) {
                dfs(v, u);
                low[u] = Math.min(low[u], low[v]);
            } else if (onStack[v]) {
                low[u] = Math.min(low[u], ids[v]);
            }
        }
//u - v is critical, there is no path for v to reach back to u or previous vertices of u
        if (low[u] == ids[u] && p != -1) {
            res.add(Arrays.asList(p, u));
        }
        onStack[u] = false;
    }
}
```

T: O(E + V) 					S: O(E + V)
