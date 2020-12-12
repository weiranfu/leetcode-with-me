---
title: Medium | Populating Next Right Pointers in Each Node 116
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-01-03 19:42:40
---

You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

[Leetcode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

<!--more--> 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/02/14/116_sample.png)

```
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

**Constraints:**

- The number of nodes in the given tree is less than `4096`.
- `-1000 <= node.val <= 1000`

**Follow up:**

- You may only use constant extra space.
- Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

---

#### Tricky 

We need to connect `left` and `right` child, and connect `right` child with `next node's left` child.

`curr.right.next = curr.next.left`.

---

#### My thoughts 

Use Level Order traversal to connect all nodes.

---

#### First solution 

```java
class Solution {
    public Node connect(Node root) {
        if (root == null) return root;
        root.next = null;
        Queue<Node> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            Node prev = null;
            for (int i = 0; i < size; i++) {
                Node n = queue.poll();
                n.next = prev;
                prev = n;
                if (n.right != null) queue.offer(n.right);
                if (n.left != null) queue.offer(n.left);
            }
        }
        return root;
    }
}
```

T : O(n) 		S: O(n)

---

#### Optimized 

We use a Queue to store nodes. How can we achieve constant space complexity?

Because this is a **perfect binary tree** which means each non-leaf node will have two children, so we could focus on the first node of each level.

Then connect nodes from left to right.

```java
class Solution {
    public Node connect(Node root) {
        if (root == null || root.left == null) return root;
        Node first = root;
        while (first.left != null) {
            Node curr = first;
            while (curr != null) {
                curr.left.next = curr.right;
                if (curr.next != null) {
                    curr.right.next = curr.next.left;
                }
                curr = curr.next;
            }
            first = first.left;
        }
        return root;
    }
}
```

T: O(n)		S: O(1)

---

#### Recursion Version

We could do this in recursion.

```java
class Solution {
    public Node connect(Node root) {
        if (root == null || root.left == null) return root;
        root.left.next = root.right;
        if (root.next != null) {
            root.right.next = root.next.left;
        }
        connect(root.left);
        connect(root.right);
        return root;
    }
}
```

T: O(n)		S: O(1)

---

#### Summary 

Perfect binary tree means each non-leaf node will have two children.