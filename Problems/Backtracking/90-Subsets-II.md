---
title: Medium | Subsets II
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-05-16 19:48:23
---

Given a collection of integers that might contain duplicates, **nums**, return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

[Leetcode](https://leetcode.com/problems/subsets-ii/)

<!--more-->

**Example:**

```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

---

#### Tricky 

How to avoid duplicate subsets?

[1, 2, 2] when we search from the first 2, we will get two subsets [1, 2] and [1,  2].

The solution is firstly sort the array, then only allow the first duplicated char to go into recursion and pass the rest duplicates. 

`if (i > curr && nums[curr] == nums[curr - 1]) continue`

---

#### Standard solution  

```java
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        List<Integer> list = new ArrayList<>();
        Arrays.sort(nums);
        helper(0, nums, list, res);
        return res;
    }
    
    private void helper(int curr, int[] nums, List<Integer> list, List<List<Integer>> res) {
        res.add(new ArrayList<>(list));
        int n = nums.length;
        for (int i = curr; i < n; i++) {
            if (i != curr && nums[i] == nums[i - 1]) continue;
            list.add(nums[i]);
            helper(i + 1, nums, list, res);
            list.remove(list.size() - 1);
        }
    }
}
```

T: O(n^n)		S: O(n)

