---
title: Hard | Reverse Nodes in K-Group 25
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-06-01 14:40:22
---

Given a linked list, reverse the nodes of a linked list *k* at a time and return its modified list.

*k* is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of *k* then left-out nodes in the end should remain as it is.

[Leetcode](https://leetcode.com/problems/reverse-nodes-in-k-group/)

<!--more-->

**Example:**

Given this linked list: `1->2->3->4->5`

For *k* = 2, you should return: `2->1->4->3->5`

For *k* = 3, you should return: `3->2->1->4->5`

---

#### Tricky 

Reverse K nodes and connect to next K nodes.

---

#### Iteration

```java
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (k == 1) return head;
        ListNode dummy = new ListNode();
        dummy.next = head;
        
        ListNode fast = dummy, slow = dummy;
        while (fast != null) {
            for (int i = 0; i < k && fast != null; i++) {  // find kth nodes
                fast = fast.next;
            }
            if (fast == null) break;
            ListNode tail = reverse(slow, fast.next);  // return tail of k nodes.
            slow = tail;
            fast = tail;     
        }
        return dummy.next;
    }
    
    private ListNode reverse(ListNode begin, ListNode end) {
        ListNode tail = begin.next;       // tail node
        ListNode curr = tail.next;        // first reversed node
        while (curr != end) {
            ListNode next = curr.next;
            curr.next = begin.next;
            begin.next = curr;
            curr = next;
        }
        tail.next = end;                 // don't forget to add link to next k nodes.
        return tail;
    }
}
```

T: O(n)		S: O(1)

---

#### Recursion

```java
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (k == 1) return head;
        ListNode dummy = new ListNode();
        dummy.next = head;
        
        ListNode end = dummy;
        for (int i = 0; i < k && end != null; i++) {
            end = end.next;
        }
        if (end == null) {
            return head;
        }
        ListNode curr = head.next;
        end = end.next;                   // end node
        while (curr != end) {
            ListNode next = curr.next;
            curr.next = dummy.next;
            dummy.next = curr;
            curr = next;
        }
        head.next = reverseKGroup(end, k); // connect to next k nodes.
        return dummy.next;
    }
}
```

T: O(n)		S: O(1)



