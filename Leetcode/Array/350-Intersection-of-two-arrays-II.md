---
title: Easy | Intersection of Two Arrays II 350
tags:
  - implement
categories:
  - Leetcode
  - Array
date: 2020-01-14 19:51:44
---

Given two arrays, write a function to compute their intersection.

[Leetcode](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

<!--more-->

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
```

**Note:**

- Each element in the result should appear as many times as it shows in both arrays.
- The result can be in any order.

**Follow up:**

- What if *nums1*'s size is small compared to *nums2*'s size? Which algorithm is better?

  Put items in nums1into map rather than nums2.

- What if elements of *nums2* are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

  If both nums1 and nums2 are so huge that neither fit into the memory, sort them individually (external sort), then read 2 elements from each array at a time in memory, record intersections.

---

#### Implement

How to copy an array?

`Arrays.copyOfRange(array, 0, k)`

---

#### Map 

Use a map to count numbers of items in an array.

```java
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return intersect(nums2, nums1);
        }
        HashMap<Integer, Integer> m = new HashMap<>();
        for (int n : nums1) {
            m.put(n, m.getOrDefault(n, 0) + 1);
        }
        int k = 0;
        for (int n : nums2) {
            int cnt = m.getOrDefault(n, 0);
            if (cnt > 0) {
                nums1[k++] = n;
                m.put(n, cnt - 1);
            }
        }
        return Arrays.copyOfRange(nums1, 0, k);
    }
}
```

T: O(n + m) 			S: O(m)

---

#### Sort 

```java
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int p = 0;
        int q = 0;
        int r = 0;
        while (p < nums1.length && q < nums2.length) {
            if (nums1[p] == nums2[q]) {
                nums1[r++] = nums1[p++];
                q++;
            } else if (nums1[p] > nums2[q]) {
                q++;
            } else {
                p++;
            }
        }
        return Arrays.copyOfRange(nums1, 0, r);
    }
}
```

T: O(nlogn)				S: O(m)

---

#### Summary

Use `Arrays.copyOfRange(a, 0, k)` to copy an array.