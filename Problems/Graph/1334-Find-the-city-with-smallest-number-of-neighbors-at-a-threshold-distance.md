---
title: Medium | Find City with Smallest Number of Neighbors at a Threshold Distance 1334
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-01-26 11:02:26
---

There are `n` cities numbered from `0` to `n-1`. Given the array `edges` where `edges[i] = [fromi, toi, weighti]` represents a bidirectional and weighted edge between cities `fromi` and `toi`, and given the integer `distanceThreshold`.

Return the city with the smallest number of cities that are reachable through some path and whose distance is **at most** `distanceThreshold`, If there are multiple such cities, return the city with the greatest number.

[Leetcode](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)

<!--more-->

Notice that the distance of a path connecting cities ***i*** and ***j*** is equal to the sum of the edges' weights along that path.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/01/16/find_the_city_01.png)

```
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2020/01/16/find_the_city_02.png)**

```
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
```

**Constraints:**

- `2 <= n <= 100`
- `1 <= edges.length <= n * (n - 1) / 2`
- `edges[i].length == 3`
- `0 <= fromi < toi < n`
- `1 <= weighti, distanceThreshold <= 10^4`
- All pairs `(fromi, toi)` are distinct.

---

#### Tricky 

1. Use Dijkstra to traverse all vertices and return the max number of visited nodes each time.

   We can use `distTo[]` to record the dist from vertex to source, so we can only store vertex index into priority queue rather than storing a node class.

   `PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> distTo[a] - distTo[b]);`

2. Use Floyd Algorithm

   

---

#### My thoughts 

Use Dijkstra Algorithm to traverse all nodes and return the max number nodes visited each time.

---

#### First solution 

Save nodes with distance in `nodes[n][2]` in order to compare in priority queue and use this map to refer node in order to remove and add from pq.

Use `boolean[] visited` to record which nodes are still in priority queue, rather than using `pq.contains(node[i])`.

```java
class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        List<int[]>[] graph = (List<int[]>[]) new LinkedList[n];
        for (int i = 0; i < n; ++i) {
            graph[i] = new LinkedList<int[]>();
        }
        for (int[] edge : edges) {
            int from = edge[0];
            int to = edge[1];
            int weight = edge[2];
            graph[from].add(new int[]{to, weight});
            graph[to].add(new int[]{from, weight});
        }
        int max = Integer.MAX_VALUE;
        int res = 0;
        for (int i = 0; i < n; ++i) {
            int visits = relax(i, graph, distanceThreshold);
            if (max >= visits) {
                max = visits;
                res = i;
            }
        }
        return res;
    }
    private int relax(int s, List<int[]>[] graph, int threshold) {
        int n = graph.length;
        // Create a map to refer all nodes in order to remove from pq.
        // Save dist to source as int[].
        int[][] nodes = new int[n][2];  
        for (int i = 0; i < n; i++) {
            if (s != i) {
                nodes[i] = new int[]{i, Integer.MAX_VALUE};
            } else {
                nodes[s] = new int[]{s, 0};
            }
        }
        boolean[] visited = new boolean[n];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        for (int i = 0; i < n; i++) {
            pq.add(nodes[i]);
        }
        int count = 0;
        while (!pq.isEmpty()) {
            int[] info = pq.poll();
            int node = info[0];
            int dist = info[1];
            visited[node] = true;
            if (dist <= threshold) {
                if (node != s) {
                    count++;
                }
            } else {
                break;
            }
            for (int[] edge : graph[node]) {
                int neighbor = edge[0];
                int weight = edge[1];
                if (!visited[neighbor]) {
                    if (dist + weight < nodes[neighbor][1]) {
                        // Use map to refer node[i] for removing.
                        pq.remove(nodes[neighbor]);
                        nodes[neighbor] = new int[]{neighbor, dist + weight};
                        pq.add(nodes[neighbor]);
                    }
                }
            }
        }
        return count;
    }
}
```

T: O(V^2logV)			S: O(V + E)

---

#### Optimized

We can use `distTo[]` to record the dist from vertex to source, so we can only store vertex index into priority queue rather than storing a node class.

`PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> distTo[a] - distTo[b]);`

```java
class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        List<int[]>[] graph = (List<int[]>[]) new LinkedList[n];
        for (int i = 0; i < n; ++i) {
            graph[i] = new LinkedList<int[]>();
        }
        for (int[] edge : edges) {
            int from = edge[0];
            int to = edge[1];
            int weight = edge[2];
            graph[from].add(new int[]{to, weight});
            graph[to].add(new int[]{from, weight});
        }
        int max = Integer.MAX_VALUE;
        int res = 0;
        for (int i = 0; i < n; ++i) {
            int visits = relax(i, graph, distanceThreshold);
            if (max >= visits) {
                max = visits;
                res = i;
            }
        }
        return res;
    }
    private int relax(int s, List<int[]>[] graph, int threshold) {
        int n = graph.length;
        // Create a map to refer all nodes in order to remove from pq.
        // Save dist to source as int[].
        int[] distTo = new int[n]; 
        for (int i = 0; i < n; i++) {
            distTo[i] = Integer.MAX_VALUE;
        }
        distTo[s] = 0;
        boolean[] visited = new boolean[n];
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> distTo[a] - distTo[b]);
        for (int i = 0; i < n; i++) {
            pq.add(i);
        }
        int count = 0;
        while (!pq.isEmpty()) {
            int node = pq.poll();
            int dist = distTo[node];
            visited[node] = true;
            if (dist <= threshold) {
                if (node != s) {
                    count++;
                }
            } else {
                break;
            }
            for (int[] edge : graph[node]) {
                int neighbor = edge[0];
                int weight = edge[1];
                if (!visited[neighbor]) {
                    if (dist + weight < distTo[neighbor]) {
                        pq.remove(neighbor);
                        distTo[neighbor] = dist + weight;
                        pq.add(neighbor);
                    }
                }
            }
        }
        return count;
    }
}
```

T: O(V^2logV)			S: O(V + E)

---

#### Floyd  

Floyd Algorithm is used to get the minimum distance between all two pair nodes in a graph.

Search all intermidiate node `k` between two nodes `i` and `j`.

Use `dist[i][j]` to record minimum distance from  node `i` and `j`. 

Interate all `i`, `j`, `k` to find `dist[i][j] > dist[i][k] + dist[k][j]`, then update `dist[i][j]`.

The time complexity is O(V^3).

```java
class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = Integer.MAX_VALUE;
            }
            dist[i][i] = 0;    // The dist from i to i is 0.
        }
        for (int[] edge : edges) {
            int from = edge[0];
            int to = edge[1];
            int weight = edge[2];
            dist[from][to] = weight;
            dist[to][from] = weight;
        }
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                // Exclude overflow
                if (dist[i][k] == Integer.MAX_VALUE) continue;
                for (int j = 0; j < n; j++) {
                    // Exclude overflow
                    if (dist[k][j] == Integer.MAX_VALUE) continue;
                    if (dist[i][j] > dist[i][k] + dist[k][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
        int min = Integer.MAX_VALUE;
        int res = -1;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (dist[i][j] <= distanceThreshold) {
                    count++;
                }
            }
            if (count <= min) {
                min = count;
                res = i;
            }
        }
        return res;
    }
}
```

T: O(V^3)			S: O(V^2)

---

#### Summary 

Use floyd algorithm to get minimum distance between all two pair nodes.