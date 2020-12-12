---
title: Easy | Invert Binary Tree 226
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-01-10 11:53:45
---

Invert a binary tree.

[Leetcode](https://leetcode.com/problems/invert-binary-tree/)

<!--more-->

**Example:**

Input:

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```

Output:

```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

---

#### Tricky 

We can use DFS or BFS to solve this problem.

---

#### BFS 

Use a Queue to perform BFS to invert tree.

```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return root;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode n = queue.poll();
            TreeNode left = n.left;
            TreeNode right = n.right;
            n.left = right;
            n.right = left;
            if (right != null) queue.offer(right);
            if (left != null) queue.offer(left);
        }
        return root;
    }
}
```

T: O(n) 		S: O(n)

---

#### DFS + Recursion 

```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return root;
        TreeNode left = root.left;
        TreeNode right = root.right;
        root.left = right;
        root.right = left;
        invertTree(left);
        invertTree(right);
        return root;
    }
}
```

T: O(n) 			S: O(n)

---

#### DFS + Iterative 

```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return root;
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            TreeNode left = n.left;
            TreeNode right = n.right;
            n.left = right;
            n.right = left;
            if (left != null) stack.push(left);
            if (right != null) stack.push(right);
        }
        return root;
    }
}
```

T: O(n)		S: O(n)

---

#### Summary 

Invert a tree using DFS and BFS.