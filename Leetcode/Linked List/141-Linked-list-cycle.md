---
title: Easy | Linked list cycle 141
tags:
  - common
  - corner case
categories:
  - Leetcode
  - Linked List
date: 2019-07-26 15:16:35
---

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where tail connects to. If `pos` is `-1`, then there is no cycle in the linked list.

[Leetcode](https://leetcode.com/problems/linked-list-cycle/)

<!--more-->

**Example 1:**

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Example 2:**

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Example 3:**

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

---

#### Corner Case

Indicate whether `fast` runs into the last item in linked list, using:

`fast == null || fast.next == null` instead of `fast == null`.

Because we moves `fast` pointer two steps everytime.

---

#### My thoughts 

Using two pointers, if there's a cycle in linked list, `fast` must catch up `slow`.

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
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {   // if cycle detected
                return true;
            }
        }
        return false;
    }
}
```

How to get its time complexity?

* If there is no cycle, O(n).

* If there is a cycle, we focus on the `slow` pointer. Before `slow` finish a cycle, `fast` will catch up `slow`, so 

  time complexity is O(n).

---

#### Summary 

Using two pointers to indicate a cycle.