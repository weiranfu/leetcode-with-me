---
title: Medium | All Nodes Distance K in Binary Tree 863
tags:
  - common
categories:
  - Leetcode
  - Tree
date: 2020-09-18 20:27:15
---

We are given a binary tree (with root node `root`), a `target` node, and an integer value `K`.

Return a list of the values of all nodes that have a distance `K` from the `target` node.  The answer can be returned in any order.

[Leetcode](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

<!--more-->

**Example 1:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
```

**Note:**

1. The given tree is non-empty.
2. Each node in the tree has unique values `0 <= node.val <= 500`.
3. The `target` node is a node in the tree.
4. `0 <= K <= 1000`.

---

#### Convert Tree to Graph 

Convert Tree to Graph (using `HashMap<TreeNode, List<TreeNode>>` or `List<List<Integer>>`).

Then perform BFS to find nodes with distance K.

Use `List<Integer> map` to record the original id of each node.

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int id = 0;
    TreeNode target;
    List<List<Integer>> g;
    List<Integer> map;
    int t = -1;
    
    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        this.target = target;
        g = new ArrayList<>();
        map = new ArrayList<>();
        dfs(root, -1);
        List<Integer> res = new ArrayList<>();
        if (t == -1) return res;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{t, -1});
        int dist = 0;
        while (!q.isEmpty()) {
            if (dist == K) {
                for (int[] info : q) {
                    res.add(map.get(info[0]));
                }
                return res;
            }
            int size = q.size();
            while (size-- != 0) {
                int[] info = q.poll();
                int curr = info[0], pa = info[1];
                for (int node : g.get(curr)) {
                    if (node == pa) continue;
                    q.add(new int[]{node, curr});
                }
            }
            dist++;
        }
        return res;
    }
    
    private void dfs(TreeNode root, int pa) {
        if (root == null) return;
        int now = id++;
        if (root.val == target.val) t = now;
        g.add(new ArrayList<>());
        map.add(root.val);
        if (pa != -1) {
            g.get(now).add(pa);
            g.get(pa).add(now);
        }
        dfs(root.left, now);
        dfs(root.right, now);
    }
}
```

T: O(n)		S: O(n)

---

#### DFS

Search target node and accumulate distance from target node.

If target node exists in left subtree, then search nodes in right subtree with `dist = left + 1`

```java
class Solution {
    List<Integer> res;
    TreeNode target;
    int K;
    
    public List<Integer> distanceK(TreeNode root, TreeNode target, int K) {
        res = new ArrayList<>();
        this.target = target;
        this.K = K;
        dfs(root);
        return res;
    }
    // to search target node and accumulate distance from target node.
    private int dfs(TreeNode root) {
        if (root == null) return -1;    // target node doesn't exist
        if (root.val == target.val) {
            searchInSubtree(root, 0);
            return 1;                   // dist is 1
        }
        int left = dfs(root.left);
        int right = dfs(root.right);
        if (left != -1) {
            if (left == K) {
                res.add(root.val);
            } else { // search in right subtree with distance {left + 1}
                searchInSubtree(root.right, left + 1);
            }
            return left + 1;
        }
        if (right != -1) {
            if (right == K) {
                res.add(root.val);
            } else {
                searchInSubtree(root.left, right + 1);
            }
            return right + 1;
        }
        return -1;
    }
    // search in subtree with distance {dist}
    private void searchInSubtree(TreeNode root, int dist) {
        if (root == null) return;
        if (dist == K) {
            res.add(root.val);
            return;
        }
        searchInSubtree(root.left, dist + 1);
        searchInSubtree(root.right, dist + 1);
    }
}
```

T: O(n)		S: O(n)

