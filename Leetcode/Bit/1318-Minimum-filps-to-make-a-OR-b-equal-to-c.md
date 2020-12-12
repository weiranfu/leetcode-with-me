---
title: Medium | Minimum Flips to Make a OR b Equal to c 1318
tags:
  - tricky
categories:
  - Leetcode
  - Bit
date: 2020-01-12 12:31:18
---

Given 3 positives numbers `a`, `b` and `c`. Return the minimum flips required in some bits of `a` and `b` to make ( `a` OR `b` == `c` ). (bitwise OR operation).
Flip operation consists of change **any** single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

[Leetcode](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/01/06/sample_3_1676.png)

```
Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
```

**Example 2:**

```
Input: a = 4, b = 2, c = 7
Output: 1
```

**Example 3:**

```
Input: a = 1, b = 2, c = 3
Output: 0
```

**Constraints:**

- `1 <= a <= 10^9`
- `1 <= b <= 10^9`
- `1 <= c <= 10^9`

---

#### Tricky 

We can use bit manipulation here.

`(a << 0) & 1` will get the right-most bit of a.

---

#### My thoughts 

Get bits of integer in two base.

```java
class Solution {
    public int minFlips(int a, int b, int c) {
        int count = 0;
        while (a != 0 || b != 0 || c != 0) {
            int r1 = a % 2, r2 = b % 2, r3 = c % 2;
            if (r3 == 1) {
                if (r1 == 0 && r2 == 0) {
                    count++;
                }
            } else {
                if (r1 != 0 || r2 != 0) {
                    count += r1 + r2;
                }
            }
            a = a / 2;
            b = b / 2;
            c = c / 2;
        }
        return count;
    }
}
```

T: O(1), because positive int will have at most 31 bits.

S: O(1)

---

#### Bit manipulation 

```java
class Solution {
    public int minFlips(int a, int b, int c) {
        int count = 0;
        for (int i = 0; i < 30; i++) { // 31 bits for positive int
            int x = (a >> i) & 1;
            int y = (b >> i) & 1;
            int z = (c >> i) & 1;
            if (z == 1) {
                if (x == 0 && y == 0) {
                    count++;
                }
            } else {
                count += x + y;
            }
        }
        return count;
    }
}
```

T: O(1) 			S: O(1)

---

#### Summary 

Bit manipulation:

`&` means bit and

`|` means bit or

`>>` means move bits right

`<<` means move bits left