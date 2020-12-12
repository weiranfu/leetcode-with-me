---
title: Hard | Single Number 136
tags:
  - tricky
categories:
  - Leetcode
  - Bit
date: 2020-05-28 17:45:01
---

Given a **non-empty** array of integers, every element appears *twice* except for one. Find that single one.

Your algorithm should have a linear runtime complexity and without using extra memory.

[Leetcode](https://leetcode.com/problems/single-number/)

<!--more-->

**Example 1:**

```
Input: [2,2,1]
Output: 1
```

**Example 2:**

```
Input: [4,1,2,1,2]
Output: 4
```

**Follow up:** [Single Number II](https://aranne.github.io/2020/05/28/137-Single-number-II/#more)

---

#### Tricky 

We could use XOR operation to get the odd count number in an array.

`a XOR a = 0`           even count number will be 0

`a XOR 0 = a`           odd count number will be left

`4 XOR 1 XOR 2 XOR 1 XOR 2 = 4`

---

#### Standard solution  

```java
class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            res ^= nums[i];
        }
        return res;
    }
}
```

T: O(n)		S: O(1)

