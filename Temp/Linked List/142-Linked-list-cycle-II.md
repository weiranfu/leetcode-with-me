---
title: Medium | 142 Linked list cycle II 142
tags:
  - common
  - corner case
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2019-07-26 15:33:35
---

Given a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where tail connects to. If `pos` is `-1`, then there is no cycle in the linked list.

**Note:** Do not modify the linked list.

[Leetcode](https://leetcode.com/problems/linked-list-cycle-ii/)

<!--more-->

**Example 1:**

```
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Example 2:**

```
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Example 3:**

```
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)



**Follow up:** 

This is a follow up problem of [Linked list cycle](https://aranne.github.io/2019/07/26/141-Linked-list-cycle/#more)

Returns the entry of the cycle.

---

#### Corner Case

In the phase 2, we need to reset `slow` to the `start` position.

so `slow = head`.

Mind that we can **NOT** initialize `fast = head.next`, `slow = head` 

Because `fast` and `slow` should start at their velocity.

So we can initialize them: `fast = head.next.next`, `slow = head.next`

---

#### My thoughts 

In [Find the duplicate number](https://aranne.github.io/2019/07/26/287-Find-the-duplicate-number/#more)

---

#### First solution 

```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {       // find cycle
                fast = head;          // reset find to head
                while (slow != fast) { // find meet point
                    slow = slow.next;
                    fast = fast.next;
                }
                return fast;
            }
        }
        return null;
    }
}
```

T: O(n), S: O(1)

---

#### Summary 

Using two pointers,

First to find the meetpoint in the cycle

Second to find the entry of the cycle.