---
title: Medium | Binary Tree Upside Down 156
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-05-31 22:12:50
---

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

[Leetcode](https://leetcode.com/problems/binary-tree-upside-down/)

<!--more-->

**Example:**

```
Input: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

Output: return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1  
```

---

#### Tricky 

**As shown in the figure, 1 shows the original tree, you can think about it as a comb, with 1, 2, 4 form the bone, and 3, 5 as the teeth. All we need to do is flip the teeth direction as shown in figure 2.**

**Don't forget to reset the `root.left = null, root.right = null`**

In iterative solution, we can't change the `left` and `right` child right away, so we need to save them into `preLeft`, `preRight` and change them in next loop.

---

#### My thoughts 

Upside down with recursion. 

---

#### Recursion

```java
class Solution {
    public TreeNode upsideDownBinaryTree(TreeNode root) {
        if (root == null) return null;
        if (root.left == null) return root;
        TreeNode left = root.left;
        TreeNode right = root.right;
        root.left = null;                                // reset child to null.
        root.right = null;
        TreeNode newNode = upsideDownBinaryTree(left);
        left.left = right;
        left.right = root;
        return newNode;
    }
}
```

T: O(n)		S: O(n)

---

#### Iteration

In iterative solution, we can't change the `left` and `right` child right away, so we need to save them into `preLeft`, `preRight` and change them in next loop.

```java
class Solution {
    public TreeNode upsideDownBinaryTree(TreeNode root) {
        TreeNode curr = root;
        TreeNode newNode = null;
        TreeNode preLeft = null, preRight = null;
        while (curr != null) {
            TreeNode left = curr.left;
            TreeNode right = curr.right;
            
            curr.left = preLeft;      // connect previous left
            curr.right = preRight;    // connect previous right
            
            preLeft = right;         // save next left
            preRight = curr;         // save next right
            
            newNode = curr;          // save new node
            curr = left;
        }
        return newNode;
    }
}
```

T: O(n)		S: O(1)

