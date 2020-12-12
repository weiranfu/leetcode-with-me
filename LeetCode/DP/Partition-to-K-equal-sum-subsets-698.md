---
title: Medium | Partition to K Equal Sum Subsets 698
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-11 14:22:14
---

Given an array of integers `nums` and a positive integer `k`, find whether it's possible to divide this array into `k` non-empty subsets whose sums are all equal.

[Leetcode](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

<!--more-->

**Example 1:**

```
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
```

**Note:**

- `1 <= k <= len(nums) <= 16`.
- `0 < nums[i] < 10000`.

---

#### Tricky 

it is a NPC problem,which means :

1. for a given specific answer, we can prove that where it can part into K subsets in polynomial time.
2. but to prove whether it exists one answer to part into K subsets, it just can search brutely. we can not make it in polynomial time.

[what is p,np,npc](http://www.matrix67.com/blog/archives/105)

1. Backtracking / DFS search

   We could search K subsets with target sum.

   We simulate we're filling up K buckets with n items, which the sum of each bucket is `target`.

   Everytime we finish one bucket, we reset the start point to `0` and try to fill up the next bucket.

   ```java
   class Solution {
       public boolean canPartitionKSubsets(int[] nums, int k) {
           if (nums == null || nums.length == 0) return false;
           int n = nums.length;
           int sum = 0;
           for (int a : nums) {
               sum += a;
           }
           if (sum % k != 0) return false;
           int target = sum / k;
           boolean[] visited = new boolean[n];
           return dfs(0, 0, target, nums, visited, k);
       }
       
       private boolean dfs(int s, int sum, int target, int[] nums, boolean[] visited, int k) {
           if (k == 0) return true;
           if (sum == target) {
               return dfs(0, 0, target, nums, visited, k - 1);// search next subsets
           }
           for (int i = s; i < nums.length; i++) {
               if (visited[i]) continue;
               visited[i] = true;
               if (dfs(i + 1, sum + nums[i], target, nums, visited, k)) {
                   return true;
               }
               visited[i] = false;
           }
           return false;
       }
   }
   ```

   T:  O(k^{N-k} k!), where N is the length of `nums`, and k*k* is as given. As we skip additional zeroes in `buckets`, naively we will make O*(*k*!) calls to `search`, then an additional O(k^{N-k}) calls after every element of `buckets` is nonzero.

   S: O(n)  (call stack is n because we're arrange n items, although we have k buckets, we need to wait for them to call back.)

2. DP with state compression

   We can use bitmask to represent the state of items. Chosen or Unchosen.

   We can simulate the K buckets by store the `mod sum` value of all chosen items.

   `dp[S] = sum(items) % target`

   If the sum of all chosen items can divide target, we will reduce the sum to 0.

   For next item we want to choose, we need to make sure `dp[S] + nums[i] <= target`.

   ```java
   class Solution {
       public boolean canPartitionKSubsets(int[] nums, int k) {
           if (nums == null || nums.length == 0) return false;
           int n = nums.length;
           int sum = 0;
           for (int a : nums) {
               sum += a;
           }
           if (sum % k != 0) return false;
           int target = sum / k;
           int[] dp = new int[1 << n];
           Arrays.fill(dp, -1);
           dp[0] = 0;
           
           for (int s = 0; s < 1 << n; s++) {
               for (int i = 0; i < n; i++) {
                   if ((s >> i & 1) == 1) {    // if choose i
                       int pre = s & ~(1 << i);
                       if (dp[pre] != -1 && dp[pre] + nums[i] <= target) {   // if sum <= target
                           dp[s] = (dp[pre] + nums[i]) % target;
                       }
                   }
               }
           }
           return dp[(1 << n) - 1] == 0;
       }
   }
   ```

   T: O(n*2^n)			S: O(n)