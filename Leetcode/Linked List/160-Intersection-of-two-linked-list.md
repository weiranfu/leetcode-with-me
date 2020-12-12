---
title: Easy | Intersection of Two Linked List 160
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-01-10 10:15:46
---

Write a program to find the node at which the intersection of two singly linked lists begins.

[Leetcode](https://leetcode.com/problems/intersection-of-two-linked-lists/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png)



```
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png)



```
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
```

**Notes:**

- If the two linked lists have no intersection at all, return `null`.
- The linked lists must retain their original structure after the function returns.
- You may assume there are no cycles anywhere in the entire linked structure.
- Your code should preferably run in O(n) time and use only O(1) memory.

---

#### Tricky 

The time complexity needs to be O(n), to use only O(1) memory, so we cannot use a map to store the node.

The idea to find the intersection is that we get the size of two linked list, then let they start at a same length, to compare each node.

Mind that get the size is O(n).

---

#### First solution 

Get the size of two linked list, and starts at a same length point to compare each node.

```java
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int sizeA = 0;
        ListNode n = headA;
        while (n != null) {
            sizeA++;
            n = n.next;
        }
        int sizeB = 0;
        n = headB;
        while (n != null) {
            sizeB++;
            n = n.next;
        }
        while (sizeA > sizeB) {
            headA = headA.next;
            sizeA--;
        }
        while (sizeB > sizeA) {
            headB = headB.next;
            sizeB--;
        }
        while (headA != null) {
            if (headA.equals(headB)) {
                return headA;
            }
            headA = headA.next;
            headB = headB.next;
        }
        return null;
    }
}
```

T: O(n)			S: O(1)

---

#### Optimized 

Actually we don't care about the "value" of difference, we just want to make sure two pointers reach the intersection node at the same time.

We can use two iterations to do that. If A pointer reaches the tail of LinkedList A, set it to head of LinkedList B, and if B pointer reaches the tail of LinkedList B, set it to head of LinkedList A.

In the first iteration, we will reset the pointer of one linkedlist to the head of another linkedlist after it reaches the tail node. In the second iteration, we will move two pointers until they points to the same node. Our operations in first iteration will help us counteract the difference. So if two linkedlist intersects, the meeting point in second iteration must be the intersection point. If the two linked lists have no intersection at all, then the meeting pointer in second iteration must be the tail node of both lists, which is null

```java
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode p1 = headA, p2 = headB;
        while (p1 != p2) {
            p1 = p1 == null ? headB : p1.next;
            p2 = p2 == null ? headA : p2.next;
        }
        return p1;
    }
}
```

T: O(n)			S: O(1)

---

#### Summary 

* Get the length of a linked list take O(n)
* We need to starts at a same length point to find the intersection point.