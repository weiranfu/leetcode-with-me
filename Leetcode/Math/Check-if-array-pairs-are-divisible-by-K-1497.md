---
title: Medium | Check If Array Pairs Are Divisible by K 1497
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-06-28 02:40:34
---

Given an array of integers `arr` of even length `n` and an integer `k`.

We want to divide the array into exactly `n / 2` pairs such that the sum of each pair is divisible by `k`.

Return *True* If you can find a way to do that or *False* otherwise.

[Leetcode](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/)

<!--more-->

**Example 1:**

```
Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
```

**Example 2:**

```
Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
```

**Example 3:**

```
Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
```

---

#### Tricky 

How to pair two numbers? According to their remainder after moduling K.

---

#### Standard solution  

```java
class Solution {
    public boolean canArrange(int[] arr, int k) {
        int n = arr.length;
        int[] cnt = new int[k];
        for (int a : arr) {
            int r = a % k;
            if (r < 0) r = r + k;
            cnt[r]++;
        }
        int l = 1, r = k - 1;
        while (l < r) {
            if (cnt[l] != cnt[r]) return false;
            l++;
            r--;
        }
        if (l == r) {
            if (cnt[l] % 2 != 0) return false;
        }
        return true;
    }
}
```

T: O(n)		S: O(n)