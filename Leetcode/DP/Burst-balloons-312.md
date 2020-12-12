---
title: Hard | Burst Balloons 312
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-09 11:49:33
---

Given `n` balloons, indexed from `0` to `n-1`. Each balloon is painted with a number on it represented by array `nums`. You are asked to burst all the balloons. If the you burst balloon `i` you will get `nums[left] * nums[i] * nums[right]` coins. Here `left` and `right` are adjacent indices of `i`. After the burst, the `left` and `right` then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

[Leetcode](https://leetcode.com/problems/burst-balloons/)

<!--more-->

**Example:**

```
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
```

**Note:**

- You may imagine `nums[-1] = nums[n] = 1`. They are not real therefore you can not burst them.
- 0 ≤ `n` ≤ 500, 0 ≤ `nums[i]` ≤ 100

**Follow up**

[Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/)

---

#### Tricky 

1. Backtracking.  **LTE**

   如何将我们的扎气球问题转化成回溯算法呢？这个应该不难想到的，我们其实就是想穷举戳气球的顺序，不同的戳气球顺序可能得到不同的分数，我们需要把所有可能的分数中最高的那个找出来

   ```java
   int res = Integer.MIN_VALUE;
   /* 输入一组气球，返回戳破它们获得的最大分数 */
   int maxCoins(int[] nums) {
       backtrack(nums, 0); 
       return res;
   }
   /* 回溯算法的伪码解法 */
   void backtrack(int[] nums, int socre) {
       if (nums 为空) {
           res = max(res, score);
           return;
       }
       for (int i = 0; i < nums.length; i++) {
           int point = nums[i-1] * nums[i] * nums[i+1];
           int temp = nums[i];
           // 做选择
           在 nums 中删除元素 nums[i]
           // 递归回溯
           backtrack(nums, score + point);
           // 撤销选择
           将 temp 还原到 nums[i]
       }
   }
   ```

   T: O(n!)			S: O(n)

2. DP

   此题初看用DP会很难。为什么它比较难呢？

   **原因在于，这个问题中我们每戳破一个气球 nums[i]，得到的分数和该气球相邻的气球 nums[i-1] 和 nums[i+1] 是有相关性的**。

   我们前文动态规划套路框架详解 说过运用动态规划算法的一个重要条件：子问题必须独立。所以对于这个戳气球问题，如果想用动态规划，必须巧妙地定义 dp 数组的含义，避免子问题产生相关性，才能推出合理的状态转移方程。

   However, if we try to divide our problem in the order where we burst balloons first, we run into an issue. As balloons burst, the adjacency of other balloons changes. We are unable to keep track of what balloons the endpoints of our intervals are adjacent to. This is where the second technique comes in.

   Working Backwards：

   如何定义 dp 数组呢，这里需要对问题进行一个简单地转化。题目说可以认为 nums[-1] = nums[n] = 1，那么我们先直接把这两个边界加进去，形成一个新的数组 points：

   ```java
   int maxCoins(int[] nums) {
       int n = nums.length;
       // 两端加入两个虚拟气球
       int[] points = new int[n + 2];
       points[0] = points[n + 1] = 1;
       for (int i = 1; i <= n; i++) {
           points[i] = nums[i - 1];
       }
       // ...
   }
   ```

   现在气球的索引变成了从 1 到 n，points[0] 和 points[n+1] 可以认为是两个「虚拟气球」。

   那么我们可以改变问题：在一排气球 points 中，请你戳破气球 0 和气球 n+1 之间的所有气球（不包括 0 和 n+1），使得最终只剩下气球 0 和气球 n+1 两个气球，最多能够得到多少分？

   现在可以定义 dp 数组的含义：

   `dp[i][j] = x` 表示，**戳破气球 i 和气球 j 之间（开区间，不包括 i 和 j）的所有气球**，可以获得的最高分数为 x。

   那么根据这个定义，题目要求的结果就是 `dp[0][n+1]` 的值，而 base case 就是 `dp[i][j]` = 0，其中 0 <= i <= n+1, j <= i+1，因为这种情况下，开区间 (i, j) 中间根本没有气球可以戳。

   ```java
   // base case 已经都被初始化为 0
   int[][] dp = new int[n + 2][n + 2];
   ```

   接下来寻找状态转移方程

   不就是想求戳破气球 i 和气球 j 之间的最高分数吗，如果「正向思考」，就只能写出前文的回溯算法；我们需要「反向思考」，想一想气球 i 和气球 j 之间最后一个被戳破的气球可能是哪一个？

   其实气球 i 和气球 j 之间的所有气球都可能是最后被戳破的那一个，不防假设为 k。回顾动态规划的套路，这里其实已经找到了「状态」和「选择」：i 和 j 就是两个「状态」，最后戳破的那个气球 k 就是「选择」。

   根据刚才对 dp 数组的定义，如果最后一个戳破气球 k，`dp[i][j]` 的值应该为：

   `dp[i][j] = dp[i][k] + dp[k][j] + points[i]*points[k]*points[j]`
   你不是要最后戳破气球 k 吗？那得先把开区间 (i, k) 的气球都戳破，再把开区间 (k, j) 的气球都戳破；最后剩下的气球 k，相邻的就是气球 i 和气球 j，这时候戳破 k 的话得到的分数就是 `points[i]*points[k]*points[j]`。

   那么戳破开区间 (i, k) 和开区间 (k, j) 的气球最多能得到的分数是多少呢？嘿嘿，就是 `dp[i][k]` 和 `dp[k][j]`，这恰好就是我们对 dp 数组的定义嘛！

   ```java
   class Solution {
       public int maxCoins(int[] nums) {
           if (nums == null || nums.length == 0) return 0;
           int n = nums.length;
           int[] newNums = new int[n + 2];
           for (int i = 1; i <= n; i++) {
               newNums[i] = nums[i - 1];
           }
           newNums[0] = 1;
           newNums[n + 1] = 1;
           
           int[][] dp = new int[n + 2][n + 2];
           
           for (int len = 3; len <= n + 2; len++) {
               for (int i = 0, j = len - 1; j < n + 2; i++, j++) {
                   int max = Integer.MIN_VALUE;
                   for (int k = i + 1; k < j; k++) {
                       max = Math.max(max, dp[i][k] + dp[k][j] + newNums[i] * newNums[k] * newNums[j]);
                   }
                   dp[i][j] = max;
               }
           }
           return dp[0][n + 1];
       }
   }
   ```

   T: O(n^3)			S: O(n)