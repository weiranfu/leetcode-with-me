---
title: Medium | Split a String into the Max Number of Unique Substrings 1593
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-09-28 00:47:32
---

Given a string `s`, return *the maximum number of unique substrings that the given string can be split into*.

You can split string `s` into any list of **non-empty substrings**, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are **unique**.

A **substring** is a contiguous sequence of characters within a string.

[Leetcode](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/)

<!--more-->

**Example 1:**

```
Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
```

**Example 2:**

```
Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
```

**Example 3:**

```
Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
```

**Constraints:**

- `1 <= s.length <= 16`
- `s` contains only lower case English letters.

---

#### DFS 

Perform DFS to try all combinations of substrings.

Maintain a set to record substrings that have been seen.

```java
class Solution {
    String s;
    int n;
    int res;
    
    public int maxUniqueSplit(String s) {
        this.s = s;
        n = s.length();
        res = 1;
        Set<String> set = new HashSet<>();
        dfs(0, set);
        return res;
    }
    private void dfs(int index, Set<String> set) {
        if (index == n) {
            res = Math.max(res, set.size());
            return;
        }
        for (int i = index; i < n; i++) {
            String tmp = s.substring(index, i + 1);
            if (set.contains(tmp)) continue;
            set.add(tmp);
            dfs(i + 1, set);
            set.remove(tmp);
        }
    }
}
```

T: O(2^n)				S: O(2^n)

---

#### Brute force

Try all combinations of substrings.

We could use bitmask of n to represents the substrings.

**`0` means we don't split, `1` means split here.**

There're `2^(n-1)` choices totally, the last bit must be `1`.

**The bitcount of bitmask represents the number of substrings**

`ababccc` => `1101101`

`a`, `b`, `ab`, `c`, `cc`

```java
class Solution {
    public int maxUniqueSplit(String s) {
        int n = s.length();
        int res = 1;
        Set<String> set = new HashSet<>();
        // 2^(n-1) states
        for (int m = 0; m < 1 << (n - 1); m++) {
            // (n-1) length + last bit 1
            if (Integer.bitCount(m) + 1 <= res) continue;  // prunning!!! 
            boolean valid = true;
            int p = 0;
      // view the (n-1) length state from right to left as index of string from 0 to n-1
            for (int i = 0; i < n && valid; i++) { 
                if (i == n - 1 || (m >> i & 1) == 1) {
                    String ss = s.substring(p, i + 1);
                    valid &= set.add(ss);
                    p = i + 1;
                }
            }
            if (valid) res = Math.max(res, set.size());
            set.clear();
        }
        return res;
    }
}
```

T: O(n\*2^(n-1))			S: O(n)

