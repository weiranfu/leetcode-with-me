---
title: Medium | Populating Next Right Pointers in Each Node II
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-05-24 19:41:11
---

Given a binary tree

```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`. Initially, all next pointers are set to `NULL`.

[Leetcode]()

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2019/02/15/117_sample.png)

```
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
```

**Follow up:** 

- You may only use constant extra space.
- Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

---

#### Tricky 

The tree is not complete binary tree! So the key is to find the next level's head.

We could use `curr` node to traverse current level and use a `dummy` node to point to next level's children and connect them if we find `not-null` child.

How to get the next level's head? `head = dummy.next`.

---

#### Stack

This solution is intuitive, but it requires O(n) space!

```java
class Solution {
    public Node connect(Node root) {
        if (root == null) return null;
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            Node prev = null;
            while (size-- != 0) {
                Node curr = queue.poll();
                curr.next = prev;
                if (curr.right != null) queue.add(curr.right);
                if (curr.left != null) queue.add(curr.left);
                prev = curr;
            }
        }
        return root;
    }
}
```

T: O(n)		S: O(n)

---

#### Iteration

```java
class Solution {
    public Node connect(Node root) {
        if (root == null) return null;
        Node head = root;
        Node dummy = new Node(0);
        while (head != null) {          // for each level, points to its head
            Node curr = head;
            Node p = dummy;             // points to next level's child
            while (curr != null) {      // traverse this level.
                if (curr.left != null) {
                    p.next = curr.left;
                    p = p.next;
                }
                if (curr.right != null) {
                    p.next = curr.right;
                    p = p.next;
                }
                curr = curr.next;
            }
            head = dummy.next;      // get next level head
            dummy.next = null;
        }
        return root;
    }
}
```

T: O(N)			S: O(1)

---

#### Recursion  

**The most tricky part using recursion is that we need to connect right subtree before left subtree!**

Because when the middle nodes are missing, we need to get the `next` information in the right subtree.

```java
class Solution {
    public Node connect(Node root) {
        if (root == null) return null;
        if (root.left != null) {
            if (root.right != null) {
                root.left.next = root.right;
            } else {
                root.left.next = findNext(root.next);
            }
        }
        if (root.right != null) {
            root.right.next = findNext(root.next);
        }
        connect(root.right);    // must prior to connect(root.left)
        connect(root.left);
        return root;
    }
    
    private Node findNext(Node node) {    // find the first non-empty child node.
        if (node == null) return null;
        else if (node.left != null) return node.left;
        else if (node.right != null) return node.right;
        return findNext(node.next);
    }
}
```

T: O(n)		S: O(n)

---

#### Summary 

How to get next level's head is the key to this problem.