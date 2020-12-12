---
title: Medium | Permutations II 47
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-05-09 22:34:59
---

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

[Leetcode](https://leetcode.com/problems/permutations-ii/)

<!--more-->

**Example:**

```
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

---

#### Tricky 

Use an extra boolean array `boolean[] visited` to indicate whether the value is added to list.

Sort the array `int[] nums` to make sure we can skip the same value.

when a number has the same value with its previous, we can use this number only if his previous is used

---

#### My thoughts 

Fail to solve

---

#### Standard solution  

```java
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;
        if (n == 0) return res;
        Arrays.sort(nums);            // sort for avoiding duplicate sets
        find(0, new boolean[n], new ArrayList<>(), res, nums);
        return res;
    }
    
    private void find(int start, boolean[] visited, List<Integer> curr, List<List<Integer>> res, int[] nums) {
        if (start == nums.length) {
            res.add(new ArrayList<>(curr));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) continue;
            if (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1]) continue; // avoid duplicate sets
            curr.add(nums[i]);
            visited[i] = true;
            find(start + 1, visited, curr, res, nums);
            curr.remove(curr.size() - 1);
            visited[i] = false;
        }
    }
}
```

