---
title: Hard | Word Break II 140
tags:
  - tricky
categories:
  - Leetcode
  - String
date: 2019-12-17 16:18:20
---

Given a **non-empty** string *s* and a dictionary *wordDict* containing a list of **non-empty** words, add spaces in *s* to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

[Leetcode](https://leetcode.com/problems/word-break-ii/)

<!--more-->

**Note:**

- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

**Example 1:**

```
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
```

**Example 2:**

```
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
```

**Example 3:**

```
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
```

**Follow up:** 

[Concatenated Words](https://leetcode.com/problems/concatenated-words/)

---

#### Tricky 

This is a common DP problem. Subproblem is suffix `string[i:]`

There're two ways to solve it. 

* One is recursion with memorization.
* The other is bottom-top.

---

#### Bottom-top 

Bottom-top usually uses dp[i] to store state. This time we use a map<Integer, List> as a DP table. 

Bottom-top with a map to store Lists formed by suffix `string[i:]`.

```java
class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        return inList(s, dict);
    }
    private List<String> inList(String s, Set<String> dict) {
        Map<Integer, List<String>> map = new HashMap<>();
        map.put(s.length(), new ArrayList<>());
        map.get(s.length()).add("#"); // Make sure suffix s[len(s)] is true
        for (int i = s.length() - 1; i >= 0; i -= 1) {
            ArrayList<String> list = new ArrayList<>();
            for (int j = i + 1; j <= s.length(); j += 1) {
                if (!map.get(j).isEmpty() && dict.contains(s.substring(i, j))) {
                    if (j == s.length()) {
                        list.add(s.substring(i, j));
                    } else {
                        for (String tail : map.get(j)) {
                            list.add(s.substring(i, j) + " " + tail);
                        }
                    }
                }
            }
            map.put(i, list);
        }
        return map.get(0);
    }
}
```

T: O(n^3) S: O(n)

---

#### Recursion with memorization

Use a map to store computed Lists formed by suffix `string[i:]`

```java
class Solution {
    Map<String, List<String>> map = new HashMap<>();
    public List<String> wordBreak(String s, List<String> wordDict) {
        Set<String> dict = new HashSet<>(wordDict);
        return inList(s, dict);
    }
    private List<String> inList(String s, Set<String> dict) {
        if (map.containsKey(s)) return map.get(s);
        List<String> result = new ArrayList<>();
        for (int i = 1; i <= s.length(); i += 1) {
            String head = s.substring(0, i);
            if (dict.contains(head)) {
                String tail = s.substring(i);
                if (tail.equals("")) {
                    result.add(head);
                } else {
                    for (String t : inList(tail, dict)) {
                        result.add(head + " " + t);
                    }
                }
            }
        }
        map.put(s, result);
        return result;
    }
}
```

T: O(n^3) S: O(n)

---

#### Summary 

For DP problems,

* Bottom-up
* Recursion with memorization