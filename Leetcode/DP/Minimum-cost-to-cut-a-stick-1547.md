---
title: Hard | Minimum Cost to Cut a Stick 1547
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-08-20 10:25:35
---

Given a wooden stick of length `n` units. The stick is labelled from `0` to `n`. For example, a stick of length **6** is labelled as follows:

![img](https://assets.leetcode.com/uploads/2020/07/21/statement.jpg)

Given an integer array `cuts` where `cuts[i]` denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return *the minimum total cost* of the cuts.

[Leetcode](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)

<!--more-->

**Example 1:**

![image](https://assets.leetcode.com/uploads/2020/07/21/e11.jpg)

```
Input: n = 7, cuts = [1,3,4,5]
Output: 16
Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:

The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).
```

**Follow up**

[Burst Balloons](https://leetcode.com/problems/burst-balloons/)

---

#### Standard solution  

This problem is just like **[Burst Balloons](https://leetcode.com/problems/burst-balloons/)**

The difference is that we focus on `cuts` array this time.

`dp[i][j]` means the minimum cost to cut sticks using all cuts in `cuts[i] ~ cuts[j]`

Since we couldn't perform cuts on `i` and `j`, we could add `0` and `n` into our cuts array.

`dp[i][j] = dp[i][k] + dp[k][j] + cuts[j] - cuts[i] for k in (i+1, j-1)`

`dp[i][i] = 0`

```java
class Solution {
    public int minCost(int n, int[] cuts) {
        List<Integer> cutList = new ArrayList<>();
        for (int cut : cuts) {
            cutList.add(cut);
        }
        cutList.add(0);
        cutList.add(n);
        Collections.sort(cutList);
        int N = cutList.size();
        int[][] dp = new int[N][N];
        for (int len = 3; len <= N; len++) {
            for (int i = 0, j = len - 1; j < N; i++, j++) {
                int min = 0x3f3f3f3f;
                for (int k = i + 1; k < j; k++) {
                    min = Math.min(min, dp[i][k] + dp[k][j] + cutList.get(j) - cutList.get(i));
                }
                dp[i][j] = min;
            }
        }
        return dp[0][N - 1];
    }
}
```

T: O(n^3)			S: O(n^2)