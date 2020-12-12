---
title: Medium | Kth Smallest Element in a BST 230
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-06-22 22:13:56
---

Given a binary search tree, write a function `kthSmallest` to find the **k**th smallest element in it.

[Leetcode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

<!--more-->

**Example 1:**

```
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```

**Example 2:**

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```

**Follow up:**  

What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

**We could use a `sum` field in BST to record how many nodes there are under this node.**

So we could perform `kthSmallest()` in O(logn) time.

Just like the Weighted Segment Tree.

---

#### Tricky 

* Recursion: use a `cnt` to count the number of smallest element.
* Iteration: Inorder traversal

---

#### Recursion

```java
class Solution {
    int cnt = 0;
    
    public int kthSmallest(TreeNode root, int k) {
        return kthSmallestHelper(root, k);
    }
    
    private int kthSmallestHelper(TreeNode n, int k) {
        if (n == null) return Integer.MAX_VALUE;
        
        int left = kthSmallestHelper(n.left, k);
        if (left != Integer.MAX_VALUE) {
            return left;
        }
        cnt++;
        if (cnt == k) {
            return n.val;
        }
        return kthSmallestHelper(n.right, k);
    }
}
```

T: O(n)			S: O(n)			(stack)

---

#### Iteration

```java
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        int cnt = 0;
        while (curr != null || !stack.isEmpty()) {
            if (curr != null) {
                stack.push(curr);
                curr = curr.left;
            } else {
                curr = stack.pop();
                cnt++;
                if (cnt == k) {
                    return curr.val;
                }
                curr = curr.right;
            }
        }
        return -1;
    }
}
```

T: O(n)			S: O(n)

---

#### Follow up

Add a `sum` field in BST to record the number of nodes under this root.

```java
class Solution {
    class Node {
        int val;
        int sum;
        Node left;
        Node right;
        public Node(int val) {
            this.val = val;
        }
    }
    Node rootNode;
    
    public int kthSmallest(TreeNode root, int k) {
        rootNode = build(root);
        return findKthSmallest(rootNode, k);
    }
    
    public Node build(TreeNode n) {
        if (n == null) return null;
        Node root = new Node(n.val);
        root.left = build(n.left);
        root.right = build(n.right);
        int left = (root.left == null) ? 0 : root.left.sum;
        int right = (root.right == null) ? 0 : root.right.sum;
        root.sum = 1 + left + right;
        return root;
    }
    
    public int findKthSmallest(Node n, int k) {
        if (n == null || n.sum < k) return -1;
        
        int left = (n.left != null) ? n.left.sum : 0;
        if (left >= k) {
            return findKthSmallest(n.left, k);
        }
        if (left == k - 1) {
            return n.val;
        }
        return findKthSmallest(n.right, k - 1 - left);
    }    
}
```

T: O(h)			h: height of Tree

---

#### Standard solution  



---

#### Summary 

