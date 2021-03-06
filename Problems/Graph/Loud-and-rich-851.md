---
title: Medium | Loud and Rich 851
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-07-20 13:39:39
---

In a group of N people (labelled `0, 1, 2, ..., N-1`), each person has different amounts of money, and different levels of quietness.

For convenience, we'll call the person with label `x`, simply "person `x`".

We'll say that `richer[i] = [x, y]` if person `x` definitely has more money than person `y`.  Note that `richer` may only be a subset of valid observations.

Also, we'll say `quiet[x] = q` if person x has quietness `q`.

Now, return `answer`, where `answer[x] = y` if `y` is the least quiet person (that is, the person `y` with the smallest value of `quiet[y]`), among all people who definitely have equal to or more money than person `x`.

[Leetcode](https://leetcode.com/problems/loud-and-rich/)

<!--more-->

**Example 1:**

```
Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
Output: [5,5,2,5,4,5,6,7]
Explanation: 
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but
it isn't clear if they have more money than person 0.

answer[7] = 7.
Among all people that definitely have equal to or more money than person 7
(which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x])
is person 7.

The other answers can be filled out with similar reasoning.
```

**Note:**

1. `1 <= quiet.length = N <= 500`
2. `0 <= quiet[i] < N`, all `quiet[i]` are different.
3. `0 <= richer.length <= N * (N-1) / 2`
4. `0 <= richer[i][j] < N`
5. `richer[i][0] != richer[i][1]`
6. `richer[i]`'s are all different.
7. The observations in `richer` are all logically consistent.

---

#### DFS with memorization 

We could build the graph from `poor` people to `richer` people.

Then we need to find the min quiet people in each subgraph.

This is a Dense Graph, so we use Adjacency Matrix to store graph.

We could dfs each node and use `res[]` array to store the min quiet node 

```java
class Solution {
    boolean[][] g;
    int[] quiet;
    int n;
    int[] res;
    public int[] loudAndRich(int[][] richer, int[] quiet) {
        n = quiet.length;
        this.quiet = quiet;
        g = new boolean[n][n];
        for (int[] rich : richer) {
            int a = rich[0], b = rich[1];
            g[b][a] = true;
        }
        res = new int[n];
        Arrays.fill(res, -1);
        for (int i = 0; i < n; i++) {
            if (res[i] == -1) {
                dfs(i);
            }
        }
        return res;
    }
    private void dfs(int u) {
        if (res[u] != -1) return; 			// memorization
        res[u] = u;
        for (int v = 0; v < n; v++) {
            if (g[u][v]) {
                dfs(v);
                if (quiet[res[u]] > quiet[res[v]]) {
                    res[u] = res[v];
                }
            }
        }
    }
}
```

T: O(n)		S: O(n^2)

---

#### Topo + memorization

We could reverse the graph and do a topogical sort.

Then the richest people will be added into queue firstly and use `res[]` to record the min quiet people.

```java
class Solution {
    public int[] loudAndRich(int[][] richer, int[] quiet) {
        int n = quiet.length;
        boolean[][] g = new boolean[n][n];
        int[] indegree = new int[n];
        for (int[] rich : richer) {
            int a = rich[0], b = rich[1];
            g[a][b] = true;
            indegree[b]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.add(i);
            }
        }
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = i;
        }
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v = 0; v < n; v++) {
                if (g[u][v]) {
                    if (quiet[res[v]] > quiet[res[u]]) {
                        res[v] = res[u];
                    }
                    indegree[v]--;
                    if (indegree[v] == 0) {
                        q.add(v);
                    }
                }
            }
        }
        return res;
    }
}
```

T: O(n)			S: O(n^2)



