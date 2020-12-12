---
title: Easy | Power of Two 231
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Bit
date: 2020-06-22 23:36:20
---

Given an integer, write a function to determine if it is a power of two.

[Leetcode](https://leetcode.com/problems/power-of-two/)

<!--more-->

**Example 1:**

```
Input: 1
Output: true 
Explanation: 20 = 1
```

**Example 2:**

```
Input: 16
Output: true
Explanation: 24 = 16
```

**Example 3:**

```
Input: 218
Output: false
```

---

#### Tricky 

We could use `x & (x - 1)` to flip the least significant `1` to `0`

---

#### Standard solution  

```java
class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) return false;
        return (n & (n - 1)) == 0;
    }
}
```

T: O(1)		S: O(1)

