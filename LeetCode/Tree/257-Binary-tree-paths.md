---
title: Easy | Binary Tree Paths 257
tags:
  - tricky
  - Oh-shit
categories:
  - Leetcode
  - Tree
date: 2020-01-13 15:55:47
---

Given a binary tree, return all root-to-leaf paths.

[Leetcode](https://leetcode.com/problems/binary-tree-paths/)

<!--more-->

**Note:** A leaf is a node with no children.

**Example:**

```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```

---

#### Tricky 

We use DFS to track the path.

We need a Pair class to store the current path according to each node. Push these Pairs into stack, when we pop the Pair out, we can easily get the current path of this node in order to construct the next path.

#### Oh Shit

In recursion method.

`if (root.left == null && root.right == null) {
            res.add("" + root.val);`

We need this line, because if `root.left == null && root.right == null`, the `leftList and rightList` will be empty, `res` will add nothing `res.add("" + root.val + "->" + s);`

---

#### DFS 

Use DFS to track the path, and use a Pair class to store current path.

```java
class Solution {
    class Pair {
        TreeNode n;
        String s;
        public Pair(TreeNode n, String s) {
            this.n = n;
            this.s = s;
        }
    }
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        if (root == null) return res;
        Stack<Pair> stack = new Stack<>();
        stack.push(new Pair(root, "" + root.val));
        while (!stack.isEmpty()) {
            Pair info = stack.pop();
            TreeNode n = info.n;
            String s = info.s;
            if (n.left != null) {
                stack.push(new Pair(n.left, s + "->" + n.left.val));
            }
            if (n.right != null) {
                stack.push(new Pair(n.right, s + "->" + n.right.val));
            }
            if (n.left == null && n.right == null) {
                res.add(s);
            }
        }
        return res;
    }
}
```

T: O(n) 			S: O(n)

---

#### Recursion 

```java
class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        if (root == null) return res;
        if (root.left == null && root.right == null) {
            res.add("" + root.val);
        } else {
            List<String> leftList = binaryTreePaths(root.left);
            for (String s : leftList) {
                res.add("" + root.val + "->" + s);
            }
            List<String> rightList = binaryTreePaths(root.right);
            for (String s : rightList) {
                res.add("" + root.val + "->" + s);
            }
        }
        return res;
    }
}
```

T: O(n) 			S: O(n) call stack.

---

#### Summary 

When we need to get the path of tree, we need a Pair class to store current path according to each node.