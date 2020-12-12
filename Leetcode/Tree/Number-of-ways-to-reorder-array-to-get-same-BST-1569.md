---
title: Hard | Number of Ways to Reorder Array to Get Same BST 1569
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-09-07 16:09:53
---

Given an array `nums` that represents a permutation of integers from `1` to `n`. We are going to construct a binary search tree (BST) by inserting the elements of `nums` in order into an initially empty BST. Find the number of different ways to reorder `nums` so that the constructed BST is identical to that formed from the original array `nums`.

For example, given `nums = [2,1,3]`, we will have 2 as the root, 1 as a left child, and 3 as a right child. The array `[2,3,1]` also yields the same BST but `[3,2,1]` yields a different BST.

Return *the number of ways to reorder* `nums` *such that the BST formed is identical to the original BST formed from* `nums`.

Since the answer may be very large, **return it modulo** `10^9 + 7`.

[Leetcode](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/08/12/bb.png)

```
Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2020/08/12/ex1.png)**

```
Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
```

**Example 3:**

**![img](https://assets.leetcode.com/uploads/2020/08/12/ex4.png)**

```
Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.
```

**Example 4:**

**![img](https://assets.leetcode.com/uploads/2020/08/12/abc.png)**

```
Input: nums = [3,1,2,5,4,6]
Output: 19
```

**Example 5:**

```
Input: nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]
Output: 216212978
Explanation: The number of ways to reorder nums to get the same BST is 3216212999. Taking this number modulo 10^9 + 7 gives 216212978.
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= nums.length`
- All integers in `nums` are **distinct**.

---

#### Standard solution  

The key idea is that **once a root is fixed, we can only reorder the alsolute position but keep the relative position of nodes in either subtree.**

So the total count is `count(root) = count(left) * count(right) * Combination(left + right, left)`

We could pre-calculate the combination number using **Pasical Triangle**

```java
class Solution {
    long[][] comb;
    long mod = (long)1e9 + 7;
    
    public int numOfWays(int[] nums) {
        int n = nums.length;
        comb = new long[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= i; j++) {
                if (j == 0) comb[i][j] = 1;
                else comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % mod;
            }
        }
        List<Integer> list = new ArrayList<>();
        for (int a : nums) list.add(a);
        return (int)dfs(list) - 1;
    }
    private long dfs(List<Integer> list) {
        int n = list.size();
        if (n <= 1) return 1;
        int root = list.get(0);
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            if (list.get(i) < root) left.add(list.get(i));
            else right.add(list.get(i));
        }
        return dfs(left) * dfs(right) % mod * comb[n - 1][left.size()] % mod;
    }
}
```

T: O(n^2)			S: O(n^2)