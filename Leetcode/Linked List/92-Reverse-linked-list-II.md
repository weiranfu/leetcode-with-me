---
title: Medium | Reverse Linked List II
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-05-20 00:42:55
---

Reverse a linked list from position *m* to *n*. Do it in one-pass.

**Note:** 1 ≤ *m* ≤ *n* ≤ length of list.

[Leetcode](https://leetcode.com/problems/reverse-linked-list-ii/)

<!--more-->

**Example:**

```
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
```

---

#### Tricky 

To append a node after a node, we need to stops before the reverse node.

```java
while (reverse.next != null && num != 1) { // append node(reverse.next) to node(curr).
  ListNode next = reverse.next.next;
  reverse.next.next = prev.next;
  prev.next = reverse.next;
  reverse.next = next;
  num--;
 }
```

---

#### First solution 

```java
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        int num = n - m + 1;
        if (head == null || num <= 1) return head;
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        for (int i = 0; i < m - 1; i++) {   // stops prior to reverse pos.
            prev = prev.next;
        }
        ListNode reverse = prev.next;
        while (reverse.next != null && num != 1) { // append node(reverse.next) to node(curr).
            ListNode next = reverse.next.next;
            reverse.next.next = prev.next;
            prev.next = reverse.next;
            reverse.next = next;
            num--;
        }
        return dummy.next;
    }
}
```

T: O(n)		S: O(1)



