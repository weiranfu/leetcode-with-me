---
title: Medium | Count Complete Tree Nodes 222
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-06-19 22:49:53
---

Given a **complete** binary tree, count the number of nodes.

[Leetcode](https://leetcode.com/problems/count-complete-tree-nodes/)

<!--more-->

**Note:**

**Definition of a complete binary tree from Wikipedia:**
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

**Example:**

```
Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
```

---

#### Tricky 

We can get the number of nodes of a complete tree is that tree is full.

If a full complete tree's height is `h`, the number of nodes is `2^h - 1`.

How to determine a complete tree is full?

We could easily check the left subtree is full by find the height of right subtree.

if `rightH == h - 1`, the left subtree is full with height `h - 1`, otherwise the right subtree is full with height `h - 2`

---

#### My thoughts 

Failed to solve.

---

#### Check left and right subtree's height

```java
class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        int h = height(root);
        int rightH = height(root.right);
        if (rightH == h - 1) {
            return (1 << h - 1) + countNodes(root.right);
        } else {
            return (1 << rightH) + countNodes(root.left);
        }
    }
    
    private int height(TreeNode n) {
        int h = 0;
        while (n != null) {
            h++;
            n = n.left;
        }
        return h;
    }
}
```

T: O(logn \* logn)				S: O(logn)

Iterative version

```java
class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        TreeNode curr = root;
        int h = height(root);
        int sum = 0;
        while (curr != null) {
            if (height(curr.right) == h - 1) {
                sum += (1 << h - 1);
                h--;
                curr = curr.right;
            } else {
                sum += (1 << h - 2);
                h--;
                curr = curr.left;
            }
        }
        return sum;
    }
    
    private int height(TreeNode n) {
        int h = 0;
        while (n != null) {
            h++;
            n = n.left;
        }
        return h;
    }
}
```

T: O(logn \* logn)				S: O(1)



