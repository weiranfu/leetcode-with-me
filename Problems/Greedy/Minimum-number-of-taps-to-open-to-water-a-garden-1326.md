---
title: Hard | 1326 Minimum Number of Taps to Open to Water a Garden 1326
tags:
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-01-21 15:56:27
---

There is a one-dimensional garden on the x-axis. The garden starts at the point `0` and ends at the point `n`. (i.e The length of the garden is `n`).

There are `n + 1` taps located at points `[0, 1, ..., n]` in the garden.

Given an integer `n` and an integer array `ranges` of length `n + 1` where `ranges[i]` (0-indexed) means the `i-th` tap can water the area `[i - ranges[i], i + ranges[i]]` if it was open.

Return *the minimum number of taps* that should be open to water the whole garden, If the garden cannot be watered return **-1**.

[Leetcode](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/)

<!--more-->

**Example 1:**

```
Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
```

**Example 2:**

```
Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
```

**Example 3:**

```
Input: n = 7, ranges = [1,2,1,0,2,1,0,1]
Output: 3
```

---

#### Tricky 

* This is a Greedy problem. We can sort this taps by start point.

  If we get our minimum taps to cover an area, we always want to find next max length area to extend to.

  So we can explore these taps to find max end point with `start point <= current length`.


---

#### DP (Brute Force)

Use a dp table to store the min taps for each start point. Sort taps by start point.

Subproblem: taps[i:].    # of subproblems is O(n)

Guess: for dp[i], guess from previous taps which can be extend to this tap. Find the min taps of them.

Recurrence: 	`dp[i] = Min{ dp[j] + 1 for j in range(i) where taps[j][1] >= taps[i][0] }`

```java
class Solution {
    public int minTaps(int n, int[] ranges) {
        int[][] taps = new int[ranges.length][2];
        for (int i = 0; i < ranges.length; ++i) {
            taps[i][0] = i - ranges[i];
            taps[i][1] = i + ranges[i];
        }
        Arrays.sort(taps, (a, b) -> a[0] - b[0]);
        int[] dp = new int[ranges.length];
        for (int i = 0; i < taps.length; ++i) {
            if (taps[i][0] <= 0) {
                dp[i] = 1;
            } else {
                dp[i] = Integer.MAX_VALUE;
                for (int j = 0; j < i; ++j) {
                    if (dp[j] != Integer.MAX_VALUE && taps[j][1] >= taps[i][0]) {
                        dp[i] = Math.min(dp[j] + 1, dp[i]);    
                    }
                }
            }
            if (taps[i][1] >= n && dp[i] != Integer.MAX_VALUE) {
                return dp[i];
            }
        }
        return -1;
    }
}
```

T: O(n^2) 			S: O(n)

---

#### Greedy (Optimized)

[Similar Question: Video Switching](https://leetcode.com/problems/video-stitching/)

We can perform greedy. Every time we only want to extend our area as far as possible.

So we only need to pick the farthest end point tap, and extend to that point.

```java
class Solution {
    public int minTaps(int n, int[] ranges) {
        int[][] taps = new int[n + 1][2];
        for (int i = 0; i <= n; i++) {
            int a = Math.max(0, i - ranges[i]);
            int b = Math.min(n, i + ranges[i]);
            taps[i] = new int[]{a, b};
        }
        Arrays.sort(taps, (a, b) -> a[0] - b[0]);
        int cnt = 0, end = 0;
        for (int i = 0; i <= n; i++) {
            int j = i, r = -1;
            while (j <= n && taps[j][0] <= end) {
                r = Math.max(r, taps[j][1]);
                j++;
            }
            cnt++;
            if (r < end) return -1;  // cannot reach end 
            if (r >= n) return cnt;  // reach the endpoint
            end = r;
            i = j - 1;
        }
        return -1;
    }
}
```

T: O(nlogn)			S: O(n)

---

#### Jump Ability  

[Similar Queston: Jump Game II](https://leetcode.com/problems/jump-game-ii/)

We can convert the taps area into jump ability. Array `jumps[i]` means at point i we can jump most `jumps[i]` far away.

So we just need to loop over jumps, and record how far away can we jump most.

If we come to a place where is ahead of last jump point, we need to a step to reach here.

```java
class Solution {
    public int minTaps(int n, int[] ranges) {
        int[] jump = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            int curr = Math.max(0, i - ranges[i]);
            jump[curr] = Math.max(jump[curr], Math.min(n, i + ranges[i]));
        }
        int end = 0;
        int cnt = 0;
        for (int i = 0; i <= n; i++) {
            int j = i, r = -1;
            while (j <= n && j <= end) {
                r = Math.max(r, jump[j++]);
            }
            cnt++;
            if (r <= end) return -1;        // cannot reach end
            if (r >= n) return cnt;         // reach endpoint
            end = r;
            i = j - 1;
        }
        return -1;
    }
}
```

T: O(n) 			S: O(n)
