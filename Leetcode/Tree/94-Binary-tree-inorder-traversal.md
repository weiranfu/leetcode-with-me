---
title: Medium | Binary Tree Inorder Traversal 94
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2019-10-24 19:15:08
---

Given a binary tree, return the *inorder* traversal of its nodes' values.

[Leetcode](https://leetcode.com/problems/binary-tree-inorder-traversal/)

<!--more-->

**Example:**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

**Follow up:** Recursive solution is trivial, could you do it iteratively?

---

#### Tricky 

This traversal is important. We use a stack to store all the stops in a tree. After processing left nodes, we come back these stops and process right nodes.

---

#### First solution 

Common DFS recursion.

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
    public List<Integer> inorderTraversal(TreeNode root) {
        List <Integer> res = new ArrayList<>();
        helper(root,res);
        return res;
        
    }
    public void helper(TreeNode root, List<Integer>res){
        if (root ==null) return;
        if (root.left!=null){
            helper(root.left, res);
        }
        res.add(root.val);
        if (root.right!=null)
            helper(root.right,res);
        
    }
}
```

---

#### Follow up: use iteration

This traversal is important. We use a stack to store all the stops in a tree. After processing left nodes, we come back these stops and process right nodes.

```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List <Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode n = root;
        while (n != null || !stack.isEmpty()) {
            if (n != null) {
                stack.push(n);  // store node waiting for processing
                n = n.left;
            } else {
                n = stack.pop(); // retrieve node to process.
                res.add(n.val);
                n = n.right;
            }
        }
        return res;
    }
}
```

---

#### Summary 

Here are Preorder, Inorder, Postorder traversal in iteration version.

```java
Preorder
public List<Integer> preorderTraversal(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    Deque<TreeNode> stack = new ArrayDeque<>();
    TreeNode p = root;
    while(!stack.isEmpty() || p != null) {
        if(p != null) {
            stack.push(p);
            result.add(p.val);  // Add before going to children
            p = p.left;
        } else {
            TreeNode node = stack.pop();
            p = node.right;   
        }
    }
    return result;
}
```

```java
Inorder
public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> result = new ArrayList<>();
    Deque<TreeNode> stack = new ArrayDeque<>();
    TreeNode p = root;
    while(!stack.isEmpty() || p != null) {
        if(p != null) {
            stack.push(p);
            p = p.left;
        } else {
            TreeNode node = stack.pop();
            result.add(node.val);  // Add after all left children
            p = node.right;   
        }
    }
    return result;
}
```

```java
Postorder
public List<Integer> postorderTraversal(TreeNode root) {
    LinkedList<Integer> result = new LinkedList<>();
    Deque<TreeNode> stack = new ArrayDeque<>();
    TreeNode p = root;
    while(!stack.isEmpty() || p != null) {
        if(p != null) {
            stack.push(p);
            result.addFirst(p.val);  // Reverse the process of preorder
            p = p.right;             // Reverse the process of preorder
        } else {
            TreeNode node = stack.pop();
            p = node.left;           // Reverse the process of preorder
        }
    }
    return result;
}
```



