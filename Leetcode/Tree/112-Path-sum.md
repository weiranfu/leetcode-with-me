---
title: Easy | Path Sum 112
tags:
  - common
categories:
  - Leetcode
  - Tree
date: 2020-01-13 16:23:01
---

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

[Leetcode](https://leetcode.com/problems/path-sum/)

<!--more-->

**Example:**

Given the below binary tree and `sum = 22`,

```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
```

return true, as there exist a root-to-leaf path `5->4->11->2`which sum is 22.

---

#### My thoughts 

Use a Pair class to store the sum along with TreeNode.

---

#### DFS

```java
class Solution {
    class Pair {
        TreeNode n;
        int sum;
        public Pair(TreeNode n, int sum) {
            this.n = n;
            this.sum = sum;
        }
    }
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        Stack<Pair> stack = new Stack<>();
        stack.push(new Pair(root, 0));
        while (!stack.isEmpty()) {
            Pair info = stack.pop();
            TreeNode n = info.n;
            int sum = info.sum;
            sum += n.val;
            if (n.left == null && n.right == null && sum == targetSum) return true;
            if (n.left != null) stack.push(new Pair(n.left, sum));
            if (n.right != null) stack.push(new Pair(n.right, sum));
        }
        return false;
    }
}
```

T: O(n) 				S: O(n)

---

#### Recursion

```java
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) return false;
        if (root.left == null && root.right == null && root.val == sum) return true;
        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }
}
```

T: O(n) 			S: O(n)

---

#### Summary 

Use a Pair class to store sum along with TreeNode.