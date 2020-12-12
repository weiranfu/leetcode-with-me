---
title: Medium | Convert Sorted List to Binary Search Tree 109
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-05-22 23:49:43
---

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of *every*node never differ by more than 1.

[Leetcode](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

<!--more-->

**Example:**

```
Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```

---

#### Tricky 

* The key is to using recursion to store the boundary of integers used in linked list when building BST.

  `mid = start + (end - start) / 2`. The root is `TreeNode(mid)`, the integers in `[start, mid]` are in the left subtree, the integers in `[mid, end]` are in the right subtree.

* When we want to find the mid node of a linked list, we could use fast/slow pointers approach.

---

#### First solution 

```java
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
        ListNode curr = head;
        int len = 0;
        while (curr != null) {
            len++;
            curr = curr.next;
        }
        return buildTree(head, 0, len);
    }
    
    private TreeNode buildTree(ListNode head, int start, int end) {
        if (start >= end) return null;
        if (end - start == 1) {
            return new TreeNode(head.val);
        }
        int mid = start + (end - start) / 2;
        ListNode curr = head;
        for (int i = start; i < mid - 1; i++) {
            curr = curr.next;
        }
        TreeNode node = new TreeNode(curr.next.val);
        ListNode newHead = curr.next.next;
        curr.next = null;
        node.left = buildTree(head, start, mid);
        node.right = buildTree(newHead, mid + 1, end);
        return node;
    }
}
```

T: O(n^2)		S: O(n)

---

#### Optimized: two pointers

Use fast/slow pointers to find the mid node of linked list.

```java
class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
        return buildTree(head, null);
    }
    
    private TreeNode buildTree(ListNode head, ListNode tail) {
        if (head == tail) return null;
        ListNode slow = head;
        ListNode fast = head;
        while (fast != tail && fast.next != tail) {
            slow = slow.next;
            fast = fast.next.next;
        }
        TreeNode root = new TreeNode(slow.val);
        root.left = buildTree(head, slow);
        root.right = buildTree(slow.next, tail);
        return root;
    }
}
```

T: O(n^2)		S: O(n)

