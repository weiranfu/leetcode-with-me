---
title: Medium | Delete Leaves With a Given Value 1325
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-01-19 12:10:32
---

Given a binary tree `root` and an integer `target`, delete all the **leaf nodes** with value `target`.

Note that once you delete a leaf node with value `target`**,** if it's parent node becomes a leaf node and has the value `target`, it should also be deleted (you need to continue doing that until you can't).

[Leetcode](https://leetcode.com/problems/delete-leaves-with-a-given-value/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2020/01/09/sample_1_1684.png)**

```
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2020/01/09/sample_2_1684.png)**

```
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
```

**Example 3:**

**![img](https://assets.leetcode.com/uploads/2020/01/15/sample_3_1684.png)**

```
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
```

**Example 4:**

```
Input: root = [1,1,1], target = 1
Output: []
```

---

#### Tricky 

The key is that how to remove parent new leaf node if we remove a child leaf.

When we do recursion, we remove all leaves of left node and right node, then we check if parent node becomes a new leaf. If it is, return null, else return root.

When we do iteration, we use a map to store each nodes parent. If we delete a child node, then we need to check its parent is leaf or not. So we need to put parent node's parent(grandparent) into stack.

---

#### My thoughts 

Do it iteratively. 

If a node's child is a target leaf, remove this child. After removing node's left child and right child, check whether the node becomes a new target leaf. If it is, push its parent into stack.

---

#### First solution 

Use a Map to store node's parent.

Use a `dummy` node to represent `root` node's parent.

```java
class Solution {
    public TreeNode removeLeafNodes(TreeNode root, int target) {
        Map<TreeNode, TreeNode> map = new HashMap<>();
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        TreeNode dummy = new TreeNode(-1);
        dummy.left = root;
        map.put(root, dummy);  // root node's parent is a dummy node.
        while(!stack.isEmpty()) {
            TreeNode n = stack.pop();
            if (n.left != null) {
                map.put(n.left, n);
                if (n.left.val == target && n.left.left == null && n.left.right == null) {
                    n.left = null;
                    map.remove(n.left);
                } else {
                    stack.push(n.left);
                }
            }
            if (n.right != null) {
                map.put(n.right, n);
                if (n.right.val == target && n.right.left == null && n.right.right == null) {
                    n.right = null;
                    map.remove(n.right);
                } else {
                    stack.push(n.right);
                }
            }
            if (n.val == target && n.left == null && n.right == null) {
                TreeNode parent = map.get(n);
                stack.push(parent);
            }
        }
        return dummy.left;
    }
}
```

T: O(n) 			S: O(n)

---

#### Standard solution  

Do it recursively.

After removing left child and right child, if node becomes a new leaf, return null, else return node.

```java
class Solution {
    public TreeNode removeLeafNodes(TreeNode root, int target) {
        if (root.left != null) {
            root.left = removeLeafNodes(root.left, target);
        }
        if (root.right != null) {
            root.right = removeLeafNodes(root.right, target);
        }
        if (root.val == target && root.left == null && root.right == null) {
            return null;
        }
        return root;
    }
}
```

T: O(n) 			S: O(n)

---

#### Summary 

When we remove a node's left and right child, we need to check whether it becomes a new leaf.

* Recursion: If it is, return null (remove it).

* Iteration: If it is, push its parent into stack.