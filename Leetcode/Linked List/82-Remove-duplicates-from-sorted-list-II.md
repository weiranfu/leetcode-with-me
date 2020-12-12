---
title: Medium | Remove Duplicates from Sorted List II
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-05-18 20:59:42
---

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only *distinct* numbers from the original list.

Return the linked list sorted as well.

[Leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

<!--more-->

**Example 1:**

```
Input: 1->2->3->3->4->4->5
Output: 1->2->5
```

**Example 2:**

```
Input: 1->1->1->2->3
Output: 2->3
```

---

#### Tricky

How to solve this problem in recursion.

* if we need to remove curr node, `return deleteDuplicates(curr.next)`.

* if we need to keep curr node, 

  `curr = deleteDuplicates(curr.next)`   

  `return curr;`

---

#### My thoughts 

```java
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dump;
        ListNode curr = prev.next;
        while (curr != null && curr.next != null) {
            if (curr.val == curr.next.val) {
                int value = curr.val;
                while (curr != null && curr.val == value) {
                    prev.next = curr.next;
                    curr = curr.next;
                }
            } else {
                prev = curr;
                curr = curr.next;
            }
        }
        return dummy.next;
    }
}
```

T: O(n)			S: O(1)

---

#### Recursion

```java
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode curr = head;
        while (curr.next != null && curr.val == curr.next.val) {
            curr = curr.next;
        }
        if (curr != head) {
            return deleteDuplicates(curr.next);
        } else {
            curr.next = deleteDuplicates(curr.next);
            return curr;
        }
    }
}
```

T: O(n)			S: O(n) (stack)