---
title: Easy | Two Sum 1
tags:
  - common
categories:
  - Leetcode
  - Array
date: 2019-10-26 22:50:37
---

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

[Leetcode](https://leetcode.com/problems/two-sum/)

<!--more-->

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

---

#### My thoughts 

We need to find a pair in an array. We can use map to store the a member in the pair in order to just iterate once.

---

#### Two pointers

We need sort array and record its original indices. 

Then we use Two pointers to scan nums from two ends.

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        if (nums == null || nums.length <= 1) return new int[0];
        int n = nums.length;
        int[][] newNums = new int[n][2];
        for (int i = 0; i < n; i++) {
            newNums[i][0] = nums[i];
            newNums[i][1] = i;
        }
        Arrays.sort(newNums, (a, b) -> a[0] - b[0]);
        int l = 0, r = n - 1;
        while (l < r) {
            int sum = newNums[l][0] + newNums[r][0];
            if (sum == target) {
                return new int[]{newNums[l][1], newNums[r][1]};
            } else if (sum > target) {
                r--;
            } else {
                l++;
            }
        }
        return new int[0];
    }
}
```

T: O(nlogn)			S: O(n)

---

#### Map

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i += 1) {
            if (map.containsKey(target - nums[i])) {
                result[0] = map.get(target - nums[i]);
                result[1] = i;
                return result;
            }
            map.put(nums[i], i);
        }
        return result;
    }
}
```

T: O(N)			S: O(N)

---

#### Summary 

Use map to store the a member in the pair in order to just iterate once.