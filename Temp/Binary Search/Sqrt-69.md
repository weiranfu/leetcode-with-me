---
title: Easy | Sqrt(x) 69
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - Binary Search
date: 2020-01-12 11:13:22
---

Implement `int sqrt(int x)`.

Compute and return the square root of *x*, where *x* is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

[Leetcode](https://leetcode.com/problems/sqrtx/)

<!--more-->

**Example 1:**

```
Input: 4
Output: 2
```

**Example 2:**

```
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
```

---

#### Tricky 

We can use binary search in all positive integers.

#### Corner Case

Take care of overflow problems! 

Use `int mid = left + (right - left) / 2`,  `mid <= x / mid`.

---

#### Brute Force 

```java
class Solution {
    public int mySqrt(int x) {
        int i = 1;
        while (i <= x / i) {
            i++;
        }
        return i - 1;
    }
}
```

T: O(n) 			S: O(1)

---

#### Binary Search

Use binary search to search all positive integers.

```java
class Solution {
    public int mySqrt(int x) {
        int l = 1, r = Integer.MAX_VALUE;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (mid <= x / mid) {  // mid * mid <= x will overflow
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l - 1;
    }
}
```

T: O(logn) 				S: O(1)

2. Or we could use `long` to avoid overflow

```java
class Solution {
    public int mySqrt(int x) {
        long l = 0, r = x;
        while (l < r) {
            long mid = l + (r - l + 1) / 2;
            if (mid <= x / mid) {
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        return (int)l;
    }
}
```

T: O(logn)		S: O(1)