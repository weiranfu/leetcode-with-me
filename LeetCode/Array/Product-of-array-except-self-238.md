---
title: Medium | Product of Array Except Self 238
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-06-23 02:32:24
---

Given an array `nums` of *n* integers where *n* > 1,  return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

Node: *Please solve it without using division and in O(n)*

[Leetcode](https://leetcode.com/problems/product-of-array-except-self/)

<!--more-->

**Example:**

```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```

**Follow up:** Could you devise a solution using constant space complexity?

---

#### Tricky 

* Prefix and suffix array
* We could calculate prefix and suffix and save partial product into res[] so that we achieve O(1) space.

---

#### Prefix and Suffix array

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        if (nums == null || nums.length == 0) return new int[0];
        int n = nums.length;
        int[] res = new int[n];
        int[] prefix = new int[n + 1];
        int[] suffix = new int[n + 1];
        prefix[0] = 1;
        suffix[n] = 1;
        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }
        for (int i = n - 1; i >= 0; i--) {
            suffix[i] = suffix[i + 1] * nums[i];
        }
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                res[i] = suffix[i + 1];
            } else if (i == n - 1) {
                res[i] = prefix[i];
            } else {
                res[i] = prefix[i] * suffix[i + 1];
            }
        }
        return res;
    }
}
```

T: O(n)		S: O(n)

---

#### Optimized

Save partial result into res array.

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        if (nums == null || nums.length == 0) return new int[0];
        int n = nums.length;
        int[] res = new int[n];
        Arrays.fill(res, 1);
        int prefix = 1;
        int suffix = 1;
        for (int i = 0; i < n; i++) {
            if (i != 0) res[i] = prefix;
            prefix *= nums[i];
        }
        for (int i = n - 1; i >= 0; i--) {
            if (i != n - 1) res[i] *= suffix;
            suffix *= nums[i];
        }
        return res;
    }
}
```

T: O(n)		S: O(1)

