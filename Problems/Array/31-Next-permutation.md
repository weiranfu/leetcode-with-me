---
title: Medium | Next Permutation 31
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-01-25 19:15:14
---

Implement **next permutation**, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

[Leetcode](https://leetcode.com/problems/next-permutation/)

<!--more-->

The replacement must be **in-place** and use only constant extra memory.

```
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
```

---

#### Tricky 

How to find next permutation?

1. Find the smallest index `i` such that `nums[i - 1] < nums[i]`. If no such index exists, just reverse `nums` and done.
2. Find the smallest item `nums[j]` larger than `nums[i - 1]`
3. Swap `nums[i - 1]` and `nums[j]`.
4. Reverse the sub-array `nums[i:]`

---

#### First solution 

```java
class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        for (int i = n - 1; i > 0; i--) {
            if (nums[i - 1] < nums[i]) {
                int j;
                for (j = n - 1; j >= i; j--) {  // Find the smallest item larger than nums[i - 1]
                    if (nums[j] > nums[i - 1]) break;
                }
                swap(nums, i - 1, j);
                reverse(nums, i, n - 1);
                return;
            }
        }
        reverse(nums, 0, n - 1);
        return;
    }
    private void reverse(int[] nums, int s, int e) {
        while (s < e) {
            swap(nums, s, e);
            s++;
            e--;
        }
    }
    private void swap(int[] nums, int a, int b) {
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }
}
```

T: O(n^2)		S: O(1)

---

#### Summary 

In tricky.