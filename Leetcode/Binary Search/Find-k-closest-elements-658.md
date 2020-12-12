---
title: Medium | Find K Closest Elements 658
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-06-27 19:21:10
---

Given a sorted array `arr`, two integers `k` and `x`, find the `k` closest elements to `x` in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

[Leetcode](https://leetcode.com/problems/find-k-closest-elements/)

<!--more-->

**Example 1:**

```
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
```

**Example 2:**

```
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
```

---

#### Tricky 

Assume we are taking `A[i] ~ A[i + k -1]`.
We can binary research `i`

We compare interval `A[mid] ~ A[mid + k - 1]` and `A[mid + 1] ~ A[mid + k]`

So we compare the distance between `x - A[mid]` and `A[mid + k] - x`

@vincent_gui listed the following cases:
Assume `A[mid] ~ A[mid + k]` is sliding window

case 1: x - A[mid] < A[mid + k] - x, need to move window go left
-------x----A[mid]-----------------A[mid + k]----------

case 2: x - A[mid] < A[mid + k] - x, need to move window go left again
-------A[mid]----x-----------------A[mid + k]----------

case 3: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]------------------x---A[mid + k]----------

case 4: x - A[mid] > A[mid + k] - x, need to move window go right
-------A[mid]---------------------A[mid + k]----x------

If `x - A[mid] > A[mid + k] - x`,
it means `A[mid + 1] ~ A[mid + k]` is better than `A[mid] ~ A[mid + k - 1]`,
So assign `left = mid + 1`.

---

#### Standard solution  

The right bound of `r` is `n - k`.

If we continues move `l` right, the return pos is `r`, `r + k - 1 == n - 1` => `r = n - k`

```java
class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> res = new ArrayList<>();
        if (arr == null || arr.length == 0) return res;
        int n = arr.length;
        int l = 0, r = n - k;      // r bound: l moves right until r
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (arr[mid + k] - x >= x - arr[mid]) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return Arrays.stream(arr, l, l + k).boxed().collect(Collectors.toList());
    }
}
```

T: O(logn)		S: O(1)

---

#### Summary 

To Binary search an interval, we need to compare two intervals.