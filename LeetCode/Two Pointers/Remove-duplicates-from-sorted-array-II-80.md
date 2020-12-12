---
title: Medium | Remove duplicates from sorted array II 80
tags:
  - common
  - tricky
  - Oh-shit
categories:
  - Leetcode
  - Two Pointers
date: 2019-07-16 23:56:17
---

Given a sorted array *nums*, remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that duplicates appeared at most *twice* and return the new length.

Do not allocate extra space for another array, you must do this by **modifying the input array in-place** with O(1) extra memory.

<!--more-->

**Example 1:**

```
Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
```

**Example 2:**

```
Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
```

**Follow up:**  

* This is a follow up problem to [Remove duplicates from sorted array](https://aranne.github.io/2019/07/19/26-Remove-duplicates-from-sorted-array/).
* Duplicates can appear twice now.

---

#### Two pointers

Keep a `index` pointer to current available position.

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2) return nums.length;
        int n = nums.length;
        int cnt = 1;
        int curr = nums[0];
        int index = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] == curr) {
                cnt++;
            } else {
                cnt = 1;
                curr = nums[i];
            }
            if (cnt <= 2) nums[index++] = curr;
        }
        return index;
    }
}
```

T: O(n)			S: O(1)