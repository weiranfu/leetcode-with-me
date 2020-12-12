---
title: Medium | Copy List With Random Pointer 138
tags:
  - tricky
  - Oh-shit
categories:
  - Leetcode
  - Linked List
date: 2019-12-14 00:02:05
---

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list.

[Leetcode](https://leetcode.com/problems/copy-list-with-random-pointer/)

<!--more-->

**Example 1:**

**![img](https://discuss.leetcode.com/uploads/files/1470150906153-2yxeznm.png)**

```
Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
```

**Note:**

1. You must return the **copy of the given head** as a reference to the cloned list.

---

#### Tricky 

**How to copy an array list with constant space complexity?**

The naive way is to store each copied node with original node in a map, and then linked them up together.

The better way is ***to associate the original node with its copy node in a single linked list***.

1. Iterate the original list and duplicate each node. The duplicate
   of each node follows its original immediately.
2. Restore the original list and extract the duplicated nodes.

#### Oh Shit

**The default value for a key not existing in a map is null!**

```
Map<Integer, Integer> map = new HashMap<>();
map.get(1) == null;  // Default value is null.
```

---

#### My thoughts 

Failed to solve.

---

#### Naive way

Using a map to store copied node with original node in order to refer them when assigning random pointers.

```java
/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;
    public Node random;

    public Node() {}

    public Node(int _val,Node _next,Node _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
    public Node copyRandomList(Node head) {
        Map<Node, Node> map = new HashMap<>();
        Node p = head;
        while (p != null) {  // Map node with copied node in order to be referred by random pointer.
            Node copy = new Node(p.val, null, null);
            map.put(p, copy);
            p = p.next;
        }
        p = head;
        while (p != null) {   
            Node curr = map.get(p);
            curr.next = map.get(p.next); // The default value for map is null.
            curr.random = map.get(p.random);
            p = p.next;
        }
        return map.get(head);
    }
}
```

T: O(n) S: O(n)

---

#### Better way 

1. Iterate the original list and duplicate each node. The duplicate
   of each node follows its original immediately.
2. Iterate the new list and assign the random pointer for each
   duplicated node.
3. Restore the original list and extract the duplicated nodes.

```java
class Solution {
    public Node copyRandomList(Node head) {
        if (head == null) return null;
        Node p = head;
        // First round: make copy of each node,
        // and link them together side-by-side in a single list.
        while (p != null) {
            Node tmp = new Node();
            tmp.val = p.val;
            tmp.next = p.next;
            p.next = tmp;
            p = tmp.next;
        }
        p = head;
        // Second round: assign random pointers for the copy nodes.
        while (p != null) {
            // Corner case: random is null.
            p.next.random = p.random != null ? p.random.next : null; 
            p = p.next.next;
        }
        p = head;
        Node res = new Node(); // New head for copied list.
        Node copy = res;
        while (p != null) {
            Node next = p.next.next;
            copy.next = p.next;
            copy = copy.next; // Move copy to next.
            p.next = next;
            p = next;  // Move p to next.
        }
        return res.next;
    }
}
```

T: O(n) S: O(1)

---

#### Summary 

**How to copy an array list with constant space complexity?**

* The naive way is to store each copied node with original node in a map, and then linked them up together.

* The better way is ***to associate the original node with its copy node in a single linked list***.

