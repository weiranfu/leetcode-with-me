---
title: Hard | Palindrome Removal 1246
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-13 01:32:53
---

Given an integer array `arr`, in one move you can select a **palindromic** subarray `arr[i], arr[i+1], ..., arr[j]` where `i <= j`, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left and on the right of that subarray move to fill the gap left by the removal.

Return the minimum number of moves needed to remove all numbers from the array.

[Leetcode](https://leetcode.com/problems/palindrome-removal/)

<!--more-->

**Example 1:**

```
Input: arr = [1,2]
Output: 2
```

**Example 2:**

```
Input: arr = [1,3,4,1,5]
Output: 3
Explanation: Remove [4] then remove [1,3,1] then remove [5].
```

**Constraints:**

- `1 <= arr.length <= 100`
- `1 <= arr[i] <= 20`

**Follow up:** 

[String Printer](https://leetcode.com/problems/strange-printer/)

---

#### Tricky 

This is a typical interval DP. `dp[i][j]` means interval `[i, j]`

How to minimize the moves of removal? 

If we find `arr[i] == arr[j]`, we can simply extend palindrome from `dp[i + 1][j - 1]`

Case 1: remove `arr[i]` alone

​			`dp[i][j] = dp[i + 1][j] + 1`

Case 2: remove with same number `arr[k]`, `k` in `[i+1, j]`

​			`dp[i][j] = min{ dp[i+1][k-1] + dp[k+1][j] for k in [i+1,j] if arr[i] == arr[k] }`

```java
class Solution {
    public int minimumMoves(int[] arr) {
        int n = arr.length;
        int[][] dp = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            dp[i][i] = 1;
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 1, j = len; j <= n; i++, j++) {
                int min = dp[i + 1][j] + 1;
                for (int k = i + 1; k <= j; k++) {
                    if (arr[i - 1] == arr[k - 1]) {
                        min = Math.min(min, (i + 1 <= k - 1 ? dp[i + 1][k - 1] : 1) + (k + 1 <= j ? dp[k + 1][j] : 0));
                    }
                }
                dp[i][j] = min;
            }
        }
        return dp[1][n];
    }
}
```

T: O(n^3)			S: O(n^2)

---

#### DFS with memorization

If we write recursion version of DP, it will much easier for us to handle edge cases

For example, in an interval `[l, r]` and `l > r` case.

```java
class Solution {
    int[][] dp;
    public int minimumMoves(int[] arr) {
        int n = arr.length;
        dp = new int[n + 1][n + 1];
        return dfs(1, n, arr);
    }
    
    private int dfs(int l, int r, int[] arr) {
        if (l > r) {
            return 0;      												// edge case
        }
        if (l == r) {
            return 1;
        }
        if (dp[l][r] > 0) return dp[l][r];
        
        int min = dfs(l + 1, r, arr) + 1;
        for (int k = l + 1; k <= r; k++) {
            if (arr[l - 1] == arr[k - 1]) {
                min = Math.min(min, (l + 1 == k ? 1 : dfs(l + 1, k - 1, arr)) + dfs(k + 1, r, arr));
            }
        }
        dp[l][r] = min;
        return min;
    }
}
```

T: O(n^3)			S: O(n^2)