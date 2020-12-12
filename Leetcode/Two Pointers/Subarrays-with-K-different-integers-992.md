---
title: Hard | Subarrays With K Different Integers 992
tags:
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2019-11-24 20:51:29
---

Given an array `A` of positive integers, call a (contiguous, not necessarily distinct) subarray of `A` *good* if the number of different integers in that subarray is exactly `K`.  `1 <= A[i] <= A.length`.

(For example, `[1,2,3,1,2]` has `3` different integers: `1`, `2`, and `3`.)

Return the number of good subarrays of `A`.

[Leetcode](https://leetcode.com/problems/subarrays-with-k-different-integers/)

<!--more-->

**Example 1:**

```
Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
```

**Example 2:**

```
Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
```

**Follow up:**

[Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/)

---

#### Convert to *At most K* problem

**Intuition**:

First you may have feeling of using sliding window. Then this idea get stuck in the middle.

**This problem will be a very typical sliding window, if it asks the number of subarrays with *at most* K distinct elements.**

**The length of max sliding window with *At most* K distinct elements will be the number of subarrays.**

Just need one more step to reach the folloing equation:
`exactly(K) = atMost(K) - atMost(K-1)`

```java
class Solution {
    public int subarraysWithKDistinct(int[] A, int K) {
        return subarraysAtMostK(A, K) - subarraysAtMostK(A, K - 1);
    }
    
    private int subarraysAtMostK(int[] A, int K) {
        int n = A.length;
        Map<Integer, Integer> map = new HashMap<>();
        int res = 0;
        for (int i = 0, j = 0; i < n; i++) {
            if (map.getOrDefault(A[i], 0) == 0) K--;
            map.put(A[i], map.getOrDefault(A[i], 0) + 1);
            while (j <= i && K < 0) {
                map.put(A[j], map.get(A[j]) - 1);
                if (map.get(A[j]) == 0) K++;
                j++;
            }
            res += i - j + 1;					// count number of subarrays
        }
        return res;
    }
}
```

T: O(n)			S: O(n)

---

#### Sliding Window 

Since we need to count the number of subarrays with exactly K distinct integers, we could use a **third** pointer `upper` to shrink the window if `cnt[A[upper]] > 1`.

If `cnt[A[upper]] > 1` , this means there're at least 2 `A[upper]` in current window, so we could delete it from window and shrink window. If we meet `cnt[A[upper]] == 1`, this means we can't shrink window any otherwise there won't be K distinct integers.

Since every time we add a new `A[i]` into window, we only move `upper` pointer, `j` will stay at window starting point, so the number of subarrays ending with `A[i]` will be `upper - j + 1`. 

If the number of distinct integers exceed K, we can just delete `A[upper]` from map and move `j` to `upper`, because all integers between `[j, upper]` have been removed already.

```java
class Solution {
    public int subarraysWithKDistinct(int[] A, int K) {
        int n = A.length;
        Map<Integer, Integer> map = new HashMap<>();
        int res = 0;
        int upper = 0;
        for (int i = 0, j = 0; i < n; i++) {
            map.put(A[i], map.getOrDefault(A[i], 0) + 1);
            if (map.size() > K) {
                map.remove(A[upper]);		// currently cnt[A[upper]] == 1,
                upper++;				// so we remove A[upper] from map to decrease map size
                j = upper;
            }
            if (map.size() == K) {		// a valid window
                while (upper < i && map.get(A[upper]) > 1) { // try to shrink window
                    map.put(A[upper], map.get(A[upper]) - 1); // if there're at least
                    upper++;																 // 2 integers in the window
                }
                res += upper - j + 1;		// count number of subarray ending with A[i]
            }
        }
        return res;
    }
}
```

T: O(n)			S: O(n)