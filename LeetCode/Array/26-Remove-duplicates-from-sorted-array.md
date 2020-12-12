---
title: Easy | Remove duplicates from sorted array 26
tags:
  - common
categories:
  - Leetcode
  - Array
date: 2019-07-16 23:37:12
---

Given a sorted array *nums*, remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each element appear only *once* and return the new length.

Do not allocate extra space for another array, you must do this by **modifying the input array in-place** with O(1) extra memory.

<!--more-->

**Example 1:**

```
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
```

**Example 2:**

```
Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
```

---

**My thoughts** 

Using two pointers to make a new array.

---

**First solution** 

*last* is a pointer to create the new array.

using *k* to indicate whether nums[i] is duplicated.

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int last = 0;
        for (int i = 0; i < nums.length; i += 1) {
            int k = 1;
            for (int j = 0; j <= last; j += 1) {
                if (nums[j] == nums[i]) {
                    k = 0;
                }    
            }
            if (k == 1) {
                nums[last + 1] = nums[i];
                last += 1;
            }
        }
        return last + 1;
    }
}
```

---

**Optimized** 

The given array is **sorted**, so we don't need to *for*-loop all the items of new array to indicate whether nums[i] is duplicated.

We just check whether the last item in new array is equal to nums[i].

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int last = 0;
        for (int i = 0; i < nums.length; i += 1) {
            if (nums[last] != nums[i]) {
                nums[last + 1] = nums[i];
                last += 1;
            }
        }
        return last + 1;  
    }
}
```

---

**Summary** 

Two pointer is a good way to solve array problems.

In this case, `last` and `i` are two pointers.