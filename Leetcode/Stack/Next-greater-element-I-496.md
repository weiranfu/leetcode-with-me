---
title: Easy | Next Greater Element I 496
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-07-27 22:36:09
---

You are given two arrays **(without duplicates)** `nums1` and `nums2` where `nums1`’s elements are subset of `nums2`. Find all the next greater numbers for `nums1`'s elements in the corresponding places of `nums2`.

The Next Greater Number of a number **x** in `nums1` is the first greater number to its right in `nums2`. If it does not exist, output -1 for this number.

[Leetcode](https://leetcode.com/problems/next-greater-element-i/)

<!--more-->

**Example:**

```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
```

**Follow up:** 

[Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)

[Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)

---

#### Stack

This is a typical problem **Find the next greater element**

Use a map to store the index of elements in `nums1`.

```java
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums1.length; i++) {
            map.put(nums1[i], i);
        }
        int[] res = new int[nums1.length];
        Stack<Integer> stack = new Stack<>();
        for (int i = nums2.length - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= nums2[i]) {
                stack.pop();
            }
            if (map.containsKey(nums2[i])) {
                res[map.get(nums2[i])] = stack.isEmpty() ? -1 : stack.peek();
            }
            stack.push(nums2[i]);
        }
        return res;
    }
}
```

T: O(m + n)		S: O(m + n)

