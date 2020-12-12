---
title: Hard | Parallel Courses II 1494
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-22 16:03:17
---

Given the integer `n` representing the number of courses at some university labeled from `1` to `n`, and the array `dependencies` where `dependencies[i] = [xi, yi]`  represents a prerequisite relationship, that is, the course `xi` must be taken before the course `yi`.  Also, you are given the integer `k`.

In one semester you can take **at most** `k` courses as long as you have taken all the prerequisites for the courses you are taking.

*Return the minimum number of semesters to take all courses*. It is guaranteed that you can take all courses in some way.

[Leetcode](https://leetcode.com/problems/parallel-courses-ii/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2020/05/22/leetcode_parallel_courses_1.png)**

```
Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
Output: 3 
Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2020/05/22/leetcode_parallel_courses_2.png)**

```
Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4 
Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.
```

**Constraints:**

- `1 <= n <= 15`
- `1 <= k <= n`
- `0 <= dependencies.length <= n * (n-1) / 2`
- `dependencies[i].length == 2`
- `1 <= xi, yi <= n`
- `xi != yi`
- All prerequisite relationships are distinct, that is, `dependencies[i] != dependencies[j]`.
- The given graph is a directed acyclic graph.

---

#### DP with Bitmask

`dp[s]` means the min semesters under state `s`.

`check[i]` means taking course `i`, we need to check the dependencies `check[i]`

**At each state `s`, we need to get all available courses we can take at that `state`, and increase current semester 1 and must take `k` courses from them.**

We could do a DFS to choose `k` courses from all available courses. (Possitive Transition of DP)

We need to do a prunning to reduce DFS time complexity from `2^m` to `C_m^(min(m,k))` （组合数级别）

```java
class Solution {
    int n, k;
    int[] check;
    int[] dp;
    public int minNumberOfSemesters(int n, int[][] dependencies, int k) {
        this.n = n; this.k = k;
        check = new int[n];
        for (int[] dependency : dependencies) {
            int a = dependency[0] - 1;
            int b = dependency[1] - 1;
            check[b] = check[b] | (1 << a);			// add dependencies
        }
        dp = new int[1 << n];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        for (int s = 0; s < 1 << n; s++) {
            if (dp[s] == -1) continue;
            List<Integer> available = new ArrayList<>();		// get all available courses
            for (int i = 0; i < n; i++) {
                if ((s >> i & 1) == 0 && (s & check[i]) == check[i]) {
                    available.add(i);
                }
            }
            int size = available.size();
            dfs(s, 0, Math.min(k, size), dp[s] + 1, available); // open a new semester
        }
        return dp[(1 << n) - 1];
    }
  	/**
  	* @param x: consider at x pos in available list
  	* @param k: must choose k courses
  	*/
    private void dfs(int state, int x, int k, int semester, List<Integer> avail) {
        int size = avail.size();
        if (size - x < k) return;          // prunning
        if (k == 0) {
            if (dp[state] == -1 || dp[state] > semester) {
                dp[state] = semester;
            }
            return;
        }
        for (int i = x; i < size; i++) {
            dfs(state | (1 << avail.get(i)), i + 1, k - 1, semester, avail);
        }
    }
}
```

T: O(2^n\*n^2) 

S: O(n)

---

#### Optimized

We could enumerate all possible k courses from available courses to perform transition.

```java
class Solution {
    public int minNumberOfSemesters(int n, int[][] dependencies, int k) {
        int[] check = new int[n];
        for (int[] dependency : dependencies) {
            int a = dependency[0] - 1;
            int b = dependency[1] - 1;
            check[b] = check[b] | (1 << a);
        }
        int[] dp = new int[1 << n];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        for (int s = 0; s < 1 << n; s++) {
            if (dp[s] == -1) continue;
            int avail = 0;
            int cnt = 0;            // count available courses
            for (int i = 0; i < n; i++) {
                if ((s >> i & 1) == 0 && (s & check[i]) == check[i]) {
                    avail |= 1 << i;
                    cnt++;
                }
            }
            int choose = Math.min(cnt, k); // must choose min(cnt, k) courses
            // enumerate all subset of available courses
            for (int state = avail; state > 0; state = (state - 1) & avail) {
                if (Integer.bitCount(state) == choose) {
                    if (dp[s | state] == -1 || dp[s | state] > dp[s] + 1) {
                        dp[s | state] = dp[s] + 1;
                    }
                }
            }
        }
        return dp[(1 << n) - 1];
    }
}
```

T: O(2^n\*n)			S: O(n)