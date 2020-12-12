---
title: Medium | Combinations 77
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-05-16 19:18:30
---

Given two integers *n* and *k*, return all possible combinations of *k* numbers out of 1 ... *n*.

[Leetcode](https://leetcode.com/problems/combinations/)

<!--more-->

**Example:**

```
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

---

#### Tricky 

We only count combinations with same numbers once. For example, we count `[1,4]`, but not `[4, 1]`.

**Intuition: the numbers in combinations are in order!**

So we record the current position during backtracking, and search number greater than it!

---

#### First solution 

```java
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        if (n == 0 || k == 0) return res;
        List<Integer> combination = new ArrayList<>();
        combineHelper(1, k, n, combination, res);
        return res;
    }
    
    private void combineHelper(int curr, int remain, int n, List<Integer> combination, List<List<Integer>> res) {
        if (remain == 0) {
            res.add(new ArrayList<>(combination));
            return;
        }
        for (int i = curr; i < n + 1; i++) {
            combination.add(i);
            combineHelper(i + 1, remain - 1, n, combination, res);//choose next from i+1
            combination.remove(combination.size() - 1);
        }
    }
}
```

T: O(n^k)			S: O(k)

---

#### Optimized: pruning

Actually, when we search remaining numbers from `curr` to `n + 1`, we could stop at `n + 1 - (remain - 1)`. Cause if we choose the next number after `n + 1 - (remain - 1)`, there won't be enough numbers left.

```java
class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        if (n == 0 || k == 0) return res;
        List<Integer> combination = new ArrayList<>();
        combineHelper(1, k, n, combination, res);
        return res;
    }
    
    private void combineHelper(int curr, int remain, int n, List<Integer> combination, List<List<Integer>> res) {
        if (remain == 0) {
            res.add(new ArrayList<>(combination));
            return;
        }
        for (int i = curr; i < n + 1 - (remain - 1); i++) { // pruning!!!
            combination.add(i);
            combineHelper(i + 1, remain - 1, n, combination, res);
            combination.remove(combination.size() - 1);
        }
    }
}
```

T: O(n^k)			S: O(k)