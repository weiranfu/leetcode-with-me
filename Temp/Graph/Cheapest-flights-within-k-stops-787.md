---
title: Medium | Cheapest Flights within K Stops 787
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-18 15:32:25
---

There are `n` cities connected by `m` flights. Each flight starts from city `u` and arrives at `v` with a price `w`.

Now given all the cities and flights, together with starting city `src` and the destination `dst`, your task is to find the cheapest price from `src` to `dst` with up to `k` stops. If there is no such route, output `-1`.

[Leetcode](https://leetcode.com/problems/cheapest-flights-within-k-stops/)

<!--more-->

**Example :**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png)

```
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
```

**Constraints:**

- The number of nodes `n` will be in range `[1, 100]`, with nodes labeled from `0` to `n`` - 1`.
- The size of `flights` will be in range `[0, n * (n - 1) / 2]`.
- The format of each flight will be `(src, dst, price)`.
- The price of each flight will be in the range `[1, 10000]`.
- `k` is in the range of `[0, n - 1]`.
- There will not be any duplicated flights or self cycles.

---

#### Tricky 

有边数限制的最短路

#### 1. Bellman Ford

迭代 K 次，且每次从上一次迭代结果relax 即能保证最短路最多只有 K 条边, 需要 backup 滚动数组存上一次迭代结果

注意一定是从上一次迭代结果relax，不能根据 edges relax 顺序在一次迭代中多次relax

例如 edge{u, v, w}: {1, 2, 1}, {2, 3, 1}, {1, 3, 3} 从 1 到 3 最多经过 1 条边的最短路是 3

但如果我们迭代一次并按照edges顺序relax的话，会发现

point        1       2       3

0            0       INF     INF

1            0       1       2(1 + 1)

如果我们迭代一次并按照edges顺序根据上一次迭代结果relax的话

0            0       INF     INF

1            0       1       3(0 + 3)

```java
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        int m = flights.length;
        int[] dist = new int[n];
        int INF = 0x3f3f3f3f;
        Arrays.fill(dist, INF);
        dist[src] = 0;
        for (int i = 0; i < K + 1; i++) {          // At most K+1 edges in shortest path
            int[] backup = Arrays.copyOf(dist, n); // backup last iterative results
            for (int j = 0; j < m; j++) {
                int u = flights[j][0], v = flights[j][1], w = flights[j][2];
                dist[v] = Math.min(dist[v], backup[u] + w);
            }
        }
        return dist[dst] == INF ? -1 : dist[dst];
    }
}
```

T: O(V\*E)			S: O(V)

#### 2. BFS

We can use BFS to control the max path won't exceed K.

However we also need to make sure we update the distance using previous updated distance.

Since the graph is a Dense graph, we choose to use Adjacency Matrix to store it.

```java
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        int m = flights.length;
        int[][] g = new int[n][n];
        for (int[] flight : flights) {
            int u = flight[0], v = flight[1], w = flight[2];
            g[u][v] = w;
        }
        int[] dist = new int[n];
        int INF = 0x3f3f3f3f;
        Arrays.fill(dist, INF);
        dist[src] = 0;
        Queue<Integer> queue = new LinkedList<>();
        int steps = 0;
        queue.add(src);
        while (!queue.isEmpty()) {
            steps++;
            int size = queue.size();
            int[] backup = Arrays.copyOf(dist, n);		// backup array
            while (size-- != 0) {
                int u = queue.poll();
                for (int v = 0; v < n; v++) {
                    if (g[u][v] == 0) continue;
                    if (dist[v] > backup[u] + g[u][v]) {// update with backup
                        dist[v] = backup[u] + g[u][v];
                        queue.add(v);
                    }
                }
            }
            if (steps > K) break;
        }
        return dist[dst] == INF ? -1 : dist[dst];
    }
}
```

T: O(V\*V + E).   Because we use `Arrays.copyOf()`.

**Optimized:**

**We can save newly updated distance of `u` with `u` in the queue to avoid using Arrays.copyOf().**

So we could easily get the previous updated distance of `u`.

```java
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        int m = flights.length;
        int[][] g = new int[n][n];
        for (int[] flight : flights) {
            int u = flight[0], v = flight[1], w = flight[2];
            g[u][v] = w;
        }
        int INF = 0x3f3f3f3f;
        int[] dist = new int[n];
        Arrays.fill(dist, INF);
        dist[src] = 0;
        /* queue: int[]{ u, previous dist } */
        Queue<int[]> queue = new LinkedList<>();
        int steps = 0;
        queue.add(new int[]{src, dist[src]});
        while (!queue.isEmpty()) {
            steps++;
            int size = queue.size();
            while (size-- != 0) {
                int[] curr = queue.poll();
                int u = curr[0], preDist = curr[1];
                for (int v = 0; v < n; v++) {
                    if (g[u][v] == 0) continue;
                    if (dist[v] > preDist + g[u][v]) {  // update with previous distance
                        dist[v] = preDist + g[u][v];
                        queue.add(new int[]{v, dist[v]});
                    }
                }
            }
            if (steps > K) break;
        }
        return dist[dst] == INF ? -1 : dist[dst];
    }
}
```

T: O(V + E)			S: O(V)

#### Dijkstra 

Like BFS, we could use Dijkstra along with the `steps` in the Priority Queue.

Only `steps <= K`, we could continue updating.

The key is to keep track the `min` distance to `dst`. If the path's length is smaller than `min`, we add it into priority queue for consideration.

```java
class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int K) {
        int m = flights.length;
        int[][] g = new int[n][n];
        for (int[] flight : flights) {
            int u = flight[0], v = flight[1], w = flight[2];
            g[u][v] = w;
        }
        int INF = 0x3f3f3f3f;
        /* queue: int[]{ dist, u, steps } */
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.add(new int[]{0, src, 0});
        int min = INF;											// min distance to dst.
        while (!pq.isEmpty()) {
            int[] info = pq.poll();
            int dist = info[0], u = info[1], steps = info[2];
            if (steps > K) continue;            // exceed K stops
            for (int v = 0; v < n; v++) {
                if (g[u][v] == 0) continue;
                if (min > dist + g[u][v]) {    // take into consideration
                    if (v == dst) {
                        min = Math.min(min, dist + g[u][v]);
                    }
                    pq.add(new int[]{dist + g[u][v], v, steps + 1});
                }
            }
        }
        return min == INF ? -1 : min;
    }
}
```

T: O(ElogV)				S: O(V)