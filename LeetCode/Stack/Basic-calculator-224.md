---
title: Hard | Basic Calculator 224
tags:
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-06-20 04:12:38
---

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open `(` and closing parentheses `)`, the plus `+` or minus sign `-`, **non-negative** integers and empty spaces `  `.

[Leetcode](https://leetcode.com/problems/basic-calculator/)

<!--more-->

**Example 1:**

```
Input: "1 + 1"
Output: 2
```

**Example 2:**

```
Input: " 2-1 + 2 "
Output: 3
```

**Example 3:**

```
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

Note: You may assume that the given expression is always valid.

**Follow up:** 

[Basic Calculator II](https://aranne.github.io/2020/06/20/Basic-Calculator-II-227/#more)

[Basic Calculator III](https://aranne.github.io/2020/06/20/Basic-Calculator-III-772/#more)

---

#### Tricky 

We store `sign` and `res` into stack when we meet `(`, for example `2 - (4 + 3)`, we will store `2`, `-` into stack.

1. digit: it should be one digit from the current number
2. '+': number is over, we can add the previous number and start a new number
3. '-': same as above
4. '(': push the previous result and the sign into the stack, set result to 0, just calculate the new result within the parenthesis.
5. ')': pop out the top two numbers from stack, first one is the sign before this pair of parenthesis, second is the temporary result before this pair of parenthesis. We add them together.

Finally if there is only one number, from the above solution, we haven't add the number to the result, so we do a check see if the number is zero.

---

#### Standard solution  

```java
class Solution {
    public int calculate(String s) {
        if (s == null || s.length() == 0) return 0;
        Stack<Integer> stack = new Stack<>();
        int res = 0;
        int sign = 1;
        int num = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            } else if (c == '+') {
                res += sign * num;
                num = 0;
                sign = 1;
            } else if (c == '-') {
                res += sign * num;
                num = 0;
                sign = -1;
            } else if (c == '(') {
                res += sign * num;
                num = 0;
                stack.push(res);  //we push the result first, then sign;
                stack.push(sign);
                res = 0;          //reset the sign and result
                sign = 1;
            } else if (c == ')') {
                res += sign * num;
                num = 0;
                sign = stack.pop(); // get sign
                res *= sign;
                res += stack.pop(); // get prev res
            }
        }
        res += sign * num;           // add remaining num
        return res;
    }
}
```

T: O(n)		S: O(n)

