---
title: Easy Medium Hard | Minimum Operations To Reduce X To Zero 1658
categories:
  - LeetCode
  - Prefix
date: 2020-12-16 20:34:23
---

# Minimum Operations To Reduce X To Zero 1658

You are given an integer array `nums` and an integer `x`. In one operation, you can either remove the leftmost or the rightmost element from the array `nums` and subtract its value from `x`. Note that this **modifies** the array for future operations.

Return *the **minimum number** of operations to reduce* `x` *to **exactly*** `0` *if it's possible**, otherwise, return* `-1`.

[Leetcode](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

<!--more-->

**Example 1:**

```
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
```

**Example 2:**

```
Input: nums = [5,6,7,8,9], x = 4
Output: -1
```

**Example 3:**

```
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
```

**Constraints:**

- `1 <= nums.length <= 105`
- `1 <= nums[i] <= 104`
- `1 <= x <= 109`

---

#### Prefix Sum

We can use a map to store Prefix sum with number of operations from left to right.

Then scan from right to left and calculate sum and search `x - sum` in map to find minimum operations.

```java
class Solution {
    public int minOperations(int[] nums, int x) {
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        int min = Integer.MAX_VALUE;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            map.put(sum, i + 1);
            if (sum == x) min = Math.min(min, i + 1);
            if (sum >= x) break;
        }
        sum = 0;
        for (int i = n - 1; i >= 0; i--) {
            sum += nums[i];
            if (map.containsKey(x - sum) && map.get(x - sum) - 1 < i) {
                min = Math.min(min, map.get(x - sum) + n - i);
            }
            if (sum == x) min = Math.min(min, n - i);
            if (sum >= x) break;
        }
        return min == Integer.MAX_VALUE ? -1 : min;
    }
}
```

T: O(n)		S: O(n)

---

#### Optimized

Think in the other way! 

We know the total sum of `nums`, and after reducing elements from two ends, the remaining sum will be `totalSum - x`.

So the problem is translated to find a max length subarray whose sum `target` is `totalSum - x`.

**Note the corner case: the subarrays sum is `target`** 

```java
if (target < 0) return -1;
if (target == 0) return n;
```

```java
class Solution {
    public int minOperations(int[] nums, int x) {
        int n = nums.length;
        int total = 0;
        for (int num : nums) total += num;
        total -= x;
        if (total < 0) return -1;
        if (total == 0) return n;
        Map<Integer, Integer> map = new HashMap<>();
        int min = Integer.MAX_VALUE;
        int sum = 0;
        map.put(0, -1);   // if Subarray starts at 0.
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            if (map.containsKey(sum - total)) {
                int len = i - map.get(sum - total);
                min = Math.min(min, n - len);
            }
            map.put(sum, i);
        }
        return min == Integer.MAX_VALUE ? -1 : min;
    }
}
```

T: O(n)		S: O(n)

---

#### Sliding Window

Since we are finding the max length subarray with sum `totalSum - x`, and all elements are positive(integers), we could use Sliding Window.

```java
class Solution {
    public int minOperations(int[] nums, int x) {
        int n = nums.length;
        int total = 0;
        for (int num : nums) total += num;
        total -= x;
        if (total < 0) return -1;
        if (total == 0) return n;
        int min = Integer.MAX_VALUE;
        int sum = 0;
        for (int i = 0, j = 0; i < n; i++) {
            sum += nums[i];
            while (j < i && sum > total) {
                sum -= nums[j];
                j++;
            }
            if (sum == total) {
                int len = i - j + 1;
                min = Math.min(min, n - len);
            }
        }
        return min == Integer.MAX_VALUE ? -1 : min;
    }
}
```

T: O(n)		S: O(1)

