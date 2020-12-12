---
title: Easy | Implement Queue using Stack 232
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Design
date: 2020-06-20 22:08:56
---

Implement the following operations of a queue using stacks.

- push(x) -- Push element x to the back of queue.
- pop() -- Removes the element from in front of queue.
- peek() -- Get the front element.
- empty() -- Return whether the queue is empty.

[Leetcode](https://leetcode.com/problems/implement-queue-using-stacks/)

<!--more-->

**Example:**

```
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
```

---

#### Tricky 

A stack is LIFO and two stacks are FIFO.

Use two stacks as `input` and `output`. One is for input items and another is to reverse the input.

---

#### Standard solution  

```java
class MyQueue {
    
    Stack<Integer> input = new Stack<>();
    Stack<Integer> output = new Stack<>();
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        input.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        peek();
        return output.pop();
    }
    
    /** Get the front element. */
    public int peek() {
        if (output.isEmpty()) {
            while (!input.isEmpty()) {
                output.push(input.pop());
            }
        }
        return output.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return input.isEmpty() && output.isEmpty();
    }
}
```

`push()` 		O(1)

`pop()`			amortized to O(1)

