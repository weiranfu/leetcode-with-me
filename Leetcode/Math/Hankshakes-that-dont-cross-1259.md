---
title: Hard | Handshakes that Don't Cross 1259
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-07-14 19:13:52
---

You are given an **even** number of people `num_people` that stand around a circle and each person shakes hands with someone else, so that there are `num_people / 2` handshakes total.

Return the number of ways these handshakes could occur such that none of the handshakes cross.

Since this number could be very big, return the answer **mod 10^9 + 7**

[Leetcode](https://leetcode.com/problems/handshakes-that-dont-cross/)

<!--more-->

**Example 1:**

```
Input: num_people = 2
Output: 1
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2019/07/11/5125_example_3.png)

```
Input: num_people = 6
Output: 5
```

---

#### Tricky 

As we fix a person as a pivot and turn for every other person who will have a handshake, the answer is the sum of the products of the new two subproblems. (就像凸多边形划分一样)

`dp[n] = dp[0]*dp[n-2] + dp[2]*dp[n-4] + ... + dp[n-2]*dp[0]`

We can find this is a *Catalan Number*.

`dp[2n] = dp[0]*dp[2n-2] + dp[2]*dp[2n-4] + ... + dp[2n-2]*dp[0]`

`dp[n] = dp[0]*dp[n-1] + dp[1]*dp[n-2] + ... + dp[n-1]*dp[0]`

```java
class Solution {
    
    int N = 1005;
    int mod = (int)1e9 + 7;
    
    public int numberOfWays(int num) {
        if (num <= 1) return 0;
        return catalan(num / 2);
    }
    
    public int catalan(int n) {
        long[] c = new long[n + 1];
        c[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                c[i] = (c[i] + c[j] * c[i - j - 1]) % mod;
            }
        }
        return (int)c[n];
    }
}
```

T: O(n^2)		S: O(n)