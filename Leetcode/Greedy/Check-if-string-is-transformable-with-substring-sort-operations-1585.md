---
title: Hard | Check If String Is Transformable With Substring Sort Operations 1585
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-09-27 21:03:53
---

Given two strings `s` and `t`, you want to transform string `s` into string `t` using the following operation any number of times:

- Choose a **non-empty** substring in `s` and sort it in-place so the characters are in **ascending order**.

For example, applying the operation on the underlined substring in `"14234"` results in `"12344"`.

Return `true` if *it is possible to transform string s into string t*. Otherwise, return `false`.

A **substring** is a contiguous sequence of characters within a string.

[Leetcode](https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/)

<!--more-->

**Example 1:**

```
Input: s = "84532", t = "34852"
Output: true
Explanation: You can transform s into t using the following sort operations:
"84532" (from index 2 to 3) -> "84352"
"84352" (from index 0 to 2) -> "34852"
```

**Example 2:**

```
Input: s = "34521", t = "23415"
Output: true
Explanation: You can transform s into t using the following sort operations:
"34521" -> "23451"
"23451" -> "23415"
```

**Example 3:**

```
Input: s = "12345", t = "12435"
Output: false
```

**Example 4:**

```
Input: s = "1", t = "2"
Output: false
```

**Constraints:**

- `s.length == t.length`
- `1 <= s.length <= 105`
- `s` and `t` only contain digits from `'0'` to `'9'`.

---

#### Brute Force

**We sort part of substring means we can move smaller digit to the left just like bubble sort.**

for each digit c in T, move the first c in S to the left.

If there're smaller digit at the left of c in S, return false.

![Screen Shot 2020-09-27 at 9 33 20 PM](https://user-images.githubusercontent.com/43511249/94382012-23176000-0109-11eb-96c0-9ad70578f93c.png)

The time complexity will be O(n^2)

---

#### Standard solution  

We don't need actually move.

Create 10 queues to store the indices of each digit.

For each digit c in T, we can check if there exisit any smaller digit to the left of it.

```java
class Solution {
    public boolean isTransformable(String s, String t) {
        Deque<Integer>[] indices = new Deque[10];
        for (int i = 0; i < 10; i++) indices[i] = new ArrayDeque<>();
        for (int i = 0; i < s.length(); i++) {
            int num = s.charAt(i) - '0';
            indices[num].addLast(i);
        }
        for (char c : t.toCharArray()) {
            int d = c - '0';
            if (indices[d].size() == 0) return false; // can't find the digit
            for (int i = 0; i < d; i++) {
                // if there exists a smaller digit before current digit
                if (indices[i].size() != 0 && indices[i].peekFirst() < indices[d].peekFirst()) return false;
            }
            indices[d].pollFirst();
        }
        return true;
    }
}
```

T: O(n)		S: O(n)

