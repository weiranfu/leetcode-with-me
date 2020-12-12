---
title: Hard | Maximum Profit in Job Scheduling 1235
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-01-15 22:02:10
---

We have `n` jobs, where every job is scheduled to be done from `startTime[i]` to `endTime[i]`, obtaining a profit of `profit[i]`.

You're given the `startTime` , `endTime` and `profit` arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

If you choose a job that ends at time `X` you will be able to start another job that starts at time `X`.

[Leetcode](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2019/10/10/sample1_1584.png)**

```
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2019/10/10/sample22_1584.png)**

```
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
```

**Example 3:**

**![img](https://assets.leetcode.com/uploads/2019/10/10/sample3_1584.png)**

```
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
```

**Constraints:**

- `1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4`
- `1 <= startTime[i] < endTime[i] <= 10^9`
- `1 <= profit[i] <= 10^4`

---

#### Tricky 

* DP1       **LTE**

  Store all these jobs into `Job[] jobs`.

  **`dp[i]` means the max profit `jobs[i]` can get if we must do this job.**

  Sort all jobs by start time then we need to search `j ~ i` to find `jobs[j].end <= jobs[i].start` to update `dp[i]`

  `dp[i] = max { dp[j] + profit[i] for j in range(i)}`

  The result will be detected during DP. (The result is not `dp[n - 1]`).

  Since the max length of profit will be `5 * 10^4`, O(n^2) will lead to **LTE**.

  ```java
  class Solution {
      class Job {
          int start;
          int end;
          int profit;
          public Job(int s, int e, int p) {
              start = s;
              end = e;
              profit = p;
          }
      }
      public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
          int n = startTime.length;
          Job[] jobs = new Job[n];
          for (int i = 0; i < n; i++) {
              jobs[i] = new Job(startTime[i], endTime[i], profit[i]);
          }
          Arrays.sort(jobs, (a, b) -> a.start - b.start);
          int[] dp = new int[n + 1];
          dp[0] = jobs[0].profit;
          int res = dp[0];
          for (int i = 1; i < n; i++) {
              int max = Integer.MIN_VALUE;
              for (int j = 0; j < i; j++) {
                  if (jobs[j].end <= jobs[i].start) {
                      max = Math.max(max, dp[j]);
                  }
              }
              dp[i] = (max == Integer.MIN_VALUE) ? jobs[i].profit : max + jobs[i].profit;
              res = Math.max(res, dp[i]);
          }
          return res;
      }
  }
  ```

  T: O(n^2)	**LTE**	

  S: O(n)

* DP2

  `dp[i]` means the max profit we can get at index `i`, which means we can do this job or not do this job.

  If we want to do this job, we need to search the nearest job end before this job.

  If we don't want to do this job, `dp[i] = dp[i - 1]`.

  To search the nearest job end  before current job, we can sort all jobs by EndTime and then we could perform BinarySearch to find `jobs[j]` that `dp[i] = dp[j] + jobs[i].profit`

  The result is `dp[n - 1]`

  ```java
  class Solution {
      class Job {
          int start;
          int end;
          int profit;
          public Job(int s, int e, int p) {
              start = s;
              end = e;
              profit = p;
          }
      }
      public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
          int n = startTime.length;
          Job[] jobs = new Job[n];
          for (int i = 0; i < n; i++) {
              jobs[i] = new Job(startTime[i], endTime[i], profit[i]);
          }
          Arrays.sort(jobs, (a, b) -> a.end - b.end);
          int[] dp = new int[n + 1];
          dp[0] = jobs[0].profit;
          for (int i = 1; i < n; i++) {
              int j = search(jobs, 0, i, jobs[i].start);
              int doJob = jobs[i].profit;
              if (j >= 0) doJob += dp[j];
              dp[i] = Math.max(dp[i - 1], doJob);
          }
          return dp[n - 1];
      }
      
      private int search(Job[] jobs, int l, int r, int key) {
          while (l < r) {
              int mid = l + (r - l) / 2;
              if (jobs[mid].end <= key) {
                  l = mid + 1;
              } else {
                  r = mid;
              }
          }
          return l - 1;
      }
  }
  ```

  T: O(nlogn)		S: O(n)