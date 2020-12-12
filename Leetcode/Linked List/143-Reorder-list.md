---
title: Medium | Reorder List 143
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-05-28 22:53:09
---

Given a singly linked list *L*: *L*0→*L*1→…→*Ln-1*→*Ln*,
reorder it to: *L*0→*Ln*→*L*1→*Ln-1*→*L*2→*Ln-2*→…

You may **not** modify the values in the list's nodes, only nodes itself may be changed.

[Leetcode](https://leetcode.com/problems/reorder-list/)

<!--more-->

**Example 1:**

```
Given 1->2->3->4, reorder it to 1->4->2->3.
```

**Example 2:**

```
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```

---

#### Tricky 

This problem is a combination of these three easy problems:

- [Middle of the Linked List](https://leetcode.com/articles/middle-of-the-linked-list/).
- [Reverse Linked List](https://leetcode.com/articles/reverse-linked-list/).
- [Merge Two Sorted Lists](https://leetcode.com/articles/merged-two-sorted-lists/).

**Find a Middle Node**

Let's use two pointers, `slow` and `fast`. While the slow pointer moves one step forward `slow = slow.next`, the fast pointer moves two steps forward `fast = fast.next.next`, *i.e.* `fast` traverses twice as fast as `slow`. When the fast pointer reaches the end of the list, the slow pointer should be in the middle.

![append](https://leetcode.com/problems/reorder-list/Figures/143/slow_fast.png)

```java
// find the middle of linked list [Problem 876]
// in 1->2->3->4->5->6 find 4 
ListNode slow = head, fast = head;
while (fast != null && fast.next != null) {
  slow = slow.next;
  fast = fast.next.next;
}
```

**Reverse the Second Part of the List**

Let's traverse the list starting from the middle node `slow` and its virtual predecessor `None`. For each current node, save its neighbours: the previous node `prev` and the next node `tmp = curr.next`.

While you're moving along the list, change the node's next pointer to point to the previous node: `curr.next = prev`, and shift the current node to the right for the next iteration: `prev = curr`, `curr = tmp`.

![append](https://leetcode.com/problems/reorder-list/Figures/143/reverse2.png)

```java
// reverse the second part of the list [Problem 206]
// convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
// reverse the second half in-place
ListNode prev = null, curr = slow, tmp;
while (curr != null) {
  tmp = curr.next;

  curr.next = prev;
  prev = curr;
  curr = tmp;
}
```

**Merge Two Sorted Lists**

This algorithm is similar to the one for list reversal.

Let's pick the first node of each list - first and second, and save their successors. While you're traversing the list, set the first node's next pointer to point to the second node, and the second node's next pointer to point to the successor of the first node. For this iteration the job is done, and for the next iteration move to the previously saved nodes' successors.

![append](https://leetcode.com/problems/reorder-list/Figures/143/first_second.png)

```java
// merge two sorted linked lists [Problem 21]
// merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
ListNode first = head, second = prev;
while (second.next != null) {
  tmp = first.next;
  first.next = second;
  first = tmp;

  tmp = second.next;
  second.next = first;
  second = tmp;
}
```

---

#### Standard solution  

```java
class Solution {
  public void reorderList(ListNode head) {
    if (head == null) return;

    // find the middle of linked list [Problem 876]
    // in 1->2->3->4->5->6 find 4 
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;
    }

    // reverse the second part of the list [Problem 206]
    // convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
    // reverse the second half in-place
    ListNode prev = null, curr = slow, tmp;
    while (curr != null) {
      tmp = curr.next;

      curr.next = prev;
      prev = curr;
      curr = tmp;
    }

    // merge two sorted linked lists [Problem 21]
    // merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
    ListNode first = head, second = prev;
    while (second.next != null) {
      tmp = first.next;
      first.next = second;
      first = tmp;

      tmp = second.next;
      second.next = first;
      second = tmp;
    }
  }
}
```

T: O(n)		S: O(1)

---

#### Recusion

Given a example, 1->2->3->4->5, the solution will reorder node(3), then reorder 2 and 4 to have (2->4->3), then 1 and 5 get have 1->5->2->4->3. Each call of reorderList(ListNode* head, int len) will return the last element after this reorderList() call.

The key of recusion solution is how to determine our recursion is at the middle of linked list.

**Here we use `len` to control recursion. if `len == 1 || len == 2`, which means we are at the middle of linked list.****

```java
class Solution {
    public void reorderList(ListNode head) {
        int len = 0;
        ListNode curr = head;
        while (curr != null) {
            curr = curr.next;
            len++;
        }
        reorderWithTail(head, len);
    }
    
    public ListNode reorderWithTail(ListNode head, int len) {
        if (len == 0) {
            return null;
        } else if (len == 1) {
            return head;
        } else if (len == 2) {
            return head.next;
        }
        ListNode tail = reorderWithTail(head.next, len - 2);
        ListNode reorder = tail.next;
        tail.next = tail.next.next;      // tail.next is connect to next one.
        reorder.next = head.next;
        head.next = reorder;
        return tail;           // return tail of [len] list
    }
}
```

T: O(n)		S: O(n) (stack)

