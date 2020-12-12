---
title: Hard | Russian Doll Envelopes 354
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-06-26 16:41:05
---

You have a number of envelopes with widths and heights given as a pair of integers `(w, h)`. One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

[Leetcode](https://leetcode.com/problems/russian-doll-envelopes/)

<!--more-->

**Example:**

```
Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
```

**Follow up:**

[Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

---

#### Tricky 

* Sort with DP

  Sort these dolls and use `dp[i]` to store the maximum length.

  ```java
  if (envelopes[j][0] < w && envelopes[j][1] < h) {
  	max = Math.max(max, dp[j] + 1);
  }
  ```

* Sort + Longest Increasing Subsequence

  After we sort our envelopes, we can simply find the length of the longest increasing subsequence on the second dimension (`h`)

  Note that we use a clever trick to solve some edge cases:

  Consider an input `[[1, 3], [1, 4], [1, 5], [2, 3]]`. If we simply sort and extract the second dimension we get `[3, 4, 5, 3]`, which implies that we can fit three envelopes (3, 4, 5). The problem is that we can only fit one envelope, since envelopes that are equal in the first dimension can't be put into each other.

  **In order fix this, we don't just sort increasing in the first dimension - we also sort *decreasing* on the second dimension, so two envelopes that are equal in the first dimension can never be in the same increasing subsequence.**

  Now when we sort and extract the second element from the input we get `[5, 4, 3, 3]`, which correctly reflects an LIS of one.

---

#### Sort + DP

```java
class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        if (envelopes == null || envelopes.length == 0) return 0;
        Arrays.sort(envelopes, (a, b) -> a[0] - b[0]);
        int n = envelopes.length;
        int[] dp = new int[n + 1];
        int res = 1;
        for (int i = 1; i <= n; i++) {
            int w = envelopes[i - 1][0];
            int h = envelopes[i - 1][1];
            int max = 1;
            for (int j = 1; j < i; j++) {
                if (envelopes[j - 1][0] < w && envelopes[j - 1][1] < h) {
                    max = Math.max(max, dp[j] + 1);
                }
            }
            dp[i] = max;
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}
```

T: O(n^2)			S: O(n)

---

#### Sort + LIS

Use binary search to find Longest Increasing Subsequences

To avoid same width and different height of envelopes, we sort envelopes with same width by decreasing height.

```java
class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        if (envelopes == null || envelopes.length == 0) return 0;
        Arrays.sort(envelopes, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1];
            } else {
                return a[0] - b[0];
            }
        });
        int n = envelopes.length;
        int[] tails = new int[n];
        int len = 0;
        for (int i = 0; i < n; i++) {
            int l = 0, r = len;
            while (l < r) {
                int mid = l + (r - l) / 2;
                if (tails[mid] < envelopes[i][1]) {
                    l = mid + 1;
                } else {
                    r = mid;
                }
            }
            tails[l] = envelopes[i][1];
            if (l == len) {
                len++;
            }
        }
        return len;
    }
}
```

T: O(nlogn)		S: O(n)

