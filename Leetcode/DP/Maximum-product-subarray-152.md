---
title: Hard | Maximum Product Subarray 152
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-05-30 18:01:42
---

Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.

[Leetcode](https://leetcode.com/problems/maximum-product-subarray/)

<!--more-->

**Example 1:**

```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

**Example 2:**

```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

**Follow up**

[Maximum Length of Subarray with Positive Product](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/)

---

#### My thoughts 

Failed to solve.

---

#### Two pass 

Let's see if there's no negative number and zero in the array, the max product must include all elements.

**If there exist negative number, then there're two cases: odd negative or even negative numbers.**

If there're even negative numbers, then max product includes all elements. 

If there're odd negative numbers, the max product must includes all elements to the end seperated by that negative numbers. For example, `[1,-1,2,-3,4,-1,2]`, the max product must be `[1] or [2,-3,4,-1,2] or [1,-1,2,-3,4] or [2]`.

If there exists zero, that zero also seperates array into two part. 

Scan from left and right in two direction. Calculate the product and store the max while scanning.

If we meet 0, we reset product into 1. `(left == 0 ? 1 : left)`

```java
class Solution {
    public int maxProduct(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        int left = 1;
        int right = 1;
        int res = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            left *= nums[i];
            right *= nums[n - i - 1];
            res = Math.max(res, Math.max(left, right));
          	if (left == 0) left = 1;
          	if (right == 0) right = 1;
        }
        return res;
    }
}
```

T: O(n)		S: O(1)

---

#### DP

We could store the max and min while scanning array.

**The max cumulative product UP TO current element starting from SOMEWHERE in the past, and the minimum cumulative product UP TO current element . it would be easier to see the DP structure if we store these 2 values for each index, like maxProduct[i],minProduct[i] .**

**At each new element, u could either add the new element to the existing product, or start fresh the product from current index (wipe out previous results), hence the 2 Math.max() lines.**

if we see a negative number, the "candidate" for max should instead become the previous min product, because a bigger number multiplied by negative becomes smaller, hence the swap() min and max.

```java
class Solution {
    public int maxProduct(int[] nums) {
        int res = Integer.MIN_VALUE;
        int imax = 1, imin = 1;
        for (int i = 0; i < nums.length; i++) {
            // swap max and min if nums[i] < 0
            if (nums[i] < 0) {
                int tmp = imax;
                imax = imin;
                imin = tmp;
            }
           // max/min product for the current number is either the current number itself
            // or the max/min by the previous number times the current one
            imax = Math.max(nums[i], imax * nums[i]);
            imin = Math.min(nums[i], imin * nums[i]);
            res = Math.max(res, imax);
        }
        return res;
    }
}
```

T: O(n)		S: O(1)

