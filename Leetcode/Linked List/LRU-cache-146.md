---
title: Medium | LRU Cache 146
tags:
  - common
  - implement
categories:
  - Leetcode
  - Linked List
date: 2019-12-15 18:21:34
---

Design and implement a data structure for [Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU). It should support the following operations: `get` and `put`.

[Leetcode](https://leetcode.com/problems/lru-cache/)

<!--more-->

`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
`put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a **positive** capacity.

**Example:**

```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```

**Follow up:** 

Could you do both operations in **O(1)** time complexity?

---

#### Implement

Using Double Linked List to implement LRU.

One advantage of *double* linked list is that the node can remove itself without other reference. In addition, it takes constant time to add and remove nodes from the head or tail.

One particularity about the double linked list implemented here is that there are *pseudo head* and *pseudo tail* to mark the boundary, so that we don't need to check the `null` node during the update.

When `size > capacity`, we always pop the node before *pseudo tail*. When we access or add a new node, we always put it after *pseudo head*.

Use a Map to keep a track of Node existence.

---

#### Standard solution

```java
class LRUCache {
    class Node {
        int key;
        int value;
        Node prev;
        Node next;
    }
    
    Map<Integer, Node> cache = new HashMap<>();
    int size;
    int capacity;
    Node head, tail;
    
    public LRUCache(int capacity) {
        size = 0;
        this.capacity = capacity;
        head = new Node();
        tail = new Node();
        head.next = tail;
        tail.prev = head;
    }
    
    // Always add the new node right after head.
    private void addNode(Node node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }
    
    // Remove an existing node from the linked list.
    private void removeNode(Node node) {
        Node prev = node.prev;
        Node next = node.next;
        prev.next = next;
        next.prev = prev;
    }
    
    // Move certain node in between to the head. (change six pointers)
    private void moveToHead(Node node) {
        removeNode(node);
        addNode(node);
    }
    
    // Pop the current tail.
    private Node popTail() {
        Node res = tail.prev;
        removeNode(res);
        return res;
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) return -1;
        Node node = cache.get(key);
        moveToHead(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            node.value = value;
            moveToHead(node);
        } else {
            Node newNode = new Node();
            newNode.key = key;
            newNode.value = value;
            cache.put(key, newNode);
            addNode(newNode);
            size++;
            if (size > capacity) {
                Node tail = popTail();
                cache.remove(tail.key);
                size--;
            }
        }
    }
}
```

T: O(1)		S: O(capacity)
