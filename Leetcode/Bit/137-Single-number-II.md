---
title: Hard | Single Number II 137
tags:
  - tricky
categories:
  - Leetcode
  - Bit
date: 2020-05-28 18:14:57
---

Given a **non-empty** array of integers, every element appears *three* times except for one, which appears exactly once. Find that single one. 

Your algorithm should have a linear runtime complexity and without using extra memory.

[Leetcode](https://leetcode.com/problems/single-number-ii/)

<!--more-->

**Example 1:**

```
Input: [2,2,3,2]
Output: 3
```

**Example 2:**

```
Input: [0,1,0,1,0,1,99]
Output: 99
```

---

#### Tricky 

**XOR**

Let's start from XOR operator which could be used to detect the bit which appears odd number of times: 1, 3, 5, etc.

XOR of zero and a bit results in that bit

`0 XOR x = x`

XOR of two equal bits (even if they are zeros) results in a zero

`x XOR x = 0`

and so on and so forth, i.e. one could see the bit in a bitmask only if it appears odd number of times.
![fig](https://leetcode.com/problems/single-number-ii/Figures/137/xor.png)

**That's already great, so one could detect the bit which appears once, and the bit which appears three times. The problem is to distinguish between these two situations.**

To separate number that appears once from a number that appears three times let's use two bitmasks instead of one: `seen_once` and `seen_twice`.

The idea is to

- change `seen_once` only if `seen_twice` is unchanged
- change `seen_twice` only if `seen_once` is unchanged

![fig](https://leetcode.com/problems/single-number-ii/Figures/137/three.png)

This way bitmask `seen_once` will keep only the number which appears once and not the numbers which appear three times.

---

#### Standard solution  

```java
class Solution {
    public int singleNumber(int[] nums) {
        int seenOnce = 0;
        int seenTwice = 0;
        for (int n : nums) {
            seenOnce = ~seenTwice & (seenOnce ^ n);
            seenTwice = ~seenOnce & (seenTwice ^ n);
        }
        return seenOnce;
    }
}
```

T: O(n)		S: O(1)

