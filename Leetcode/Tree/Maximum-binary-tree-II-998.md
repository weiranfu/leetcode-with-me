---
title: Medium | Maximum Binary Tree II 998
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-09-29 03:06:02
---

We are given the `root` node of a *maximum tree:* a tree where every node has a value greater than any other value in its subtree.

Just as in the [previous problem](https://leetcode.com/problems/maximum-binary-tree/), the given tree was constructed from an list `A` (`root = Construct(A)`) recursively with the following `Construct(A)` routine:

- If `A` is empty, return `null`.
- Otherwise, let `A[i]` be the largest element of `A`.  Create a `root` node with value `A[i]`.
- The left child of `root` will be `Construct([A[0], A[1], ..., A[i-1]])`
- The right child of `root` will be `Construct([A[i+1], A[i+2], ..., A[A.length - 1]])`
- Return `root`.

Note that we were not given A directly, only a root node `root = Construct(A)`.

Suppose `B` is a copy of `A` with the value `val` appended to it.  It is guaranteed that `B` has unique values.

Return `Construct(B)`.

[Leetcode](https://leetcode.com/problems/maximum-binary-tree-ii/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-1-1.png)![img](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-1-2.png)**

```
Input: root = [4,1,3,null,null,2], val = 5
Output: [5,4,null,1,3,null,null,2]
Explanation: A = [1,4,2,3], B = [1,4,2,3,5]
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-2-1.png)![img](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-2-2.png)**

```
Input: root = [5,2,4,null,1], val = 3
Output: [5,2,4,null,1,null,3]
Explanation: A = [2,1,5,4], B = [2,1,5,4,3]
```

**Example 3:**

**![img](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-3-1.png)![img](https://assets.leetcode.com/uploads/2019/02/21/maximum-binary-tree-3-2.png)**

```
Input: root = [5,2,3,null,1], val = 4
Output: [5,2,4,null,1,3]
Explanation: A = [2,1,5,3], B = [2,1,5,3,4]
```

**Constraints:**

- `1 <= B.length <= 100`

---

#### Recursion 

The new `val` can only be inserted into the right part of the Max Tree (as known as [Cartesian Tree](https://en.wikipedia.org/wiki/Cartesian_tree)) since the new val is the last item in the `nums[]` array.

```java
class Solution {
    public TreeNode insertIntoMaxTree(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);
        if (root.val < val) {
            TreeNode newRoot = new TreeNode(val);
            newRoot.left = root;
            return newRoot;
        }
        root.right = insertIntoMaxTree(root.right, val);
        return root;
    }
}
```

T: O(n)		S: O(n)

---

#### Iterative

```java
class Solution {
    public TreeNode insertIntoMaxTree(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);
        TreeNode dummy = new TreeNode();
        dummy.right = root;
        TreeNode curr = dummy;
        while (curr.right != null && curr.right.val > val) {
            curr = curr.right;
        }
        TreeNode tmp = curr.right;
        curr.right = new TreeNode(val);
        curr.right.left = tmp;
        return dummy.right;
    }
}
```

T: O(n)			S: O(1)