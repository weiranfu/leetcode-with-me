---
title: Medium | Increasing triplet subsequence 334
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2019-07-25 14:33:04
---

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

> Return true if there exists *i, j, k* 
> such that *arr[i]* < *arr[j]* < *arr[k]* given 0 ≤ *i* < *j* < *k* ≤ *n*-1 else return false.

**Note:** Your algorithm should run in O(*n*) time complexity and O(*1*) space complexity.

[Leetcode](https://leetcode.com/problems/increasing-triplet-subsequence/)

<!--more-->

**Example 1:**

```
Input: [1,2,3,4,5]
Output: true
```

**Example 2:**

```
Input: [5,4,3,2,1]
Output: false
```

---

#### Tricky 

Keep two values when check all elements in the array, the minimum one and the second minimum one.

- If we find an item greater than s`econdMin`, return true;

- If we find an item greater than `min`, but smaller than `secondMin`, renew the `secondMin`.
- If we find an item smaller than `min`, renew the `min`. (you may wonder this works, **because we only care about whether there exists a triplet, we don't need to know exact triplet is, so we could renew and lose the `min` in the old triplet, and record the renewed `min` for the next triplet.**) 

We could set `min` and `secondMin` to Integer.MAX_VALUE, then we could go into the loop successfully.

If an item == `min` or `secondMin`, we could still renew them.

---

#### My thoughts 

Fail to solve.

---

#### First solution 

```java
class Solution {
    public boolean increasingTriplet(int[] nums) {
        int min = Integer.MAX_VALUE;
        int secondMin = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i += 1) {
            if (nums[i] <= min) {       // numns[i] <= min
                min = nums[i];
            } else if (nums[i] <= secondMin) {  // min < nums[i] <= secondMin
                secondMin = nums[i];
            } else {                   // nums[i] > secondMin
                return true;
            }   
        }
        return false; 
    }
}
```

T: O(n), S: O(1)

---

#### Summary 

We don't care about exact triplet is, we just care about if it exists.

So keep two values, `min` used to start a new triplet, `secondMin` to indicate whether the third item exists.