---
title: Medium | Palindrome Partition 131
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-05-27 17:37:47
---

Given a string *s*, partition *s* such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of *s*.

[Leetcode](https://leetcode.com/problems/palindrome-partitioning/)

<!--more-->

**Example:**

```
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
```

**Follow up:** [Palindrome Partition II](https://aranne.github.io/2020/05/27/132-Palindrome-partition-II/)

---

#### Tricky 

**This is not a DP problem, it is a backtracking problem!** 

All backtracking problems are composed by these three steps: `choose`, `explore`, `unchoose`.
So for each problem, you need to know:

1. `choose what?` For this problem, we choose each substring.
2. `how to explore?` For this problem, we do the same thing to the remained string.
3. `unchoose` Do the opposite operation of choose.

We try each substring to see whether it is a palindrome, if it is, then add it to `list` and continue explore.

---

#### My thoughts 

My first thought is recursion with memorization. 

However, concatenate two `List<List<String>>` palindrome lists together is too expensive.

So here is the **LTE** solution:

```java
class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        Set<List<String>> lists = partitionHelper(s);
        for (List<String> list : lists) {
            res.add(list);
        }
        return res;
    }
    
    private Set<List<String>> partitionHelper(String s) {
        Set<List<String>> res = new HashSet<>();
        List<String> list = new ArrayList<>();
        if (s.length() == 0) return res;
        if (s.length() == 1) {
            list.add(s);
            res.add(list);
            return res;
        }
        int n = s.length();
        for (int i = 1; i < n; i++) {
            Set<List<String>> leftList = partitionHelper(s.substring(0, i));
            Set<List<String>> rightList = partitionHelper(s.substring(i, n));
            for (List<String> left : leftList) {      // too expensive!!!!
                for (List<String> right : rightList) {
                    List<String> newList = new ArrayList<>(left);
                    newList.addAll(right);
                    res.add(newList);
                }
            }
        }
        if (isPalindrome(s)) {
            list.add(s);
            res.add(list);
        }
        return res;
    }
    
    private boolean isPalindrome(String s) {
        int n = s.length();
        int left = 0, right = n;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right - 1)) {
                return false;
            } else {
                left++;
                right--;
            }
        }
        return true;
    }
}
```

**LTE!!!**

---

#### Backtracking

We try each substring to see whether it is a palindrome, if it is, then add it to `list` and continue explore.

```java
class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        List<String> list = new ArrayList<>();
        if (s == null) return res;
        partitionHelper(s, list, res);
        return res;
    }
    
    private void partitionHelper(String s, List<String> list, List<List<String>> res) {
        if (s.length() == 0) {
            res.add(new ArrayList<>(list));
            return;
        }
        int n = s.length();
        for (int i = 1; i <= n; i++) {
            String tmp = s.substring(0, i);
            if (isPalindrome(tmp)) {
                list.add(tmp);
                partitionHelper(s.substring(i, n), list, res);
                list.remove(list.size() - 1);
            }
        }
    }
    
    private boolean isPalindrome(String s) {
        int n = s.length();
        int left = 0, right = n;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right - 1)) {
                return false;
            } else {
                left++;
                right--;
            }
        }
        return true;
    }
}
```

T: O(n^n)		S: O(n)

---

#### Optimized

We could avoid doing `s.substring()` by only record current exploring index of `s`.

```java
class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        List<String> list = new ArrayList<>();
        if (s == null) return res;
        partitionHelper(0, s, list, res);
        return res;
    }
    
    private void partitionHelper(int start, String s, List<String> list, List<List<String>> res) {
        int n = s.length();
        if (start >= n) {
            res.add(new ArrayList<>(list));
            return;
        }
        for (int i = start + 1; i <= n; i++) {
            if (isPalindrome(s, start, i)) {
                list.add(s.substring(start, i));
                partitionHelper(i, s, list, res);
                list.remove(list.size() - 1);
            }
        }
    }
    
    private boolean isPalindrome(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left) != s.charAt(right - 1)) {
                return false;
            } else {
                left++;
                right--;
            }
        }
        return true;
    }
}
```

T: O(n^n)		S: O(n)

