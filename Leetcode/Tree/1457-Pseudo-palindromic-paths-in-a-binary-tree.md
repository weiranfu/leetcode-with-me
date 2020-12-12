---
title: Medium | Pseudo-Palindromic Paths in a Binary Tree 1457
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2020-05-26 15:16:54
---

Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be **pseudo-palindromic** if at least one permutation of the node values in the path is a palindrome.

*Return the number of **pseudo-palindromic** paths going from the root node to leaf nodes.*

[Leetcode](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/)

<!--more-->

**Example :**

![img](https://assets.leetcode.com/uploads/2020/05/06/palindromic_paths_1.png)

```
Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
```

**Follow up:** 

---

#### Tricky 

Since there're only 9 digits in a node, so we could use bit map to store them!

---

#### My thoughts 

Use `int[] map` to store the 9 digits occurrence and recursively backtracking `map`.

---

#### First solution 

```java
class Solution {
    public int pseudoPalindromicPaths (TreeNode root) {
        if (root == null) return 0;
        int[] map = new int[10];
        int[] res = new int[1];
        helper(root, map, res);
        return res[0];
    }
    
    private void helper(TreeNode node, int[] map, int[] res) {
        map[node.val] ^= 1;
        if (node.left == null && node.right == null) {
            if (isPalindrome(map)) {
                res[0]++;
            }
            map[node.val] ^= 1;                      // backtracking
            return;
        }
        if (node.left != null) helper(node.left, map, res);
        if (node.right != null) helper(node.right, map, res);
        map[node.val] ^= 1;                         // backtracking
    }
    
    private boolean isPalindrome(int[] map) {
        int cnt = 0;
        for (int i = 1; i < 10; i++) {
            cnt += map[i];
        }
        return cnt <= 1;
    }
}
```

T: O(n)			S: O(n)

---

#### Optimized

Use bit map to store 9 digits so that we don't need to backtrack `map`.

`count ^= 1 << (root.val - 1)` -> Flips the `root.val-1`th bit, which here is used to flip between denoting even and odd occurrence.

Although it's possible that all bits will be flipped, `root.val-1`th bit will be opposite to other bits.

`count & (count - 1)` -> Used to check that only a single bit is set - checkout [LC 231](https://leetcode.com/problems/power-of-two/) for details.
This is used here to make sure that there is only 1 odd occurence.

```java
class Solution {
    public int pseudoPalindromicPaths (TreeNode root) {
        if (root == null) return 0;
        int[] res = new int[1];
        helper(root, 0, res);
        return res[0];
    }
    
    private void helper(TreeNode node, int count, int[] res) {
        count ^= 1 << (node.val - 1);                   // flip bit
        if (node.left == null && node.right == null) {
            if ((count & (count - 1)) == 0) {           // check only one bit is flipped
                res[0]++;
            }
            return;
        }
        if (node.left != null) helper(node.left, count, res);
        if (node.right != null) helper(node.right, count, res);
    }
}
```

T: O(n)		S: O(n)



