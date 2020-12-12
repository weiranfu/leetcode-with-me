---
title: Medium | Number of Good Leaf Nodes Pairs 1530
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-07-26 15:14:16
---

Given the `root` of a binary tree and an integer `distance`. A pair of two different **leaf** nodes of a binary tree is said to be good if the length of **the shortest path** between them is less than or equal to `distance`.

Return *the number of good leaf node pairs* in the tree.

[Leetcode](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/07/09/e1.jpg)

```
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/07/09/e2.jpg)

```
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
```

---

#### Build graph + BFS 

Convert TreeNode to graph.

Perform BFS to search at most `distance` leaves.

```java
class Solution {
    
    List<List<Integer>> g;
    int id;									// each TreeNode's id
    int distance;
    List<Integer> isLeaf;		// is leaf or not
    int[] visited;
    int[] dist;
    int res;
    
    public int countPairs(TreeNode root, int distance) {
        this.distance = distance;
        id = 0;
        g = new ArrayList<>();
        isLeaf = new ArrayList<>();
        build(root, -1);
        visited = new int[id];
        Arrays.fill(visited, -1);
        dist = new int[id];
        for (int i = 0; i < id; i++) {
            if (isLeaf.get(i) == 1) {
                bfs(i);
            }
        }
        return res / 2;			// recalculate a pair during bfs
    }
    private void bfs(int x) {
        visited[x] = x;// use id to color visited node avoid clearing visited every time
        dist[x] = 0;
        Queue<Integer> q = new LinkedList<>();
        q.add(x);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : g.get(u)) {
                if (visited[v] == x) continue;
                visited[v] = x;
                dist[v] = dist[u] + 1;
                if (dist[v] > distance) continue; // prunning
                if (isLeaf.get(v) == 1) res++;    // find a leaf
                else q.add(v);
            }
        }
    }
    
    private void build(TreeNode n, int pa) {
        if (n == null) return;
        int now = id++;							// increase id
        g.add(new ArrayList<>());
        isLeaf.add(0);
        if (pa != -1) {
            g.get(now).add(pa);			// build graph
            g.get(pa).add(now);
        }
        if (n.left == null && n.right == null) {
            isLeaf.set(now, 1);			// set isLeaf = true
            return;
        }
        build(n.left, now);
        build(n.right, now);
    }
}
```

T: O(n^2)			S: O(n)

---

#### Tree DP

Use `dp[i][d]` to store number of leaves in distance `d` of `i`th node.

So for `left` and `right` nodes of `n` node, 

`if d1 + d2 + 2 <= distance`, number of new pairs is `res += cnt[l][d1] * cnt[r][d2]`

```java
class Solution {
    int[][] cnt = new int[1050][11];
    int id;
    int distance;
    int res;
    
    public int countPairs(TreeNode root, int distance) {
        this.distance = distance;
        id = 0;
        res = 0;
        dfs(root);
        return res;
    }
    private int dfs(TreeNode n) {
        int now = ++id;             // 0 is for null node
        int l = 0, r = 0;
        if (n.left != null) l = dfs(n.left);
        if (n.right != null) r = dfs(n.right);
        
        if (r > 0 && l > 0) {
            for (int i = 0; i <= distance; i++) {
                for (int j = 0; j <= distance; j++) {
                    if (i + j + 2 <= distance) {
                        res += cnt[l][i] * cnt[r][j];
                    }
                }
            }
        }
        if (r == 0 && l == 0) {
            cnt[now][0] = 1;        // leaf node
            return now;
        }
        for (int i = 0; i < distance; i++) {
            cnt[now][i + 1] = cnt[l][i] + cnt[r][i];
        }
        return now;
    }
}
```

T: O(n)			S: O(n)

---

#### Optimized: return `cnt` array for each node  

To avoid allocating `cnt[][]` array, we could return `cnt[]` for each child node.

```java
class Solution {
    int distance;
    int res;
    
    public int countPairs(TreeNode root, int distance) {
        this.distance = distance;
        res = 0;
        dfs(root);
        return res;
    }
    private int[] dfs(TreeNode n) {
        int[] cnt = new int[distance + 1];
        if (n == null) return cnt;								// return empty cnt array
        if (n.left == null && n.right == null) {
            cnt[0] = 1;
            return cnt;
        }
        int[] left = dfs(n.left);									// get cnt[] from children
        int[] right = dfs(n.right);
        
        for (int i = 0; i < distance; i++) {
            for (int j = 0; j < distance; j++) {
                if (i + j + 2 <= distance) {
                    res += left[i] * right[j];
                }
            }
        }
        
        for (int i = 0; i < distance; i++) {
            cnt[i + 1] += left[i] + right[i];
        }
        
        return cnt;
    }
}
```

T: O(n)			S: O(n)

