---
title: Easy | Number of 1 Bits 191
tags:
  - tricky
categories:
  - Leetcode
  - Bit
date: 2020-06-05 23:54:49
---

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the [Hamming weight](http://en.wikipedia.org/wiki/Hamming_weight)).

[Leetcode](https://leetcode.com/problems/number-of-1-bits/)

<!--more-->

**Example:**

```
Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
```

---

#### Tricky 

Flip least significant `1` into `0`: `n = n & (n - 1)`.

---

#### Find all `1`

```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            int bit = n & 1;
            if (bit == 1) {
                res++;
            }
            n >>= 1;
        }
        return res;
    }
}
```

T: O(1)		S: O(1)

---

#### Flip all `1`

Fliping all `1` is a little faster than finding all `1`.

```java
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int res = 0;
        while (n != 0) {
            res++;
            n = n & (n - 1);
        }
        return res;
    }
}
```

T: O(1)	 	S: O(1)



