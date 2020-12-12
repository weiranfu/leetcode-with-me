---
title: Hard | Max Value of Equation 1499
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-06-28 04:14:12
---

Given an array `points` containing the coordinates of points on a 2D plane, sorted by the x-values, where `points[i] = [xi, yi]` such that `xi < xj` for all `1 <= i < j <= points.length`. You are also given an integer `k`.

Find the *maximum value of the equation* `yi + yj + |xi - xj|` where `|xi - xj| <= k` and `1 <= i < j <= points.length`. It is guaranteed that there exists at least one pair of points that satisfy the constraint `|xi - xj| <= k`.

[Leetcode](https://leetcode.com/problems/max-value-of-equation/)

<!--more-->

**Example 1:**

```
Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
```

**Example 2:**

```
Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
```

---

#### Tricky 

This is a typical *monotone stack* problem.

We need to find the max `yi + yj + |xi - xj|` => `yi - xi + yj + xj`     and `xj - xi <= k`

So we only need to find out the maximum `yi - xi` in a window `xj - xi <= k`
To find out the maximum element in a sliding window,
we can use priority queue or monotone stack.

---

#### Priority Queue

```java
class Solution {
    public int findMaxValueOfEquation(int[][] points, int k) {
        int n = points.length;
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        int res = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            int x = points[i][0];
            int y = points[i][1];
            while (!queue.isEmpty() && x - queue.peek()[1] > k) { // out-of-date
                queue.poll();
            }
            if (!queue.isEmpty()) {
                res = Math.max(res, queue.peek()[0] + x + y);   
            }
            queue.add(new int[]{y - x, x});  // save yi - xi, xi
        }
        return res;
    }
}
```

T: O(nlogn)		S: O(n)

---

#### Monotone Stack

```java
class Solution {
    public int findMaxValueOfEquation(int[][] points, int k) {
        int n = points.length;
        Deque<int[]> queue = new LinkedList<>();
        int res = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            int x = points[i][0];
            int y = points[i][1];
            while (!queue.isEmpty() && x - queue.peekFirst()[1] > k) { // out-of-date
                queue.pollFirst();
            }
            if (!queue.isEmpty()) {
                res = Math.max(res, queue.peekFirst()[0] + x + y);   
            }
            while (!queue.isEmpty() && queue.peekLast()[0] <= y - x) {// monotone
                queue.pollLast();
            }
            queue.add(new int[]{y - x, x});
        }
        return res;
    }
}
```

T: O(n)		S: O(n)

