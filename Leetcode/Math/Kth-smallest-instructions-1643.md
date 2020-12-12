---
title: Hard | Kth Smallest Instructions 1643
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-11-26 22:30:30
---

Bob is standing at cell `(0, 0)`, and he wants to reach `destination`: `(row, column)`. He can only travel **right** and **down**. You are going to help Bob by providing **instructions** for him to reach `destination`.

The **instructions** are represented as a string, where each character is either:

- `'H'`, meaning move horizontally (go **right**), or
- `'V'`, meaning move vertically (go **down**).

Multiple **instructions** will lead Bob to `destination`. For example, if `destination` is `(2, 3)`, both `"HHHVV"` and `"HVHVH"` are valid **instructions**.

However, Bob is very picky. Bob has a lucky number `k`, and he wants the `kth` **lexicographically smallest instructions** that will lead him to `destination`. `k` is **1-indexed**.

Given an integer array `destination` and an integer `k`, return *the* `kth` **lexicographically smallest instructions** that will take Bob to* `destination`.

[Leetcode](https://leetcode.com/problems/kth-smallest-instructions/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/10/12/ex1.png)

```
Input: destination = [2,3], k = 1
Output: "HHHVV"
Explanation: All the instructions that reach (2, 3) in lexicographic order are as follows:
["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"].
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2020/10/12/ex2.png)**

```
Input: destination = [2,3], k = 2
Output: "HHVHV"
```

**Example 3:**

**![img](https://assets.leetcode.com/uploads/2020/10/12/ex3.png)**

```
Input: destination = [2,3], k = 3
Output: "HHVVH"
```

**Constraints:**

- `destination.length == 2`
- `1 <= row, column <= 15`
- `1 <= k <= nCr(row + column, row)`, where `nCr(a, b)` denotes `a` choose `b`.

---

#### Standard solution  

There're `C[m + n][m]` ways to reach `(m, n)` from `(0, 0)`.

How to find the `Kth` way to reach `(m, n)`? There're 10 ways to reach `(2, 3)`

`"HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"`

We can divide them into two parts: one that begins with `H`, one that begins with `V`

`"HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH" ||| "VHHHV", "VHHVH", "VHVHH", "VVHHH"`

**If the number of strings beginning with `H` is smaller than `k`, we should move `V` ,**

**else we should move `H`.**

The number of strings beginning with `H` is `C[m + n - 1][m]`

And then we can recursively compare remaining number of ways with `k` to determine the next char is `H` or `V`.

```java
class Solution {
    public String kthSmallestPath(int[] destination, int k) {
        int m = destination[0], n = destination[1];
        int[][] C = new int[m + n + 1][m + n + 1];
        C[0][0] = 1;
        for (int i = 1; i <= m + n; i++) {
            for (int j = 0; j <= i; j++) {
                if (j == 0) C[i][j] = 1;
                else C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
            }
        }
        StringBuilder res = new StringBuilder();
        for (int i = 1, lim = m + n; i <= lim; i++) {
          	// if we can move right, compare remains number ways with k
            if (n >= 1 && C[m + n - 1][m] >= k) { // n: number of right moves
                res.append('H');									// m: number of down moves
                n--;
            } else {
                res.append('V');
                if (n >= 1) k -= C[m + n - 1][m];
                m--;
            }
        }
        return res.toString();
    }
}
```

T: O((m+n)^2)		S: O(m\*n)