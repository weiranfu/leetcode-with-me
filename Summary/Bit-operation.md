---
title: Bit Operation
tags:
  - tricky
categories:
  - Summary
date: 2020-03-06 19:22:21
---

Some common bit operations.



<!--more-->

#### Basic Operations

---

```bash
&    00101 & 00011 = 00001         sets 0 if meets 0
|    00101 | 00011 = 00111         sets 1 if meets 1
^    00101 ^ 00011 = 00110         XOR: if different sets 1, otherwise 0
~    ~00101 = 11010                sets the opposite bit
```



#### Advanced Operations

---

1. Get `ith` bit state in bitmask x

    `(x >> i) & 1`

2. insert i

   `x |= 1 << i`

3. Remove i

   `x &= ~(1 << i)`

   `x ^= 1 << i`  if `i`th is 1.

4. Check a flag

   `(x >> i) & 1 == 1`

5. Bit map for true false value

   x ^= 1        (0 set to be 1, 1 set to be 0)

6. Turn off / Flip least significant `1` into `0`

   `10100 & (10100 - 1) = 10100 & 10011 = 10000`

   `n = n & (n - 1)` 

7. Get the low bit value of an integer.

   可以取出一个集合的最小元

   `10110  => 00010`

   `100  =>  100`

   `101 => 001`

   `lowbit(x) = x & (-x)`   
   
   

#### Bit operation API

---

1. Get number of 1 bits in an integer

   `10110  =>  3`
   
   `num = Integer.bitCount(n)`

2. Get the negative value of an integer.

   `-5 = ~101 + 1 = 010 + 1 = 011`

   `-x = ~x + 1`

4. Check only 1 bit is set.

   Flip least significant `1` into `0`.

   `count & (count - 1) == 0` 
   
5. Get the odd count number in an array.

   `a XOR 0 = a`

   `a XOR a = 0`

   Odd count number in an array `[a,b,b,a,c]` is `c`

   `a XOR b XOR b XOR a XOR c = c`

5. XOR preSum     (for quick computation of  XOR on a range of nums)

   ```java
   preSum[1] = A[1];
   preSum[i] = preSum[i - 1] XOR A[i]
   
   A[i] ^ A[i+1] ^ A[i + 2] ^ ... ^ A[j] = preSum[j] ^ preSum[i - 1]
   ```

6. How to get all bits value of an integer in its binary format from left to right?

   We should scan from `31` to `0` bit position.

   ```
   for (int i = 31; i >= 0; i--) {
   	int bit = (1 << i) & num;
   }
   ```

   