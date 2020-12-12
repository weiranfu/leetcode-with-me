---
title: Easy | Detect Pattern of Length M Repeated K or More Times 1566
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-09-03 11:55:19
---

Given an array of positive integers `arr`,  find a pattern of length `m` that is repeated `k` or more times.

A **pattern** is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times **consecutively** without overlapping. A pattern is defined by its length and the number of repetitions.

Return `true` *if there exists a pattern of length* `m` *that is repeated* `k` *or more times, otherwise return* `false`.

[Leetcode](https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/)

<!--more-->

**Example 1:**

```
Input: arr = [1,2,4,4,4,4], m = 1, k = 3
Output: true
Explanation: The pattern (4) of length 1 is repeated 4 consecutive times. Notice that pattern can be repeated k or more times but not less.
```

**Example 2:**

```
Input: arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
Output: true
Explanation: The pattern (1,2) of length 2 is repeated 2 consecutive times. Another valid pattern (2,1) is also repeated 2 times.
```

---

#### Brute Force

Iterate the start pointer `i` from `i = 0, i + k * m <= n`,

then iterate the startt pointer `j` to check `k` same pairs.

If we find a difference between two chars, break the iteration and check next `i`.

```java
class Solution {
    public boolean containsPattern(int[] arr, int m, int k) {
        int n = arr.length;
        if (k * m > n) return false;
        for (int i = 0; i + k * m <= n; i++) {
            int cnt = 1;
            boolean ok = true;
            outer:
            for (int j = i + m; cnt < k; cnt++, j += m) {
                for (int t = 0; t < m; t++) {
                    if (arr[i + t] != arr[j + t]) {
                        ok = false;
                        break outer;
                    }
                }
            }
            if (ok) return true;
        }
        return false;
    }
}
```

T: O(n\*k\*m)			S: O(1)

---

#### Optimized

We check a pair of chars with distance `m`, each time we find a mismatch, we reset the count to 0.

Once we accumulate `count == (k - 1) * m`, return true.

```java
class Solution {
    public boolean containsPattern(int[] arr, int m, int k) {
        int n = arr.length;
        int cnt = 0;
        for (int i = 0; i + m < n; i++) {
            if (arr[i] == arr[i + m]) cnt++;
            else cnt = 0;
            if (cnt == (k - 1) * m) return true;
        }
        return false;
    }
}
```

T: O(n)			S: O(1)

