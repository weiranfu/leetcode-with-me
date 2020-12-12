---
title: Easy | Reverse Linked List 206
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-01-03 20:52:41
---

Reverse a singly linked list.

[Leetcode](https://leetcode.com/problems/reverse-linked-list/)

<!--more-->

**Example:**

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

**Follow up:**

A linked list can be reversed either iteratively or recursively. Could you implement both?

---

#### Tricky 

When we use recursion to reverse a linked list, we could use a pointer `ListNode tmp = head.next` to mark the head of rest of linked list, so after reverse the rest of linked list `reverse(head.next)`, we could use `ListNode tmp` to refer the tail of rest of linked list.

---

#### First solution 

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode curr = head;
        ListNode rest = head.next;
        curr.next = null;
        while (rest != null) {
            ListNode tmp = rest.next;
            rest.next = curr;
            curr = rest;
            rest = tmp;
        }
        return curr;
    }
}
```

T: O(n^2) 		S: O(n) call stack

---

#### Optimized

Use a pointer `ListNode tmp = head.next` to mark the head of rest of linked list.

So after reverse `reverse(head.next)`, we can use `ListNode tmp` to refer the `tail node ` of rest of linked list.

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode tail = head.next;
        ListNode newHead = reverseList(head.next);
        tail.next = head;
        head.next = null;
        return newHead;
    }
}
```

T: O(n)		S: O(n). call stack

---

#### Iterative

Use `ListNode tmp` to record the rest of linked list.

```java
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode newHead = head;
        ListNode rest = head.next;
        newHead.next = null;
        while (rest != null) {
            ListNode tmp = rest.next;
            rest.next = newHead;
            newHead = rest;
            rest = tmp;
        }
        return newHead;
    }
} 
```

T: O(n) 		S: O(n)

---

#### Optimized 

opimize the initial case.

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode newHead = null;
        while (head != null) {
            ListNode tmp = head.next;
            head.next = newHead;
            newHead = head;
            head = tmp;
        }
        return newHead;
    }
}
```

T: O(n) 		S: O(n)

