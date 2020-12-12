---
title: Medium | Unique Binary Search Tree
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-05-20 15:35:41
---

Given *n*, how many structurally unique **BST's** (binary search trees) that store values 1 ... *n*?

[Leetcode](https://leetcode.com/problems/unique-binary-search-trees/)

<!--more-->

**Example:**

```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

**Follow up:** [Unique Binary Search Tree II](https://leetcode.com/problems/unique-binary-search-trees-ii/)

---

#### Tricky 

This is a **[Catalan Number](https://www.cnblogs.com/Morning-Glory/p/11747744.html)** problem! 

**How to construct a binary search tree given n? We try to find the sum of number of unique trees when we use each integer in [1, n] as a root node.**

For example, when we choose `k` as root node, integers in `[1, k)` are smaller than `k` and will be put into left part of root. Integers in `(k, n]` are greater than `k` and will be put into right part of root.

number of trees will be `numTrees(k - 1) * numTrees(n - k)`.

So this is a typical DP problem.

\# of subproblems: O(n)

time/ subproblem = O(n)     (Because we will try all possible root in `[1, n]`)

---

#### Standard solution  

```java
class Solution {
    public int numTrees(int n) {
        if (n == 0) return 0;
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i < n + 1; i++) {
            int total = 0;
            for (int root = 1; root <= i; root++) {     // try all possible root
                total += dp[root - 1] * dp[i - root];
            }
            dp[i] = total;
        }
        return dp[n];
    }
} 
```

T: O(n^2)			S: O(n)

