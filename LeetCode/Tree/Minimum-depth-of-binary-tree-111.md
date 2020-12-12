---
title: Easy | Minimum Depth of Binary Tree 111
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-01-13 19:43:25
---

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

[Leetcode](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

<!--more-->

**Example:**

Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its minimum depth = 2.

---

#### Tricky 

* Use recursion to store depth with TreeNode.
* Use Pair class to store depth along with TreeNode during DFS
* Use BFS to find the first leaf, then reture depth.

---

#### DFS  -> bottom up 

```java
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        return dfs(root);
    }
    private int dfs(TreeNode n) {
        int min = Integer.MAX_VALUE;
        if (n.left == null && n.right == null) return 1;		// find leaf
        if (n.left != null) min = Math.min(min, dfs(n.left));
        if (n.right != null) min = Math.min(min, dfs(n.right));
        return min + 1;
    }
}
```

T: O(n) 			S: O(n) call stack

---

#### DFS  -> top down

```java
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        int[] min = new int[1];
        min[0] = Integer.MAX_VALUE;
        findMin(root, 1, min);
        return min[0];
    }
    private void findMin(TreeNode n, int longth, int[] min) {
        if (n == null) return;
        if (n.left == null && n.right == null) {  // find leave
            min[0] = Math.min(min[0], longth);
        }
        if (n.left != null) {
            findMin(n.left, longth + 1, min);
        }
        if (n.right != null) {
            findMin(n.right, longth + 1, min);
        }
    }
}
```

T: O(n)				S: O(n)

---

#### BFS 

```java
class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int depth = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            depth++;
            while (size-- != 0) {
                TreeNode n = queue.poll();
                if (n.left == null && n.right == null) return depth; // find leaf
                if (n.left != null) queue.offer(n.left);
                if (n.right != null) queue.offer(n.right);
            }
        }
        return depth;
    }
}
```

T: O(n)			S: O(n)
