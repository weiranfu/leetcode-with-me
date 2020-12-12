---
title: Hard | Split Array Largest Sum 410	
tags:
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-06-15 17:16:16
---

Given an array which consists of non-negative integers and an integer *m*, you can split the array into *m* non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these *m* subarrays.

[Leetcode](https://leetcode.com/problems/split-array-largest-sum/)

<!--more-->

**Note:**
If *n* is the length of array, assume the following constraints are satisfied:

- 1 ≤ *n* ≤ 1000
- 1 ≤ *m* ≤ min(50, *n*)

**Examples:**

```
Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
```

---

#### Tricky 

最小值最大 或者 最大值最小 (maximize the minimum OR minimize the maximum) we all use Binary Search

**How to determine the largest sum value? If large sum value is very large, we could find a method to divide array into appropriate subarrays. If this value is too small, we have to divide array into many subarrays.**

**We can use binary search to find this largest sum value. **

For a given largest sum value `mid`, we use greedy approach to divide the array into subarrays. If the number of subarrays is greater than `m`, we will search a larger sum value, so `[mid + 1, right]`. If the number of subarrays is smaller or equal to `m`, we will search a smaller sum value, so `[left, mid]`.

---

#### DP

We could use DP to solve this problem. `dp[k][i]` means for `array[:i]`, we divide it into `k` subarrays, the minimum largest subarray sum is `dp[i][k]`.

We could try to split array from a smaller index `j` to `i` to form the `k`th subarray.

`dp[k][i] = min{ dp[k][i], max{ dp[k-1][j], nums[j + 1] + ... + nums[i]} for j in [1, i-1] } }`

Initialize:

we need to initialize all cases `k == 1` and `i` must greater than or equal to `k`: `i >= k`

```java
class Solution {
    public int splitArray(int[] nums, int m) {
        int n = nums.length;
        int[] preSum = new int[n + 1];
        for (int i = 1; i <= n; i++) {
             preSum[i] = preSum[i - 1] + nums[i - 1];
        }
        int[][] dp = new int[m + 1][n + 1];
        
        for (int i = 1; i <= n; i++) {
            dp[1][i] = preSum[i];          // initialize
        }
        for (int k = 2; k <= m; k++) {
            for (int i = k; i <= n; i++) { // i must >= k
                int min = Integer.MAX_VALUE;
                for (int j = 1; j < i; j++) {
                    min = Math.min(min, Math.max(dp[k - 1][j], preSum[i] - preSum[j]));
                }
                dp[k][i] = min;
            }
        }
        
        return dp[m][n];
    }
}
```

T: O(n^2 \* m)				S: O(n^2)

---

#### Binary search

For a given largest sum value `mid`, we use greedy approach to divide the array into subarrays. If the number of subarrays is greater than `m`, we will search a larger sum value, so `[mid + 1, right]`. If the number of subarrays is smaller or equal to `m`, we will search a smaller sum value, so `[left, mid]`.

```java
class Solution {
    public int splitArray(int[] nums, int m) {
        int n = nums.length;
        long left = 0, right = 0;
        for (int i : nums) {
            left = Math.max(left, i);// left bound is max of array
            right += i;              // right bound is sum of array
        }
        while (left < right) {
            long mid = left + (right - left) / 2;
            if (check(nums, m, mid)) {   // find smaller sum value
                right = mid;
            } else {           
                left = mid + 1;
            }
        }
        return (int)left;
    }
    
    // small --- large
    // n          1
    // if (check) we will search for smaller max
    private boolean check(int[] nums, int m, long max) {
        int n = nums.length;
        int count = 0;
        long sum = 0;
        for (int i = 0; i < n; i++) {
            if (sum + nums[i] > max) { // greedy 
                count++;
                sum = 0;
            }
            sum += nums[i];
        }
        count++;                  // last subarray
        return count <= m;
    }
}
```

T: O(n\*logMax)			S: O(1)



