---
title: Medium | Maximum Width Ramp 962
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-07-24 17:12:49
---

Given an array `A` of integers, a *ramp* is a tuple `(i, j)` for which `i < j` and `A[i] <= A[j]`.  The width of such a ramp is `j - i`.

Find the maximum width of a ramp in `A`.  If one doesn't exist, return 0.

[Leetcode](https://leetcode.com/problems/maximum-width-ramp/)

<!--more-->

**Example 1:**

```
Input: [6,0,8,2,1,5]
Output: 4
Explanation: 
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
```

**Example 2:**

```
Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: 
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
```

**Follow up**

[Longest Well-Performing Interval](https://leetcode.com/problems/longest-well-performing-interval/)

[Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)

---

#### Two Pointers

**Given an array, for every index, we need to find farthest smaller element on its left.**

We keep to pointers j, i (j <= i), if we find `A[j] > max(A[i], A[i+1], ..., A[n])`

`A[j]` will be useless, cause every `A[i]` and its right items will be smaller than `A[j]`, `j++`

```java
class Solution {
    public int maxWidthRamp(int[] A) {
        int n = A.length;
        int[] rMax = new int[n];
        rMax[n - 1] = A[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            rMax[i] = Math.max(A[i], rMax[i + 1]);
        }
        int res = 0;
        for (int i = 0, j = 0; i < n; i++) {
            while (j <= i && A[j] > rMax[i]) {
                j++;
            }
            res = Math.max(res, i - j);
        }
        return res;
    }
}
```

T: O(n)			S: O(n)

---

#### Decreasing List with Binary Search

Keep a decraesing stack. For each number, binary search the first smaller number in the stack.

When the number is smaller the the last, push it into the stack.

```java
    public int maxWidthRamp(int[] A) {
        List<Integer> s = new ArrayList<>();
        int res = 0, n = A.length;
        for (int i = 0; i < n; ++i) {
            if (s.size() == 0 || A[i] < A[s.get(s.size() - 1)]) {
                s.add(i);
            } else {
                int left = 0, right = s.size() - 1, mid = 0;
                while (left < right) {
                    mid = (left + right) / 2;
                    if (A[s.get(mid)] > A[i]) {
                        left = mid + 1;
                    } else {
                        right = mid;
                    }
                }
                res = Math.max(res, i - s.get(left));
            }
        }
        return res;
    }
```

T: O(nlogn)			S: O(n)

---

#### Monotonic Stack

**Given an array, for every index, we need to find farthest smaller element on its left.**

Firstly, fix `j` and minimize `i`. Consider any `i1` and `i2` that `i1 < i2 < j` and `A[i1] <= A[i2]`, it is obvious that `(i2, j)` can't be a candidate of optimal tuple because `(i1, j)` will be valid and longer than `(i2, j)`.

Therefore candidates are monotone decreasing will help us to find the minimize `i` that `A[i] <= A[j]`

We keep a decreasing stack to store the index of array because if we meet a larger item on the right of a smaller item, that larger item will be useless. So we only add smaller item.

Secondly, fix `i` and maximize `j`. Consider any `j1` and `j2` that `i < j1 < j2` and `A[j1] <= A[j2]`

`(i, j1)` cannot be the candidate cause `(i, j2)` will be a longer candidate. 

So we scan from right to left and if we find a valid `(i, j)`, we won't need to keep `i` in the stack any longer.

```java
class Solution {
    public int maxWidthRamp(int[] A) {
        int n = A.length;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            if (stack.isEmpty() || A[stack.peek()] > A[i]) { // only add smaller item
                stack.push(i);
            }
        }
        int res = 0;
        for (int i = n - 1; i >= 0; i--) {									// scan from right to left
            while (!stack.isEmpty() && A[stack.peek()] <= A[i]) {
                res = Math.max(res, i - stack.peek());
              	stack.pop();
            }
        }
        return res;
    }
}
```

T: O(n)			S: O(n)