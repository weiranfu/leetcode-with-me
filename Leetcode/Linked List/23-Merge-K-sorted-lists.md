---
title: Medium | Merge K Sorted Lists 23
tags:
  - common
categories:
  - Leetcode
  - Linked List
date: 2019-12-31 00:11:49
---

Merge *k* sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

[Leetcode](https://leetcode.com/problems/merge-k-sorted-lists/)

<!--more-->

**Example:**

```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

---

#### My thoughts 

Maintain a priority queue, add tail of each linked list into priority queue, and poll out the smallest one.

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
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                return a[0] - b[0];
            }
        });
        for (int i = 0; i < lists.length; i++) {
            ListNode n = lists[i];
            if (n == null) continue;
            lists[i] = n.next;
            pq.offer(new int[]{n.val, i});
        }
        ListNode res = new ListNode(0);
        ListNode curr = res;
        while (!pq.isEmpty()) {
            int[] info = pq.poll();
            int index = info[1];
            curr.next = new ListNode(info[0]);
            if (lists[index] != null) {
                ListNode tmp = lists[index];
                lists[index] = tmp.next;
                pq.offer(new int[]{tmp.val, index});
            }
            curr = curr.next;
        }
        return res.next;
    }
}
```

T: O(nlog(K)) K is the length of lists.

S: O(n)

---

#### Optimized 

Instead of store `ind[]{value, index}` in the priority queue, we can store `ListNode` in priority queue.

And when we use a node of a ListNode, we move forward by `n = n.next` and `pq.offer(n)`.

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>(new Comparator<ListNode>() {
            @Override
            public int compare(ListNode a, ListNode b) {
                return a.val - b.val;
            }
        });
        for (int i = 0; i < lists.length; i++) {
            ListNode n = lists[i];
            if (n == null) continue;
            pq.offer(n);
        }
        ListNode res = new ListNode(0);
        ListNode curr = res;
        while (!pq.isEmpty()) {
            ListNode n = pq.poll();
            curr.next = new ListNode(n.val);
            curr = curr.next;
            n = n.next;
            if (n != null) {
                pq.offer(n);
            }
        }
        return res.next;
    }
}
```

T: O(nlogK)  K is length of lists

S: O(n)

---

#### Divide and Conquer

We can divide this problem into many subproblems. The subproblem is to merge two lists.

So this problem becomes a merge sort.

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        return mergeKListsHelper(lists, 0, lists.length);
    }
    
    private ListNode mergeKListsHelper(ListNode[] lists, int start, int end) {
        if (end - start == 1) {
            return lists[start];
        }
        int mid = start + (end - start) / 2;
        ListNode n1 = mergeKListsHelper(lists, start, mid);
        ListNode n2 = mergeKListsHelper(lists, mid, end);
        return mergeTwoLists(n1, n2);
    }
    
    private ListNode mergeTwoLists(ListNode n1, ListNode n2) {
        ListNode res = new ListNode(0);
        ListNode curr = res;
        while (n1 != null && n2 != null) {
            if (n1.val < n2.val) {
                curr.next = n1;
                curr = curr.next;
                n1 = n1.next;
            } else {
                curr.next = n2;
                curr = curr.next;
                n2 = n2.next;
            }
        }
        if (n1 != null) {
            curr.next = n1;
        }
        if (n2 != null) {
            curr.next = n2;
        }
        return res.next;
    }
}
```

T: O(n*logK) K is the length of lists

S: O(n)

---

#### Iteration 

We can use iteration to divide and conquer this problem.

Use an `interval` to control the merge process.

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) {
            return null;
        }
        int interval = 1;
        while (0 + interval < lists.length) {
            for (int i = 0; i + interval < lists.length; i = i + 2 * interval) {
                lists[i] = mergeTwoLists(lists[i], lists[i + interval]);
            }
            interval *= 2;
        }
        return lists[0];
    }
    
    private ListNode mergeTwoLists(ListNode n1, ListNode n2) {
        ListNode res = new ListNode(0);
        ListNode curr = res;
        while (n1 != null && n2 != null) {
            if (n1.val < n2.val) {
                curr.next = n1;
                curr = curr.next;
                n1 = n1.next;
            } else {
                curr.next = n2;
                curr = curr.next;
                n2 = n2.next;
            }
        }
        if (n1 != null) {
            curr.next = n1;
        }
        if (n2 != null) {
            curr.next = n2;
        }
        return res.next;
    }
}
```

T: O(n*logK) K is length of lists

S: O(n)

---

#### Summary 

Divide and conquer is useful to divide K problems into `logK` subproblems.