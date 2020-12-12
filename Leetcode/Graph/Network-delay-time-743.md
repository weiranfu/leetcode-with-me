---
title: Medium | Network Delay Time 743
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-17 23:03:30
---

There are `N` network nodes, labelled `1` to `N`.

Given `times`, a list of travel times as **directed** edges `times[i] = (u, v, w)`, where `u` is the source node, `v` is the target node, and `w` is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node `K`. How long will it take for all nodes to receive the signal? If it is impossible, return `-1`.

[Leetcode](https://leetcode.com/problems/network-delay-time/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
```

**Note:**

1. `N` will be in the range `[1, 100]`.
2. `K` will be in the range `[1, N]`.
3. The length of `times` will be in the range `[1, 6000]`.
4. All edges `times[i] = (u, v, w)` will have `1 <= u, v <= N` and `0 <= w <= 100`.

---

#### Tricky 

This is **Dense Graph**, because `N` will be in the range `[1, 100]` and The length of `times` will be in the range `[1, 6000]`, so that `V^2 = E`

We choose to use **Adjacency Matrix** to store graph and use **Basic Dijkstra**.

The time complexity will be O(V^2) which is much faster than **Heap based Dijkstra** with O(ElogV)

```java
class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        int INF = 0x3f3f3f3f;
        int[][] g = new int[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(g[i], INF);
        }
        for (int[] time : times) {
            int u = time[0] - 1, v = time[1] - 1, w = time[2];
            g[u][v] = Math.min(g[u][v], w);
        }
        int[] dist = new int[N];
        for (int i = 0; i < N; i++) {
            dist[i] = INF;
        }
        boolean[] visited = new boolean[N];
        dist[K - 1] = 0;
        for (int i = 0; i < N; i++) {
            int u = -1;
            for (int j = 0; j < N; j++) {
                if (!visited[j] && (u == -1 || dist[j] < dist[u])) {
                    u = j;
                }
            }
            visited[u] = true;
            for (int v = 0; v < N; v++) {
                if (!visited[v] && dist[v] > dist[u] + g[u][v]) {
                    dist[v] = dist[u] + g[u][v];
                }
            }
        }
        int max = 0;
        for (int i = 0; i < N; i++) {
            max = Math.max(max, dist[i]);
        }
        return max == INF ? -1 : max;
    }
}
```

T: O(V^2)			S: O(V^2)

---

#### SPFA

We could also use *Shortest Path Faster Algorithm*

```java
class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        int INF = 0x3f3f3f3f;
        int[][] g = new int[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(g[i], INF);
        }
        for (int[] time : times) {
            int u = time[0] - 1, v = time[1] - 1, w = time[2];
            g[u][v] = Math.min(g[u][v], w);
        }
        int[] dist = new int[N];
        for (int i = 0; i < N; i++) {
            dist[i] = INF;
        }
        Queue<Integer> q = new LinkedList<>();
        boolean[] onQueue = new boolean[N];
        dist[K - 1] = 0;
        onQueue[K - 1] = true;
        q.add(K - 1);
        while (!q.isEmpty()) {
            int u = q.poll();
            onQueue[u] = false;
            for (int v = 0; v < N; v++) {
                if (dist[v] > dist[u] + g[u][v]) {
                    dist[v] = dist[u] + g[u][v];
                    if (!onQueue[v]) {
                        onQueue[v] = true;
                        q.add(v);
                    }
                }
            }
        }
        int max = 0;
        for (int i = 0; i < N; i++) {
            max = Math.max(max, dist[i]);
        }
        return max == INF ? -1 : max;
    }
}
```

T: O(E) on average, O(VE) in worst case.

S: O(V)