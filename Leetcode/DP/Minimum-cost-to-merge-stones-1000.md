---
title: Hard | Minimum Cost to Merge Stones 1000
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-09 18:46:20
---

There are `N` piles of stones arranged in a row.  The `i`-th pile has `stones[i]` stones.

A *move* consists of merging **exactly K consecutive** piles into one pile, and the cost of this move is equal to the total number of stones in these `K` piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return `-1`.

[Leetcode](https://leetcode.com/problems/minimum-cost-to-merge-stones/)

<!--more-->

**Example 1:**

```
Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation: 
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
```

**Example 2:**

```
Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
```

**Example 3:**

```
Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation: 
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
```

**Note:**

- `1 <= stones.length <= 30`
- `2 <= K <= 30`
- `1 <= stones[i] <= 100`

---

#### Tricky 

#### 3D DP

This is a interval DP and cause we need to divide stones into k parts, we need additional 1D to represent the state.

`dp[l][r][k]` represents the cost that we divide `[l, r]` stones into k parts.

If we can successfully divide `[l, r]` into `K` parts, then we can merge these `K` parts into 1 part.

`dp[l][r][1] = dp[l][r][K] + sum(stones)`

**So we need to first calculate `dp[l][r][k]` k from `2` to `K` to get the cost to divide `[l, r]` into K parts, then we can get the cost to merge `[l, r]` into 1 part: `dp[l][r][1]`**

`dp[l][r][k] = min{ dp[l][i][1] + dp[i+1][r] }`

Base case:

`dp[i][i][1] = 0` otherwise `dp[i][j][k] = Integer.MAX_VALUE`

Final result: `dp[1][n][1]` means we merge `[1, n]` into 1 part.

```java
class Solution {
    public int mergeStones(int[] stones, int K) {
        if (stones.length <= 1) return 0;
        int n = stones.length;
        int[][][] dp = new int[n + 1][n + 1][K + 1];
        int[] preSum = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            preSum[i] = preSum[i - 1] + stones[i - 1];
        }
        for (int len = 1; len <= n; len++) {
            for (int i = 1, j = len; j <= n; i++, j++) {
                for (int k = 1; k <= K; k++) {
                    dp[i][j][k] = Integer.MAX_VALUE; // initialize
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            dp[i][i][1] = 0;                     // initialize
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 1, j = len; j <= n; i++, j++) {
                for (int k = 2; k <= len && k <= K; k++) {   // k must <= len
                    int min = Integer.MAX_VALUE;
                    for (int x = i; x < j; x++) {
                        if (dp[i][x][1] == Integer.MAX_VALUE || dp[x + 1][j][k - 1] == Integer.MAX_VALUE) continue;
                        min = Math.min(min, dp[i][x][1] + dp[x + 1][j][k - 1]);   
                    }
                    dp[i][j][k] = min;
                }
                if (dp[i][j][K] != Integer.MAX_VALUE) {
                    dp[i][j][1] = dp[i][j][K] + preSum[j] - preSum[i - 1];
                }
            }
        }
        return dp[1][n][1] == Integer.MAX_VALUE ? -1 : dp[1][n][1];
    }
}
```

T: O(n^3\*k)				S: O(n^2\*k)

#### 2D DP

We can determine whether `n` stones can be merge by`(n - 1) % (K - 1) == 0`.

Because if we merge `K` stones, if will become 1 stones. If everytime we merge `K - 1` stones with that very `1` stones, it will become the new `1` stone and merge with other `K - 1` stones.

`dp[l][r]` means the cost we merge interval `[l, r]`

`dp[l][r] = min{dp[l][i] + dp[i+1][r]} for i += K - 1 in [l,r-1]`

每一次 `i` 移动 `K - 1` 步，保证`dp[l][i]` 一定是可以合并的

如果可以合并，则合并，否则暂时先不动

if `(l - r) % (K - 1) == 0` `dp[l][r] += sum(stones)`

```java
class Solution {
    public int mergeStones(int[] stones, int K) {
        if (stones.length <= 1) return 0;
        int n = stones.length;
        if ((n - 1) % (K - 1) != 0) return -1;     // cannot merge
        
        int[] preSum = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            preSum[i] = preSum[i - 1] + stones[i - 1];
        }
        int[][] dp = new int[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        for (int i = 1; i <= n; i++) {
            dp[i][i] = 0;
        }
        for (int len = 2; len <= n; len++) {  
            for (int i = 1, j = len; j <= n; i++, j++) {
                int min = Integer.MAX_VALUE;
                for (int k = i; k < j; k+= K-1) {        // moves K-1 everytime
                    if (dp[i][k] == Integer.MAX_VALUE || dp[k + 1][j] == Integer.MAX_VALUE) continue;
                    min = Math.min(min, dp[i][k] + dp[k + 1][j]);
                }
                dp[i][j] = min;
                
                if ((j - i) % (K - 1) == 0 && dp[i][j] != Integer.MAX_VALUE) {
                    dp[i][j] += preSum[j] - preSum[i - 1];
                }
            }
        }
        return dp[1][n];
    }
}
```

T: O(n^2\*k)			S: O(n^2)	