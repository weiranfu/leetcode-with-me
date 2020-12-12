---
title: Easy | Merge Sorted Array 88
tags:
  - common
categories:
  - Leetcode
  - Array
date: 2020-01-12 11:30:41
---

Given two sorted integer arrays *nums1* and *nums2*, merge *nums2* into *nums1* as one sorted array.

[Leetcode](https://leetcode.com/problems/merge-sorted-array/)

<!--more-->

**Note:**

- The number of elements initialized in *nums1* and *nums2* are *m* and *n* respectively.
- You may assume that *nums1* has enough space (size that is greater or equal to *m* + *n*) to hold additional elements from *nums2*.

**Example:**

```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

---

#### My thoughts 

In-place Merge Sort.

Move all elements in `nums1` back to the tail of array.

Then merge two arrays.

---

#### First solution 

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int size = nums1.length;
        int p = size - 1;
        for (int i = m - 1; i >= 0; i--) {
            nums1[p] = nums1[i];
            p--;
        }
        p++;
        int q = 0;
        int i = 0;
        while (p < size && q < n) {
            if (nums1[p] < nums2[q]) {
                nums1[i++] = nums1[p++];
            } else {
                nums1[i++] = nums2[q++];
            }
        }
        while (p < size) {
            nums1[i++] = nums1[p++];
        }
        while (q < n) {
            nums1[i++] = nums2[q++];
        }
    }
}
```

T: O(m + n) 				S: O(1)

---

#### Optimized 

We can merge from the tail to head.

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
        // while (i >= 0) {             // We don't need to merge lefted nums1,
        //     nums1[k--] = nums1[i--]; // because it is at head of nums1 and sorted.
        // }
        while (j >= 0) {
            nums1[k--] = nums2[j--];
        }
    }
}
```

T: O(m + n) 			S: O(1)

---

#### Summary 

In place merge sort for array.