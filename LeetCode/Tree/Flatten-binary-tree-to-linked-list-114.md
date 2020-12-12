---
title: Hard | Flatten Binary Tree to Linked List
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-05-23 16:48:24
---

Given a binary tree, flatten it to a linked list in-place.

[Leetcode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

<!--more-->

For example, given the following tree:

```
    1
   / \
  2   5
 / \   \
3   4   6
```

The flattened tree should look like:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

---

#### Tricky 

The key is to find the last node in the `root.left` after flatten, then append `root.right` to that last node.

* Recursion: find the last node in `root.left` part and append `root.right` to it.

* Iteration: the last node can be found at: 

  ```java
  TreeNode last = root.left;
  while (last != null && last.right != null) {
  	last = last.right;
  }
  ```

* Stack: postorder traversal: maintain a pointer to previous node, exchange its left subtree and right subtree.

---

#### Recursion

1. Find the last node in `root.left` part and append `root.right` to it.

```java
class Solution {
    public void flatten(TreeNode root) {
        if (root == null) return;
        TreeNode left = root.left;
        TreeNode right = root.right;
        flatten(left);
        flatten(right);
        root.right = left;
        root.left = null;
        TreeNode last = root;
        while (last.right != null) {
            last = last.right;
        }
        last.right = right;
    }
}
```

T: O(n)			S: O(n)

2. Return the last node when recursion.

```java
class Solution {
    public void flatten(TreeNode root) {
        helper(root);
    }
    
    private TreeNode helper(TreeNode root) {
        if (root == null) return null;
        TreeNode leftLast = helper(root.left);
        TreeNode rightLast = helper(root.right);
        if (leftLast != null) {
            leftLast.right = root.right;
            root.right = root.left;
            root.left = null;
        }
        if (leftLast == null && rightLast == null) {
            return root;
        }
        return (rightLast != null) ? rightLast : leftLast;
    }
}
```

T: O(n)		S: O(n)

---

#### Iteration

Find the last node in `root.left` part. This is similar with Morris Traversal.

```java
class Solution {
    public void flatten(TreeNode root) {
        if (root == null) return;
        TreeNode curr = root;
        while (curr != null) {
            if (curr.left != null) {
                TreeNode last = curr.left;      // find last node in root.left.
                while (last.right != null) {
                    last = last.right;
                }
                last.right = curr.right;   // append root.right to last node.
                curr.right = curr.left;
                curr.left = null;
            }
            curr = curr.right;
        }
    }
}
```

T: O(n)		S: O(1)

---

#### Stack  

Postorder traversal with stack.

Use `prev` pointer to track the previous node and concatenate `curr` node to the the right child node of `prev` node.

```java
class Solution {
    public void flatten(TreeNode root) {
        if (root == null) return;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode pre = null;
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode curr = stack.pop();
            if (pre != null) {
                pre.right = curr;
                pre.left = null;
            }
            if (curr.right != null) stack.push(curr.right);
            if (curr.left != null) stack.push(curr.left);
            pre = curr;
        }
    }
}
```

T: O(n)		S: O(n)
