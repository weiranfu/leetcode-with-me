---
title: Easy | Symmetric Tree 101
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Tree
date: 2019-10-25 11:05:00
---

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

[Leetcode](https://leetcode.com/problems/symmetric-tree/)

<!--more-->

For example, this binary tree `[1,2,2,3,4,4,3]` is symmetric:

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

 

But the following `[1,2,2,null,3,null,3]` is not:

```
    1
   / \
  2   2
   \   \
   3    3
```



**Follow up:**  Bonus points if you could solve it both recursively and iteratively.

---

#### Tricky

Firstly we may think to use BFS to compare nodes in each level.

However, we could track two corresponding nodes in the same time to determine whether they are symmetric.

---

#### My thoughts 

Use BFS to compare nodes in every level.

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
    public boolean isSymmetric(TreeNode root) {
        Queue<TreeNode> fringe = new LinkedList<>();
        fringe.add(root);
        while (!fringe.isEmpty()) {
            int levelOrder = fringe.size();           // get the size of this level.
            List<TreeNode> list = new ArrayList<>();
            for (int i = 0; i < levelOrder; i += 1) {
                TreeNode n = fringe.remove();
                list.add(n);
                if (n != null) {
                    fringe.add(n.left);
                    fringe.add(n.right);
                }
            }
            int first = 0;
            int end = levelOrder;
            while (first < end) {
                TreeNode f = list.get(first);
                TreeNode e = list.get(end - 1);
                if (f == null && e == null) {
                    first += 1;
                    end -= 1;
                    continue;
                }
                if (f == null || e == null) {
                    return false;
                }
                if (f.val != e.val) {
                    return false;
                }
                first += 1;
                end -= 1;
            }
        }
        return true;
    }
}
```

T: O(n) S: O(n)

---

#### Recursion 

Track two corresponding nodes A, B at the same time. A'left node is same as B'right node and A'right node is same as B'left node.

```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        TreeNode left = root;
        TreeNode right = root;
        return isSymmetricHelper(left, right);
    }
    public boolean isSymmetricHelper(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        }
        if (left == null || right == null) {
            return false;
        }
        if (left.val != right.val) {
            return false;
        }
        return isSymmetricHelper(left.left, right.right) && isSymmetricHelper(left.right, right.left);  // left node is symmetric with right node.
    }
}
```

T: O(n) S: O(n)

---

#### Optimization

So we can optimize our first solution. We store two pair nodes in the fringe, and compare them together.

```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        Queue<TreeNode> fringe = new LinkedList<>();
        if (root == null) return true;
        fringe.add(root.left);// add two pair nodes in fringe.
        fringe.add(root.right);
        while (!fringe.isEmpty()) {
            TreeNode left = fringe.remove();
            TreeNode right = fringe.remove();
            if (left == null && right == null) {
                continue;
            }
            if (left == null || right == null) {
                return false;
            }
            if (left.val != right.val) {
                return false;
            }
            fringe.add(left.left);  // add two pair nodes' children in order.
            fringe.add(right.right);
            fringe.add(left.right);
            fringe.add(right.left);
        }
        return true;
    }
}
```

T: O(n) S: O(n)

---

#### Summary 

We can track two corresponding nodes to see a tree is symmetric or not.

