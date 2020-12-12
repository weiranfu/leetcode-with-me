---
title: Medium | Validate Binary Search Tree 98
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-05-20 23:00:24
---

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

[Leetcode](https://leetcode.com/problems/validate-binary-search-tree/)

<!--more-->

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**

```
    2
   / \
  1   3

Input: [2,1,3]
Output: true
```

**Example 2:**

```
    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

---

#### Tricky 

How to make sure a tree is valid? The possible case is:

```
    10
   / \
  5   15
     / \
    6   20
output: false
Explanation: 6 is smaller than 10.
```

1. **In-order traversal is a traversal which starts from the smallest node to the largest node**

2. Maintain a `min` value and a `max` value when doing recursion. When recursively call on left node, update  `max` value, when recursively call on right node, update `min` value.

---

#### My thoughts 

The approach two.

---

#### Recursion with min and max 

Tree DP problem.

Return value should contains `valid`, `min`, `max`.

```java
class Solution {
    /*
    0: valid or not
    1: max
    2: min
    */
    public boolean isValidBST(TreeNode root) {
        return dfs(root)[0] == 1;
    }
    
    private int[] dfs(TreeNode n) {
        if (n == null) return new int[]{1, -1, -1};
        int[] left = dfs(n.left);
        int[] right = dfs(n.right);
        if (left[0] == 0 || right[0] == 0) return new int[]{0, -1, -1};
        if (n.left != null && left[1] >= n.val || n.right != null && right[2] <= n.val) return new int[]{0, -1, -1};
        int max = n.right == null ? n.val : right[1];
        int min = n.left == null ? n.val : left[2];
        return new int[]{1, max, min};
    }
    
}
```

T: O(n)		S: O(n)

---

#### In-order traversal

In-order traversal is a traversal which starts from the smallest node to the largest node.

```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        TreeNode prev = null;
        while (!stack.isEmpty() || curr != null) {
            if (curr != null) {
                stack.push(curr);
                curr = curr.left;
            } else {
                TreeNode tmp = stack.pop();
                if (prev != null && prev.val >= tmp.val) return false;
                prev = tmp;
                curr = tmp.right;
            }
        }
        return true;
    }
}
```

T: O(n)		S: O(n)

---

#### Summary 

**In-order traversal is a traversal which starts from the smallest node to the largest node**

