---
title: Medium | Construct Binary Tree from Inorder and Postorder Traversal 106
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-05-22 22:17:00
---

Given inorder and postorder traversal of a tree, construct the binary tree.

**Note:**
You may assume that duplicates do not exist in the tree.

[Leetcode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

<!--more-->

For example, given

```
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
```

Return the following binary tree:

```
    3
   / \
  9  20
    /  \
   15   7
```

---

#### Tricky 

This problem is similar with [Construct Binary Tree from Preorder and Inorder Traversal](https://aranne.github.io/2020/05/21/105-Construct-Binary-Tree-from-Preorder-and-inorder-traversal/#more)

Postorder traversal can seen as a reversed preorder traversal.

---

#### Iteration 

```java
class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder.length == 0 || postorder.length == 0 || inorder.length != postorder.length) return null;
        int n = postorder.length;
        TreeNode root = new TreeNode(postorder[n - 1]);
        TreeNode curr = root;
        Stack<TreeNode> stack = new Stack<>();
        for (int i = n - 2, j = n - 1; i >= 0; i--) {
            if (curr.val != inorder[j]) {
                curr.right = new TreeNode(postorder[i]);
                stack.push(curr);
                curr = curr.right;
            } else {
                j--;
                while (!stack.isEmpty() && stack.peek().val == inorder[j]) {
                    curr = stack.pop();
                    j--;
                }
                curr.left = new TreeNode(postorder[i]);
                curr = curr.left;
            }
        }
        return root;
    }
}
```

T: O(n)		S:  O(n)

---

#### Recursion 

```java
class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        return findRoot(postorder.length - 1, 0, inorder.length, inorder, postorder);
    }
    
    private TreeNode findRoot(int post, int inStart, int inEnd, int[] inorder, int[] postorder) {
        if (post < 0 || inStart >= inEnd) return null;
        int target = postorder[post];
        TreeNode root = new TreeNode(target);
        if (inEnd - inStart == 1 && inorder[inStart] == target) {
            return root;
        }
        int nextStart;
        for (nextStart = inEnd - 1; nextStart >= inStart; nextStart--) {
            if (inorder[nextStart] == target) {
                break;
            }
        }
        root.right = findRoot(post - 1, nextStart + 1, inEnd, inorder, postorder);
        root.left = findRoot(post - inEnd + nextStart, inStart, nextStart, inorder, postorder);
        return root;
    }
}
```

T: O(n)		S: O(n)

