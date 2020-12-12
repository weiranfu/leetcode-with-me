---
title: Hard | Recover Binary Search Tree
tags:
  - tricky
  - Corner Case
categories:
  - Leetcode
  - Tree
date: 2020-05-21 00:41:11
---

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

[Leetcode](https://leetcode.com/problems/recover-binary-search-tree/)

<!--more-->

**Example 1:**

```
Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
```

**Example 2:**

```
Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
```

**Follow up:** Could you devise a constant space solution?

---

#### Tricky 

**The in-order traversal will traverse nodes in ascending order.**

**When we swap two nodes, the ascending order will break. Since we get two elements that are swapped by mistake, there must be a smaller TreeNode get a larger value and a larger TreeNode get a smaller value.**

During in-order traversal, we will visit the incorrect smaller node first, and this node will be detected when we compare its value with next.val, i.e. when it is treated as prev node. The incorrect larger node will be detected when we compare its value with prev.val. We don't know if it is close or not close to incorrect smaller node, so we should continue search BST and update it if we found another incorrect node.

**When we want to do a in-order traversal in constant space, we could use Morris-traversal.**

#### Corner Case

When we use recursion, we cannot pass previous node as an argument, otherwise we need to set previous node as a global argument.

---

#### Recursion 

```java
class Solution {
    TreeNode prev;
    TreeNode first, second;
    
    public void recoverTree(TreeNode root) {
        inOrder(root);
        if (first != null) {
            int tmp = first.val;
            first.val = second.val;
            second.val = tmp;
        }
    }
    private void inOrder(TreeNode root) {
        if (root == null) return;
        inOrder(root.left);
        if (prev != null && prev.val >= root.val) {
            if (first == null) {   // first meet
                first = prev;
                second = root;
            } else {							// meet again
                second = root;
            }
        }
        prev = root;
        inOrder(root.right);
    }
}
```

T: O(n)		S: O(n)

---

#### Iteration

```java
class Solution {
    public void recoverTree(TreeNode root) {
        if (root == null) return;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        TreeNode prev = null;
        TreeNode start = null, end = null;
        while (curr != null || !stack.isEmpty()) {
            if (curr != null) {
                stack.push(curr);
                curr = curr.left;
            } else {
                curr = stack.pop();
                if (prev != null && prev.val >= curr.val) {
                    if (start == null) {
                        start = prev;
                        end = curr;
                    } else {
                        end = curr;
                    }
                }
                prev = curr;
                curr = curr.right;
            }
        }
        int temp = start.val;
        start.val = end.val;
        end.val = temp;
    }
}
```

T: O(n)		S: O(n)

---

#### Morris Traversal

Using Morris Traversal for in-order traversal. [Morris Traversal](https://aranne.github.io/2020/01/11/Tree-traversal/)

```java
class Solution {
    public void recoverTree(TreeNode root) {
        if (root == null) return;
        TreeNode start = null;
        TreeNode end = null;
        TreeNode curr = root;
        TreeNode prev = null;
        while (curr != null) {
            if (curr.left != null) {
                TreeNode tmp = curr.left;
                while (tmp.right != null && tmp.right != curr) {
                    tmp = tmp.right;
                }
                if (tmp.right == null) {
                    tmp.right = curr;
                    curr = curr.left;
                } else {
                    if (prev != null && prev.val >= curr.val) {
                        if (start == null) {
                            start = prev;
                        }
                        end = curr;
                    }
                    tmp.right = null;
                    prev = curr;
                    curr = curr.right;
                }
            } else {
                if (prev != null && prev.val >= curr.val) {
                    if (start == null) {
                        start = prev;
                    }
                    end = curr;
                }
                prev = curr;
                curr = curr.right;
            }
        }
        
        int tmp = start.val;
        start.val = end.val;
        end.val = tmp;
    }
}
```

T: O(n)			S: O(1)

---

#### Summary 

**In-order traveral will traverse a tree's nodes in ascending order, so we can detect errors easily when using in-order traversal.**