---
title: Hard | Shortest Subarray with Sum at Least K 862
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-07-25 21:41:33
---

Return the **length** of the shortest, non-empty, contiguous subarray of `A` with sum at least `K`.

If there is no non-empty subarray with sum at least `K`, return `-1`.

[Leetcode](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)

<!--more-->

**Example 1:**

```
Input: A = [1], K = 1
Output: 1
```

**Example 2:**

```
Input: A = [1,2], K = 4
Output: -1
```

**Example 3:**

```
Input: A = [2,-1,2], K = 3
Output: 3
```

**Follow up:** 

---

#### Monotonic Queue 

What makes this problem hard is that we have negative values. 

**Recall of the Sliding window solution in a positive array**

The `Sliding window` solution finds the subarray we are looking for in a `linear` time complexity. The idea behind it is to maintain two pointers: **start** and **end**, moving them in a smart way to avoid examining all possible values `0<=end<=n-1` and `0<=start<=end` (to avoid brute force).
What it does is:

1. Incremeting the **end** pointer while the sum of current subarray (defined by current values of `start` and `end`) is smaller than the target.
2. `Once we satisfy` our condition (the sum of current subarray >= target) we keep `incrementing` the **start** pointer until we `violate` it (until `sum(array[start:end+1]) < target`).
3. Once we violate the condition we keep incrementing the **end** pointer until the condition is satisfied again and so on.

The reason why we stop incrementing `start` when we violate the condition is that we are sure we will not satisfy it again if we keep incrementing `start`. In other words, if the sum of the current subarray `start -> end` is smaller than the target then the sum of `start+1 -> end` is neccessarily smaller than the target. (positive values)
The problem with this solution is that it doesn't work if we have negative values, this is because of the sentence above `Once we "violate" the condition we stop incrementing start`.

**Problem of the Sliding window with negative values**

Now, let's take an example with negative values `nums = [3, -2, 5]` and `target=4`. Initially `start=0`, we keep moving the **end** pointer until we satisfy the condition, here we will have `start=0` and `end=2`. Now we are going to move the start pointer `start=1`. The sum of the current subarray is `-2+5=3 < 4` so we violate the condition. However if we just move the **start** pointer another time `start=2` we will find `5 >= 4` and we are satisfying the condition. And this is not what the Sliding window assumes.

---

We could convert problem to **Find the nearest prefix Sum[j] that `preSum[j] + K <= preSum[i]` (j < i)**

Then we could maintain an **increasing Stack** to get the nearest smaller element.

However, we're not finding smaller element that `preSum[j] <= preSum[i]`, but we're finding smaller element that `preSum[j] + K <= preSum[i]`.

We can rephrase this as a problem about the prefix sums of `A`. Let `P[i] = A[0] + A[1] + ... + A[i-1]`. We want the largest `x` such that `x < y` and `P[x] + K <= P[y]`.

Motivated by that equation, let `opt(y)` be the largest `x` such that `P[x] + K <= P[y]`. We need two key observations:

- If `x1 < x2` and `P[x2] <= P[x1]`, then `opt(y)` can never be `x1`, as if `P[x1] <= P[y] - K`, then `P[x2] <= P[x1] <= P[y] - K` but `y - x2` is smaller. This implies that our candidates `x` for `opt(y)` will have increasing values of `P[x]`.  (**Increasing Queue**)
- If `opt(y1) = x`, then we do not need to consider this `x` again. For if we find some `y2 > y1` with `opt(y2) = x`, then it represents an answer of `y2 - x` which is worse (larger) than `y1 - x`.

**Algorithm**

Maintain a "monoqueue" of indices of `P`: a deque of indices `x_0, x_1, ...` such that `P[x_0], P[x_1], ...` is increasing.

When adding a new index `y`, we'll pop `x_i` from the end of the deque so that `P[x_0], P[x_1], ..., P[y]` will be increasing.

If `P[y] >= P[x_0] + K`, then (as previously described), we don't need to consider this `x_0` again, and we can pop it from the front of the deque.

```java
class Solution {
    public int shortestSubarray(int[] A, int K) {
        int n = A.length;
        int[] preSum = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            preSum[i] = preSum[i - 1] + A[i - 1];
        }
        Deque<Integer> q = new ArrayDeque<>();
        q.addFirst(0);                          // preSum initail index is 0
        int res = n + 1;
        for (int i = 1; i <= n; i++) {	// find nearest upper bound for j.
            while (!q.isEmpty() && preSum[q.peekFirst()] + K <= preSum[i]) {
                res = Math.min(res, i - q.peekFirst());
                q.pollFirst();
            }
          	// increasing queue
            while (!q.isEmpty() && preSum[q.peekLast()] >= preSum[i]) {
                q.pollLast();
            }
            q.addLast(i);
        }
        return res == n + 1 ? -1 : res;
    }
}
```

T: O(n)			S: O(n)



