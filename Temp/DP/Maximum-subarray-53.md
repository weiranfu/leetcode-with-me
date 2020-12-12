---
title: Hard | Maximum Subarray 53	
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-05-12 22:23:50
---

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

[Leetcode](https://leetcode.com/problems/maximum-subarray/)

<!--more-->

**Example:**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Follow up:** solve it in O(n)

---

#### Tricky 

* Greedy 

  How to calculate the sum when deciding whether add a new item.

  if `sum + nums[i] < nums[i]`, we choose to find a new subarray beginning with `nums[i]`, so `sum = nums[i]`.

  else we contiguous extend current array, so `sum = sum + nums[i]`.

* DP

  `dp[i]` represents the max sum of subarray including `nums[i]`.

  We choose whether consider `nums[:i-1]`

  `dp[i] = Math.max(nums[i], dp[i - 1] + nums[i])`

---

#### My thoughts 

Failed to solve.

---

#### Standard solution  

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        if (n == 0) return 0;
        int max = nums[0];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum = Math.max(nums[i], sum + nums[i]);
            max = Math.max(max, sum);
        }
        return max;
    }
}
```

T: O(n)			S: O(1)

---

#### DP

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = nums[0];
        int res = nums[0];
        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}
```

T: O(n)		S: O(n)