---
title: Medium | Subarray Sum Equals K 560
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - Two Pointers
date: 2020-01-04 21:12:07
---

Given an array of integers and an integer **k**, you need to find the total number of continuous subarrays whose sum equals to **k**.

[Leetcode](https://leetcode.com/problems/subarray-sum-equals-k/)

<!--more-->

**Example 1:**

```
Input:nums = [1,1,1], k = 2
Output: 2
```

**Note:**

1. The length of the array is in range [1, 20,000].
2. The range of numbers in the array is [-1000, 1000] and the range of the integer **k** is [-1e7, 1e7].

**Follow up**

[Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)

---

#### Tricky 

Firstly, I thought to use sliding window. But I found that there're negative values, so the sum will decrease and stops shrinking the window.

We could calculate `sum(i, j)` using `preSum[j] - preSum[i]`.

And store number of subarrays with sum in a map.

Then when we at index `j`, we can get number of subarrays with `sum(i, j) = k` by `map.get(preSum[j] - k)`

---

#### Standard solution 

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        int sum = 0;
        int res = 0;
        map.put(0, 1);								// initial prefix sum value
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            res += map.getOrDefault(sum - k, 0);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return res;
    }
}
```

T: O(n) 		S: O(n)
