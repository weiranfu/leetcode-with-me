---
title: Medium | Balance a Binary Search Tree 1382
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-09-19 00:32:26
---

Given a binary search tree, return a **balanced** binary search tree with the same node values.

A binary search tree is *balanced* if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

[Leetcode](https://leetcode.com/problems/balance-a-binary-search-tree/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/08/22/1515_ex1.png)![img](https://assets.leetcode.com/uploads/2019/08/22/1515_ex1_out.png)**

```
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
```

**Constraints:**

- The number of nodes in the tree is between `1` and `10^4`.
- The tree nodes will have distinct values between `1` and `10^5`.

**Follow up:** 

[Convert Sorted Array to Balanced BST](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

---

#### Standard solution  

Use in-order traversal to get the sorted nodes.

Then construct a balanced BST with mid node as root, `[left, mid-1]` nodes as left subtree, `[mid+1, right]` nodes as right subtree.

```java
class Solution {
    List<TreeNode> list = new ArrayList<>();
    
    public TreeNode balanceBST(TreeNode root) {
        preOrder(root);
        return dfs(0, list.size() - 1);
    }
    private TreeNode dfs(int left, int right) {
        // must stops at leaf, to assign leaf.left = null, leaf.right = null;
        if (left > right) return null; 
        int mid = left + (right - left) / 2;
        TreeNode curr = list.get(mid);
        TreeNode lnode = dfs(left, mid - 1);
        TreeNode rnode = dfs(mid + 1, right);
        curr.left = lnode;      
        curr.right = rnode;
        return curr;
    }
    
    private void preOrder(TreeNode root) {
        if (root == null) return;
        preOrder(root.left);
        list.add(root);
        preOrder(root.right);
    }
}
```

T: O(n)			S: O(n)

