---
title: Medium | Sort List 148
tags:
  - common
categories:
  - Leetcode
  - Sort
date: 2020-01-02 19:17:10
---

Sort a linked list in *O*(*n* log *n*) time using constant space complexity.

[Leetcode](https://leetcode.com/problems/sort-list/)

<!--more-->

**Example 1:**

```
Input: 4->2->1->3
Output: 1->2->3->4
```

**Example 2:**

```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```

---

#### My thoughts 

Use Merge Sort to sort two linked list.

---

#### Recursion 

Use fast/slow pointer to split a linked list into two parts.

```java
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode fast = head, slow = head;
        ListNode prev = slow;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        prev.next = null;
        
        ListNode l1 = sortList(head);
        ListNode l2 = sortList(slow);
        
        return merge(l1, l2);
    }
    
    public ListNode merge(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode p = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                p.next = l1;
                l1 = l1.next;
            } else {
                p.next = l2;
                l2 = l2.next;
            }
            p = p.next;
        }
        if (l1 != null) {
            p.next = l1;
        }
        if (l2 != null) {
            p.next = l2;
        }
        return dummy.next;
    }
}
```

T: O(nlogn)		S: O(logn) (stack)

---

#### Iteration

Iteration implementation of Merge Sort.

The key is that `merge(left, right)` need to return the tail of merged linked list, cause we need it to connect to next merged linked list.

```java
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dummy = new ListNode();
        dummy.next = head;
        
        int len = 0;
        ListNode curr = head;
        while (curr != null) {
            len++;
            curr = curr.next;
        }
        
        for (int step = 1; step < len; step = step * 2) {
            ListNode tail = dummy;
            curr = dummy.next;
            while (curr != null) {
                ListNode left = curr;
                ListNode right = splitByStep(left, step);
                curr = splitByStep(right, step);
                tail = merge(left, right, tail);
            }
        }
        return dummy.next;
    }
    
    /**
	 * Divide the linked list into two lists,
     * while the first list contains first n ndoes
	 * return the second list's head
	 */
    public ListNode splitByStep(ListNode head, int step) {
        if (head == null) return null;
        for (int i = 0; head.next != null && i < step - 1; i++) {
            head = head.next;
        }
        ListNode second = head.next;
        head.next = null;
        return second;
    }
    
    /**
	  * merge the two sorted linked list l1 and l2,
	  * then append the merged sorted linked list to the node head
	  * return the tail of the merged sorted linked list
	 */
    private ListNode merge(ListNode left, ListNode right, ListNode tail) {
        ListNode cur = tail;
        while (left != null && right != null) {
            if (left.val < right.val) {
                cur.next = left;
                left = left.next;
            }
            else {
                cur.next = right;
                right = right.next;
            }
            cur = cur.next;
        }
        
        if (left != null) cur.next = left;
        if (right != null) cur.next = right;
        
        while (cur.next != null) {
            cur = cur.next;
        }
        return cur;
    }
}
```

T: O(nlogn)		S: O(1)

