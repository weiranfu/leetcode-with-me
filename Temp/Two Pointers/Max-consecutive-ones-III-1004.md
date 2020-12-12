---
title: Medium | Max Consecutive Ones III 1004
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-07-28 17:14:40
---

Given an array `A` of 0s and 1s, we may change up to `K` values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

[Leetcode](https://leetcode.com/problems/max-consecutive-ones-iii/)

<!--more-->

**Example:**

```
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
```

---

#### Sliding Window 

The longest window size with **at most K** zeroes in the window.

```java
class Solution {
    public int longestOnes(int[] A, int K) {
        int n = A.length;
        int res = 0;
        for (int i = 0, j = 0; i < n; i++) {
            if (A[i] == 0) K--;
            while (j <= i && K < 0) {
                if (A[j] == 0) K++;
                j++;
            }
            res = Math.max(res, i - j + 1);
        }
        return res;
    }
}
```

T: O(n)			S: O(n)

---

#### Sliding Window II

We can solve this problem a little efficiently. Since we have to find the MAXIMUM window, we never reduce the size of the window. We either increase the size of the window or remain same but never reduce the size.

```java
class Solution {
    public int longestOnes(int[] A, int K) {
        int n = A.length;
        int i, j;
        for (i = 0, j = 0; i < n; i++) {
            if (A[i] == 0) K--;
            if (K < 0) {
                if (A[j] == 0) K++;
                j++;
            }
        }
        return i - j;			// final window size
    }
}
```

T: O(n)			S: O(n)

