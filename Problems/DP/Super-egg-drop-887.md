---
title: Hard | Super Egg Drop 887
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-08 20:35:07
---

You are given `K` eggs, and you have access to a building with `N` floors from `1` to `N`. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor `F` with `0 <= F <= N` such that any egg dropped at a floor higher than `F` will break, and any egg dropped at or below floor `F` will not break.

Each *move*, you may take an egg (if you have an unbroken one) and drop it from any floor `X` (with `1 <= X <= N`). 

Your goal is to know **with certainty** what the value of `F` is.

What is the minimum number of moves that you need to know with certainty what `F` is, regardless of the initial value of `F`?

[Leetcode](https://leetcode.com/problems/super-egg-drop/)

<!--more-->

**Example 1:**

```
Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
```

**Note:**

1. `1 <= K <= 100`
2. `1 <= N <= 10000`

---

#### Tricky 

We could define `dp[k][l][r]` as the DP state, because we need to devide `[1, n]` into intervals.

We choose `x` floor to drop the egg, 

`dp[k][l][r] = min{ max{dp[k-1][l][x-1], dp[k][x+1][r]} for x in [l, r-1] }`

Because we don't need to exact interval infomation just the length of interval.

We define `dp[k][i]` as smallest number of drop to get the optimal floor with `k` eggs and `i` floors left.

`dp[k][i] = min{ max{dp[k-1][x-1], dp[k][i-x]} for x in [1, i-1] }`

Base case

if we only have 1 egg, we can test from lowest floor and test `i` times, then we can make sure the `F`

`dp[1][i] = i`

If we have only 1 floor left to test, we only need 1 move.

`dp[k][1] = 1`

`dp[k][0] = 0`

1. Brute Force       **LTE**

   ```java
   class Solution {
       public int superEggDrop(int K, int N) {
           if (N == 0) return 0;
           int[][] dp = new int[K + 1][N + 1];
           for (int i = 1; i <= N; i++) {
               dp[1][i] = i;
           }
           for (int k = 1; k <= K; k++) {
               dp[k][0] = 0;
               dp[k][1] = 1;
           }
           for (int k = 2; k <= K; k++) {
               for (int i = 2; i <= N; i++) {
                   int min = Integer.MAX_VALUE;
                   for (int j = 1; j < i; j++) {
                       int max = Math.max(dp[k - 1][j - 1], dp[k][i - j]);
                       min = Math.min(min, max + 1);
                   }
                   dp[k][i] = min;
               }
           }
           return dp[K][N];
       }
   }
   ```

   T: O(kn^2)			S: O(kn)

2. DP with memorization         (**LTE**)

   When we have 1 egg and N floor, we must test N times. Because we need to test from 1 floor to N to make sure the `F`.

   When we have `0` floor, we don't need to test.

   When we have `0` egg, we cannot test.

   When we have `1` floor, we just need to test once.

   ```java
   class Solution {
       
       int[][] dp;
       int INF = 0x3f3f3f3f;
       
       public int superEggDrop(int K, int N) {
           dp = new int[K + 1][N + 1];
           for (int i = 0; i <= K; i++) {
               Arrays.fill(dp[i], -1);
           }
           return helper(K, N);
       }
       private int helper(int egg, int floor) {
           if (floor == 0) return 0;
           else if (egg == 0) return INF;
           else if (egg == 1) return floor;
           else if (floor == 1) return 1;
           if (dp[egg][floor] != -1) return dp[egg][floor];
           int min = INF;
           for (int i = 1; i <= floor; i++) {
               min = Math.min(min, Math.max(helper(egg - 1, i - 1), helper(egg, floor - i)) + 1);
           }
           dp[egg][floor] = min;
           return min;
       }
   }
   ```

   T:  O(N^2\*K)				10^10

3. Binary search

   The brute force solution gets TLE. To optimize, we should check for the unnecessary iteration in the for-loops. More specifically, to get the `j` that best fits each drop, we don't need to go over all floors from `1` to `i`.

   We want to find `max{ dp[k-1][j-1], dp[k][i-j] } for j in [1, i-1]`

   `dp[k-1][j-1]` goes up as `k` increases and `dp[k][i-j]` goes down as `k` increase.

   So we can use binary search for `j` in `[1, i-1]` to find the max of two terms.

   ![](https://cdn.jsdelivr.net/gh/weiranfu/image-hosting@main/img/leetcode/super-egg-drop-887.png)

   ```java
   class Solution {
       public int superEggDrop(int K, int N) {
           if (N == 0) return 0;
           int[][] dp = new int[K + 1][N + 1];
           for (int i = 1; i <= N; i++) {
               dp[1][i] = i;
           }
           for (int k = 1; k <= K; k++) {
               dp[k][0] = 0;
               dp[k][1] = 1;
           }
           for (int k = 2; k <= K; k++) {
               for (int i = 2; i <= N; i++) {
                   int idx = binarySearch(dp, k, i);
                   if (idx == -1) dp[k][i] = i;
                   else dp[k][i] = Math.max(dp[k - 1][idx - 1], dp[k][i - idx]) + 1;
               }
           }
           return dp[K][N];
       }
       
       private int binarySearch(int[][] dp, int k, int n) {
           int l = 1, r = n + 1;
           while (l < r) {
               int mid = l + (r - l) / 2;
               if (dp[k - 1][mid - 1] >= dp[k][n - mid]) {
                   r = mid;
               } else {
                   l = mid + 1;
               }
           }
           return l != n + 1 ? l : -1;
       }
   }
   ```

   T: O(knlogn)			S: O(n^2)

4. DP

   `dp[K][M]`means that, given `K` eggs and `M` tests, the maximum number of floor that we can check.

   we take 1 test to a floor,
   if egg breaks, then we can check `dp[k - 1][m - 1]` floors.
   if egg doesn't breaks, then we can check `dp[k][m]` floors.

   `dp[k][m] = dp[k - 1][m - 1] + dp[k][m] + 1`

   `dp[k][m]` is the number of combinations and it will increase exponentially to N.

   经过若干次扔鸡蛋，你已经确定了[0, h]都没有碎，则F >= h，不确定的楼层为[h+1, N]。这时我们采用上面的策略，在第h + 1层扔鸡蛋（注意不是第h层，第h层已经知道了不会碎），如果鸡蛋碎了则F = h，否则鸡蛋没有碎，F > h，这时你又确定了F不在第h层，所以增加了一层。

   如果你有`m`个测试机会（扔鸡蛋的机会 或者移动的次数），`k`个鸡蛋，这时我们任意选择在第 `x` 层扔鸡蛋，如果鸡蛋没碎，这时你还剩余`m - 1`次机会，`k` 个鸡蛋，我们可以确定 `x+1`  上面的`dp[k][x - 1]`层
   如果鸡蛋碎了，这时你还剩余`m - 1`次机会, `k - 1` 个鸡蛋，我们可以确定`x` 下面 `dp[k-1][m - 1]`层

   并且`x` 层也被确定了

   当我们能确定的层数超过`N`时，停止测试。

   ```java
   class Solution {
       public int superEggDrop(int K, int N) {
           if (N == 0) return 0;
           // max testing times is N
           int[][] dp = new int[K + 1][N + 1];
           for (int t = 1; t <= N; t++) {
               for (int k = 1; k <= K; k++) {
                   dp[k][t] = dp[k - 1][t - 1] + dp[k][t - 1] + 1;
               }
               if (dp[K][t] >= N) return t;   // if we can check N floors
           }
           return N;
       }
   }
   ```

   T: lest than O(nlogn)			S: O(n^2)