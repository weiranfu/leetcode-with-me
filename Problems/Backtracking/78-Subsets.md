---
title: Medium | Subsets 78
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-05-16 19:39:26
---

Given a set of **distinct** integers, *nums*, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

[Leetcode](https://leetcode.com/problems/subsets/)

<!--more-->

**Example:**

```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

**[Follow up:](https://leetcode.com/problems/subsets-ii/)** 

---

#### Tricky 

**The numbers in subsets are in order, which means we don't consider the subsets with same numbers**. For example, we count `[1, 2]` but don't count `[2, 1]`

Intuition, we should search the candidates after the curr position.

---

#### Standard solution 

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        List<Integer> list = new ArrayList<>();
        subsetsHelper(0, nums, list, res);
        return res;
    }
    
    private void subsetsHelper(int curr, int[] nums, List<Integer> list, List<List<Integer>> res) {
        res.add(new ArrayList<>(list));
        int n = nums.length;
        for (int i = curr; i < n; i++) {
            list.add(nums[i]);
            subsetsHelper(i + 1, nums, list, res);
            list.remove(list.size() - 1);
        }
    }
}
```

T: O(n^n)		S: O(n)