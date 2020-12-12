---
title: Medium | Minimum Swaps to Arrange a Binary Grid 1536
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-08-25 10:14:22
---

Given an `n x n` binary `grid`, in one step you can choose two **adjacent rows** of the grid and swap them.

A grid is said to be **valid** if all the cells above the main diagonal are **zeros**.

Return *the minimum number of steps* needed to make the grid valid, or **-1** if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell `(1, 1)` and ends at cell `(n, n)`.

[Leetcode](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/)

<!--more-->

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/07/28/fw.jpg)

```
Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/07/16/e2.jpg)

```
Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.
```

**Example 3:**

![img](https://assets.leetcode.com/uploads/2020/07/16/e3.jpg)

```
Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0
```

**Constraints:**

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 200`
- `grid[i][j]` is `0` or `1`

---

#### Standard solution  

Store the max contiguous `0` for each row in `cnt[]`.

Perform **Selection sort** to find the minimum cost.

Each time we search the minimum cost candidates the have more than `n - 1 - i` `0`s.

Then move the `cnt[]` backward one step.

The complexity is O(n^2) which is acceptable.

```java
class Solution {
    public int minSwaps(int[][] grid) {
        int n = grid.length;
        int[] cnt = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 0) cnt[i]++;
                else break;
            }
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            int min = n + 1;
            int idx = -1;
            for (int j = i; j < n; j++) {
                if (cnt[j] < n - 1 - i) continue;
                if (min > j - i) {
                    min = j - i;
                    idx = j;
                }
            }
            if (min == n + 1) return -1;
            res += min;
            for (int j = idx; j > i; j--) {
                cnt[j] = cnt[j - 1];
            }
        }
        return res;
    }
}
```

T: O(n^2)			S: O(n)

