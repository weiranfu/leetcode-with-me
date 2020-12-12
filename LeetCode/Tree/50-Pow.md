---
title: Medium | Pow(x, n) 50
tags:
  - common
  - tricky
  - corner case
categories:
  - Leetcode
  - Tree
date: 2020-05-11 16:58:35
---

Implement [pow(*x*, *n*)](http://www.cplusplus.com/reference/valarray/pow/), which calculates *x* raised to the power *n* (x^n).

[Leetcode](https://leetcode.com/problems/powx-n/)

<!--more-->

**Example 1:**

```
Input: 2.00000, 10
Output: 1024.00000
```

**Example 2:**

```
Input: 2.10000, 3
Output: 9.26100
```

**Example 3:**

```
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
```

**Note:**

- -100.0 < *x* < 100.0
- *n* is a 32-bit signed integer, within the range [−231, 231 − 1]

---

#### Tricky 

We could compute it in O(logN).

`x^n = (x * x)^(n / 2)`

#### Corner Case

Note the overflow cases when `n == Integer.MIN_VALUE`.

`-n` will be overflow.

---

#### Binary Search 

```java
class Solution {
    public double myPow(double x, int n) {
        if (n == 0) {
            return 1;
        }
        if (n == Integer.MIN_VALUE) {
            x = x * x;
            n = n / 2;
        }
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        if (n % 2 == 0) {
            return myPow(x * x, n / 2);
        } else {
            return myPow(x * x, n / 2) * x;
        }
    }
}
```

T: O(logn)		S: O(1)

---

#### Quick Pow

To avoid overflow, we could also use `long`

```java
class Solution {
    public double myPow(double x, int n) {
        double res = 1.0;
        long p = n;     // avoid overflow
        if (p < 0) {
            p = -p;
            x = 1 / x;
        }
        while (p > 0) {
            if ((p & 1) == 1) {
                res *= x;
            }
            x *= x;
            p >>= 1;
        }
        return res;
    }
}
```

T: O(logn)		S: O(1)