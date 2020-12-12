---
title: Medium | Binary Search Tree Iterator 173
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-06-04 03:14:01
---

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling `next()` will return the next smallest number in the BST.

[Leetcode](https://leetcode.com/problems/binary-search-tree-iterator/)

<!--more-->

**Example:**

**![img](https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png)**

```
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
```

---

#### Tricky 

The intuition is that save the inorder traversal nodes into an array. However the space complexity is O(h).

So we could only save the left nodes into Stack. When `next()` is called, we pop out a new TreeNode and try to process its right node and save its left nodes into Stack.

**Since each node in tree can be visited at most twice, the average time complexity for `next()` is O(1).**

---

#### Standard solution  

```java
class BSTIterator {
    
    Stack<TreeNode> stack = new Stack<>();

    public BSTIterator(TreeNode root) {
        TreeNode curr = root;
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
    }
    
    /** @return the next smallest number */
    public int next() {
        TreeNode curr = stack.pop();
        int res = curr.val;
        curr = curr.right;
        while (curr != null) {   // amortized O(1)
            stack.push(curr);
            curr = curr.left;
        }
        return res;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }
}

```

T: O(1)		S: O(h)

