---
title: Medium | Daily Temperature 739
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-07-27 21:04:38
---

Given a list of daily temperatures `T`, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put `0` instead.

[Leetcode](https://leetcode.com/problems/daily-temperatures/)

<!--more-->

For example, given the list of temperatures `T = [73, 74, 75, 71, 69, 72, 76, 73]`, your output should be `[1, 1, 4, 2, 1, 1, 0, 0]`.

**Follow up:** 

[Online Stock Span](https://leetcode.com/problems/online-stock-span/)

---

#### Stack

We could using Stock to find *Next greater element*

```java
class Solution {
    public int[] dailyTemperatures(int[] T) {
        int n = T.length;
        int[] res = new int[n];
        Stack<Integer> stack = new Stack<>();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && T[stack.peek()] <= T[i]) {
                stack.pop();
            }
            int idx = stack.isEmpty() ? i : stack.peek();
            res[i] = idx - i;
            stack.push(i);
        }
        return res;
    }
}
```

T: O(n)		S: O(n)