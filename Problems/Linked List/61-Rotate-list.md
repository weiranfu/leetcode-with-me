---
title: Medium | Rotate List 61
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-05-13 22:23:49
---

Given a linked list, rotate the list to the right by *k* places, where *k* is non-negative.

[Leetcode](https://leetcode.com/problems/rotate-list/)

<!--more-->

**Example 1:**

```
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
```

**Example 2:**

```
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
```

---

#### Tricky 

We could form a cycle. Connect the tail to head. And cut off at proper position.

```java
1->2->3->4->5->NULL,  k = 2
1. connect tail to head
  1->2->3->4->5->1->
2. cut off at 3
  1->2->3->NULL
  new head is starting from 4
  4->5->1->2->3->NULL
```

---

#### Standard

```java
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || k == 0) return head;
        int len = 1;               
        ListNode tail = head;
        while (tail.next != null) {  // len starting from 1
            len++;
            tail = tail.next;
        }
        k = k % len;
        
        tail.next = head;    // form a cycle
        for (int i = 0; i < len - k; i++) {
            tail = tail.next;
        }
        head = tail.next;    // new head
        tail.next = null;    // cut off the list.
        return head;
    }
}
```

T: O(n)		S: O(1)

---

#### Summary 

In tricky.