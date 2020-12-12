---
title: Easy | Kth Missing Positive Number 1539
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-10-29 11:29:42
---

Given an array `arr` of positive integers sorted in a **strictly increasing order**, and an integer `k`.

*Find the* `kth` *positive integer that is missing from this array.*

[Leetcode](https://leetcode.com/problems/kth-missing-positive-number/)

<!--more-->

**Example 1:**

```
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
```

**Example 2:**

```
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
```

**Constraints:**

- `1 <= arr.length <= 1000`
- `1 <= arr[i] <= 1000`
- `1 <= k <= 1000`
- `arr[i] < arr[j]` for `1 <= i < j <= arr.length`

---

#### Brute Force 

```java
class Solution {
    public int findKthPositive(int[] arr, int k) {
        int n = arr.length;
        int expect = 1;
        int missCnt = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] != expect) {
                missCnt++;
                if (missCnt == k) return expect;
                i--;
            }
            expect++;
        }
        for (int i = 0; i < k - missCnt - 1; i++) {
            expect++;
        }
        return expect;
    }
}
```

T: O(n)			S: O(1)

---

#### Binary Search

Since we are expecting integers in array `[1, 2, 3, 4, 5, …]`, we could use binary search to determine the missing numbers.

`if (arr[mid] - (mid + 1) < k)`, the missing number is small, we update `l = mid + 1`

else we update `r = mid`

When we exit the loop, `l` means current expecting number is `l + 1`, the kth missing number is `l + 1 + (k - 1) = l + k`.

```java
class Solution {
    public int findKthPositive(int[] arr, int k) {
        int n = arr.length;
        int l = 0, r = n;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (arr[mid] - (mid + 1) < k) l = mid + 1;
            else r = mid;
        }
        return l + k;
    }
}
```

T: O(logn)			S: O(1)