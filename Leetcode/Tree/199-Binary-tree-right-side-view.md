---
title: Medium | Binary Tree Right Side View 199
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-06-06 05:43:15
---

Given a binary tree, imagine yourself standing on the *right* side of it, return the values of the nodes you can see ordered from top to bottom.

[Leetcode](https://leetcode.com/problems/binary-tree-right-side-view/)

<!--more-->

**Example:**

```
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```

---

#### Tricky 

* BFS: to get the first node in each level.

* DFS: We try to search right most node as much as we can. If we firstly meet a node in a new level, we add it into result. `if (depth == res.size()) res.add(n.val)`

---

#### BFS



---

#### DFS

We try to search right most node as much as we can. If we firstly meet a node in a new level, we add it into result. `if (depth == res.size()) res.add(n.val)`

```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        dfs(root, res, 0);
        return res;
    }
    
    private void dfs(TreeNode node, List<Integer> res, int depth) {
        if (node == null) return;
        if (depth == res.size()) {  // if firstly meet right node.
            res.add(node.val);
        }
        dfs(node.right, res, depth + 1);
        dfs(node.left, res, depth + 1);
    }
}
```

T: O(n)		S: O(n)

---

#### BFS

```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode n = queue.poll();
                if (i == 0) res.add(n.val);   // only add first node.
                if (n.right != null) queue.add(n.right);
                if (n.left != null) queue.add(n.left);
            }
        }
        return res;
    }
}
```

T: O(n)		S: O(n)

