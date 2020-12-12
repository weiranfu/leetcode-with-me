---
title: Medium | Longest Well-Performing Interval 1124
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-07-25 00:21:30
---

We are given `hours`, a list of the number of hours worked per day for a given employee.

A day is considered to be a *tiring day* if and only if the number of hours worked is (strictly) greater than `8`.

A *well-performing interval* is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

[Leetcode](https://leetcode.com/problems/longest-well-performing-interval/)

<!--more-->

**Example 1:**

```
Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
```

---

#### Two Pointers  

**Make a new array A of +1/-1s corresponding to if hours[i] is > 8 or not. The goal is to find the longest subarray with positive sum.**

For every index `i`, we need to find the farthest `j <= i` that `preSum[i] - preSum[j-1] > 0`

So we try to extend `i`.

If max `preSum[i]` on the right of `i` satisfies `rMax[i] - preSum[j-1] <= 0`, `j` will be useless, `j++`

Otherwise, we could extend `i`, `i++`

So we need to track the max right `preSum[i]` `rMax[i]`.

```java
class Solution {
    public int longestWPI(int[] hours) {
        int n = hours.length;
        int[] A = new int[n];
        for (int i = 0; i < n; i++) A[i] = hours[i] > 8 ? 1 : -1;	// convert to 1 / -1
        int[] preSum = new int[n + 1];
        for (int i = 0; i < n; i++) preSum[i + 1] = preSum[i] + A[i];
        int[] rMax = new int[n];																
        rMax[n - 1] = preSum[n];
        for (int i = n - 2; i >= 0; i--) {
            rMax[i] = Math.max(rMax[i + 1], preSum[i + 1]);			// max right preSum[]
        }
        int res = 0;
        for (int i = 0, j = 0; i < n; i++) {
            while (j <= i && rMax[i] - preSum[j] <= 0) {	// shrink j
                j++;
            }
            res = Math.max(res, i - j + 1);
        }
        return res;
    }
}
```

T: O(n)			S: O(n)

---

#### Monotonic Stack

For simplicity, call `(i, j)` a valid pair if the inequation `prefixSum[j] - prefixSum[i] > 0` holds. Our goal is to **optimize** `j-i` over all valid pair `(i, j)`.

- Firstly, fix `j` and minimize `i`. Consider any `i1` and `i2` that `i1 < i2 < j` and `prefixSum[i1] <= prefixSum[i2]`. It is obvious that `(i2, j)` can't be a candidate of optimal subarray because `(i1, j)` is more promising to be valid and longer than `(i2, j)`. Therefor candidates are monotone decreasing, and we can use a **strictly monotonic descresing stack** to find all candidates. 
- Secondly, fix `i` and maximize `j`. Consider any `j1` and `j2` that `i < j1 < j2` and `prefixSum[j2] - prefix[i] > 0`. We can find that `(i, j1)` can't be a candidate of optimal subarrary because `(i, j2)` is better. This discovery tells us that we should iterate `j` from end to begin and if we find a valid `(i, j)`, we don't need to keep `i` in `Stack` any longer.

```java
class Solution {
    public int longestWPI(int[] hours) {
        int n = hours.length;
        int[] A = new int[n];
        for (int i = 0; i < n; i++) A[i] = hours[i] > 8 ? 1 : -1;
        int[] preSum = new int[n + 1];
        for (int i = 0; i < n; i++) preSum[i + 1] = preSum[i] + A[i];
        
        Stack<Integer> stack = new Stack<>();		// monotonic stack
        for (int i = 0; i <= n; i++) {
            if (stack.isEmpty() || preSum[stack.peek()] > preSum[i]) {
                stack.push(i);
            }
        }
        int res = 0;
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && preSum[stack.peek()] < preSum[i + 1]) {
                res = Math.max(res, i + 1 - stack.peek());
                stack.pop();
            }
        }
        return res;
    }
}
```

T: O(n)			S: O(n)



