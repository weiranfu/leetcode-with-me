---
title: Medium | Find Latest Group of Size M 1562
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Union Find
date: 2020-08-24 12:12:18
---

Given an array `arr` that represents a permutation of numbers from `1` to `n`. You have a binary string of size `n` that initially has all its bits set to zero.

At each step `i` (assuming both the binary string and `arr` are 1-indexed) from `1` to `n`, the bit at position `arr[i]` is set to `1`. You are given an integer `m` and you need to find the latest step at which there exists a group of ones of length `m`. A group of ones is a contiguous substring of 1s such that it cannot be extended in either direction.

Return *the latest step at which there exists a group of ones of length **exactly*** `m`. *If no such group exists, return* `-1`.

[Leetcode](https://leetcode.com/problems/find-latest-group-of-size-m/)

<!--more-->

**Example 1:**

```
Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "00101", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "11101", groups: ["111", "1"]
Step 5: "11111", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.
```

**Example 2:**

```
Input: arr = [3,1,5,4,2], m = 2
Output: -1
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "10100", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "10111", groups: ["1", "111"]
Step 5: "11111", groups: ["11111"]
No group of size 2 exists during any step.
```

---

#### Union Find

Since we need to union current point with left and right points and maintain the size of each union, we should use a `size[]` and `count[]` to track the size of each union and the count number of each size of union.

We need to consider two sides together. 

```java
size[a] = 1 + size[left] + size[right];  // union together
```

And check `count[m] > 0` to get the last step.

We can add two dummy nodes to the head and tail of array.

```java
class Solution {
    int[] uf, size, count;
    int last;
    
    public int findLatestStep(int[] arr, int m) {
        int n = arr.length;
        uf = new int[n + 2];  // for head & tail elements
        for (int i = 0; i < n + 2; i++) uf[i] = i;
        size = new int[n + 2];
        count = new int[n + 1];
        last = -1;
        
        for (int i = 0; i < n; i++) {
            int a = arr[i];
            int left = find(a - 1), right = find(a + 1);
            count[size[left]]--; count[size[right]]--;
            size[a] = 1 + size[left] + size[right];  // union together
            count[size[a]]++;
            if (size[left] != 0) uf[left] = a; 
            if (size[right] != 0) uf[right] = a;
            if (count[m] > 0) last = i + 1;
        }
        return last;
    }
    
    private int find(int x) {
        if (uf[x] != x) {
            uf[x] = find(uf[x]);
        }
        return uf[x];
    }
}
```

T: O(n \* A(1))			S: (n)

---

#### Optimized: Use array to record the boundary

We could store the length of interval in the head and tail of this interval in `length[]`.

Each time we store left and right boundary in `length[]`.

```java
class Solution {
    public int findLatestStep(int[] arr, int m) {
        int n = arr.length;
        int[] length = new int[n + 2];
        int[] count = new int[n + 1];
        int last = -1;
        for (int i = 0; i < n; i++) {
            int a = arr[i];
            int left = length[a - 1], right = length[a + 1];
            count[left]--; count[right]--;
            int len = 1 + left + right;
            length[a - left] = len; length[a + right] = len; // left & right boudary
            count[len]++;
            if (count[m] > 0) last = i + 1;
        }
        return last;
    }
}
```

T: O(n)			S: O(n)



