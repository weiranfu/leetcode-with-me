---
title: Medium | Find the duplicate number 287
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2019-07-26 12:36:36
---

Given an array *nums* containing *n* + 1 integers where each integer is between 1 and *n*(inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

[Leetcode](https://leetcode.com/problems/find-the-duplicate-number/)

<!--more-->

**Example 1:**

```
Input: [1,3,4,2,2]
Output: 2
```

**Example 2:**

```
Input: [3,1,3,4,2]
Output: 3
```

**Note:**

1. You **must not** modify the array (assume the array is read only).
2. You must use only constant, *O*(1) extra space.
3. Your runtime complexity should be less than *O*(*n*2).
4. There is only one duplicate number in the array, but it could be repeated more than once.

**Follow up:** 

This is a follow up problem of [Linked List Cycle II](https://aranne.github.io/2019/07/26/142-Linked-list-cycle-II/#more)

* How can an array convert to a linked list?
* Why does an duplicate in an array mean a cycle in a linked list?

---

#### Tricky 

1. Build the model.

When an item `i` in array uses its value `v` pointing to another item in position `v`, then the array becomes a linked list.

index [0, 1, 2, 3]                                                                      index [0, 1, 2, 3]

value [1, 2, 3, 4]                                                                      value  [2, 4, 3, 1]

linked list: 1 -> 2 -> 3 -> 4 -> null.                                         linked list: 2 -> 3 -> 1 -> 4 -> null.

The last item always points to null, however if we make our array `nums[n]` to `nums[n + 1]` which still has `n` numbers(there must be a duplicate), the linked list will have a cycle in it.

index [0, 1, 2, 3, 4]

value [2, 4, 3, 1, 3]

linked list: 2 -> 3 -> 1 -> 4 -> 3 -> 1 -> 4 -> 3 -> ….          The cycle is 3 -> 1 -> 4

The entry of this cycle is 3 which is the duplicate we want to find.

2. Find the entry.

Use `fast` and `slow` pointers to find the entry of the cycle.

Everytime `slow` moves one step, `fast` moves two step.  `slow = nums[slow]`, `fast = nums[nums[fast]]`.

When `fast` catches up `slow`, they meet at `meetpoint` in the cycle.

We assume the distance between `start position 0`  to the `entry` is x, the distance between `entry` to the `meetpoint` is `a`, the whole cycle is `c`.

So, `fast` moves `x + n*c + a`, `slow` moves `x + a`. And `fast` moves twice steps as `slow`, 

So we get  `2 * (x + a) = x + n*c + a` => `x = n*c - a` 

`x` is what we want to caculate the entry.

`x = n*c - a` => `x = (n-1)*c + (c-a)`  

So we could use two new pointer, one starts at `start position 0`, the other starts at `meetpoint`, and their velocity is same. So they must meet at the `entry`!

Because one moves `x` steps to the entry, the other one moves `(c-a) + n*c` steps to the entry. 

---

#### My thoughts 

Failed to solve.

---

#### Standard solution 

After we get the `meetpoint` in the cycle, we put `fast` back to position `0`, and make `fast` and `slow` move at same velocity. Next time they must meet at `entry` which is the duplicate.

```java
class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0;
        int fast = 0;
        if (nums.length < 2) {
            return -1;
        }
        // Phase 1: find the meetpoint in the cycle.
        slow = nums[slow];
        fast = nums[nums[fast]];
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[nums[fast]];
        }
        // Phase 2: find the entry of the cycle.
        fast = 0;// Put fast back to 0.
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];// Same velocity.
        }
        return fast;
    }
}
```

T: O(n), S: O(1)

---

#### Summary 

To find the entry of cycle in a linked list, we could use two pointers twice,

First to find the meetpoint (`fast` is twice faster than `slow`)

Second find the entry (`fast` is same as `slow`)