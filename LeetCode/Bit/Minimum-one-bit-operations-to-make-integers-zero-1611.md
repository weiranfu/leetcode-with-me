---
title: Hard | Minimum One Bit Operations to Make Integers Zero 1611
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Bit
date: 2020-11-26 00:49:16
---

Given an integer `n`, you must transform it into `0` using the following operations any number of times:

- Change the rightmost (`0th`) bit in the binary representation of `n`.
- Change the `ith` bit in the binary representation of `n` if the `(i-1)th` bit is set to `1` and the `(i-2)th` through `0th` bits are set to `0`.

Return *the minimum number of operations to transform* `n` *into* `0`*.*

[Leetcode](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/)

<!--more-->

**Example 1:**

```
Input: n = 0
Output: 0
```

**Example 2:**

```
Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.
```

**Example 3:**

```
Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.
```

**Constraints:**

- `0 <= n <= 109`

---

#### Standard Solution

Note that the number of operations for `n` to become 0 is the same as the number of operations for 0 to become `n`...

Let's see how it can be done for numbers that are powers of 2.
`1 -> 0` => 1
`10 -> 11 -> 01 -> ...` => 2 + 1
`100 -> 101 -> 111 -> 110 -> 010 -> ...` => 4 + 2 + 1
`1000 -> 1001 -> 1011 -> 1010 -> 1110 -> 1111 -> 1101 -> 1100 -> 0100 -> ...` => 8 + 4 + 2 + 1
We can find that for `2^n`, it needs `2^(n+1) - 1` operations to become 0.

Now suppose we want to know the number of operations for `1100` to become `0`. We know it takes 15 operations for 0 to become `1000`, and it takes 7 operations for `1000` to become `1100`. We get the solution by `15 - 7`, since `1000` should become `1100` first, then become `0000`.

Note that `4` here is the number of operations from `1000` to become `1100`, which is the same as the number of operations from `000` to `100` (ignoring the most significant bit), and it can be computed recursively. The observation gives us: `minimumOneBitOperations(1100) + minimumOneBitOperations(0100) = minimumOneBitOperations(1000)`.

```java
class Solution {
    public int minimumOneBitOperations(int n) {
        if (n <= 1) return n;
        int cnt = 0;
        int a = n;
        while ((a & (a - 1)) != 0) {
            a = a & (a - 1);
        }
        int b = n & ~a;
      	// a is the most significant bit number, b is the rest number
        return (a << 1) - 1 - minimumOneBitOperations(b);
    }
}
```

T: O(logn)		S: O(logn)

