---
title: Medium | Permutations 46
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-02-05 16:38:51
---

Given a collection of **distinct** integers, return all possible permutations.

[Leetcode](https://leetcode.com/problems/permutations/)

<!--more-->

**Example:**

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

**Follow up**

[Combination Sum](https://leetcode.com/problems/combination-sum/)

---

#### Tricky 

Backtracking.

Use a `visited` array to indicated whether we have used this num for this permutation. 

---

#### My thoughts 

Backtracking.

---

#### First solution 

```java
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        int n = nums.length;
        List<List<Integer>> res = new LinkedList<>();
        if (n == 0) return res;
        boolean[] visited = new boolean[n];
        find(nums, visited, new LinkedList<Integer>(), res);
        return res;
    }
    private void find(int[] nums, boolean[] visited, List<Integer> curr, List<List<Integer>> res) {
        int n = nums.length;
        if (curr.size() == n) {
            res.add(new LinkedList<Integer>(curr));
            return;
        }
        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            curr.add(nums[i]);
            find(nums, visited, curr, res);
            visited[i] = false;
            curr.remove(curr.size() - 1);
        }
    }
}
```

T: O(len^N) len is the recursive call length

S: O(len) call back

