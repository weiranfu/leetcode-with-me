---
title: Medium | Next Greater Element II 503
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-07-27 23:04:41
---

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

[Leetcode](https://leetcode.com/problems/next-greater-element-ii/)

<!--more-->

**Example 1:**

```
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
```

**Example 2:**

```
Input: [1,3,2,1]
Output: [3,-1,3,3]
```

**Follow up:** 

[Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

[Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)

---

#### Stack

How to deal with a circular array?

**We could append another same array to original array to simulate circular array. **

```java
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] A = new int[n * 2];
        for (int i = 0; i < A.length; i++) {
            A[i] = nums[i % n];
        }
        Stack<Integer> stack = new Stack<>();
        int[] res = new int[n];
        for (int i = 2 * n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= A[i]) {
                stack.pop();
            }
            if (i < n) {
                res[i] = stack.isEmpty() ? -1 : stack.peek();
            }
            stack.push(A[i]);
        }
        return res;
    }
}
```

T: O(n)			S: O(n)

---

#### Optimized

We don't need create a double size array actually.

```java
class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        Stack<Integer> stack = new Stack<>();
        int[] res = new int[n];
        for (int i = 2 * n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= nums[i % n]) {
                stack.pop();
            }
            if (i < n) {
                res[i] = stack.isEmpty() ? -1 : stack.peek();
            }
            stack.push(nums[i % n]);
        }
        return res;
    }
}
```

T: O(n)			S: O(n)

