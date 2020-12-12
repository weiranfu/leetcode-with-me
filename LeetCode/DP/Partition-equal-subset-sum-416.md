---
title: Medium | Partition Equal Subset Sum 416
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-09 23:37:42
---

Given a **non-empty** array containing **only positive integers**, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

**Note:**

1. Each of the array element will not exceed 100.
2. The array size will not exceed 200.

[Leetcode](https://leetcode.com/problems/partition-equal-subset-sum/)

<!--more-->

**Example 1:**

```
Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**

```
Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
```

**Follow up:** 

[Partition to K Equal Sum Subset](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

---

#### Tricky 

This is a knapsack problem. Because we want to find a combination of items with a target sum.

We can see the volume is `sum`, the items is the `nums`.

We want to find whether we can find a solution to get the max value. `dp[n] == sum`

```java
class Solution {
    public boolean canPartition(int[] nums) {
        if (nums == null || nums.length == 0) return false;
        int n = nums.length;
        int sum = 0;
        for (int a : nums) {
            sum += a;
        }
        if (sum % 2 != 0) return false;
        sum = sum / 2;
        int[] dp = new int[sum + 1];
        for (int a : nums) {
            for (int i = sum; i >= a; i--) {
                dp[i] = Math.max(dp[i], dp[i - a] + a);
            }
        }
        return dp[sum] == sum;
    }
}
```

T: O(n\*sum)			S: O(n)

2. DFS  **LTE**

   ```java
   class Solution {
       public boolean canPartition(int[] nums) {
           if (nums == null || nums.length == 0) return false;
           int n = nums.length;
           int sum = 0;
           for (int a : nums) {
               sum += a;
           }
           if (sum % 2 != 0) return false;
           sum = sum / 2;
           Arrays.sort(nums);
           return dfs(0, 0, sum, nums);
       }
       
       private boolean dfs(int s, int sum, int target, int[] nums) {
           if (sum == target) return true;
           int n = nums.length;
           if (s >= n) return false;
           
           for (int i = s; i < n; i++) {
               if (sum + nums[i] > target) return false;      // pruning!!
               if (dfs(i + 1, sum + nums[i], target, nums)) {
                   return true;
               }
           }
           return false;
       }
   }
   ```

   T: O(2^n)			S: O(n)