---
title: Medium | Maximum Binary Tree 654
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-09-29 01:34:53
---

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

1. The root is the maximum number in the array.
2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

[Leetcode](https://leetcode.com/problems/maximum-binary-tree/)

<!--more-->

**Example 1:**

```
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
```

**Note:**

1. The size of the given array will be in the range [1,1000].

**Follow up:** 

[Maximum Binary Tree II](https://leetcode.com/problems/maximum-binary-tree-ii/)

---

#### Brute Force

Find the max val in `nums[]`  in range `[l, r]`

```java
class Solution {
    public TreeNode insertIntoMaxTree(TreeNode root, int val) {
        if (val > root.val) {
            TreeNode newRoot = new TreeNode(val);
            newRoot.left = root;
            return newRoot;
        }
        insert(root, val);
        return root;
    }
    private boolean insert(TreeNode root, int val) {
        if (root == null) return false;
        if (root.val < val) return false;
        boolean left = insert(root.left, val);
        boolean right = insert(root.right, val);
        if (!left && !right) {
            TreeNode tmp = root.right;
            root.right = new TreeNode(val);
            root.right.left = tmp;
        }
        return true;
    }
}
```

T: O(n^2)			S: O(n)

---

#### Cartesian Tree

**This is a Cartesian Tree. One interesting property is that if we do an in-order traversal, we'll get back the original array which we used to create it.**

We can keep a monotonic decreasing deque to store TreeNode.

When we meet a node `curr` with `curr.val < deque.peekLast().val`, we append `curr` to the right of node that `deque.peekLast().right = curr` and add it into deque.

When we meet a node `curr` with `curr.val > deque.peekLast().val`, we continually poll out the node and set `curr.left = deque.pollLast()`

```java
class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        Deque<TreeNode> deque = new ArrayDeque<>();
        for (int i = 0; i < nums.length; i++) {
            TreeNode curr = new TreeNode(nums[i]);
            while (!deque.isEmpty() && deque.peekLast().val < curr.val) {
                curr.left = deque.pollLast();
            }
            if (!deque.isEmpty()) {
                deque.peekLast().right = curr; // append to the right
            }
            deque.add(curr);
        }
        return deque.peekFirst();
    }
}
```

T: O(n)			S: O(n)