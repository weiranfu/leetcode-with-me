---
title: Hard | Construct Binary Tree from Preorder and Inorder Traversal 105
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-05-21 22:07:47
---

Given preorder and inorder traversal of a tree, construct the binary tree.

**Note:**
You may assume that duplicates do not exist in the tree.

[Leetcode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

<!--more-->

For example, given

```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

Return the following binary tree:

```
    3
   / \
  9  20
    /  \
   15   7
```

**Follow up:** [Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

---

#### Tricky 

Consider this input:

```
preorder: [1, 2, 4, 5, 3, 6]
inorder: [4, 2, 5, 1, 6, 3]
```

The obvious way to build the tree is:

1. Use the first element of `preorder`, the `1`, as root.
2. Search it in `inorder`.
3. Split `inorder` by `root`, here into `[4, 2, 5]` and `[6, 3]`.
4. Split the rest of  `preorder` into two parts as large as the `inorder` parts, here into `[2, 4, 5]` and `[3, 6]`.
5. Use `preorder = [2, 4, 5]` and `inorder = [4, 2, 5]` to add the left subtree.
6. Use `preorder =`[3, 6]`and`inorder = `[6, 3]` to add the right subtree.

---

#### First solution 

```java
class Solution {
    int[] preorder, inorder;
    int n;
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        this.n = preorder.length;
        return build(0, 0, n - 1);
    }
    private TreeNode build(int preCurr, int inLeft, int inRight) {
        if (preCurr >= n || inLeft > inRight) return null;
        TreeNode root = new TreeNode(preorder[preCurr]);
        if (inLeft == inRight) return root;  // no child
        int inCurr;
        for (inCurr = inLeft; inCurr <= inRight; inCurr++) {
            if (preorder[preCurr] == inorder[inCurr]) break;
        }
        root.left = build(preCurr + 1, inLeft, inCurr - 1);
        root.right = build(preCurr + inCurr - inLeft + 1, inCurr + 1, inRight);
        return root;
    }
}
```

T: O(n)		S: O(n)

---

#### Iteration

1. Keep pushing the nodes from the preorder into a stack (and keep making the tree by adding nodes to the left of the previous node) until the top of the stack matches the inorder.
2. At this point, pop the top of the stack until the top does not equal inorder (keep a flag to note that you have made a pop).
3. Repeat 1 and 2 until preorder is empty. The key point is that whenever the flag is set, insert a node to the right and reset the flag.

```java
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0 || inorder.length == 0 || preorder.length != inorder.length) return null;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode root = new TreeNode(preorder[0]);
        TreeNode curr = root;
        for (int i = 1, j = 0; i < preorder.length; i++) {
            if (curr.val != inorder[j]) { // traverse pre-order and save nodes in stack.
                curr.left = new TreeNode(preorder[i]);
                stack.push(curr);
                curr = curr.left;
            } else {                       // traverse back to find spit node.
                j++;
                // find right node position
                while (!stack.isEmpty() && stack.peek().val == inorder[j]) { 
                    curr = stack.pop();
                    j++;
                }
                curr.right = new TreeNode(preorder[i]);  // the root of right node.
                curr = curr.right;
            }
        }
        return root;
    }
}
```

T:  O(n)			S: O(n)

---

#### Summary 

The distribution of arrays for preorder and inorder traversal:

Preorder: `[root][left-part][right-part]`

Inorder: `[left-part][root][right-part]`