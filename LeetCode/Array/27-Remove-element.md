---
title: Easy | Remove element 27
tags:
  - common
categories:
  - Leetcode
  - Array
date: 2019-07-16 22:02:53
---

Given an array *nums* and a value *val*, remove all instances of that value [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) and return the new length.

Do not allocate extra space for another array, you must do this by **modifying the input array in-place** with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

<!--more-->

**Example 1** 

```
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
```

**Example 2** 

```
Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
```

---

**My thoughts** 

Using a pointer to point the last item in array.

Exchange the target item with the last item.

---

**First solution** 

using *last* pointer, *for* loop from 0 to last.

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int last = nums.length - 1;
        for (int i = 0; i <= last; i += 1) {
            if (nums[i] == val) {
                int temp = nums[i];
                nums[i] = nums[last];
                nums[last] = temp;
                last -= 1;
                i -= 1;      // re-check the nums[i]
            }
        }
        return last + 1;
    }
}
```

---

**Optimized** 

don't need to exchange two items.

just give value of last item to nums[i].

```java
        for (int i = 0; i <= last; i += 1) {
            if (nums[i] == val) {
                nums[i] = nums[last];
                last -= 1;
                i -= 1;      // re-check the nums[i]
            }
        }
```

---

**Summary** 

one may get confused by the term "in-place" and think it is impossible to remove an element from the array without making a copy of the array.

The answer is to use a pointer.