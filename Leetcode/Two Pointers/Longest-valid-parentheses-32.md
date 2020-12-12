---
title: Hard | Longest Valid Parentheses 32
tags:
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-01-29 21:00:48
---

Given a string containing just the characters `'('` and `')'`, find the length of the longest valid (well-formed) parentheses substring.

[Leetcode](https://leetcode.com/problems/longest-valid-parentheses/)

<!--more-->

**Example 1:**

```
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
```

**Example 2:**

```
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
```

---

#### Tricky 

How to get the max length of adjacent valid parentheses is the key to this problem.

---

#### Stack.peek() to compute distance

We can store the index of `(` in the stack and compute the distance of parentheses using 

`i - stack.peek()`. 

For every `(` encountered, we push its index onto the stack.

For every `)` encountered, we pop the topmost element and subtract the current element's index from the top element of the stack, which gives the length of the currently encountered valid string of parentheses. If while popping the element, the stack becomes empty, we push the current element's index onto the stack. In this way, we keep on calculating the lengths of the valid substrings, and return the length of the longest valid string at the end.

As we can see, `((()))` we can compute distance in this situation.

`()()()` we can compute adjacent distance in this situation.

```java
class Solution {
    public int longestValidParentheses(String s) {
        int n = s.length();
        Stack<Integer> stack = new Stack<>();
        int max = 0;
        stack.push(-1);                // The head of valid parentheses
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.isEmpty()) {  // meeting ")"
                    stack.push(i);    // Insert another head of valid parentheses
                } else {
                    // stack.peek() get the head of valid parentheses.
                    max = Math.max(max, i - stack.peek());
                }
            }
        }
        return max;
    }
}
```

T: O(n)			S: O(n)

---

#### DP  

1. Subproblems: s[:i] prefix of string. s[:i] the longest valid parentheses at index i.

   num of subproblems is O(n)

2. Guess: s[:i] must ends with `)`. So `s[i] == )`. If `s[i] == (`, then `s[:i] == 0`. 

   * If `s[i - 1] == (`,  `s[:i]` is formed with a pair `()` with `s[:i - 2]`.  Just like `....()`

   * If `s[i - 1] == )`, then we need to consider about `s[:i-1]`.

     * If `i - s[:i-1] - 1 == (`, then `s[:i]` is valid.

       `s[:i]` is formed with a pair `()` with `s[:i-1]` and `s[:i-s[:i-1]-2]`  Just like `...((...))`

     * If `i - s[:i-1] - 1 == )`, then `s[:i] ` is invalid and `s[:i] == 0`.

3. Recurrence:

   * If `s[i] == ) && s[i-1] == (`, `dp[i] = 2 + dp[i - 2]`.
   * If `s[i] == ) && s[i-1] == )`,
     * If `s[i - dp[i-1] - 1] == (`, `dp[i] = 2 + dp[i-1] + dp[i - dp[i-1] - 2]`. 

   time/subproblem is O(1)

4. Runtime: O(n)

5. Topological order: from left to right.

```java
class Solution {
    public int longestValidParentheses(String s) {
        int n = s.length();
        if (n == 0) return 0;
        char[] cs = s.toCharArray();
        int[] dp = new int[n];
        dp[0] = 0;
        int max = 0;
        for (int i = 1; i < n; i++) {
            if (cs[i] == ')') {
                if (cs[i - 1] == '(') {
                    if (i - 1 == 0) {
                        dp[i] = 2;
                    } else {
                        dp[i] = 2 + dp[i - 2];
                    }
                } else { // cs[i - 1] == ')'
                    int openPos = i - dp[i - 1] - 1;
                    if (openPos >= 0 && s.charAt(openPos) == '(') {
                        if (openPos == 0) {
                            dp[i] = 2 + dp[i - 1];
                        } else {
                            dp[i] = 2 + dp[i - 1] + dp[openPos - 1];
                        }
                    }
                }
                max = Math.max(max, dp[i]);
            }
        }
        return max;
    }
}
```

T: O(N)			S: O(N)

---

#### Count number of parenthesis

In this approach, we make use of two counters `open` and `close`.

First, we start traversing the string from the left towards the right and for every `(` encountered, we increment the `open` counter and for every `)`  encountered, we increment the `close` counter. Whenever `open` becomes equal to `close`, we calculate the length of the current valid string and keep track of maximum length substring found so far. If `close` becomes greater than `open`  we reset `open` and `close` to 0.

Next, we start traversing the string from right to left and similar procedure is applied.

Why do we need to traverse twice? from left to right then from right to left.

Consider the situation: `()(()()`. If we traverse from left to right, we only get max length of 2 and left with `(()()` `open = 3, close = 2`. So we need to traverse from right to left to get the max length of 4.

```java
class Solution {
    public int longestValidParentheses(String s) {
        int n = s.length();
        int open = 0, close = 0;
        char[] cs = s.toCharArray();
        int res = 0;
        for (int i = 0; i < n; i++) {
            if (cs[i] == '(') {
                open++;
            } else {
                close++;
            }
            if (open == close) {
                res = Math.max(res, open * 2);
            } else if (open < close) {
                open = 0; close = 0;
            }
        }
        open = 0; close = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (cs[i] == '(') {
                open++;
            } else {
                close++;
            }
            if (open == close) {
                res = Math.max(res, open * 2);
            } else if (open > close) {
                open = 0; close = 0;
            }
        }
        return res;
    }
}
```

T: O(n)			S: O(1)
