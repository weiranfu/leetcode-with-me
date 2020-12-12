---
title: Medium | Min Stack 155
tags:
  - tricky
categories:
  - Leetcode
  - Linked List
date: 2020-01-09 20:48:52
---

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.

[Leetcode](https://leetcode.com/problems/min-stack/)

<!--more-->

**Example:**

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

---

#### Tricky 

How to get the min value of a stack quickly?

* Store the min value.
* Using another stack to store this min value.
* Using Linked List.

---

#### My thoughts 

Using a priority queue. 

This is waster of space, because we need to store data twice.

---

#### Linked List 

Use a Linked List to store min value in ListNode.

And then we can store all the min values along with stack.

```java
class MinStack {
    
    class Node {
        int value;
        int min;
        Node prev;
        public Node(int value, int min, Node prev) {
            this.value = value;
            this.min = min;
            this.prev = prev;
        }
    }
    
    Node root;
    Node curr;

    /** initialize your data structure here. */
    public MinStack() {
        root = new Node(-1, Integer.MAX_VALUE, null);
        curr = root;
    }
    
    public void push(int x) {
        if (curr.equals(root)) {
            Node tmp = new Node(x, x, curr);
            curr = tmp;
        } else {
            Node tmp = new Node(x, Math.min(curr.min, x), curr);
            curr = tmp;
        }
    }
    
    public void pop() {
        if (!curr.equals(root)) {
            curr = curr.prev;
        }
    }
    
    public int top() {
        return curr.value;
    }
    
    public int getMin() {
        return curr.min;
    }
}
```

T: O(n)			S: O(n)

---

#### Store min value 

We can store the min value. 

**Everytime we find an item smaller than min, we push min into stack as a mark, then set the new min.**

```java
class MinStack {
    
    Stack<Integer> stack;
    int min;

    /** initialize your data structure here. */
    public MinStack() {
        stack = new Stack<>();
        min = Integer.MAX_VALUE;
    }
    
    public void push(int x) {
        if (x <= min) {
            stack.push(min);      // Push min into stack as a mark, this data has been 
            min = x;              // stored already.
        }
        stack.push(x);
    }
    
    public void pop() {
        if (stack.peek() == min) {//If we find previous min mark, pop it and set new min
            stack.pop();
            min = stack.peek();
        }
        stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return min;
    }
}
```

T: O(n) 		S: O(n)

---

#### Two stacks

Use another stack to store all min values, and when we want to pop an item, we compare it with top item in minStack. If they're same, pop this min value from minStack.

```java
class MinStack {
    
    Stack<Integer> stack;
    Stack<Integer> minStack;

    /** initialize your data structure here. */
    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int x) {
        if (minStack.isEmpty() || x <= minStack.peek()) {  // THIS should be <=
            minStack.push(x);
        }
        stack.push(x);
    }
    
    public void pop() {
        int i = minStack.peek();
        int j = stack.peek();
        if (i == j) {
            minStack.pop();
        }
        stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
```

T: O(n) 			S: O(n)

---

#### Summary 

We can use a Linked List to implement a stack, and retrieve min value in O(1).