---
title: Linked List Manipulation
tags:
  - common
  - tricky
categories:
  - Summary
date: 2020-05-28 22:58:15
---

Some manipulations on Linked List.



<!--more-->

#### 1. Find a Middle Node

Let's use two pointers, `slow` and `fast`. While the slow pointer moves one step forward `slow = slow.next`, the fast pointer moves two steps forward `fast = fast.next.next`, *i.e.* `fast` traverses twice as fast as `slow`. When the fast pointer reaches the end of the list, the slow pointer should be in the middle.

![append](https://leetcode.com/problems/reorder-list/Figures/143/slow_fast.png)

```java
// find the middle of linked list [Problem 876]
// in 1->2->3->4->5->6 find 4 
ListNode slow = head, fast = head;
ListNode prev = slow;    // use to track the prev node before slow pointer.
while (fast != null && fast.next != null) {
  prev = slow;
  slow = slow.next;
  fast = fast.next.next;
}
// middle node is at slow pointer pos.
// if we want to cut linked in half
ListNode secondHead = slow;
prev.next = null;
```

Recursive solution:

```java
class Solution {
    public ListNode middleNode(ListNode head) {
        int len = 0;
        ListNode curr = head;
        while (curr != null) {
            len++;
            curr = curr.next;
        }
        return middle(head, len);
    }
    
    private ListNode middle(ListNode head, int len) {
        if (len == 0) return null;
        if (len == 1) return head;
        if (len == 2) return head.next;
        return middle(head.next, len - 2);
    }
}
```

---

#### 2. Reverse a linked list

For each current node, save its neighbours: the previous node `prev` and the next node `tmp = curr.next`.

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
return prev;
// Reverse linked list's head is at prev pointer pos.
```

Recursive solution

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) return null;
        if (head.next == null) return head;
        ListNode tail = head.next;
        ListNode newHead = reverseList(head.next);
        tail.next = head;
        head.next = null;
        return newHead;
    }
}
```

---

#### 3. Merge two linked list one by one

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

#### Merge two linked list

```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode();
        ListNode curr = dummy;
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                curr.next = list1;
                list1 = list1.next;
            } else {
                curr.next = list2;
                list2 = list2.next;
            }
            curr = curr.next;
        }
        if (list1 != null) {
            curr.next = list1;
        }
        if (list2 != null) {
            curr.next = list2;
        }
        return dummy.next;
    }
}
```

Recursive:

```java
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }
        if (l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        }
        l2.next = mergeTwoLists(l1, l2.next);
        return l2;
    }
}
```

---

#### Find Nth node from end of list

We could use two pointers `slow` and `fast`. `fast` pointer is `n` moves forward than `slow` pointer. 

We move both pointers together until `fast` reach the end of list. Then `slow` pointer is at `nth` node from end of list.

```java
ListNode fast = dummy, slow = dummy;
for (int i = 0; i < n + 1; i++) {
  fast = fast.next;
}
while (fast != null) {
  fast = fast.next;
  slow = slow.next;
}
// slow pointer is at nth node from end of list.
```

