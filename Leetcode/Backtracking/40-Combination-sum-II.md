---
title: Medium | Combination Sum II 40
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - Backtracking
date: 2020-01-31 14:32:28
---

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

Each number in `candidates` may only be used **once** in the combination.

[Leetcode](https://leetcode.com/problems/combination-sum-ii/)

<!--more-->

**Note:**

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

**Example 2:**

```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

[Combination Sum](https://aranne.github.io/2020/01/31/39-Combination-sum/#more)

---

#### Tricky 

Use backtracking to try all possiblities.

How to deal with the constraint that each item can be used only once.

There will be duplicate items in array, so we cannot just pass all duplicate items.

However, we can consider the first item in its all duplicates. After considering all the possibilities of first item, pass other duplicates.

E.g `candidates[1, 1, 2, 5, 6]`. We can perform dfs() on `candidates[0]`, then pass `candidates[1]` because there'll be duplicate result.

Or we can just use Set to avoid duplicate result.

#### Corner Case

We need check `remain` before `start`. Because it is possible that `remain == 0` and `start == candidates.length`

---

#### My thoughts 

Use backtracking to try all possibilities.

---

#### First solution 

```java
class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> res = new LinkedList<>();
        if (candidates == null || candidates.length == 0) return res;
        Arrays.sort(candidates);               // Sort for pruning
        find(candidates, 0, target, new LinkedList<Integer>(), res);
        return res;
    }
    private void find(int[] candi, int start, int remain, List<Integer> curr, List<List<Integer>> res) {
        if (remain == 0) {
            res.add(new LinkedList<Integer>(curr));
            return;
        }
        // Corner case: check start after checking remain. 
        if (start == candi.length) return;    
        if (candi[start] > remain) return;   // pruning
        for (int i = start; i < candi.length; i++) {
            if (i > start && candi[i - 1] == candi[i]) continue; // remove duplicates.
            curr.add(candi[i]);
            // try next item, i + 1
            find(candi, i + 1, remain - candi[i], curr, res); 
            curr.remove(curr.size() - 1);   // backtracking
        }
    }
}
```

T: O(N^target)		S: O(target). call stack

---

#### Summary 

In tricky.