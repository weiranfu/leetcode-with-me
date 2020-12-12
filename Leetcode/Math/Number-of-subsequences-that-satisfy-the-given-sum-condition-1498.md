---
title: Medium | Number of Subsequences that Satisfy the Given Sum Condition 1498
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-06-28 03:07:44
---

Given an array of integers `nums` and an integer `target`.

Return the number of **non-empty** subsequences of `nums` such that the sum of the minimum and maximum element on it is less or equal than `target`.

Since the answer may be too large, return it modulo 10^9 + 7.

[Leetcode](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

<!--more-->

**Example 1:**

```
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
```

**Example 2:**

```
Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
```

**Example 3:**

```
Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them don't satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
```

---

#### Tricky 

**How to avoid overflow if the answer is too large?**

We will module mod with every adder.

We need to precalculate 2 to the Nth power with `mod`

```java
twoPower[0] = 1;
for (int i = 1; i <= n; i++) {
  twoPower[i] = (twoPower[i - 1] + twoPower[i - 1]) % mod;
}
```

We enumerate the min value in the subsequences and try to find the max value.

---

#### Standard solution  

```java
class Solution {
    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int mod = (int)1e9 + 7;
        int[] twoPower = new int[n + 1];       // save two to nth power
        twoPower[0] = 1;
        for (int i = 1; i <= n; i++) {
            twoPower[i] = (twoPower[i - 1] + twoPower[i - 1]) % mod;  // mod
        }
        int ans = 0;
        for (int i = 0, j = n - 1; i <= j; i++) {
            while (i <= j && nums[i] + nums[j] > target) j--;
            int cnt = j - i;
            if (cnt >= 0) ans = (ans + twoPower[cnt]) % mod;   // mod
        }
        return ans;
    }
}
```

T: O(n)		S: O(n)

