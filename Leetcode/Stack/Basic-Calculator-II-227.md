---
title: Medium | Basic Calculator II 227
tags:
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-06-20 14:23:07
---

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only **non-negative** integers, `+`, `-`, `*`, `/` operators and empty spaces ``. The integer division should truncate toward zero.

[Leetcode](https://leetcode.com/problems/basic-calculator-ii/)

<!--more-->

**Example 1:**

```
Input: "3+2*2"
Output: 7
```

**Example 2:**

```
Input: " 3/2 "
Output: 1
```

**Example 3:**

```
Input: " 3+5 / 2 "
Output: 5
```

**Note:**  You may assume that the given expression is always valid.

**Follow up:** 

[Basic Calculator I](https://aranne.github.io/2020/06/20/Basic-calculator-224/#more)

[Basic Calculator III](https://aranne.github.io/2020/06/20/Basic-Calculator-III-772/#more)

---

#### Tricky 

View every part in stack a positive number and we will add them all.

Use `char sign` to store the previous sign `+`, `-`, `*`, `/` we meet. 

If `sign == *`, we should pop out previous num in stack and multiply with current num.

If `sign == -`, we should add a `-num` into stack.

Append a `+` to string s to process the remaining `num`

---

#### Stack

```java
class Solution {
    public int calculate(String s) {
        if (s == null || s.length() == 0) return 0;
        Stack<Integer> stack = new Stack<>();
        int num = 0;
        char sign = '+';         // to record previous sign
        for (int i = 0; i <= s.length(); i++) {
            // append '+' to process remaining num
            char c = (i != s.length()) ? s.charAt(i) : '+';      
            if (c == ' ') continue;
            if (Character.isDigit(c)) {
                num = num * 10 + c - '0';
            } else {
                if (sign == '+') {
                    stack.push(num);
                    num = 0;
                } else if (sign == '-') {
                    stack.push(-num);
                    num = 0;
                } else if (sign == '*') {
                    stack.push(stack.pop() * num);
                    num = 0;
                } else if (sign == '/') {
                    stack.push(stack.pop() / num);
                    num = 0;
                }
                sign = c;
            }
        }
        int res = 0;
        while (!stack.isEmpty()) {
            res += stack.pop();
        }
        return res;
    }
}
```

T: O(n)		S: O(n)

---

#### Optimized

We can solve it without using Stack.

We store two adding operands in `res` and `tmp`.  

If we meet `*` or `/`, we update `tmp`, and if we meet `+` or `-`, we add `tmp` to `res` and save `num` to `tmp`.

Finally we return `res + tmp`.

```java
class Solution {
    public int calculate(String s) {
        if (s == null || s.length() == 0) return 0;
        int res = 0;
        int tmp = 0;
        char sign = '+';
        int num = 0;
        for (int i = 0; i <= s.length(); i++) {
            char c = (i != s.length()) ? s.charAt(i) : '+';
            if (c == ' ') continue;
            if (Character.isDigit(c)) {
                num = num * 10 + c - '0';
            } else {
                if (sign == '*') {
                    tmp *= num;
                    num = 0;
                } else if (sign == '/') {
                    tmp /= num;
                    num = 0;
                } else if (sign == '+') {
                    res += tmp;       // save tmp
                    tmp = num;
                    num = 0;
                    
                } else if (sign == '-') {
                    res += tmp;
                    tmp = -num;
                    num = 0;
                }
                sign = c;
            }
        }
        return res + tmp;
    }
}
```

T: O(n)			S: O(1)



