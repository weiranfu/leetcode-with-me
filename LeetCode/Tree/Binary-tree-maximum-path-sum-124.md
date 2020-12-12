---
title: Medium | Binary Tree Maximum Path Sum 124
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-05-26 17:30:46
---

Given a **non-empty** binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain **at least one node** and does not need to go through the root.

[Leetcode](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

<!--more-->

**Example 1:**

```
Input: [1,2,3]

       1
      / \
     2   3

Output: 6
```

**Example 2:**

```
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
```

---

#### Tricky 

When we consider Node `n`, we find the max sum cross `n`.

If `left` or `right` max sum is smaller than 0, we don't use it.

Finally we return the max sum from `n` to leaves.

```java
class Solution {
  	int res = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        maxRootSum(root);
        return res;
    }
    
    public int maxRootSum(TreeNode n) {
        if (n == null) return 0;
        int max = n.val;
        int left = maxRootSum(n.left);       // left max sum
        int right = maxRootSum(n.right);     // right max sum
      	if (left > 0) max += left;
        if (right > 0) max += right;
      	res = Math.max(res, max);
      	return node.val + Math.max(0, Math.max(left, right)); // max sum from n to leaf
    }
}
```

T: O(n)		S: O(n) call stack

---

#### Iteration

**The topological order of get the sum of path is bottom-up. So we could get the postorder nodes of the tree.**

```java
class Solution {
    public int maxPathSum(TreeNode root) {
        int res = Integer.MIN_VALUE;
        List<TreeNode> list = getPostOrder(root);
        Map<TreeNode, Integer> map = new HashMap<>();
        map.put(null, 0);
        for (TreeNode node : list) {
            int left = Math.max(0, map.get(node.left));
            int right = Math.max(0, map.get(node.right));
            res = Math.max(res, node.val + left + right);
            map.put(node, node.val + Math.max(left, right));
        }
        return res;
    }
    
    private List<TreeNode> getPostOrder(TreeNode root) {
        List<TreeNode> res = new ArrayList<>();
        if (root == null) return res;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        while (!stack.isEmpty() || curr != null) {
            if (curr != null) {
                res.add(curr);
                stack.push(curr);
                curr = curr.right;
            } else {
                curr = stack.pop();
                curr = curr.left;
            }
        }
        return Collections.reverse(res);
    }
}
```

T: O(n)		S: O(n)

