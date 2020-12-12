---
title: Hard | Minimum Number of Increments on Subarrays to Form a Target Array 1526
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-08-01 15:52:23
---

Given an array of positive integers `target` and an array `initial` of same size with all zeros.

Return the minimum number of operations to form a `target` array from `initial` if you are allowed to do the following operation:

- Choose **any** subarray from `initial` and increment each value by one.

The answer is guaranteed to fit within the range of a 32-bit signed integer.

[Leetcode](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/)

<!--more-->

**Example 1:**

```
Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.
```

**Example 2:**

```
Input: target = [3,1,1,2]
Output: 4
Explanation: (initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (target).
```

---

#### Diffence Function

差分数组的经典例题
差分数组 B 是前缀和数组 A 的逆运算
`B[i] = A[i] - A[i-1]`

`A[i] = B[0] + B[1] + ... + B[i]`

对某一个区间`[l, r]` 中所有元素加 1
即 `B[l] += 1`, `B[r + 1] -= 1`

求得原数组 A 的差分数组后，把所有正数加起来就是至少需要操作的次数

```java
class Solution {
    
    int[] B;
    
    public int minNumberOperations(int[] target) {
        int n = target.length;
        B = new int[n + 2];
        for (int i = 1; i <= n; i++) {
            add(i, i, target[i - 1]);			// 想象成原数组初始为0，在[i,i]区间插入 target[i-1]
        }
        int res = 0;
        for (int i = 1; i <= n; i++) {
            if (B[i] > 0) res += B[i];    // 统计差分数组中的正数
        }
        return res;
    }
    
    private void add(int l, int r, int c) {
        B[l] += c;
        B[r + 1] -= c;
    }
}
```

T: O(n)			S: O(n)

