---
title: Medium | House Robber III 337
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-07-14 02:41:00
---

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

[Leetcode](https://leetcode.com/problems/house-robber-iii/)

<!--more-->

**Example 1:**

```
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
```

---

#### Tricky 

Tree DP 里面的最大独立点集问题

use `dp[i][0]` store the max cnt if we don't rob `i`

use `dp[i][1]` store the max cnt if we rob `i`

So we need two info to store during DFS.

```java
class Solution {
    /*
    0:  max cnt if not rob
    1:  max cnt if rob
    */
    public int rob(TreeNode root) {
        int[] info = dfs(root);
        return Math.max(info[0], info[1]);
    }
    private int[] dfs(TreeNode n) {
        if (n == null) return new int[]{0, 0};
        int[] left = dfs(n.left);
        int[] right = dfs(n.right);
        int rob = left[0] + right[0] + n.val;
        int notRob = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        return new int[]{notRob, rob};
    }
}
```

T: O(n)			S: O(n)