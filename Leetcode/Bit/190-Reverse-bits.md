---
title: Easy | Reverse Bits 190
tags:
  - tricky
categories:
  - Leetcode
  - Bit
date: 2020-06-05 22:55:58
---

Reverse bits of a given 32 bits unsigned integer.

[Leetcode](https://leetcode.com/problems/reverse-bits/)

<!--more-->

**Example:**

```
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
```

---

#### Tricky 

* Bit manipulation: Get `k` and `31 - k` bit, clear them, swap them and set them.

* Bit by Bit: Accumulate bits reversely bit by bit.

* Byte by Byte: 

  **Follow up: If this function `reverseBits(int n)` is called many times, how would you optimize it?** 

  **We could reverse bits byte by byte with memorization.**

* Divide and Conquer: divide bits into blocks wih fewer bits via bit masking, then reverse each block.

---

#### Bit manipulation

Get `k` and `31 - k` bit, clear them, swap them and set them.

```java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        for (int i = 0; i < 16; i++) {
            n = swapBits(n, i);
        }
        return n;
    }
    
    private int swapBits(int n, int k) {
        int leftBit = (n >> (31 - k)) & 1; // get bit
        int rightBit = (n >> k) & 1;
        n &= ~(1 << (31 - k));             // clear bit
        n &= ~(1 << k);
        n |= (leftBit << k);               // set bit
        n |= (rightBit << (31 - k));
        return n;
    }
}
```

T: O(1)		S: O(1)

---

#### Bit by Bit

Accumulate bits reversely bit by bit.

```java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            int bit = n & 1;     // get bit
            res <<= 1;  // shift left 1 space for new bit.
            res |= bit;
            n >>= 1;
        }
        return res;
    }
}
```

T: O(1)		S: O(1)

---

#### Byte by Byte with memorization

1. We iterate over the bytes of an integer. To retrieve the right-most byte in an integer, again we apply the bit AND operation (*i.e.* `n & 0xff`) with the bit mask of `11111111`.

2. For each byte, first we reverse the bits within the byte, via a function called `reverseByte(byte)`. Then we shift the reversed bits to their final positions.

3. With the function `reverseByte(byte)`, we apply the technique of memoization, which caches the result of the function and returns the result directly for the future invocations of the same input.

```java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int res = 0;
        Map<Integer, Integer> cache = new HashMap<>();
        for (int i = 0; i < 4; i++) {
            int b = (n & 0xff);
            b = reverseByte(b, cache);
            res <<= 8;
            res |= b;
            n >>= 8;
        }
        return res;
    }
    
    private int reverseByte(int b, Map<Integer, Integer> cache) {
        if (cache.containsKey(b)) {
            return cache.get(b);
        }
        int res = 0, tmp = b;
        for (int i = 0; i < 8; i++) {
            int bit = tmp & 1;
            res <<= 1;
            res |= bit;
            tmp >>= 1;
        }
        cache.put(b, res);
        return res;
    }
}
```

T: O(1)		S: O(1)

---

#### Divide and Conquer

**divide and conquer**, where we divide the original 32-bits into blocks with fewer bits via **bit masking**, then we reverse each block via **bit shifting**, and at the end we merge the result of each block to obtain the final result.

**Note: we need logic shift `<<<` instead of arithmetic shift `<<`**

Cause in an arithmetic shift, the sign bit is extended to preserve the signedness of the number.

```java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        n = (n >>> 16) | (n << 16);
        n = ((n & 0xff00ff00) >>> 8) | ((n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >>> 4) | ((n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >>> 2) | ((n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >>> 1) | ((n & 0x55555555) << 1);
        return n;
    }
}
```

T: O(1)		S: O(1)