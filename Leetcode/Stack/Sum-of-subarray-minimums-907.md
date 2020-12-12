---
title: Medium | Sum of Subarray Minimums 907
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-07-27 00:28:43
---

Given an array of integers `A`, find the sum of `min(B)`, where `B` ranges over every (contiguous) subarray of `A`.

Since the answer may be large, **return the answer modulo 10^9 + 7.**

[Leetcode](https://leetcode.com/problems/sum-of-subarray-minimums/)

<!--more-->

**Example 1:**

```
Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
```

**Note:**

1. `1 <= A.length <= 30000`
2. `1 <= A[i] <= 30000`

**Follow up:** 

---

#### Stack

**Intuition**:

**Intuition**

Let's try to count the number of subarrays `#(j)` for which `A[j]` is the *right-most* minimum. Then, the answer will be `sum #(j) * A[j]`. (We must say *right-most* so that we form disjoint sets of subarrays and do not double count any, as the minimum of an array may not be unique.)

For example, `[4,3,3,3,4]`, the *right-most* 3 is the minimum 3.

This in turn brings us the question of knowing the smallest index `i <= j` for which `A[i], A[i+1], ..., A[j]` are all `>= A[j]`; and the largest index `k >= j` for which `A[j+1], A[j+2], ..., A[k]` are all `> A[j]`.

**Algorithm**

For example, if `A = [10, 3, 4, 5, _3_, 2, 3, 10]` and we would like to know `#(j = 4)` [the count of the second `3`, which is marked], we would find `i = 1` and `k = 5`.

From there, the actual count is `#(j) = (j - i + 1) * (k - j + 1)`, as there are `j - i + 1` choices `i, i+1, ..., j` for the left index of the subarray, and `k - j + 1` choices `j, j+1, ..., k` for the right index of the subarray.

**Answering these queries (ie. determining `(i, k)` given `j`) is a classic problem that can be answered with a stack. We'll focus on the problem of finding `i`: the problem of finding `k` is similar.**

We could keep an increasing stack so that we could know the number of larger items on the left/right.

```java
class Solution {
    public int sumSubarrayMins(int[] A) {
        int mod = (int)1e9 + 7;
        int n = A.length;
        int[] left = new int[n];				// count for A[i] >= A[j]
        int[] right = new int[n];				// count for A[k] > A[j]
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && A[stack.peek()] >= A[i]) {
                stack.pop();
            }
            int idx = stack.isEmpty() ? -1 : stack.peek();
            left[i] = i - idx - 1;
            stack.push(i);
        }
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && A[stack.peek()] > A[i]) {
                stack.pop();
            }
            int idx = stack.isEmpty() ? n : stack.peek();
            right[i] = idx - i - 1;
            stack.push(i);
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            int l = left[i] + 1;
            int r = right[i] + 1;
            res = (res + l * r % mod * A[i]) % mod;
        }
        return res;
    }
}
```

T: O(n)		S: O(n)