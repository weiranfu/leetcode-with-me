---
title: Medium | Binary Tree Preorder Traversal 144
tags:
  - common
  - implement
categories:
  - Leetcode
  - Tree
date: 2019-10-23 21:56:46
---

Given a binary tree, return the *preorder* traversal of its nodes' values.

[Leetcode](https://leetcode.com/problems/binary-tree-preorder-traversal/)

<!--more-->

**Example:**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
```

**Follow up:** Recursive solution is trivial, could you do it iteratively?

---

#### Implement

We use ArrayList to collect node values, but what if this ArrayList needs to created inside the recursion during Preorder traversal?

Use `Array.addAll(array)` to catch up what returned by last recursion.

#### Oh-Shit

When using stack for preorder traversal, we need to first push right child node into stack and then left child node in order to traverse left hand side firstly.

---

#### Recursion

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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> a = new ArrayList<>();
        if (root == null) {
            return a;
        }
        a.add(root.val);
        a.addAll(preorderTraversal(root.left));
        a.addAll(preorderTraversal(root.right));
        return a;
    }
}
```

Because of `array.addAll(array)` , this is much slower than recursion with helper function below.

---

#### Use help function for recursion

```java
public List<Integer> preorderTraversal(TreeNode root) {
		List<Integer> pre = new LinkedList<Integer>();
		preHelper(root,pre);
		return pre;
	}
	public void preHelper(TreeNode root, List<Integer> pre) {
		if(root==null) return;
		pre.add(root.val);
		preHelper(root.left,pre);
		preHelper(root.right,pre);
	}
```

---

#### Iteration

Use Stack to store what needs to be done. After you process a node, you add its two children into stack waiting for processing.

Similar to DFS using stack, and BFS uses a queue.

```java
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> a = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            if (n != null) {
                a.add(n.val);
                stack.push(n.right);
                stack.push(n.left);
            }
        }
        return a;
    }
}
```

---

#### Follow up

Using iteration to get the postorder traversal.

Still use stack to deal with DFS, however we need to reverse the result that we get in preordre traversal.

```java
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            if (n != null) {
                stack.push(n.left);
                stack.push(n.right);
                list.add(0, n.val);     // add postorder node to the end of list.
            }
        }
        return list;
    }
}
```

---

#### Summary 

Stack is for DFS and Queue is for BFS.