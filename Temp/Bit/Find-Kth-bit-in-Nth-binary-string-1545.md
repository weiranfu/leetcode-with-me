---
title: Medium | Find Kth Bit in Nth Binary String 1545
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Bit
date: 2020-08-21 15:47:35
---

Given two positive integers `n` and `k`, the binary string  `Sn` is formed as follows:

- `S1 = "0"`
- `Si = Si-1 + "1" + reverse(invert(Si-1))` for `i > 1`

Where `+` denotes the concatenation operation, `reverse(x)` returns the reversed string x, and `invert(x)` inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first 4 strings in the above sequence are:

- `S1 = "0"`
- `S2 = "0**1**1"`
- `S3 = "011**1**001"`
- `S4 = "0111001**1**0110001"`

Return *the* `kth` *bit* *in* `Sn`. It is guaranteed that `k` is valid for the given `n`.

[Leetcode](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/)

<!--more-->

**Example 1:**

```
Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001". The first bit is "0".
```

**Example 2:**

```
Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001". The 11th bit is "1".
```

**Constraints:**

- `1 <= n <= 20`
- `1 <= k <= 2^n - 1`

---

#### Brute Force

Note that the `n == 20`, which means we could double the size of string 20 times.

So we couldn't use Bitmask to represent the sequence. We choose to use StringBuilder.

The max length of StringBuilder will be `2^20 = 10^6` which is acceptable.

```java
class Solution {
    public char findKthBit(int n, int k) {
        StringBuilder sb = new StringBuilder();
        sb.append('0');
        n--;
        while (n-- != 0) {
            sb.append('1');
            for (int i = sb.length() - 2; i >= 0; i--) {
                sb.append(sb.charAt(i) == '0' ? '1' : '0');
            }
        }
        return sb.charAt(k - 1);
    }
}
```

T: O(2^n)			S: O(2^n)

---

#### Bit Operation

Since we only care about the Kth bit after nth flip, we can focus on `Kth` bit.

The length of `Sn` is `(1 << n) - 1`.

1. If `k` is on the left part of the string, we do nothing.
2. If `K` is right in the middle, and the middle is 1.
   We have flipped `count` times, we return `count % 2 == 0 ? '1' : '0'`
3. If `k` is on the right part of the string,
   find it's symeric postion `k = l + 1 - k`.
   Also we increment `count++`.

```java
class Solution {
    public char findKthBit(int n, int k) {
        int count = 0, l = (1 << n) - 1;
        while (k > 1) {
            if (k == l / 2 + 1)
                return count % 2 == 0 ? '1' : '0';
            if (k > l / 2) {
                k = l + 1 - k;
                count++;
            }
            l /= 2;
        }
        return count % 2 == 0 ? '0' : '1';
    }
}
```

T: O(n)			S: O(1)