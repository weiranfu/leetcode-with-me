---
title: Hard | Get the maximum score 1537
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-08-25 10:06:47
---

You are given two **sorted** arrays of distinct integers `nums1` and `nums2.`

A **valid path** is defined as follows:

- Choose array nums1 or nums2 to traverse (from index-0).
- Traverse the current array from left to right.
- If you are reading any value that is present in `nums1` and `nums2` you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).

*Score* is defined as the sum of uniques values in a valid path.

Return the maximum *score* you can obtain of all possible **valid paths**.

Since the answer may be too large, return it modulo 10^9 + 7.

[Leetcode](https://leetcode.com/problems/get-the-maximum-score/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2020/07/16/sample_1_1893.png)**

```
Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
Output: 30
Explanation: Valid paths:
[2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from nums1)
[4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nums2)
The maximum is obtained with the path in green [2,4,6,8,10].
```

**Constraints:**

- `1 <= nums1.length <= 10^5`
- `1 <= nums2.length <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^7`
- `nums1` and `nums2` are strictly increasing.

---

#### DP 

Store the maximum score at each state into `dp1[i]` and `dp2[j]`.

Since two arrays are sorted, we can try to compare two arrays in *merge two sorted array* way.

**Note that we need to mod the result by 10^9+7, we cannot mod the result during the caculation of dp1[i] and dp2[j], so we need to use `long[]`to store results and mod the result at the end.**

```java
class Solution {
    public int maxSum(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        long[] dp1 = new long[m + 1];
        long[] dp2 = new long[n + 1];
        int mod = (int)1e9 + 7;
        int i = 1, j = 1;
        while (i <= m && j <= n) {
            if (nums1[i - 1] > nums2[j - 1]) {
                dp2[j] = dp2[j - 1] + nums2[j - 1];
                j++;
            } else if (nums1[i - 1] < nums2[j - 1]) {
                dp1[i] = dp1[i - 1] + nums1[i - 1];
                i++;
            } else {
                dp1[i] = dp2[j] = Math.max(dp1[i - 1], dp2[j - 1]) + nums1[i - 1];
                i++; j++;
            }
        }
        while (i <= m) {
            dp1[i] = dp1[i - 1] + nums1[i - 1];
            i++;
        }
        while (j <= n) {
            dp2[j] = dp2[j - 1] + nums2[j - 1];
            j++;
        }
        return (int)(Math.max(dp1[m], dp2[n]) % mod);
    }
}
```

T: O(n)			S: O(n)

**Optimization:** we could perform space optimization on `dp[]` array.

