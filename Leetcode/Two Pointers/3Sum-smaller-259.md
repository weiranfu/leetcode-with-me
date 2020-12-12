---
title: Medium | 3Sum Smaller 259
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-07-06 19:10:22
---

Given an array of *n* integers *nums* and a *target*, find the number of index triplets `i, j, k` with `0 <= i < j < k < n` that satisfy the condition `nums[i] + nums[j] + nums[k] < target`.

Could you solve it in *O*(*n*2) runtime?

[Leetcode](https://leetcode.com/problems/3sum-smaller/)

<!--more-->

**Example:**

```
Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
```

**Follow up:** 

[3Sum](https://leetcode.com/problems/3sum/)

---

#### Tricky 

Since we only need to return the number of combinations, we could perform Two Pointers to find sum of two numbers with third number fixed.

---

#### Standard solution  

```java
class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        Arrays.sort(nums);
        int res = 0;
        for (int i = 0; i < n; i++) {
            int l = i + 1, r = n - 1;
            while (l < r) {
                if (nums[i] + nums[l] + nums[r] < target) {
                    res += r - l;
                    l++;
                } else {
                    r--;
                }
            }
        }
        return res;
    }
}
```

T: O(n^2)			S: O(1)