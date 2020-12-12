---
title: Medium | Balanced Binary Tree 110
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-01-14 15:19:46
---

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

> a binary tree in which the left and right subtrees of *every* node differ in height by no more than 1.

[Leetcode](https://leetcode.com/problems/balanced-binary-tree/)

<!--more-->

**Example 1:**

Given the following tree `[3,9,20,null,null,15,7]`:

```
    3
   / \
  9  20
    /  \
   15   7
```

Return true.

**Example 2:**

Given the following tree `[1,2,2,3,3,null,null,4,4]`:

```
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
```

Return false.

---

#### Tricky 

The key is how to get the backtracking infomation during travesal the tree.

* Use recursion, get the backtracking by recursion.

  When we calculate the height of tree, we will get the height of its children, then compare them.

* Preorder traversal. Visited a treenode twice.

  First time, mark it as visited and push it back for second time process. Push its children into stack.

  Second time, which means its children has been processed, then get the backtracking infomation from map. 

---

#### My thoughts 

Recursion.

---

#### Recursion 

Use `res[0]` to store whether it is balanced.

```java
class Solution {
    public boolean isBalanced(TreeNode root) {
        boolean[] res = new boolean[1];
        res[0] = true;
        getDepth(root, res);
        return res[0];
    }
    private int getDepth(TreeNode n, boolean[] res) {
        if (n == null) return 0;
        int a = getDepth(n.left, res);
        int b = getDepth(n.right, res);
        if (Math.abs(a - b) > 1) res[0] = false;
        return Math.max(a, b) + 1;
    }
}
```

T: O(n)			S: O(n) call stack

---

#### Preorder + map  

Use `visited` to indicated treenode is visited or not.

Use map to store the infomation of children.

If firstly visiting this node, mark it as visited and push it back for second time process. Push its children into stack.

If secondly visiting this node, which means we have visited its children, get the infomation of children by map.

```java
class Solution {
    class Pair {
        TreeNode n;
        boolean visited;
        public Pair(TreeNode n, boolean visited) {
            this.n = n;
            this.visited = visited;
        } 
    }
    public boolean isBalanced(TreeNode root) {
        Map<TreeNode, Integer> map = new HashMap<>();
        map.put(null, 0);                  // For the leaf node.
        Stack<Pair> stack = new Stack<>();
        if (root == null) {
            return true;
        }
        stack.push(new Pair(root, false));
        while (!stack.isEmpty()) {
            Pair info = stack.pop();
            TreeNode n = info.n;
            boolean visited = info.visited;
            if (!visited) {
                visited = true;
                stack.push(new Pair(n, visited));
                if (n.left != null) stack.push(new Pair(n.left, false));
                if (n.right != null) stack.push(new Pair(n.right, false));
            } else {
                int left = map.get(n.left);
                int right = map.get(n.right);
                if (Math.abs(left - right) > 1) return false;
                map.put(n, Math.max(left, right) + 1);
            }
        }
        return true;
    }
}
```

T: O(n)				S: O(n)

---

#### Summary 

How to use the backtracking infomation in tree?

* Use recursion.
* Use a map and visite a node twice.