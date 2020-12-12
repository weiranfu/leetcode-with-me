---
title: Easy | Merge Two Sorted Lists 21
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2019-11-24 15:34:12
---

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

[Leetcode](https://leetcode.com/problems/merge-two-sorted-lists/)

<!--more-->

**Example:**

```
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

**Follow up**

[Merge K sorted lists](https://aranne.github.io/2019/12/31/23-Merge-K-sorted-lists/#more)

---

#### Tricky 

* When we construct a linked list, we can firstly construct `newList = new ListNode(0)`, then return `newList.next` as result.

* Given a LinkedList, when we want to concatenate a new LinkedList, we just need to change the `curr` pointer to that LinkedList, we don't need to create a new ListNode.

---

#### My thoughts 

Recursion or Iteration

---

#### First solution 

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) {
            return null;
        } else if (l1 == null) {
            return l2;
        } else if (l2 == null) {
            return l1;
        }
        ListNode newList;
        // Construct the newList;
        if (l1.val > l2.val) {
            newList = new ListNode(l2.val);
            l2 = l2.next;
        } else {
            newList = new ListNode(l1.val);
            l1 = l1.next;
        }
        ListNode end = newList;
        while (l1 != null && l2 != null) {
            if (l1.val > l2.val) {
                end.next = new ListNode(l2.val);
                l2 = l2.next;
            } else {
                end.next = new ListNode(l1.val);
                l1 = l1.next;
            }
            end = end.next;
        }
        if (l1 == null && l2 == null) {
        } else if (l1 == null) {
            end.next = l2;
        } else if (l2 == null) {
            end.next = l1;
        }
        return newList;
    }
}
```

T: O(n), S: O(n)

---

#### Optimized 

```java
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        } else if (l2 == null) {
            return l1;
        }
        ListNode newList = new ListNode(0);  // Construct newList use 0.
        ListNode curr = newList;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                curr.next = l1;     // Don't need to new a ListNode.
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        // Control curr.next;
        if (l1 == null) {
            curr.next = l2;
        } else if (l2 == null) {
            curr.next = l1;
        }
        return newList.next;   // return newList.next
    }
}
```

T: O(n), S: O(n)

---

#### Recursion 

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

T: O(n), S: O(n)

---

#### Summary 

Use `newList = new ListNode(0)` to begin construction of a linked list.