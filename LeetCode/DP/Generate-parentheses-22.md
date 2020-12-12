---
title: Medium | Generate Parenthesis 22
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-01-24 23:03:36
---

Given *n* pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

[Leetcode](https://leetcode.com/problems/generate-parentheses/)

<!--more-->

For example, given *n* = 3, a solution set is:

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

---

#### Tricky 

How to generate parenthesis?

* [Catalan Number](https://www.cnblogs.com/Morning-Glory/p/11747744.html) problem. Given any prefix of s, the number of close parentheses is smaller than the number of opening parentheses. So we use `open` and `close` to record the number of parentheses in current prefix.
* DP: how to get n pairs parenthesis from n-1 parenthesis? `"(" + i pairs + ")" + (n - i - 1)pairs`

---

#### My thoughts 

Failed to solve.

---

#### First solution 

Control openning parenthesis.

```java
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        helper("", 0, 0, n, res);
        return res;
    }
    
    private void helper(String s, int open, int close, int n, List<String> res) {
        if (s.length() == n * 2) {
            res.add(s);
            return;
        }
        if (open < n) {                                 // append openning parenthese
            helper(s + "(", open + 1, close, n, res);    
        }
        if (close < open) {                             // append closing parenthese
            helper(s + ")", open, close + 1, n, res);
        }
    }
}
```

T: O(2^n) 			S: O(n)

---

#### DP

Use DP to memorize repeated computing.

When we want to get n pairs from n-1 pairs.

Guess: ["(" + x + ")" + y for x in `i` pairs, for y in `(n - i - 1)` pairs]

time/subproblem is O(n)

Total runtime: subproblems* time/subproblem = O(n^2)

Topological order: from 1 to n.

```java
class Solution {
    public List<String> generateParenthesis(int n) {
        Map<Integer, Set<String>> map = new HashMap<>();
        Set<String> init = new HashSet<>();
        init.add("");
        map.put(0, init);
        for (int i = 1; i <= n; ++i) {
            Set<String> set = new HashSet<>();
            for (int j = 0; j < i; ++j) {
                Set<String> set1 = map.get(j);
                Set<String> set2 = map.get(i - j - 1);
                for (String s1 : set1) {
                    for (String s2 : set2) {
                        set.add("(" + s1 + ")" + s2);
                    }
                }
            }
            map.put(i, set);
        }
        return new ArrayList<String>(map.get(n));
    }
}
```

T: O(n^2)			S: O(n)

---

#### Summary 

How to generate n parenthesis from n-1 parenthesis.

Try `["(" + x + ")" + y for x in i pairs and y in (n-i-1) pairs]`.