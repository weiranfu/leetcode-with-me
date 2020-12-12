---
title: Medium | Insertion Sort List 147
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-05-29 01:48:52
---

Sort a linked list using insertion sort.

![img](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

**Algorithm of Insertion Sort:**

1. Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
3. It repeats until no input elements remain.

[Leetcode](https://leetcode.com/problems/insertion-sort-list/)

<!--more-->

**Example:**

```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

---

#### Tricky 

As linked list node only has reference to its next node, so we need to find right position to insert node from the beginning of list.

---

#### Standard solution  

```java
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode curr = head;
        ListNode next, p;
        while (curr != null && curr.next != null) { // insert node is curr.next
            if (curr.val <= curr.next.val) { // insert node val >= last node val in sorted list
                curr = curr.next;
            } else {
                p = dummy;         // rewind p
                while (p.next != curr && p.next.val <= curr.next.val) { // find insert position
                    p = p.next;
                }
                ListNode inserted = curr.next;
                curr.next = inserted.next;
                inserted.next = p.next;
                p.next = inserted;
            }
        }
        return dummy.next;
    }
}
```

T: O(n^2)		S: O(1)

---

#### Recursion

```java
class Solution {
    public ListNode insertionSortList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode sorted = insertionSortList(head.next);    // sorted head.
        ListNode dummy = new ListNode();
        dummy.next = sorted;
        ListNode curr = dummy;
        while (curr != null && curr.next != null && curr.next.val < head.val) {
            curr = curr.next;
        }
        ListNode tmp = curr.next;
        curr.next = head;
        head.next = tmp;
        return dummy.next;
    }
}
```

T: O(n^2)			S: O(n)