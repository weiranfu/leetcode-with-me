---
title: Hard | First missing positive 41
tags:
  - tricky
  - Oh-shit
categories:
  - Leetcode
  - Array
date: 2019-07-19 00:21:14
---

Given an unsorted integer array, find the smallest missing positive integer.

**Follow up:** Could you implement an algorithm that runs in `O(n)` time and uses constant extra space.?

<!--more-->

**Example 1:**

```
Input: [1,2,0]
Output: 3
```

**Example 2:**

```
Input: [3,4,-1,1]
Output: 2
```

**Example 3:**

```
Input: [7,8,9,11,12]
Output: 1
```

---

#### Brute Force

```java
class Solution {
    public int firstMissingPositive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        int i = 1;
        while (i != 0) {
            if (!set.contains(i)) return i;
            i++;
        }
        return -1;
    }
}
```

T: O(n) S: O(n)

---

#### Standard solution 

Put each number in its right place.

e.g. When we find 5, then swap it with A[4].

the first index where its number is not right, return `index + 1`.

```java
class Solution {
    public int firstMissingPositive(int[] nums) {
        if (nums == null || nums.length == 0) return 1;
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] >= 1 && nums[i] <= n) {
                if (nums[i] != nums[nums[i] - 1]) { // they're different
                    swap(i, nums[i] - 1, nums);
                    i--;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            if (nums[i] != i + 1) return i + 1;
        }
        return n + 1;
    }
    private void swap(int a, int b, int[] nums) {
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }
}
```

T: O(n) S: O(1)

