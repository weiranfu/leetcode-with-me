---
title: Medium | Divide Two Integers 29
tags:
  - tricky
categories:
  - Leetcode
  - Bit
date: 2020-01-25 00:17:24
---

Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing `dividend` by `divisor`.

The integer division should truncate toward zero.

[Leetcode](https://leetcode.com/problems/divide-two-integers/)

<!--more-->

**Example 1:**

```
Input: dividend = 10, divisor = 3
Output: 3
```

**Example 2:**

```
Input: dividend = 7, divisor = -3
Output: -2
```

**Note:**

- Both dividend and divisor will be 32-bit signed integers.
- The divisor will never be 0.
- Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

---

#### Tricky 

1. We cannot use multiple, divide and mod. We can use plus and minus. So we need to minus subtractor and this subtractor needs to grow by 2.

```java
while (dividend - (subtractor + subtractor) >= 0 ) {
    subtractor += subtractor;
}
```

2. We also need to handle overflow.

   Let's see the only case that can cause overflow is `dividend == Integer.MIN_VALUE && divisor == -1`.

   Or we can use long type.

3. We can use bit manipulation to implement mutilple.

---

#### My thoughts 

Use subtractor and base to store the largest subtractor and base divisor.

```java
class Solution {
    public int divide(int divident, int divisor) {
        long res = divideLong((long) divident, (long) divisor);
        if (res > Integer.MAX_VALUE || res < Integer.MIN_VALUE) return Integer.MAX_VALUE;
        return (int) res;
    }
    public long divideLong(long dividend, long divisor) {
        int sign = (dividend >= 0) == (divisor >= 0) ? 1 : -1;
        long divd = Math.abs(dividend);
        long divs = Math.abs(divisor);
        return sign * divideHelper(divd, divs, divs, 1);
    }
    private long divideHelper(long dividend, long divisor, long subtractor, long base) {
        if (dividend < divisor) return 0;
        if (dividend < subtractor) {  // Reset subtractor back to divisor.
            return divideHelper(dividend, divisor, divisor, 1);
        }
        return base + divideHelper(dividend - subtractor, divisor, subtractor + subtractor, base + base);
    }
}
```

T: O(logn)			S: O(logn)

---

#### Iterative 

Always find the largest subtractor and subtract it.

The only case that can cause overflow is `dividend == Integer.MIN_VALUE && divisor == -1`. So we don't need to use long type.

Mind that if `dividend == Integer.MIN_VALUE && divisor == -2`,  we can still use

`a = Math.abs(Integer.MIN_VALUE`**(overflow)** and get `a == Integer.MIN_VALUE`. 

But `a - subtractor ` will be positive, this solution will work.

```java
class Solution {
    public int divide(int dividend, int divisor) {
        if(dividend == Integer.MIN_VALUE && divisor == -1){
            return Integer.MAX_VALUE;
        }
        int sign = (dividend >= 0) == (divisor >= 0) ? 1 : -1;
        int a = Math.abs(dividend);
        int b = Math.abs(divisor);
        int res = 0;
        while(a - b >= 0){
            int substractor = b;
            int base = 1;
            while (a - (substractor << 1) >= 0) { 
                substractor = substractor << 1;  // substractor * 2 everytime
                base = base << 1;              // base * 2 everytime
            }
            a -= substractor;
            res += base;
        }
        return sign * res;
    }
}
```

T: O(logn)			S: O(1)

---

#### Optimized

We can use x to store how many bit we need to move left.

```java
class Solution {
    public int divide(int dividend, int divisor) {
        if(dividend == Integer.MIN_VALUE && divisor == -1){
            return Integer.MAX_VALUE;
        }
        int sign = (dividend >= 0) == (divisor >= 0) ? 1 : -1;
        int a = Math.abs(dividend);
        int b = Math.abs(divisor);
        int res = 0;
        while(a - b >= 0){
            int x = 0;
            while (a - (b << 1 << x) >= 0) {
                x++;
            }
            a -= b << x;
            res += 1 << x;
        }
        return sign * res;
    }
}
```

T: O(logn)			S: O(1)

---

#### Summary 

Bit manipulation can implement mutilple two easily.

