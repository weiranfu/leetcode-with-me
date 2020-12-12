---
title: Medium | Diameter of Binary Tree 543	
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-01-03 15:28:26
---

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the **longest** path between any two nodes in a tree. This path may or may not pass through the root.

[Leetcode](https://leetcode.com/problems/diameter-of-binary-tree/)

<!--more-->

**Example:**
Given a binary tree 

```
          1
         / \
        2   3
       / \     
      4   5    
```

Return **3**, which is the length of the path [4,2,1,3] or [5,2,1,3].

**Note:** The length of path between two nodes is represented by the number of edges between them.

---

#### Tricky 

We can use number of nodes to represent the height which can be much easier.

```java
class Solution {
    int max = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) return 0;
        dfs(root);
        return max - 1;           // return nodes - 1
    }
    private int dfs(TreeNode n) {
        if (n == null) return 0;
        int left = dfs(n.left);
        int right = dfs(n.right);
        max = Math.max(max, left + right + 1);
        return Math.max(left, right) + 1;
    }
}
```

T: O(n)		S: O(n)

---

If we use the number of paths to represent the height, the code will be cleaner.

```java
class Solution {
    int max = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return max;
    }
    private int dfs(TreeNode n) {
        if (n == null) return 0;
        int left = dfs(n.left);
        int right = dfs(n.right);
        max = Math.max(max, left + right);
        return Math.max(left, right) + 1;  // add path + 1
    }
}
```

T: O(n)		S: O(n)