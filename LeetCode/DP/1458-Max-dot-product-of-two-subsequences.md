---
title: Hard | Max Dot Product of Two Subsequences 1458
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-05-26 13:04:15
---

Given two arrays `nums1` and `nums2`.

Return the maximum dot product between **non-empty** subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, `[2,3,5]` is a subsequence of `[1,2,3,4,5]` while `[1,5,3]` is not).

[Leetcode](https://leetcode.com/problems/max-dot-product-of-two-subsequences/)

<!--more-->

**Example 1:**

```
Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.
```

**Example 2:**

```
Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.
```

**Example 3:**

```
Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.
```

**Constraints:**

- `1 <= nums1.length, nums2.length <= 500`
- `-1000 <= nums1[i], nums2[i] <= 1000`

---

#### Tricky 

This is a typical DP problem like *Longest Common Subsequences*. 

```java
F(X, Y) = max (
            nums1[X]*nums2[Y],// ignore previous F(.., ..) because it might be better to 																	not add it at all (i.e. if it is negative).     
  					F(X-1, Y-1) + nums[X] * nums[Y],  // use last numbers from both the first and 																								 the second
            F(X-1, Y),                             // ignore the last number from first
            F(X, Y-1),                            // ignore the last number from second
          )
```

In order not to overflow when adding `F() + nums[X] * nums[Y]`, we initialize `F()` to be `-2000`

---

#### Standard solution  

```java
class Solution {
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) {
            dp[i][0] = -2000;               // in case of overflow
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = -2000;
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int max = nums1[i - 1] * nums2[j - 1];
                max = Math.max(max, dp[i - 1][j - 1] + max);  // may overflow
                max = Math.max(max, dp[i - 1][j]);
                max = Math.max(max, dp[i][j - 1]);
                dp[i][j] = max;
            }
        }
        return dp[m][n];
    }
}
```

T: O(mn)		S: O(mn)

---

#### Summary 

In tricky.