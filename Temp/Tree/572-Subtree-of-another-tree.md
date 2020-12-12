---
title: Easy | Subtree of Another Tree 572
tags:
  - common
  - Oh-shit
categories:
  - Leetcode
  - Tree
date: 2019-12-08 11:07:41
---

Given two non-empty binary trees **s** and **t**, check whether tree **t** has exactly the same structure and node values with a subtree of **s**. A subtree of **s** is a tree consists of a node in **s** and all of this node's descendants. The tree **s** could also be considered as a subtree of itself.

[Leetcode](https://leetcode.com/problems/subtree-of-another-tree/)

<!--more-->

**Example 1:**
Given tree s:

```
     3
    / \
   4   5
  / \
 1   2
```

Given tree t:

```
   4 
  / \
 1   2
```

Return **true**, because t has the same structure and node values with a subtree of s.

**Example 2:**
Given tree s:

```
     3
    / \
   4   5
  / \
 1   2
    /
   0
```

Given tree t:

```
   4
  / \
 1   2
```

Return **false**.

**Follow up:** 

[same tree](https://leetcode.com/problems/same-tree/)

---

#### Oh-Shit

To check a subtree, we need to check a same-tree for each node. 

we cannot just check root is equal or not and then recurse.

```java
public boolean isSubtree(TreeNode s, TreeNode t) {
        if (s == null && t == null) {
            return true;
        } else if (s == null || t == null) {
            return false;
        } else if (s.val == t.val) {
            boolean rootLevel = isSubtree(s.left, t.left) 
                		&& isSubtree(s.right, t.right);
            boolean childLevel = isSubtree(s.left, t) || isSubtree(s.right, t);
            return rootLevel || childLevel;
        }
    }
```

The missing corner case of this code is:

 Given tree s:

```
     3
    / \
   4   5
  / \
 1   2
    /
   0
```

Given tree t:

```
   3
  / \
 1   2
```

Expected Return **false**.  (But we got true.)

---

#### My thoughts 

To check a subtree, we need to check a same-tree for each node. 

---

#### First solution 

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (s == null && t == null) {
            return true;
        } else if (s == null) {
            return false;
        } else if (t == null) {
            return false;
        } else {
            boolean rootLevel = isSameTree(s, t);
            boolean childLevel = isSubtree(s.left, t) || isSubtree(s.right, t);
            return rootLevel || childLevel;
        }
    }
    
    private boolean isSameTree(TreeNode s, TreeNode t) {
        if (s == null && t == null) {
            return true;
        } else if (s == null || t == null) {
            return false;
        } else return s.val == t.val && isSameTree(s.left, t.left) && isSameTree(s.right, t.right);
    }
}
```

T: O(n^2) S: O(n)

---

#### Optimized 

To check a subtree using same-tree, t won't change. So we can optimize if-else statement in subtree recursion.

```java
class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (s == null) {
            return false;
        }
        if (isSameTree(s, t)) {
            return true;
        }
        return isSubtree(s.left, t) || isSubtree(s.right, t);
    }
    
    private boolean isSameTree(TreeNode s, TreeNode t) {
        if (s == null && t == null) {
            return true;
        } else if (s == null || t == null) {
            return false;
        } else return s.val == t.val && isSameTree(s.left, t.left) && isSameTree(s.right, t.right);
    }
}
```

T: O(mn) S: O(n)

---

#### O(n): serilization and KMP string comparison

We could serilize tree into a string using pre-order traversal.

default string comparison `s1.contains(s2)` has O(mn) time, but if we use KMP algorithm, we could achieve O(n) time complexity.

```java
class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        String s1 = serilize(s).toString();
        String t1 = serilize(t).toString();
        return s1.contains(t1);  // O(mn) time complexity 
    }
    private StringBuilder serilize(TreeNode t) {
        StringBuilder sb = new StringBuilder();
        if (t == null) {
            sb.append("$");
        } else {
            // add delimiter to handle same values but not subtree cases
            sb.append("^" + t.val + "#" + serilize(t.left) + serilize(t.right));
        }
        return sb;
    }
}
```

T: O(mn) S: O(n)

---

#### Summary 

To check a subtree, we need to check a same-tree for each node. 