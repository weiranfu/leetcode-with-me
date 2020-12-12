---
title: Medium | Largest BST Subtree 333
tags:
  - common
  - tricky
categories:
  - Leetcode
  - BST
date: 2020-07-14 02:09:56
---

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it. Could you figure it out in O(n) ?

[Leetcode](https://leetcode.com/problems/largest-bst-subtree/)

<!--more-->

**Example:**

```
Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
```

**Follow up:** 

[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

---

#### Tricky 

Tree DP

We need to store four info for a node `bst`, `cnt`, `max`, `min`

`bst` means whether `n` and its subtree is a BST.

`cnt` means the number of nodes in `n` and its subtree

`min` & `max` means the max and min value in `n` and its subtree.

```java
class Solution {
    class Pair {
        boolean bst;
        int cnt;
        int max;
        int min;
        Pair(boolean t, int c, int max, int min) {
            bst = t; cnt = c; this.max = max; this.min = min;
        }
    }
    int max = 0;
    public int largestBSTSubtree(TreeNode root) {
        dfs(root);
        return max;
    }
    private Pair dfs(TreeNode n) {
        if (n == null) return new Pair(true, 0, -1, -1);
        Pair left = dfs(n.left);
        Pair right = dfs(n.right);
        if (!left.bst || !right.bst) return new Pair(false, 0, -1, -1);
        if (left.cnt != 0 && left.max >= n.val || right.cnt != 0 && right.min <= n.val) {
            return new Pair(false, 0, -1, -1);
        }
        int cnt = left.cnt + right.cnt + 1;
        max = Math.max(max, cnt);
        int cmin = left.cnt == 0 ? n.val : left.min;
        int cmax = right.cnt == 0 ? n.val : right.max;
        return new Pair(true, cnt, cmax, cmin);
    }
}
```

T: O(n)			S: O(n) call stack

