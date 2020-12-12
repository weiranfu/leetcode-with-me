---
title: Easy | Implement Stack using Queue 225
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Design
date: 2020-06-20 21:57:56
---

Implement the following operations of a stack using queues.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- empty() -- Return whether the stack is empty.

[Leetcode](https://leetcode.com/problems/implement-stack-using-queues/)

<!--more-->

**Example:**

```
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
```

---

#### Tricky 

As queue is FIFO, we need to swap the newly added item to the top of queue. This takes O(n).

---

#### Standard solution  

```java
class MyStack {
    
    Queue<Integer> queue;

    /** Initialize your data structure here. */
    public MyStack() {
        queue = new LinkedList<>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        queue.add(x);
        for (int i = 0; i < queue.size() - 1; i++) {
            queue.add(queue.poll());
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return queue.poll();
    }
    
    /** Get the top element. */
    public int top() {
        return queue.peek();
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return queue.isEmpty();
    }
}
```

`push()`  O(n)

`pop()`    O(1)



