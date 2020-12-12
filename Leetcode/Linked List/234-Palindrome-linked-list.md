---
title: Easy | Palindrome Linked List 234
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-01-10 16:04:33
---

Given a singly linked list, determine if it is a palindrome. Please do it in O(n) time and O(1) space.

[Leetcode](https://leetcode.com/problems/palindrome-linked-list/)

<!--more-->

**Example 1:**

```
Input: 1->2
Output: false
```

**Example 2:**

```
Input: 1->2->2->1
Output: true
```

---

#### Tricky 

How to do it in O(n) time and O(1) space ? 

Find the mid-point of a linked list —— using fast / slow pointers.

Then reverse the prior half linked list.

Finally compare two half linked list.

---

#### My thoughts 

Use a stack to push in all items of linked list.

Then pop out items to compare with original linked list.

However, this solution will cause extra space. 

---

#### First solution 

```java
class Solution {
    public boolean isPalindrome(ListNode head) {
        Stack<ListNode> stack = new Stack<>();
        ListNode n = head;
        while (n != null) {
            stack.push(n);
            n = n.next;
        }
        n = head;
        while (n != null) {
            ListNode tmp = stack.pop();
            if (tmp.val != n.val) {
                return false;
            }
            n = n.next;
        }
        return true;
    }
}
```

T: O(n) 			S: O(n)

---

#### Reverse half linked list 

```java
class Solution {
    public boolean isPalindrome(ListNode head) {
        int size = 0;
        ListNode n = head;
        while (n != null) {
            size++;
            n = n.next;
        }
        boolean odd = size % 2 == 0 ? false : true;
        size = size / 2;
        n = head;
        ListNode prev = null;
        while (size-- != 0) {       // Reverse half linked list.
            ListNode tmp = n.next;
            n.next = prev;
            prev = n;
            n = tmp;
        }
        if (odd) {
            n = n.next;
        }
        while (n != null) {         // Compare two half linked list.
            if (n.val != prev.val) {
                return false;
            }
            n = n.next;
            prev = prev.next;
        }
        return true;
    }
}
```

T: O(n) 		 	S: O(1)

---

#### Optimized 

Use fast / slow pointers to find the mid point of a linked list.

```java
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;
        ListNode fast = head.next.next;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        ListNode head2 = slow.next;
        if (fast != null && fast.next == null) { // Means length is odd.
            head2 = head2.next;
        }
        slow.next = null;
        ListNode newHead = null;
        while (head != null) {       // Reverse half Linked List.
            ListNode tmp = head.next;
            head.next = newHead;
            newHead = head;
            head = tmp;
        }
        while (newHead != null) {    // Compare two half linked list.
            if (newHead.val != head2.val) {
                return false;
            }
            newHead = newHead.next;
            head2 = head2.next;
        }
        return true;
    }
}
```

T: O(n)				S: O(1)

---

#### Summary 

Use fast / slow pointers to get the mid-point of linked list.