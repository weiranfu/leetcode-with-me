---
title: Medium | Add Two Numbers 2
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2019-12-02 13:45:51
---

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

[Leetcode](https://leetcode.com/problems/add-two-numbers/)

<!--more-->

**Example:**

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

---

#### Tricky 

When there're a lot of if-else statements in a same mode, we can use `int sum = (l1 == null? 0 : l1.val) + (l2 == null ? 0 : l2.val) + carry;`  instead.

---

#### My thoughts 

Iterate to sum each pair up. Use carry bit to record carrying information.

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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addTwoNumsHelper(l1, l2, 0);
    }
    
    private ListNode addTwoNumsHelper(ListNode l1, ListNode l2, int carry) {
        if (carry == 0) {
            if (l1 == null && l2 == null) {
                return null;
            } else if (l1 == null) {
                return l2;
            } else if (l2 == null) {
                return l1;
            } else {
                int a = l1.val;
                int b = l2.val;
                if (a + b > 9) {
                    carry = 1;
                } 
                ListNode res = new ListNode((a + b) % 10);
                res.next = addTwoNumsHelper(l1.next, l2.next, carry);
                return res;
            }
        } else {
            if (l1 == null && l2 == null) {
                return new ListNode(1);
            } else if (l1 == null || l2 == null) {
                int a = l1 == null ? l2.val : l1.val;
                carry = 0;
                if (a + 1 > 9) {
                    carry = 1;
                }
                ListNode res = new ListNode((a + 1) % 10);
                res.next = l1 == null ? addTwoNumsHelper(l1, l2.next, carry) : addTwoNumsHelper(l1.next, l2, carry);
                return res;
            } else {
                int a = l1.val;
                int b = l2.val;
                carry = 0;
                if (a + b + 1 > 9) {
                    carry = 1;
                } 
                ListNode res = new ListNode((a + b + 1) % 10);
                res.next = addTwoNumsHelper(l1.next, l2.next, carry);
                return res;
            }
        }
    }
}
```

T: O(n) S: O(n)

---

#### Optimized 

There're a lot of duplicated codes in above solution, we can use `int sum = (l1 == null? 0 : l1.val) + (l2 == null ? 0 : l2.val) + carry;` to simplify it.

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addTwoNumsHelper(l1, l2, 0);
    }
    
    private ListNode addTwoNumsHelper(ListNode l1, ListNode l2, int carry) {
        if (l1 == null && l2 == null && carry == 0) {
            return null;
        }
        int sum = (l1 == null ? 0 : l1.val) + (l2 == null ? 0 : l2.val) 
            + (carry == 0 ? 0 : 1);
        ListNode res = new ListNode(sum % 10);
        ListNode tmp = res;
        tmp.next = addTwoNumsHelper(l1 == null ? l1 : l1.next, 
                                    l2 == null ? l2 : l2.next, sum > 9 ? 1 : 0);
        return res;
    }
}
```

T: O(n) S: O(n)

---

#### Iteration

We could also use iteration to solve this problem.

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(0);
        ListNode tmp = res;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            int sum = (l1 == null? 0 : l1.val) + (l2 == null ? 0 : l2.val) + carry;
            carry = sum / 10;
            tmp.next = new ListNode(sum % 10);
            tmp = tmp.next;
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        return res.next;
    }
}
```

T: O(n) S: O(n)

---

#### Summary 

When there're a lot of if-else statements in a same mode, we can use `int sum = (l1 == null? 0 : l1.val) + (l2 == null ? 0 : l2.val) + carry;`  to simplify if-else statements.