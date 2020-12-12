---
title: Medium | 132 Pattern 456
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-07-27 16:42:44
---

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence a**i**, a**j**, a**k** such that **i** < **j** < **k** and a**i** < a**k** < a**j**. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

**Note:** n will be less than 15,000.

[Leetcode](https://leetcode.com/problems/132-pattern/)

<!--more-->

**Example 1:**

```
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
```

**Example 2:**

```
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
```

**Example 3:**

```
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
```

**Follow up:** 

---

#### Brute Force 

We need to find `ai < ak < aj` and `i < j < k`. 

We fix `ai` and try to find proper `aj` and `ak`.

Since `aj` and `ak` both are greater than `ai`, we only need to find whether there exist `aj` greater `ak` and keep track the min value of `ak`.

```java
class Solution {
    public boolean find132pattern(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int min = nums[i];
            int mid = Integer.MAX_VALUE;
            for (int j = n - 1; j > i; j--) {
                if (nums[j] <= min) continue;
                if (nums[j] > mid) return true;   // aj > ak
                mid = Math.min(mid, nums[j]);     // min value of ak
            }
        }
        return false;
    }
}
```

T: O(n^2)			S: O(1)

---

#### Stack

We have known the `a[i]` using `min[]` array. The only thing we need to do is to find if there is an item `a[k]` to the right of `a[j]` that is smaller than `a[j]` and greater than `a[i]`. (`i < j < k`)

**We can iterater `a[k]` and find whether there exists a previous item `a[j]` and `a[j] > a[k]`. (This is same with finding previous greater element).**

We can maintain a decreasing stack to find previous greater element.

However how can we make sure that `a[i] = min[k]`  is before `a[j]`? 

For example, `[1, -3, -2]`  `a[k] = nums[2] = -2` and `a[i] = min[2] = nums[1] = -3` and previous greate element is `a[j] = nums[0] = 1`.

And `a[i]` is after `a[j]`.

So we need to store the smallest item `a[i]` along with `a[j]` in the stack.

Everytime we pop out a `a[i]` and `a[j]` from stack, we compare `a[k]` with `a[i]` and `a[j]`.

```java
class Solution {
    public boolean find132pattern(int[] nums) {
        if (nums == null || nums.length == 0) return false;
        int n = nums.length;
        /* int[]{ item, smallest } */
        Stack<int[]> stack = new Stack<>();
        int smallest = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && stack.peek()[0] <= nums[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) { // stack.peek()[0] > nums[i], a[j] > a[k]
                int[] info = stack.peek();
                if (info[1] < nums[i]) {												// a[i] < a[k]
                    return true;
                }
            }
            smallest = Math.min(smallest, nums[i]);
            stack.push(new int[]{nums[i], smallest});
        }
        return false;
    }
}
```

T: O(n)		S: O(n)

---

#### Stack2

We scan from right to left and only store larger items in the stack.

Since we pop out smaller items of stack and we meet them before, the index of these items must be greater than current index.

**(k > j && a[k] < a[j])**

so we can update `a[k]` while poping out items from stack, and `a[j]` will be the top of stack.

If we meet an item smaller than `a[k]`, it could be `a[i]`, then we return true

```java
class Solution {
    public boolean find132pattern(int[] nums) {
        if (nums == null || nums.length == 0) return false;
        int n = nums.length;
        Stack<Integer> stack = new Stack<>();
        int ak = Integer.MIN_VALUE;
        for (int i = n - 1; i >= 0;  i--) {
            if (nums[i] < ak) return true;
            while (!stack.isEmpty() && stack.peek() < nums[i]) {
                ak = stack.pop();
            }
            stack.push(nums[i]);
        }
        return false;
    }
}
```

T: O(n)		S: O(n)





