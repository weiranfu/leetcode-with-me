---
title: Hard | Minimum Number of Days to Eat N Oranges 1553
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-08-17 16:20:55
---

There are `n` oranges in the kitchen and you decided to eat some of these oranges every day as follows:

- Eat one orange.
- If the number of remaining oranges (`n`) is divisible by 2 then you can eat  n/2 oranges.
- If the number of remaining oranges (`n`) is divisible by 3 then you can eat  2*(n/3) oranges.

You can only choose one of the actions per day.

Return the minimum number of days to eat `n` oranges.

[Leetcode](https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/)

<!--more-->

**Example 1:**

```
Input: n = 10
Output: 4
Explanation: You have 10 oranges.
Day 1: Eat 1 orange,  10 - 1 = 9.  
Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)
Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. 
Day 4: Eat the last orange  1 - 1  = 0.
You need at least 4 days to eat the 10 oranges.
```

**Example 2:**

```
Input: n = 6
Output: 3
Explanation: You have 6 oranges.
Day 1: Eat 3 oranges, 6 - 6/2 = 6 - 3 = 3. (Since 6 is divisible by 2).
Day 2: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1. (Since 3 is divisible by 3)
Day 3: Eat the last orange  1 - 1  = 0.
You need at least 3 days to eat the 6 oranges.
```

**Constraints:**

- `1 <= n <= 2*10^9`

---

#### DP  **LTE**

A typical DP solution. Note that the `n` can be `2*10^9`, so there'll be `LTE`

```java
class Solution {
    public int minDays(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            int min = Integer.MAX_VALUE;
            min = 1 + dp[i - 1];
            if (i % 2 == 0) min = Math.min(min, 1 + dp[i / 2]);
            if (i % 3 == 0) min = Math.min(min, 1 + dp[i / 3]);
            dp[i] = min;
        }
        return dp[n];
    }
}
```

T: O(n)			S: O(n)

---

#### Optimized: DP + Greedy

1. Greedy

   Since it will be much better if `n` can be divided by `2` or `3`. If it is, we will never choose to eat only 1 orange. If it cannot be divided by `2` or `3`, we will try to eat some oranges and divide it by `2` or `3`.

2. Memory optimization

   Since we will never reuse the `dp[x]` if `x` is very large, we can optimize the memory space to avoid **memory limit exceeded** problem.

   We could use a map to store our state of dp.

   ```java
   class Solution {
       Map<Integer, Integer> dp;
       public int minDays(int n) {
           dp = new HashMap<>();
           return dfs(n);
       }
       private int dfs(int n) {
           if (n == 1) return 1;
           if (n == 2 || n == 3) return 2;
           if (dp.containsKey(n)) return dp.get(n);
           int min = Math.min(dfs(n / 2) + n % 2, dfs(n / 3) + n % 3) + 1;
           dp.put(n, min);
           return min;
       }
   }
   ```

   T: O(logn)		S: O(logn)

---

#### Graph + BFS

Since we have three choices at `n`, we could build a graph of connected states with edge weight 1.

Then we could perform BFS to find the minimum weight path from `n` to `0`.

**How to deal with duplicate State?** we could use a set the remember which state we have visited to avoid **LTE**

```java
class Solution {
    public int minDays(int n) {
        int cnt = 0;
        Set<Integer> set = new HashSet<>();
        Queue<Integer> q = new LinkedList<>();
        q.add(n);
        while (!q.isEmpty()) {
            cnt++;
            int size = q.size();
            while (size-- != 0) {
                int u = q.poll();
                set.add(u);
                if (u - 1 == 0) return cnt;
                if (!set.contains(u - 1)) q.add(u - 1);
                if (u % 2 == 0 && !set.contains(u / 2)) q.add(u / 2);
                if (u % 3 == 0 && !set.contains(u / 3)) q.add(u / 3);
            }
        }
        return -1;
    }
}
```

T: O(logn)		S: O(logn)

