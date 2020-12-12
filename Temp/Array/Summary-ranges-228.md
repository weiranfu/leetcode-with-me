---
title: Medium | Summary Ranges 228
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-06-22 16:02:16
---

Given a sorted integer array without duplicates, return the summary of its ranges.

[Leetcode](https://leetcode.com/problems/summary-ranges/)

<!--more-->

**Example 1:**

```
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
```

**Example 2:**

```
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
```

**Follow up:** [Missing Ranges](https://leetcode.com/problems/missing-ranges/)

---

#### Tricky 

We need to search contiguous discretized points in an array.

* One is to use map to record the ranges of each point.
* Another is using two pointers to find range boundary of contiguous points.

---

#### My thoughts 

For a consicutive range `[a, b]`, `len = b - a + 1`.

We will save the length in both `start` and `end` point.

`map.put(a, len)` `map.put(b, len)`

```java
class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (!map.containsKey(num)) {
                int left = (num != Integer.MIN_VALUE && map.containsKey(num - 1)) ? map.get(num - 1) : 0;
                int right = (num != Integer.MAX_VALUE && map.containsKey(num + 1)) ? map.get(num + 1) : 0;
                int sum = left + 1 + right;   // extend range
                map.put(num, sum);
                if (left != 0) {
                    map.put(num - 1, sum);
                    map.put(num - left, sum);
                }
                if (right != 0) {
                    map.put(num + 1, sum);
                    map.put(num + right, sum);
                }
            }
        }
        int end = Integer.MAX_VALUE;
        for (int num : nums) {
            if (end != Integer.MAX_VALUE && num <= end) continue;
            end = num + (map.get(num) - 1);
            if (end < num) break;           // avoid overflow
            if (num == end) {
                res.add("" + num);
            } else {
                res.add(num + "->" + end);
            }
        }
        return res;
    }
}
```

T: O(n)			S: O(n)

---

#### Search 

We search from left to right to find possible contiguous ranges.

```java
class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<>();
        int n = nums.length;
        int i = 0;
        while (i < n) {
            int j = i;
            while (j + 1 < n && nums[j + 1] == nums[j] + 1) {
                j++;
            }
            if (j == i) {
                res.add("" + nums[i]);
            } else {
                res.add(nums[i] + "->" + nums[j]);
            }
            i = j + 1;
        }
        return res;
    }
}
```

T: O(n)			S: O(1)



