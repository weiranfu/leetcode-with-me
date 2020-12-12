---
title: Medium | House Robber II 213
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-06-09 18:42:00
---

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.

[Leetcode](https://leetcode.com/problems/house-robber-ii/)

<!--more-->

**Example 1:**

```
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
```

**Example 2:**

```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

**Follow up**

[House Robber III](https://leetcode.com/problems/house-robber-iii/)

---

#### Tricky 

The key is how to handle the cycle?

**There're two possible cases:**

1. Rob the first house: then we can only consider houses from `[0, n - 1]`.
2. DONT rob the first house: then we can only consider houses from `[1, n]`

---

#### First solution 

`dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1])`

So we only need to keep two variables to track dp. `prev2` & `prev1`.

```java
class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);
        return Math.max(robHelp(nums, true), robHelp(nums, false));
    }
    
    private int robHelp(int[] nums, boolean robFirst) {
        int prev1, prev2;     // prev2 - prev1 - curr
        int left, right;      // left, right bound
        if (robFirst) {
            prev2 = nums[0];
            prev1 = nums[0];
            left = 2;
            right = nums.length - 1;
        } else {
            prev2 = 0;
            prev1 = nums[1];
            left = 2;
            right = nums.length;
        }
        for (int i = left; i < right; i++) {
            int tmp = prev1;
            prev1 = Math.max(nums[i] + prev2, prev1);
            prev2 = tmp;
        }
        return prev1;
    }
}
```

T: O(n)			S: O(1)

---

#### Optimized

We could give dp boundary to the recursive function.

Case1: rob the first house, boundary from `[0, n - 1]`

Case2: Don't rob the first house, boundary from `[1, n]`

**You may wonder that why we could use boundary [0, n-1] to represent the case1? It is possible that under boundary [0, n-1] we still don't rob house[0].** 

Although that situation is possible, it doesn't affect we don't have the possibility to rob last house.

```java
class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        if (n == 1) return nums[0];
        return Math.max(robHelp(nums, 0, n - 1), robHelp(nums, 1, n));
    }
    
    private int robHelp(int[] nums, int left, int right) {
        int prev1 = 0, prev2 = 0;
        for (int i = left; i < right; i++) {
            int tmp = prev1;
            prev1 = Math.max(nums[i] + prev2, prev1);
            prev2 = tmp;
        }
        return prev1;
    }
}
```

T: O(n)		S: O(1)



