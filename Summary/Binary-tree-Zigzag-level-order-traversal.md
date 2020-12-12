---
title: Binary Tree Zigzag Level Order Traversal
tags:
  - common
categories:
  - Summary
date: 2020-05-21 02:10:53
---

Given a binary tree, return the *zigzag level order* traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

[Leetcode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

<!--more-->

For example:
Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its zigzag level order traversal as:

```
[
  [3],
  [20,9],
  [15,7]
]
```

---

#### Two Stack

Use two stack to store the current level nodes and next level nodes.

If `currLevel.isEmpty()`, exchange `currLevel` with `nextLevel` stack.

```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Stack<TreeNode> currLevel = new Stack<>();
        Stack<TreeNode> nextLevel = new Stack<>();
        currLevel.push(root);
        boolean leftToRight = true;
        List<Integer> list = new ArrayList<>();
        while (!currLevel.isEmpty()) {
            TreeNode node = currLevel.pop();
            list.add(node.val);
            if (leftToRight) {
                if (node.left != null) nextLevel.push(node.left);
                if (node.right != null) nextLevel.push(node.right);
            } else {
                if (node.right != null) nextLevel.push(node.right);
                if (node.left != null) nextLevel.push(node.left);
            }
            if (currLevel.isEmpty()) {
                res.add(list);
                list = new ArrayList<>();
                leftToRight = !leftToRight;
                Stack<TreeNode> tmp = currLevel;
                currLevel = nextLevel;
                nextLevel = tmp;
            }    
        }
        return res;
    }
}
```

T: O(n)		S: O(n)

---

#### One Deque

Use size to control level traversal with a deque.

When `leftToRight`, we `removeFirst` node from deque, and `addLast` node to deque.

When `rightToLeft`, we `removeLast` node from deque, and `addFirst` node to deque.

```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> deque = new LinkedList<>();
        deque.add(root);
        boolean leftToRight = true;
        while (!deque.isEmpty()) {
            int size = deque.size();
            List<Integer> list = new ArrayList<>();
            while (size-- != 0) {
                if (leftToRight) {
                    TreeNode node = deque.removeFirst();
                    list.add(node.val);
                    if (node.left != null) deque.addLast(node.left);
                    if (node.right != null) deque.addLast(node.right);
                } else {
                    TreeNode node = deque.removeLast();
                    list.add(node.val);
                    if (node.right != null) deque.addFirst(node.right);
                    if (node.left != null) deque.addFirst(node.left);
                }
            }
            leftToRight = !leftToRight;
            res.add(list);
        }
        return res;
    }
}
```

T: O(n)		S: O(n)

---

#### Recursion  

Maintain `level` to indicate at which level current node is during recursion.

Use `res.get(level)` to get current level's list.

If `res.size() >= level`, which means we enters into a new level. So we need create an empty list for it.

```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        zigzag(root, 0, res);
        return res;
    }
    
    private void zigzag(TreeNode node, int level, List<List<Integer>> res) {
        if (node == null) return;
        if (res.size() <= level) {
            List<Integer> newList = new ArrayList<>();
            res.add(newList);
        }
        List<Integer> list = res.get(level);
        if (level % 2 == 0) {
            list.add(node.val);
        } else {
            list.add(0, node.val);
        }
        zigzag(node.left, level + 1, res);
        zigzag(node.right, level + 1, res);
    }
}
```

T: O(n)		S: O(n)



