---
title: Medium | Combination Sum 39
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-01-31 13:32:27
---

Given a **set** of candidate numbers (`candidates`) **(without duplicates)** and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

The **same** repeated number may be chosen from `candidates` unlimited number of times.

[Leetcode](https://leetcode.com/problems/combination-sum/)

<!--more-->

**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

**Example 2:**

```
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

---

#### Tricky 

We can search all the possibilities of usage of items in array.

Perform backtracking to do this.

Maintain a temp LinkedList to store possible combination.

A try: put an item into it and search next possible item.

Backtrack: remove the item lastly added, then try next item.

How to achieve that items can be added duplicately?

We use a point `start` to indicate which item we are considering, DFS starts at that point, which means we can use that item again.

---

#### My thoughts 

Failed to solve.

---

#### First Solution

```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        int n = candidates.length;
        List<List<Integer>> res = new LinkedList<>();
        if (n == 0) return res;
        find(candidates, target, 0, new LinkedList<Integer>(), res);
        return res;
    }
    private void find(int[] candi, int remain, int start, List<Integer> curr, List<List<Integer>> res) {
        if (remain < 0) return;           // cannot form valid combination
        if (remain == 0) {
            res.add(new LinkedList<>(curr));
            return;
        }
        for (int i = start; i < candi.length; i++) {// try all possible items
            curr.add(candi[i]);
            find(candi, remain - candi[i], i, curr, res);//starts at i (duplicate items)
            curr.remove(curr.size() - 1);          // Backtrack
        }
    }
}
```

Time complexity:

It is a N-tree structure. Because we have recursion in for loop. 

Suppose we search all candidates and the max recursion deep is `target`, then the time complexity is O(N^target).

Space complexity: O(target). call stack.

---

#### Optimized (Pruning)

Actually, we can pruning our tree (recursion).

We can sort `candidates` array. And If we meet an item greater than remain value, which means `remain - candi[i] < 0`, then we don't need to consider remaining candidates. Because candidates after it will all greater than it and they all cannot form a valid combination.

```java
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        int n = candidates.length;
        List<List<Integer>> res = new LinkedList<>();
        if (n == 0) return res;
        Arrays.sort(candidates);                      // Sort for pruning
        find(candidates, target, 0, new LinkedList<Integer>(), res);
        return res;
    }
    private void find(int[] candi, int remain, int start, List<Integer> curr, List<List<Integer>> res) {
        if (remain == 0) {
            res.add(new LinkedList<>(curr));
            return;
        }
        if (candi[start] > remain) return;                // Pruning
        for (int i = start; i < candi.length; i++) {
            curr.add(candi[i]);
            find(candi, remain - candi[i], i, curr, res);
            curr.remove(curr.size() - 1);
        }
    }
}
```

T: O(N^target) 			S: O(target)

---

#### Summary 

Use backtracking to try all possible combinations.

Use pruning to optimized recursion.