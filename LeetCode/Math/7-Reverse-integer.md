---
title: Easy | Reverse Integer 7
tags:
  - tricky
categories:
  - Leetcode
  - Math
date: 2019-11-27 00:06:36
---

Given a 32-bit signed integer, reverse digits of an integer.

[Leetcode](https://leetcode.com/problems/reverse-integer/)

<!--more-->

**Example 1:**

```
Input: 123
Output: 321
```

**Example 2:**

```
Input: -123
Output: -321
```

**Example 3:**

```
Input: 120
Output: 21
```

**Note:**
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

---

#### Tricky 

How to detect overflows with range [−2^31,  2^31 − 1] ?

* compare num with the privious one. If overflow exists, the new num will not equal previous one.

  This is only valid for `res * 10` causes overflow in `res = res * 10 + tail`, if `+ tail` causes overflow, it doesn't work. Because overflow is a cycle.

* Or we can use long type to detect overflow.

---

#### My thoughts 

Construct reverse integer using `\ and %`.

---

#### First solution 

```java
class Solution {
    public int reverse(int x) {
        int res = 0;
        while (x != 0) {
            int newInt = res * 10 + x % 10;
            if ((newInt - x % 10) / 10 != res) { // if they aren't equal, overflow!
                return 0;
            }
            res = newInt;
            x = x / 10;
        }
        return res;
    }
}
```

T: O(n) S: O(1)

---

#### Long type

Use long type. 

```java
class Solution {
    public int reverse(int x) {
        long res = 0;
        while (x != 0) {
            res = res * 10 + x % 10;
            if (res > Integer.MAX_VALUE || res < Integer.MIN_VALUE) {
                return 0;
            }
            x = x / 10;
        }
        return (int) res;
    }
}
```

T: O(n) S: O(1)

---

#### Summary 

How to detect overflows with range [−2^31,  2^31 − 1] ?

- compare num with the privious one. If overflow exists, the new num will not equal previous one.
- Or we can use long type to detect overflow.