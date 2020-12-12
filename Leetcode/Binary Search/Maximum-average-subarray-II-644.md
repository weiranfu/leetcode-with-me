---
title: Hard | Maximum Average Subarray II 644
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-06-28 18:15:02
---

Given an array consisting of `n` integers, find the contiguous subarray whose **length is greater than or equal to** `k` that has the maximum average value. And you need to output the maximum average value.

[Leetcode](https://leetcode.com/problems/maximum-average-subarray-ii/)

<!--more-->

**Example 1:**

```
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
when length is 4, maximum average value is 12.75.  =>. [12,-5,-6,50]
Thus return 12.75.
```

**Note:**

1. 1 <= `k` <= `n` <= 10,000.
2. Elements of the given array will be in range [-10,000, 10,000].
3. The answer with the calculation error less than 10-5 will be accepted.

---

#### Tricky 

We want to compute the average:

```java
(nums[i]+nums[i+1]+...+nums[j])/(j-i+1) >= x
=>nums[i]+nums[i+1]+...+nums[j] >= x*(j-i+1)
=>(nums[i]-x)+(nums[i+1]-x)+...+(nums[j]-x) >= 0
```

**Then the problem become to find a subarray with sum greater than or equal to 0 and with length greater than K.**

We want to find the maximum of this average, we could check whether `sum >= 0` under this average is satsified with length greater than K.

How to check the `sum >= 0` under an average and with length greater than K?

**We could perform window sliding and keep track the sum before the window with size K.**

if `prev < 0`, we can remove that part of subarray.

---

#### Standard solution  

```java
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int n = nums.length;
        double min = nums[0], max = nums[0];
        for (int num : nums) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }
        double l = min, r = max;
        while (l + 1e-6 < r) {
            double mid = (l + r) / 2;
            if (hasAvg(nums, k, mid)) {   // this average satsify the condition
                l = mid;
            } else {
                r = mid;
            }
        }
        return l;
    }
    
    // check nums[] can have this average value.
    public boolean hasAvg(int[] nums, int k, double val) {
        int n = nums.length;
        double[] arr = new double[n];
        for (int i = 0; i < n; i++) {
            arr[i] = nums[i] - val;
        }
        double sum = 0;
        for (int i = 0; i < k; i++) {
            sum += arr[i];
        }
        if (sum >= 0) return true;       // check sum >= 0
        double prev = 0;
        for (int i = k; i < n; i++) {
            sum += arr[i];
            prev += arr[i - k];
            if (prev < 0) {
                sum -= prev;           // remove that part of subarray
                prev = 0;
            }
            if (sum >= 0) return true;
        }
        return false;
    }
}
```

T: O(n * logMax)			S: O(n)