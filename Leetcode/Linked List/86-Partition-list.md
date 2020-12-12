---
title: Medium | Partition List 86
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-05-19 19:48:10
---

Given a linked list and a value *x*, partition it such that all nodes less than *x* come before nodes greater than or equal to *x*.

You should preserve the original relative order of the nodes in each of the two partitions.

[Leetcode](https://leetcode.com/problems/partition-list/)

<!--more-->

**Example:**

```
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
```

---

#### Tricky 

We could maitain two linked list, one for smaller nodes, one for larger nodes.

---

#### My thoughts 

Maintain a pointer `smaller` to the last node in smaller list and a pointer to the curr node,

check `curr.next` node's value: `curr.next < x`. If we find a smaller node, append this node to `smaller`.

---

#### First solution 

```java
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode dummy = new ListNode(0, head);
        ListNode smaller = dummy;
        ListNode curr = dummy;
        while (curr.next != null) {
            if (curr.next.val < x) {
                if (smaller != curr) {          // move node(curr.next) after node(smaller).
                    ListNode next = curr.next.next;
                    curr.next.next = smaller.next;
                    smaller.next = curr.next;
                    curr.next = next;
                    smaller = smaller.next;     // smaller move next, but curr won't move.
                } else {
                    curr = curr.next;          // curr move next
                    smaller = smaller.next;    // smaller move next
                }
            } else {
                curr = curr.next;
            }
        }
        return dummy.next;
    }
}
```

T: O(n)			S: O(1)

---

#### Optimized

Maitain two linked list for smaller and larger nodes.

```java
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode dummy1 = new ListNode(0);
        ListNode dummy2 = new ListNode(0);
        ListNode smaller = dummy1;
        ListNode larger = dummy2;
        ListNode curr = head;
        while (curr != null) {
            if (curr.val < x) {
                smaller.next = curr;
                smaller = smaller.next;
            } else {
                larger.next = curr;
                larger = larger.next;
            }
            curr = curr.next;
        }
        smaller.next = dummy2.next;  // connect two lists.
        larger.next = null;          // add end to larger lists.
        return dummy1.next;
    }
}
```

T:  O(n)			S: O(1)