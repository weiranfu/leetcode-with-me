---
title: Medium | Combination Sum III 216
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-06-11 18:16:07
---

Find all possible combinations of ***k*** numbers that add up to a number ***n***, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

**Note:**

- All numbers will be positive integers.
- The solution set must not contain duplicate combinations.

[Leetcode](https://leetcode.com/problems/combination-sum-iii/)

<!--more-->

**Example 1:**

```
Input: k = 3, n = 7
Output: [[1,2,4]]
```

**Example 2:**

```
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
```

---

#### Tricky 

Select int from 1 to 9 to avoid duplicate numbers.

---

#### Standard solution  

```java
class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<>();
        if (k == 0 || n == 0) return res;
        List<Integer> list = new ArrayList<>();
        combination(1, k, n, list, res);
        return res;
    }
    
    private void combination(int start, int k, int sum, List<Integer> list, List<List<Integer>> res) {
        if (k == 0 && sum == 0) {
            res.add(new ArrayList<>(list));
        } else if (k == 0 || sum <= 0) {
            return;
        }
        for (int i = start; i < 10; i++) {
            list.add(i);
            combination(i + 1, k - 1, sum - i, list, res);
            list.remove(list.size() - 1);
        }
    }
}
```

T: O(9^k)			S: O(k)

