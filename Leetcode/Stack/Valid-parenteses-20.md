---
title: Easy | Valid Parenthese 20
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - Stack
date: 2020-01-22 22:59:58
---

Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

[Leetcode](https://leetcode.com/problems/valid-parentheses/)

<!--more-->

**Example 1:**

```
Input: "()"
Output: true
```

**Example 2:**

```
Input: "()[]{}"
Output: true
```

**Example 3:**

```
Input: "(]"
Output: false
```

**Example 4:**

```
Input: "([)]"
Output: false
```

**Example 5:**

```
Input: "{[]}"
Output: true
```

---

#### Tricky 

Use a monotonic stack.

#### Corner Case

* Mind the stack may be empty if we meet the closing parentheses.

* In the end, the stack may not be empty.

---

#### First solution 

```java
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) return false;  // Mind stack may be empty.
                char pair = stack.pop();
                if (c == ')' && pair != '(') return false;
                if (c == ']' && pair != '[') return false;
                if (c == '}' && pair != '{') return false;
            }
        }
        return stack.isEmpty(); // Mind stack may not be empty.
    }
}
```

T: O(n)			S: O(n)

---

#### Optimized

We can put what we want into stack rather than what we have.

```java
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (char c : s.toCharArray()) {
            if (c == '(')
                stack.push(')');
            else if (c == '{')
                stack.push('}');
            else if (c == '[')
                stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c)
                return false;
        }
        return stack.isEmpty();
    }
}
```

T: O(N)			S: O(N)

---

#### Summary 

Use a monotonic stack.