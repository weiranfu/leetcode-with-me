---
title: Medium | Count Number of Nice Subarrays 1248
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-07-28 19:55:19
---

Given an array of integers `nums` and an integer `k`. A subarray is called **nice** if there are `k` odd numbers on it.

Return the number of **nice** sub-arrays.

[Leetcode](https://leetcode.com/problems/count-number-of-nice-subarrays/)

<!--more-->

**Example 1:**

```
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
```

**Example 2:**

```
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
```

**Example 3:**

```
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
```

---

#### Convert to *At Most K* odd numbers

Conver the problem to *Finding the subarrays with at most k odd numbers on it*.

```java
class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        return atMostK(nums, k) - atMostK(nums, k - 1);
    }
    private int atMostK(int[] nums, int k) {
        int n = nums.length;
        int res = 0, cnt = 0;
        for (int i = 0, j = 0; i < n; i++) {
            if (nums[i] % 2 != 0) cnt++;
            while (cnt > k) {
                if (nums[j] % 2 != 0) cnt--;
                j++;
            }
            res += i - j + 1;
        }
        return res;
    }
}
```

T: O(n)			S: O(1)

---

#### Sliding Window

Use `upper` to shrink the window, and count number of nice subarrays with `res += upper - j + 1`

```java
class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int n = nums.length;
        int upper = 0, cnt = 0;
        int res = 0;
        for (int i = 0, j = 0; i < n; i++) {
            if (nums[i] % 2 != 0) cnt++;
            while (upper <= i && cnt > k) {
                if (nums[upper] % 2 != 0) cnt--;
                upper++;
                j = upper;
            }
            if (cnt == k) {
                while (upper <= i && nums[upper] % 2 == 0) {
                    upper++;
                }
                res += upper - j + 1;
            }
        }
        return res;
    }
}
```

T: O(n)		S: O(1)

---

#### Cached Prefix Sum

Since the number of odd numbers satisfies the prefix sum.

`cnt[j, i] = cnt[0, i] - cnt[0, j]`

So we could cache number of subarrays with certain number of odd numbers.

When we need to compute the number of subarrays at index `i`, with current cnt `curr_cnt`

we can get it by `map.get(curr_cnt - k)`

```java
class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int n = nums.length;
        int[] cnt = new int[n + 1];
        cnt[0] = 1;     // initial prefix value
        int prefix_cnt = 0;
        int res = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 != 0) prefix_cnt++;
            res += prefix_cnt - k >= 0 ? cnt[prefix_cnt - k] : 0;     // retrieve subarrays
            cnt[prefix_cnt]++;
        }
        return res;
    }
}
```

T: O(n)			S: O(1)

