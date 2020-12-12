---
title: Medium | Path Sum II 113
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-01-13 17:05:23
---

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

[Leetcode](https://leetcode.com/problems/path-sum-ii/)

<!--more-->

**Example:**

Given the below binary tree and `sum = 22`,

```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
```

Return:

```
[
   [5,4,11,2],
   [5,8,4,5]
]
```

---

#### Tricky 

1. When we use recursion method, we visited a node, and add it into path.

   After we finishing DFS this node, we need to remove this node from path.

   `path.add(node.val);`

   `path.remove(path.size() - 1);`

2. When we add a path into result path list, we need to copy this path rather than just referring it.

   `res.add(new LinkedList<>(path));`

---

#### My thoughts 

Use a Pair class to store path and sum along with each node during DFS.

---

#### First solution 

```java
class Solution {
    class Pair {
        TreeNode n;
        List<Integer> list;
        int sum;
        public Pair(TreeNode n, List<Integer> list, int sum) {
            this.n = n;
            this.list = list;
            this.sum = sum;
        }
    }
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Stack<Pair> stack = new Stack<>();
        stack.push(new Pair(root, new ArrayList<>(), 0));
        while (!stack.isEmpty()) {
            Pair info = stack.pop();
            TreeNode n = info.n;
            List<Integer> list = info.list;
            int sum = info.sum;
            list.add(n.val);
            sum += n.val;
            if (n.left == null && n.right == null && sum == targetSum) {
                res.add(list);
            }
            if (n.left != null) {
                stack.push(new Pair(n.left, new ArrayList<>(list), sum));
            }
            if (n.right != null) {
                stack.push(new Pair(n.right, new ArrayList<>(list), sum));
            }
        }
        return res;
    }
}
```

T: O(n) 			S: O(n)

---

#### Recursion 

```java
class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        if (root.left == null && root.right == null && root.val == sum) {
            List<Integer> list = new ArrayList<>();
            list.add(root.val);
            res.add(list);
            return res;
        }
        List<List<Integer>> left = pathSum(root.left, sum - root.val);
        List<List<Integer>> right = pathSum(root.right, sum - root.val);
        for (List<Integer> list : left) {
            list.add(0, root.val);
            res.add(list);
        }
        for (List<Integer> list : right) {
            list.add(0, root.val);
            res.add(list);
        }
        return res;
    }
}
```

T: O(n) 			S: O(n)

---

#### Recusion with Path 

We use a path nodes during recursion.

We need to remove the node after finishing DFS on that node.

```java
class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> path = new LinkedList<>();
        pathFind(root, sum, path, res);
        return res;
    }
    private void pathFind(TreeNode node, int sum, List<Integer> path, List<List<Integer>> res) {
        if (node == null) return;
        path.add(node.val);
        if (node.left == null && node.right == null && node.val == sum) {
            res.add(new LinkedList<>(path));
        }
        pathFind(node.left, sum - node.val, path, res);
        pathFind(node.right, sum - node.val, path, res);
        path.remove(path.size() - 1);
    }
}
```

T: O(n)			S: O(n)

---

#### Summary 

* Use a pair class to store path along with node.

* Use a `List<Integer> path` to track path during DFS. 

  Mind that this path is dynamical, it will change during DFS. After we finishing visiting a node, we need to  delete that node from path.