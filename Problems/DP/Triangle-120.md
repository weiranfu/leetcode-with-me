---
title: Medium | Triangle 120
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-05-24 23:46:24
---

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Could you devise a constant space solution?

[Leetcode](https://leetcode.com/problems/triangle/)

<!--more-->

For example, given the following triangle

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is `11` (i.e., **2** + **3** + **5** + **1** = 11).

---

#### Tricky 

This is a DP problem, we could reuse the dp array to devise a constant space solution.

`dp[i][j] = Math.min(dp[i - 1][j] + dp[i - 1][j - 1]) + triangle.get(j)`

**Constant space: `i` only depends on `i-1`, so we can remove dp[i] level and update from right to left**

`dp[j] = Math.min(dp[j], dp[j - 1]) + triangle[j]`

```java
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        if (triangle == null || triangle.size() == 0) return 0;
        int m = triangle.size();
        int n = triangle.get(m - 1).size();
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[1] = triangle.get(0).get(0);
        for (int i = 1; i < m; i++) {
            List<Integer> list = triangle.get(i);
            for (int j = list.size(); j >= 1; j--) {
                dp[j] = Math.min(dp[j], dp[j - 1]) + list.get(j - 1);
            }
        }
        int res = Integer.MAX_VALUE;
        for (int i = 1; i <= n; i++) {
            res = Math.min(res, dp[i]);
        }
        return res;
    }
}
```

T: O(mn)		S: O(n)

