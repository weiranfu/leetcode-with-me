---
title: Medium | Remove Nth Node from End of List
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-05-31 23:53:11
---

Given a linked list, remove the *n*-th node from the end of list and return its head. Could you devise a solution in one pass? (Given *n* will always be valid.)

[Leetcode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

<!--more-->

**Example:**

```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```

---

#### Tricky 

Use two pointers `fast` and `slow`. `fast` pointers is `n` move forward than `slow`. And we move both of them together until end, then we will find the right place to remove the node.

---

#### Standard solution  

```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode();
        dummy.next = head;
        
        ListNode fast = dummy, slow = dummy;
        for (int i = 0; i < n; i++) {
            fast = fast.next;
        }
        
        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }
}
```

T: O(n)		S: O(1)

---

#### Summary 

Use two pointers with n moves to find Nth node from end.