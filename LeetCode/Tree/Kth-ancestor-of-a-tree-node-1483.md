---
title: Hard | Kth Ancestor of a Tree Node 1483
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-06-15 19:00:48
---

You are given a tree with `n` nodes numbered from `0` to `n-1` in the form of a parent array where `parent[i]` is the parent of node `i`. The root of the tree is node `0`.

Implement the function `getKthAncestor``(int node, int k)` to return the `k`-th ancestor of the given `node`. If there is no such ancestor, return `-1`.

The *k-th* *ancestor* of a tree node is the `k`-th node in the path from that node to the root.

[Leetcode](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/)

<!--more-->

**Example:**

**![img](https://assets.leetcode.com/uploads/2019/08/28/1528_ex1.png)**

```
Input:
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

Output:
[null,1,0,-1]

Explanation:
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2);  // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3);  // returns -1 because there is no such ancestor
```

**Constraints:**

- `1 <= k <= n <= 5*10^4`
- `parent[0] == -1` indicating that `0` is the root node.
- `0 <= parent[i] < n` for all `0 < i < n`
- `0 <= node < n`
- There will be at most `5*10^4` queries.

---

#### Tricky 

This is a problem of [Lowest Common Ancestors](https://cp-algorithms.com/graph/lca_binary_lifting.html)

* We could use Binary Lifting method. 

  We can record the ancestors in `2^0`, `2^1`, `2^2`,…,`2^j` jump steps for a node `i` in `jump[i][j]`.

  The how to compute `jump[i][j]` ? `jump[i][j]` means we jump `2^j` steps from `i`, which means we could jump `2^j-1` steps first and then jump another `2^j-1` steps.

  So `jump[i][j] = jump[jump[i][j-1]][j-1]`

  How to jump `k` steps? We can represent `k` in its binary format. For example, we want to jump 11 steps.

  `11 = 1011` we need to jump `2^0`, `2^1`, `2^3` steps. So if its binary is 1 at `i`th pos, we need to jump `2^i` steps.

* 

---

#### Binary Lifting

Since node `n <= 5*10^4`, the max jump step can be set 20.

```java
class TreeAncestor {
    
    int max = 20;       // max jump 2^20
    int[][] jump;
    
    public TreeAncestor(int n, int[] parent) {
        jump = new int[n][max];
        for (int i = 0; i < max; i++) {
            jump[0][i] = -1;
        }
        for (int i = 0; i < n; i++) {
            jump[i][0] = parent[i];  // jump 2^0 = 1 step
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < max; j++) {
                if (jump[i][j - 1] == -1) { // cannot jump further
                    jump[i][j] = -1;
                } else {
                    jump[i][j] = jump[jump[i][j - 1]][j - 1];// jump 2^j-1 & 2^j-1 steps
                }
            }
        }
    }
    
    public int getKthAncestor(int node, int k) {
        for (int i = 0; i < max; i++) {
            if (((k >> i) & 1) == 1) {     // get ith bit in binary
                node = jump[node][i];      // jump 2^i steps.
                if (node == -1) break;
            }
        }
        return node;
    }
}
```

T: O(nMax)			S: O(nMax)

---

#### DFS序

We use DFS to give each node an id. (preorder traversal)

​	  	   0

​		1	    7

​	2	  5		 8

3    4 	   6

**In a subtree, the root has the smallest DFS number.** For example in subtree

​		1	

​	2	  5	

3    4 	   6

root's dfs number 1 is smallest.

in subtree 

​	2	

3    4 	  

root's dfs number 2 is smallest.

We can save nodes into levels.

If we want to find the `k`th ancestor of node `n`, we can find it in all nodes in level `level[n] - k`

**Then the ancestor must be the node with largest dfs number which is smaller than dfs number of node `n`.**

If a node with dfs number greater than `dfn[n]` is the ancestor, this node cann't belong to this subtree. So the dfs number must be smaller than `dfn[n]`.

Let's find node `6`'s `1`th ancestor. `2 5 8` are in this level.

if 2 is ancestor and 5 is smaller than 6, then 5 cannot be at the same level with 2.

So the ancestor must be 5, the largest one smaller than 6.

**We could use binary search to find this node in the level.**

```java
class TreeAncestor {
    
    List<Integer>[] tree;       
    List<List<Integer>> level;  // nodes in a level
    int[] dfn;            // dfs number
    int ndfn;             // dfs number starts wih 0
    int[] depth;          // depth of each node
    
    public TreeAncestor(int n, int[] parent) {
        tree = new List[n];
        for (int i = 0; i < n; i++) {
            tree[i] = new ArrayList<>();
        }
        level = new ArrayList<>();
        dfn = new int[n];
        ndfn = 0;
        depth = new int[n];
        
        for (int i = 1; i < n; i++) {      // build tree
            tree[parent[i]].add(i);
        }
        dfs(0, 0);
    }
    
    private void dfs(int n, int dep) {
        if (level.size() == dep) {
            level.add(new ArrayList<>());
        }
        dfn[n] = ndfn++;                              // mark dfs number
        depth[n] = dep;                               // save the depth  
        level.get(dep).add(n);                    // save nodes into level
        for (int child : tree[n]) {
            dfs(child, dep + 1);
        }
    }
    
    public int getKthAncestor(int node, int k) {
        int d = depth[node];
        if (d - k < 0) return -1;
        List<Integer> list = level.get(d - k);
        int left = 0, right = list.size();
        while (left < right) {                                       // binary search
            int mid = left + (right - left) / 2;               
            if (dfn[list.get(mid)] < dfn[node]) {        // find the first node larger than or equal to dfn[node]
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return list.get(left - 1);                             // ancestor is the largest one smaller than dfn[node]
    }
}
```

T: O(nlogL)			S: O(n)

