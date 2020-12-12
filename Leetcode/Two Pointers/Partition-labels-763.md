---
title: Medium | Partition Labels 673
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-09-01 20:56:24
---

A string `S` of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

[Leetcode](https://leetcode.com/problems/partition-labels/)

<!--more-->

**Example 1:**

```
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
```

**Note:**

- `S` will have length in range `[1, 500]`.
- `S` will consist of lowercase English letters (`'a'` to `'z'`) only.

**Follow up:** 

[Maximum Number of Non-Overlapping Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/)

---

#### Standard solution  

We keep two pointers to track the last occurrence of each char and update the `last` pointer.

```java
class Solution {
    public List<Integer> partitionLabels(String S) {
        int n = S.length();
        int[] max = new int[26];
        for (int i = 0; i < n; i++) {
            char c = S.charAt(i);
            max[c - 'a'] = i;
        }
        List<Integer> res = new ArrayList<>();
        int end = 0;
        int start = 0;
        for (int i = 0; i < n; i++) {
            end = Math.max(end, max[S.charAt(i) - 'a']);
            if (i == end) {
                res.add(end - start + 1);
                end = start = i + 1;
            }
        }
        return res;
    }
}
```

T: O(n)			S: O(1)

