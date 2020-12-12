---
title: Easy | Remove Duplicates from Sorted List
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-05-18 21:26:50
---

Given a sorted linked list, delete all duplicates such that each element appear only *once*.

[Leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

<!--more-->

**Example 1:**

```
Input: 1->1->2
Output: 1->2
```

**Example 2:**

```
Input: 1->1->2->3->3
Output: 1->2->3
```

**Follow up:** [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

---

#### Tricky 

Linked List deletion.

---

#### First solution 

```java
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return head;
        ListNode curr = head;
        while (curr != null && curr.next != null) {
            if (curr.val == curr.next.val) {
                ListNode tmp = curr.next;
                while (tmp != null && curr.val == tmp.val) {
                    tmp = tmp.next;
                }
                curr.next = tmp;
            } else {
                curr = curr.next;
            }
        }
        return head;
    }
}
```

T: O(n)			S: O(1)

---

#### Optimized

```java
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return head;
        ListNode curr = head;
        while (curr.next != null) {
            if (curr.val == curr.next.val) {
                curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }
        return head;
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
        ListNode tmp = head.next;
        while (tmp != null && head.val == tmp.val) {
            tmp = tmp.next;
        }
        head.next = deleteDuplicates(tmp);
        return head;
    }
}
```

T: O(n)			S: O(n)