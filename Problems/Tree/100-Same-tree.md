---
title: Easy | Same Tree 100
tags:
  - common
categories:
  - Leetcode
  - Tree
date: 2019-10-24 23:35:30
---

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

[Leetcode](https://leetcode.com/problems/same-tree/)

<!--more-->

**Example 1:**

```
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
```

**Example 2:**

```
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
```

**Example 3:**

```
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
```

**Follow up:** What about using iteration?

---

#### My thoughts 

Traversal all nodes in a tree to compare node.

---

#### First solution 

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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if ((p == null && q != null) || (p != null && q == null))  {
            return false;
        }
        if (p != null && q != null) {
            if (p.val != q.val) {
                return false;
            }
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }
        return true;
    }
}
```

T: O(n) S: O(n)

---

#### Optimized 

There all only three cases for p and q.

```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if (p == null || q == null) {
            return false;
        }
        if (p.val != q.val) {
            return false;
        }
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
```

T: O(n) S: O(n)

---

#### Follow up

If using iteration, we need a stack to store nodes waiting for processing during DFS.

```java
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Stack<TreeNode> stack = new Stack<>();
        stack.push(q);
        stack.push(p);
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            TreeNode m = stack.pop();
            if (n == null && m == null) continue;
            if (n == null || m == null) return false;
            if (n.val != m.val) return false;
            stack.push(m.left);
            stack.push(n.left);
            stack.push(m.right);
            stack.push(n.right);
        }
    return true;
    }
}
```

T: O(n) S: O(n)

---

#### Summary 

Traversal all nodes of tree to compare two trees.