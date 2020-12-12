---
title: Medium | Score of Parentheses 856
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-07-27 22:09:21
---

Given a balanced parentheses string `S`, compute the score of the string based on the following rule:

- `()` has score 1
- `AB` has score `A + B`, where A and B are balanced parentheses strings.
- `(A)` has score `2 * A`, where A is a balanced parentheses string.

[Leetcode](https://leetcode.com/problems/score-of-parentheses/)

<!--more-->

**Example 1:**

```
Input: "()"
Output: 1
```

**Example 2:**

```
Input: "(())"
Output: 2
```

**Example 3:**

```
Input: "()()"
Output: 2
```

**Example 4:**

```
Input: "(()(()))"
Output: 6
```

---

#### Stack

This is just like the [Calculator III](https://aranne.github.io/2020/06/20/Basic-Calculator-III-772/)

We could use `curr` to store the value of current level.

When we meet `(`, we push `curr` into stack.

When we meet `)`, we double `curr` result and add `stock.pop()`.

```java
class Solution {
    public int scoreOfParentheses(String S) {
        Stack<Integer> stack = new Stack<>();
        int curr = 0;
        for (char c : S.toCharArray()) {
            if (c == '(') {
                stack.push(curr);
                curr = 0;
            } else {
                if (curr == 0) {
                    curr = 1;
                } else {
                    curr *= 2;
                }
                curr += stack.pop();
            }
        }
        return curr;
    }
}
```

T: O(n)			S: O(n)

---

#### Optimized -> Space: O(1)

It gives a different approach to calculate the formula.
For example : (()()()) = (()) + (()) + (())

We count the number of layers.
If we meet `'('` layers number `l++`
else we meet `')'` layers number `l--`

If we meet `"()"`, we know the number of layer outside,
so we can calculate the score `res += 1 << l`.

```java
class Solution {
    public int scoreOfParentheses(String S) {
        int res = 0;
        int level = 0;
        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == '(') level++;
            else level--;
            if (S.charAt(i) == ')' && S.charAt(i - 1) == '(') {
                res += 1 << level;
            }
        }
        return res;
    }
}
```

T: O(n)			S: O(1)

