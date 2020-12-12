---
title: Medium | Lowest Common Ancestor of a Binary Tree 236
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-06-23 01:43:59
---

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

[Leetcode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

<!--more-->

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

**Example 1:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

**Example 2:**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

**Note:**

- All of the nodes' values will be unique.
- p and q are different and both values will exist in the binary tree.

---

#### Tricky 

* Recursion: Try to find node p and node q in left and right subtrees.

  if both sides find node, return root.

* Iteration: we can save the parent nodes so we can traverse back from p or q.

  Then we add all parents of p into a set.

  When we traverse back from q, if we meet a node already in the set, that node is LCA.

---

#### Recursion

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return null;
        else if (root == p) return p;
        else if (root == q) return q;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root;
        else if (left != null) return left;
        return right;
    }
}
```

T: O(n)			S: O(n)

---

#### Iteration

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        Map<TreeNode, TreeNode> parent = new HashMap<>();
        Stack<TreeNode> stack = new Stack<>();
        parent.put(root, null);
        stack.push(root);
        while (!parent.containsKey(p) || !parent.containsKey(q)) {
            TreeNode curr = stack.pop();
            if (curr.left != null) {
                parent.put(curr.left, curr);
                stack.push(curr.left);
            }
            if (curr.right != null) {
                parent.put(curr.right, curr);
                stack.push(curr.right);
            }
        }
        
        Set<TreeNode> set = new HashSet<>();
        while (p != null) {
            set.add(p);
            p = parent.get(p);
        }
        while (q != null && !set.contains(q)) {
            q = parent.get(q);
        }
        return q;
    }
}
```

T: O(n)		S: O(n)

