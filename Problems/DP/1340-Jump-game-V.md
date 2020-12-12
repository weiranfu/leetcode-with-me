---
title: Hard | Jump Game V 1340
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-02-05 15:13:21
---

Given an array of integers `arr` and an integer `d`. In one step you can jump from index `i` to index:

- `i + x` where: `i + x < arr.length` and `0 < x <= d`.
- `i - x` where: `i - x >= 0` and `0 < x <= d`.

In addition, you can only jump from index `i` to index `j` if `arr[i] > arr[j]` and `arr[i] > arr[k]` for all indices `k` between `i` and `j` (More formally `min(i, j) < k < max(i, j)`).

You can choose any index of the array and start jumping. Return *the maximum number of indices* you can visit.

Notice that you can not jump outside of the array at any time.

[Leetcode](https://leetcode.com/problems/jump-game-v/)

<!--more-->

**Example 1:**





```
Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.
```

**Example 2:**

```
Input: arr = [3,3,3,3,3], d = 3
Output: 1
Explanation: You can start at any index. You always cannot jump to any index.
```

**Example 3:**

```
Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indicies. 
```

---

#### Tricky 

This is not a typical DP problem.

The common solution is dp with memorization. Try all possible start point and memorize max steps can reach from each point.

As for bottom-up DP, because we cannot jump from lower to higher place, we sort the array by height.

1. Subproblems: `array[:i]`

   number of subproblems is O(n)

However, we need to preserve the original index, cause we need to check out whether we can jump.

So we create a 2D array to store original index and sort it by height.

2. Guess

   Try to jump left and right with limit `d`.

3. Recurrence

   `dp[index] = Math.max(dp[index], 1 + dp[j]) for j in range(index - d, index + d);`

4. Total time

   num of subproblem* time/subproblem = O(n)* O(d) = O(nd)

---

#### My thoughts 

DP with memorization.

Use a map to store max steps can reach from index i.

---

#### Memorization 

Because we need to store steps, we choose to use `int[] map` instead of  `Map<Integer, Integer> map`.

```java
class Solution {
    public int maxJumps(int[] arr, int d) {
        int n = arr.length;
        if (n == 0) return 0;
        int[] map = new int[n];
        Arrays.fill(map, -1);
        int res = 0;
        for (int i = 0; i < n; i++) {
            res = Math.max(res, getJump(arr, i, map, d) + 1);
        }
        return res;
    }
    private int getJump(int[] arr, int s, int[] map, int d) {
        if (map[s] != -1) return map[s];
        int max = 0;
        for (int i = s - 1; i >= 0 && i >= s - d; i--) {
            if (arr[i] >= arr[s]) break;
            max = Math.max(max, 1 + getJump(arr, i, map, d));
        }
        for (int i = s + 1; i < arr.length && i <= s + d; i++) {
            if (arr[i] >= arr[s]) break;
            max = Math.max(max, 1 + getJump(arr, i, map, d));
        }
        map[s] = max;
        return max;
    }
}
```

T: O(nd) 			S: O(n)

---

#### Bottom-up

Sort array by height, subproblem is `array[:i]`

```java
class Solution {
    public int maxJumps(int[] arr, int d) {
        int n = arr.length;
        if (n == 0) return 0;
        int[][] array = new int[n][2];
        for (int i = 0; i < n; i++) {
            array[i] = new int[]{arr[i], i};
        }
        Arrays.sort(array, (a, b) -> a[0] - b[0]);
        int[] dp = new int[n];
        int res = 0;
        for (int i = 0; i < n; i++) {
            int index = array[i][1];
            for (int j = index - 1; j >= 0 && j >= index - d; j--) {
                if (arr[j] >= arr[index]) break;
                dp[index] = Math.max(dp[index], 1 + dp[j]);
            }
            for (int j = index + 1; j < arr.length && j <= index + d; j++) {
                if (arr[j] >= arr[index]) break;
                dp[index] = Math.max(dp[index], 1 + dp[j]);
            }
            res = Math.max(res, dp[index] + 1);
        }
        return res;
    }
}
```

T: O(nd)			S: O(n)

---

#### Summary 

In tricky.