---
title: Easy | Special Array with X Elements Greater Than or Equal X
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Sort
date: 2020-11-01 00:59:53
---

You are given an array `nums` of non-negative integers. `nums` is considered **special** if there exists a number `x` such that there are **exactly** `x` numbers in `nums` that are **greater than or equal to** `x`.

Notice that `x` **does not** have to be an element in `nums`.

Return `x` *if the array is **special**, otherwise, return* `-1`. It can be proven that if `nums` is special, the value for `x` is **unique**.

[Leetcode](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/)

<!--more-->

**Example 1:**

```
Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
```

**Example 2:**

```
Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.
```

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

---

#### Count Sort 

We can use counting sort to get the number of items which are greater or equal to `x`.

```java
class Solution {
    public int specialArray(int[] nums) {
        int n = nums.length;
        int[] count = new int[1001];
        for (int num : nums) {
            count[num]++;
        }
        int cnt = 0;
        for (int i = 1000; i >= 0; i--) {
            cnt += count[i];
            if (cnt == i) return i;
        }
        return -1;
    }
}
```

T: O(n)		S: O(n)

