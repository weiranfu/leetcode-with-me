---
title: Hard | Minimum Difficulty of a Job Schedule 1335
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-01-26 16:41:15
---

You want to schedule a list of jobs in `d` days. Jobs are dependent (i.e To work on the `i-th` job, you have to finish all the jobs `j` where `0 <= j < i`).

You have to finish **at least** one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the `d` days. The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers `jobDifficulty` and an integer `d`. The difficulty of the `i-th` job is `jobDifficulty[i]`.

Return *the minimum difficulty* of a job schedule. If you cannot find a schedule for the jobs return **-1**.

[Leetcode](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)

<!--more-->

**Example 1:**





```
Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 
```

**Example 2:**

```
Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
```

**Example 3:**

```
Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.
```

**Example 4:**

```
Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15
```

---

#### Tricky 

This is a typical DP problem.

1. Subproblems: finish the `job[i:]` with `k` days left.

   Number of subproblems: O(n* len).  (len means how many days)

2. Guess: next day, we choose to solve `job[i:j] jobs for j in range(i, n)` 

3. Recurrence:

   dp(i, j) means solve job[i:] with j days left.

   `dp(i, k) = `

   `min{ dp(i, k), max{job[k] for k in range(i, j)} + dp(j, k-1) } for j in range(i, n)`

   time/subproblem: O(n)

4. Total run time: O(n^2* len)

5. Topological Order:

   from right to left. 

---

#### First solution 

Mind the initialization:

all `dp[n][i]` and `dp[i][0]` should be Integer.MAX_VALUE

```java
class Solution {
    public int minDifficulty(int[] jobDifficulty, int d) {
        int n = jobDifficulty.length;
        if (n < d) return -1;
        int[][] dp = new int[n+1][d+1];
        for (int i = 1; i <= d; i++) {
            dp[n][i] = Integer.MAX_VALUE; // There're days unused.
        }
        for (int i = 0; i < n; i++) {
            dp[i][0] = Integer.MAX_VALUE; // No day left.
        }
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 1; j <= d; ++j) {
                int min = Integer.MAX_VALUE;
                int max = 0;
                for (int k = i; k <= n - 1; k++) {
                    max = Math.max(max, jobDifficulty[k]);
                    if (dp[k+1][j-1] != Integer.MAX_VALUE) {
                        min = Math.min(min, max + dp[k+1][j-1]);
                    }
                }
                dp[i][j] = min;
            }
        }
        return dp[0][d] == Integer.MAX_VALUE ? -1 : dp[0][d];
    }
}
```

T: O(n^2* D)			S: O(n* D)

---

#### Summary 

In tricky.