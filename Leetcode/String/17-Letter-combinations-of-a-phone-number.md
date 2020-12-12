---
title: Medium | Letter Combinations of a Phone Number 17
tags:
  - common
  - implement
categories:
  - Leetcode
  - String
date: 2019-12-22 15:56:54
---

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent.

[Leetcode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

<!--more-->

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![img](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

**Example:**

```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

**Note:**

Although the above answer is in lexicographical order, your answer could be in any order you want.

---

#### Implement

When we use recursion, we need to consider about how to implement the initial case.

We should consider if there's not any tail strings at the last digit of digits.

```java
for (char c : map[first - '0'].toCharArray()) {
  if (!tails.isEmpty()) {
    for (String tail : tails) {
      res.add(c + tail);
    }
  } else {
    res.add(c + "");   // Initial case.
  }
}
```

---

#### My thoughts 

Using BFS to store each level's strings, with queue and size() to control levels.

```java
class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) return new ArrayList<String>();
        String[] map = new String[]{"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        Queue<String> queue = new LinkedList<>();
        queue.offer("");
        int k = 0;
        while (k < digits.length()) {
            int size = queue.size();
            char c = digits.charAt(k);
            for (int i = 0; i < size; i += 1) { // For each level.
                String prev = queue.poll();
                for (char ch : map[c - '0'].toCharArray()) {
                    queue.offer(prev + ch);
                }
            }
            k += 1;
        }
        return new ArrayList<String>(queue);
    }
}
```

T: O(n* 3^n),  because there're n digits, and tails are 3^n

S: O(2^n), because there are n digits, each digit is mapping 3 letters, so there're 3^n strings.

---

#### Recursion 

Mind the initial case.

```java
class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) return new ArrayList<String>();
        String[] map = new String[]{"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        List<String> res = new ArrayList<>();
        char first = digits.charAt(0);
        List<String> tails = letterCombinations(digits.substring(1));
        for (char c : map[first - '0'].toCharArray()) {
            if (!tails.isEmpty()) {
                for (String tail : tails) {
                    res.add(c + tail);
                }
            } else {
                res.add(c + "");   // Initial case.
            }
        }
        return res;
    }
}
```

T: O(n* 3^n)

S: O(3^n)

---

#### Summary 

* Save the mapping relationship in a String[].

* Store the temp strings in queue during BFS.

