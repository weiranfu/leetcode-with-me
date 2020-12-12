---
title: Medium | Binary Tree Longest Consecutive Sequence 298
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-01-13 17:47:29
---

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

[Leetcode](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/)

<!--more-->

**Example 1:**

```
Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
```

**Example 2:**

```
Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
```

---

#### Tricky 

The key is to store current longth along with node. 

* We can use a pair class to combine TreeNode and longth together. 
* Or we can use recursion to store longth with TreeNode (Because of call stack)

How to compute the max longth?

During DFS, we compare every longth with max[0] to get the max longth.

---

#### My thoughts 

Use a Pair class to store every TreeNode along with current longth.

```java
class Solution {
    class Pair {
        TreeNode n;
        int longth;
        public Pair(TreeNode n, int longth) {
            this.n = n;
            this.longth = longth;
        }
    }
    public int longestConsecutive(TreeNode root) {
        if (root == null) return 0;
        Stack<Pair> stack = new Stack<>();
        stack.push(new Pair(root, 1));
        int max = 0;
        while (!stack.isEmpty()) {
            Pair info = stack.pop();
            TreeNode n = info.n;
            int longth = info.longth;
            max = Math.max(max, longth);
            if (n.left != null) {
                if (n.left.val - n.val == 1) {
                    stack.push(new Pair(n.left, longth + 1));
                } else {
                    stack.push(new Pair(n.left, 1));
                }
            }
            if (n.right != null) {
                if (n.right.val - n.val == 1) {
                    stack.push(new Pair(n.right, longth + 1));
                } else {
                    stack.push(new Pair(n.right, 1));
                }
            }
        }
        return max;
    }
}
```

T: O(n) 			S: O(n)

---

#### Recursion  

Recursion is kind of stack, so we can store some useful infomation during recursion.

We store current longth, and compare it with max longth.

```java
class Solution {
    public int longestConsecutive(TreeNode root) {
        int[] max = new int[1];
        findMaxLongth(root, 1, max);
        return max[0];
    }
    private void findMaxLongth(TreeNode n, int longth, int[] max) {
        if (n == null) return;
        max[0] = Math.max(max[0], longth);
        if (n.left != null) {
            if (n.left.val - n.val == 1) {
                findMaxLongth(n.left, longth + 1, max);
            } else {
                findMaxLongth(n.left, 1, max);
            }
        }
        if (n.right != null) {
            if (n.right.val - n.val == 1) {
                findMaxLongth(n.right, longth + 1, max);
            } else {
                findMaxLongth(n.right, 1, max);
            }
        }
    }
}
```

T: O(n) 			S: O(n) Because of call stack.

---

#### Summary 

Recursion is kind of stack, so we can store some useful infomation during recursion.