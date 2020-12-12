---
title: Medium | Count Univalue Subtrees 250
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-06-24 15:22:18
---

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

[Leetcode](https://leetcode.com/problems/count-univalue-subtrees/)

<!--more-->

**Example :**

```
Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
```

---

#### Tricky

Traverse all nodes and push up (just like push up in segment tree!)

---

#### Recursion

```java
class Solution {
    public int countUnivalSubtrees(TreeNode root) {
        int[] cnt = new int[1];
        isSame(root, cnt);
        return cnt[0];
    }
    
    private boolean isSame(TreeNode n, int[] cnt) {
        if (n == null) {
            return true;
        }
        boolean left = isSame(n.left, cnt);
        boolean right = isSame(n.right, cnt);
        if (left && right) {
            if (n.left != null && n.left.val != n.val) {
                return false;
            }   
            if (n.right != null && n.right.val != n.val) {
                return false;
            }
            cnt[0]++;
            return true;
        }
        return false;
    }
}
```

T: O(n)		S: O(n).  (stack)

---

#### Iteration

We use Stack to control the traversal of nodes.
We use Map to store the achieved results of each node.
If we haven't gotten the result of right node of current node, we will point curr to the right node
Only if we get left result and right result, we can compute the result of current node.

```java
class Solution {
    public int countUnivalSubtrees(TreeNode root) {
        if (root == null) return 0;
        Map<TreeNode, Boolean> map = new HashMap<>();
        map.put(null, true);                           // store null for true as result
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;                          // point to root
        int cnt = 0;
        while (curr != null || !stack.isEmpty()) {
            if (!map.containsKey(curr)) {
                stack.push(curr);
                curr = curr.left;
            } else {
                TreeNode n = stack.peek();
                if (!map.containsKey(n.right)) {
                    curr = n.right;                  // point to right node
                } else {
                    curr = stack.pop();
                    boolean same = true;
                    if (map.get(curr.left) && map.get(curr.right)) {
                        if (curr.left != null && curr.left.val != curr.val) {
                            same = false;
                        }
                        if (curr.right != null && curr.right.val != curr.val) {
                            same = false;
                        }
                    } else {
                        same = false;
                    }
                    if (same) {
                        cnt++;
                        map.put(curr, true);
                    } else {
                        map.put(curr, false);
                    }
                    curr = null;                    // clear curr = null
                }
            }
        }
        return cnt;
    }
}
```

T: O(n)			S: O(n)

---

#### Optimized



---

#### Standard solution  



---

#### Summary 

