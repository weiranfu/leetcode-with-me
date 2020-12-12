---
title: Medium | Bitwise AND of Numbers Range 201
tags:
  - tricky
categories:
  - Leetcode
  - Bit
date: 2020-06-06 14:57:48
---

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

[Leetcode](https://leetcode.com/problems/bitwise-and-of-numbers-range/)

<!--more-->

**Example 1:**

```
Input: [5,7]
Output: 4
```

**Example 2:**

```
Input: [0,1]
Output: 0
```

---

#### Tricky 

We could iterate all the numbers one by one to get result, however this will cause TLE.

![pic](https://leetcode.com/problems/bitwise-and-of-numbers-range/Figures/201/201_prefix.png)

**In the above example, one might notice that after the AND operation on all the numbers, the remaining part of bit strings is the *common prefix* of all these bit strings.**

* Bit shift: shift `m` and `n` one bit right until they're equal.
* Bit flip: `n = n & (n - 1)` flip `n`'s least significant `1` into `0` until `m >= n`

---

#### My thoughts 

LTE

---

#### Bit shift

shift `m` and `n` one bit right until they're equal to find common prefix of `m` and `n`

```java
class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        int cnt = 0;
        while (m != n) {
            m >>= 1;
            n >>= 1;
            cnt++;
        }
        return m << cnt;
    }
}
```

T: O(1)		S: O(1)

---

#### Flip least significant 1

Use `n = n & (n - 1)` to flip `n`'s least significant `1` into `0` until `m >= n`, then the common prefix is `n`

```java
class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        while (m < n) {
            n = n & (n - 1);
        }
        return n;
    }
}
```

T: O(1)		S: O(1)

