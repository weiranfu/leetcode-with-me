---
title: Hard | Minimum Cost to Connect Two Groups of Points 1595
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-09-28 11:37:23
---

You are given two groups of points where the first group has `size1` points, the second group has `size2` points, and `size1 >= size2`.

The `cost` of the connection between any two points are given in an `size1 x size2` matrix where `cost[i][j]` is the cost of connecting point `i` of the first group and point `j` of the second group. The groups are connected if **each point in both groups is connected to one or more points in the opposite group**. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.

Return *the minimum cost it takes to connect the two groups*.

[Leetcode](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/09/03/ex1.jpg)

```
Input: cost = [[15, 96], [36, 2]]
Output: 17
Explanation: The optimal way of connecting the groups is:
1--A
2--B
This results in a total cost of 17.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/09/03/ex2.jpg)

```
Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
Output: 4
Explanation: The optimal way of connecting the groups is:
1--A
2--B
2--C
3--A
This results in a total cost of 4.
Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.
```

**Constraints:**

- `size1 == cost.length`
- `size2 == cost[i].length`
- `1 <= size1, size2 <= 12`
- `size1 >= size2`
- `0 <= cost[i][j] <= 100`

---

#### First solution (LTE)

We use `dp[s1][s2]` to represent the min cost where `s1` is the state of points in set1, `s2` is the state of points in set2. (`s1` and `s2` are bitmask)

Since the size of each group could be 12, so total time complexity will be `O(2^12 * 2^12) = O(2^24)`

```java
class Solution {
    int[][] dp;
    int m, n;
    List<List<Integer>> cost;
    
    public int connectTwoGroups(List<List<Integer>> cost) {
        this.cost = cost;
        m = cost.size(); n = cost.get(0).size();
        dp = new int[1 << m][1 << n];
        for (int i = 0; i < 1 << m; i++) {
            Arrays.fill(dp[i], -1);
        }
        return dfs(0, 0);
    }
    private int dfs(int s1, int s2) {
        if (s1 == (1 << m) - 1 && s2 == (1 << n) - 1) return 0;
        if (dp[s1][s2] != -1) return dp[s1][s2];
        int min = 0x3f3f3f3f;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if ((s1 >> i & 1) == 1 && (s2 >> j & 1) == 1) continue;
                min = Math.min(min, dfs(s1 | 1 << i, s2 | 1 << j) + cost.get(i).get(j));
            }
        }
        dp[s1][s2] = min;
        return min;
    }
}
```

T: O(2^2n)			S: O(2^2n)

---

#### Standard solution  

`dp[i][s]` represents we have considered `i`th items in set1 with `state = s` in set2.

We have three cases here:

1. `A[i]` is not connected yet, connect `A[i]` with an already connected `B[j]` in `s`.

   `dp[i][s] = dp[i - 1][s] + cost[i][j]`

2. `A[i]` is not connected yet, connect `A[i]` with a not connected `B[j]` in `s`.

   `dp[i][s] = dp[i - 1][s & ~(1 << j)] + cost[i][j]`

3. `A[i]` is connected yet, connect `A[i]` with a not connected `B[j]` in `s`.

   `dp[i][s] = dp[i][s & ~(1 << j)] + cost[i][j]`

If `A[i]` is connected, we don't need to connect it with an already connected `B[j]` in `s`.

```java
class Solution {
    public int connectTwoGroups(List<List<Integer>> cost) {
        int m = cost.size(), n = cost.get(0).size();
        int INF = 0x3f3f3f3f;
        int[][] dp = new int[m + 1][1 << n];
        for (int i = 0; i <= m; i++) {
            Arrays.fill(dp[i], INF);
        }
        dp[0][0] = 0;
        for (int i = 1; i <= m; i++) {
            for (int s = 0; s < 1 << n; s++) {
                int min = INF;
                for (int j = 0; j < n; j++) {
                    if ((s >> j & 1) == 0) continue;
                    min = Math.min(min, Math.min(dp[i - 1][s & ~(1 << j)], Math.min(dp[i - 1][s], dp[i][s & ~(1 << j)])) + cost.get(i - 1).get(j));
                }
                dp[i][s] = min;
            }
        }
        return dp[m][(1 << n) - 1];
    }
}
```

T: O(m\*n\*2^n)			S: O(n\*2^n)