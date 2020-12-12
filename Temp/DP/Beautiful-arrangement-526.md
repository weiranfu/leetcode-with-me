---
title: Medium | Beautiful Arrangement 526
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-12 01:02:17
---

Suppose you have **N** integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these **N** numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

1. The number at the ith position is divisible by **i**.
2. **i** is divisible by the number at the ith position.

Now given N, how many beautiful arrangements can you construct?

[Leetcode](https://leetcode.com/problems/beautiful-arrangement/)

<!--more-->

**Example 1:**

```
Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
```

**Note:**

1. **N** is a positive integer and will not exceed 15.

---

#### Tricky 

This is a full arrangement problem.

**The time complexity for brute force will be O(n!)**

1. Backtracking

   Brute force: enumerate all possible arrangement.

   ```java
   class Solution {
       
       int cnt = 0;
       
       public int countArrangement(int N) {
           if (N == 0) return 0;
           boolean[] visited = new boolean[N + 1];
           dfs(0, N, visited);
           return cnt;
       }
       
       private void dfs(int size, int N, boolean[] visited) {
           if (size == N) {
               cnt++;
               return;
           }
           for (int i = 1; i <= N; i++) {
               if (!visited[i] && ((size + 1) % i == 0 || i % (size + 1) == 0)) {
                   visited[i] = true;
                   dfs(size + 1, N, visited);
                   visited[i] = false;
               }
           }
       }
   }
   ```

   T: O(n!)			S: O(n)

2. DP with bitmask

   Use bitmask to represent an arrangement of N numbers,

   for `dp[s]`, we need to find the last added number and its position to check whether it is beautiful.

   Use `Integer.bitCount(i)` to find its position.

   ```java
   class Solution {
       public int countArrangement(int N) {
           if (N == 0) return 0;
           int[] dp = new int[1 << N];
           dp[0] = 1;
           for (int s = 1; s < 1 << N; s++) {
               for (int i = 0; i < N; i++) {
                   if ((s >> i & 1) == 1) {        // if contains i
                       int p = Integer.bitCount(s);// pos index
                       if ((i + 1) % p == 0 || p % (i + 1) == 0) {
                           int k = s & ~(1 << i);
                           dp[s] += dp[k];
                       }
                   }
               }
           }
           return dp[(1 << N) - 1];
       }
   }
   ```

   T: O(n\*2^n)