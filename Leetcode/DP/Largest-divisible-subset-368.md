---
title: Medium | Largest Divisible Subset 368
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-10 01:38:54
---

Given a set of **distinct** positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

[Leetcode](https://leetcode.com/problems/largest-divisible-subset/)

<!--more-->

**Example 1:**

```
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
```

**Example 2:**

```
Input: [1,2,4,8]
Output: [1,2,4,8]
```

---

#### Tricky 

This is a *Longest Increasing subsequences* problem.

We want an item `x` can mod every items in set `[a, b, c]`. We can sort this set, and try to use `x % c`.

If `x % c == 0`, then `x` can mod every items in set.

So we need to firstly sort `nums`.

`dp[i]` the max length of set.

Then for `dp[i]` we need to check every `dp[j]` to test `nums[i] % nums[j]`

`dp[i] = max{ dp[j] + 1 for j in [0, i-1] if nums[i] % nums[j] == 0 }`

Finaly, we need to print out the best result.

We can use `distTo[]` to record which path we use to get the best result.

```java
class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        List<Integer> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        
        Arrays.sort(nums);            // must sort to test mod
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = 1;
        int[] distTo = new int[n];    // to record path
        Arrays.fill(distTo, -1);
        int max = 1, idx = 0;
        for (int i = 1; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0 && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    distTo[i] = j;
                }
            }
            if (max < dp[i]) {
                max = dp[i];
                idx = i;
            }
        }
        res.add(nums[idx]);
        while (distTo[idx] != -1) {
            idx = distTo[idx];
            res.add(nums[idx]);
        }
        return res;
    }
}
```

T: O(n^2)		S: O(n)