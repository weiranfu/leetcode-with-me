---
title: Easy | K-diff Pairs in an Array 532
tags:
  - common
  - tricky
  - corner case
categories:
  - Leetcode
  - Array
date: 2020-08-26 11:56:49
---

Given an array of integers and an integer **k**, you need to find the number of **unique** k-diff pairs in the array. Here a **k-diff** pair is defined as an integer pair (i, j), where **i** and **j** are both numbers in the array and their [absolute difference](https://en.wikipedia.org/wiki/Absolute_difference) is **k**.

[Leetcode](https://leetcode.com/problems/k-diff-pairs-in-an-array/)

<!--more-->

**Example 1:**

```
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
```

**Example 2:**

```
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
```

**Example 3:**

```
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
```

**Follow up**

[Pairs of Songs with Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)

---

#### Standard solution  

The key is to deal with **unique** pairs and deal with the case that `k == 0`.

If `k == 0`, we need to check whether `nums[i]` occurs for the second time.

So we cannot use a Set but to use a Map.

```java
class Solution {
    public int findPairs(int[] nums, int k) {
        if (nums == null || nums.length == 0 || k < 0) return 0;
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (map.containsKey(nums[i])) {
                if (k == 0 && map.get(nums[i]) == 1) {	// check nums[i]'s occurrence
                    cnt++;
                }
                map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
            } else {
                if (map.containsKey(nums[i] - k)) cnt++;	// unique pairs
                if (map.containsKey(nums[i] + k)) cnt++;
                map.put(nums[i], 1);
            }
        }
        return cnt;
    }
}
```



