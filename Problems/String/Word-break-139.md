---
title: Medium | Word Break 139
tags:
  - tricky
categories:
  - Leetcode
  - String
date: 2019-12-17 00:29:13
---

Given a **non-empty** string *s* and a dictionary *wordDict*containing a list of **non-empty** words, determine if *s* can be segmented into a space-separated sequence of one or more dictionary words.

[Leetcode](https://leetcode.com/problems/word-break/)

<!--more-->

**Note:**

- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

**Example 1:**

```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2:**

```
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

**Example 3:**

```
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

**Follow up:** 

[Word Break II](https://leetcode.com/problems/word-break-ii/)

[Concatenated Words](https://leetcode.com/problems/concatenated-words/)

---

#### Tricky 

This is a common dp problem.

We consider suffix string `string[i:]` as subproblem. Number of subproblems are n.

For each subproblem `sub = string[i:]`

```python
sub = s[i:]
for j in range(i + 1 : len(s) + 1):
  if dp[j] && s[i:j] in dict:
    dp[i] = true
    break;
```

The time/subproblem is O(n). So total time complexity is O(n^2).

The topological order is from s[n:], s[n-1:], … , s[0:]

The original problem is s[0:]

---

#### First solution 

```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int n =  s.length();
        Set<String> set = new HashSet<>(wordDict);
        boolean[] dp = new boolean[n + 1];
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = i; j >= 1; j--) {
                if (dp[j - 1] && set.contains(s.substring(j - 1, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}
```

T: O(n^2) S: O(n)

---

#### Summary 

Using `prefix` and `suffix` with DP to solve string problems.