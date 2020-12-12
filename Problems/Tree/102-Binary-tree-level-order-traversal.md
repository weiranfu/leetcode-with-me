---
title: Medium | Binary Tree Level Order traversal 102
tags:
  - common
  - implement
  - Oh-shit
categories:
  - Leetcode
  - Tree
date: 2019-10-24 12:57:22
---

Given a binary tree, return the *level order* traversal of its nodes' values. (ie, from left to right, level by level).

[Leetcode](https://leetcode.com/problems/binary-tree-level-order-traversal/)

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

return its level order traversal as:

```
[
  [3],
  [9,20],
  [15,7]
]
```

**Follow up:** How about using DFS to implement level order traversal?

---

#### Implement

When using DFS to implement level order traversal, we can record each traversal's height, and add these nodes into array's index corresponding height.

#### Oh-Shit 

`Queue<> queue = new LinkedList<>()`, because queue is a LinkedList in runtime, and linkedlist is permitted to add a null value. So we should take care of the situation that `root == null` .

---

#### My thoughts 

Using BFS and a queue to store each level's nodes, record the number of each level's node, after processing all nodes in this level, then go to next level.

---

#### First solution 

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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        if (root == null) {
            return result;
        }
        queue.offer(root);
        while (!queue.isEmpty()) {
            int levelNum = queue.size();
            List<Integer> subList = new ArrayList<>();
            for (int i = 0; i < levelNum; i += 1) {
                TreeNode n = queue.poll();
                if (n != null) {
                    subList.add(n.val);
                    if (n.left != null) {
                        queue.offer(n.left);
                    }
                    if (n.right != null) {
                        queue.offer(n.right);
                    }
                }
            }
            result.add(subList);
        }
        return result;
    }
}
```

When adding next level nodes into queue, we should not add null. Because at the leaves of a tree, the next level will all be null, then `result.add(subList)` will add an empty list to `result`. 

---

#### DFS  

Give every node a height attribute to recode its height, and then add it into array at the index corresponding to its height.

Attention, the order of add nodes is first left and then right. 

```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        levelOrderHelper(result, root, 0);
        return result;
    }
    public void levelOrderHelper(List<List<Integer>> result, TreeNode node, int height) {
        if (node == null) {
            return;
        }
        if (height >= result.size()) {
            result.add(new ArrayList<Integer>());
        }
        result.get(height).add(node.val);
        levelOrderHelper(result, node.left, height + 1);
        levelOrderHelper(result, node.right, height + 1);
    }
}
```

---

#### Summary 

BFS, we record the total number of nodes in a level. After processing them all then move to next level.

DFS, we record each node's belonging to which level(height). Then when processing a node, add it to array at index that corresponding to its height.