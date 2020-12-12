---
title: Medium | Path Sum III 437
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - Tree
date: 2020-01-12 09:59:58
---

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

[Leetcode](https://leetcode.com/problems/path-sum-iii/)

<!--more-->

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

**Example:**

```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```

---

#### Tricky 

PrefixSum is just like a `Two Sum` problem. `prefixSum(0, a) = prefixSum(0, b) + sum(b, a)`.

`sum(b, a) = targetSum`. 

However, this is a tree problem, different path should have different prefixSum map, which means we need delete sums of a path from prefixSum map after performing DFS on that path.

#### Corner Case

we need to check `prefixSum.containsKey(sum - target)`. DO NOT forget to take care of the situation that `sum == target`, which means `prefixSum.get(0) == 1`.

---

#### My thoughts 

Use prefixSum method, store sum into map. And check if `prefixSum.containsKey(sum - targetSum).`

However this method doesn't work, because prefixSum stores sum of different paths. Whenever we DFS a whole path, we need to delete all prefix sums of that path in prefixSum map.

---

#### First solution 

Failed to solve. I can't delete sums of a whole path in a map after DFS.

Because I use iteration method.

---

#### Standard solution 

Let's try recursion. In recursion, we can easily delete sums of path after DFS a whole path.

PrefixSum is just like a `Two Sum` problem. `prefixSum(0, a) = prefixSum(0, b) + sum(b, a)`.

`sum(b, a) = targetSum`. 

```java
class Solution {
    public int pathSum(TreeNode root, int targetSum) {
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);                               // For the case: sum == targetSum
        return findPath(root, targetSum, 0, map);
    }
    private int findPath(TreeNode n, int targetSum, int sum, Map<Integer, Integer> prefixSum) {
        if (n == null) return 0;
        sum += n.val;
        int count = 0;
        if (prefixSum.containsKey(sum - targetSum)) {
            count += prefixSum.get(sum - targetSum);
        }
        prefixSum.put(sum, prefixSum.getOrDefault(sum, 0) + 1);
        count += findPath(n.left, targetSum, sum, prefixSum);
        count += findPath(n.right, targetSum, sum, prefixSum);
        prefixSum.put(sum, prefixSum.get(sum) - 1); // Need to delete sums of this path.
        return count;
    }
}
```

T: O(n)				S: O(n)

---

#### Summary 

PrefixSum + Two Sum + DFS delete