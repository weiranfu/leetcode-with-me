---
title: Hard | Basic Calculator III 772
tags:
  - tricky
categories:
  - Leetcode
  - Design
date: 2020-06-20 15:46:49
---

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open `(` and closing parentheses `)`, the plus `+` or minus sign `-`, **non-negative** integers and empty spaces ``.

The expression string contains only non-negative integers, `+`, `-`, `*`, `/` operators , open `(` and closing parentheses `)` and empty spaces ``. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2147483648, 2147483647]`.

[Leetcode](https://leetcode.com/problems/basic-calculator-iii/)

<!--more-->

Some examples:

```
"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
```

**Follow up:**

[Basic Calculator I](https://aranne.github.io/2020/06/20/Basic-calculator-224/#more)

[Basic Calculator II](https://aranne.github.io/2020/06/20/Basic-Calculator-II-227/#more)

---

#### Tricky 

1. This is a combination of [Basic Calculator I](https://aranne.github.io/2020/06/20/Basic-calculator-224/#more) and [Basic Calculator II](https://aranne.github.io/2020/06/20/Basic-Calculator-II-227/#more).

   To process an expression without parentheses, we use `res`, `tmp` and `sign` in Basic Calculator II.

   In order to process parentheses, we can save states of `res`, `tmp` and `sign` into stack.

   When we meet `(`, we save states into stack. When we meet `)`, we extract them from stack and assign current `res + tmp` to `num`.

2. Optimized to two precedence levels. `l1, o1, l2, o2`

3. Recursive call to process parentheses

4. Convert Infix expression to Postfix one, and evaluate postfix expression.

---

#### Stack + Two variables

```java
class Solution {
    public int calculate(String s) {
        if (s == null || s.length() == 0) return 0;
        Stack<Integer> stack = new Stack<>();
        int res = 0;
        int tmp = 0;
        int num = 0;
        int sign = 1;  // 1: '+', 2: '-', 3: '*', 4: '/'
        for (int i = 0; i <= s.length(); i++) {
            char c = (i != s.length()) ? s.charAt(i) : '+';
            if (c == ' ') continue;
            if (Character.isDigit(c)) {
                num = num * 10 + c - '0';
            } else if (c == '(') {
                stack.push(res);            // save states
                stack.push(tmp);
                stack.push(sign);
                res = 0;
                tmp = 0;
                sign = 1;
            } else {                        // process res & tmp
                if (sign == 1) {
                    res += tmp;
                    tmp = num;
                    num = 0;
                } else if (sign == 2) {
                    res += tmp;
                    tmp = -num;
                    num = 0;
                } else if (sign == 3) {
                    tmp *= num;
                    num = 0;
                } else {
                    tmp /= num;
                    num = 0;
                }
                
                if (c == ')') {
                    sign = stack.pop();
                    num = res + tmp;       // assign res + tmp to num
                    tmp = stack.pop();
                    res = stack.pop();
                } else if (c == '+') {
                    sign = 1;
                } else if (c == '-') {
                    sign = 2;
                } else if (c == '*') {
                    sign = 3;
                } else if (c == '/') {
                    sign = 4;
                }
            } 
        }
        return res + tmp;
    }
}
```

T: O(n)			S: O(n)

---

#### Optimized

**Separation rule**:

- We separate the calculations into two different levels corresponding to the two precedence levels.
- For each level of calculation, we maintain two pieces of information: the *partial result* and the *operator in effect*.
- For level one, the partial result starts from `0` and the initial operator in effect is `+`; for level two, the partial result starts from `1` and the initial operator in effect is `*`.
- We will use `l1` and `o1` to denote respectively the partial result and the operator in effect for level one; `l2` and `o2` for level two. The operators have the following mapping:
  `o1 == 1` means `+`; `o1 == -1` means `-` ;
  `o2 == 1` means `*`; `o2 == -1` means `/`.
  By default we have `l1 = 0`, `o1 = 1`, and `l2 = 1`, `o2 = 1`.

**Precedence rule**:

- Each operand in the expression will be associated with a precedence of level two by default, meaning they can only take part in calculations of precedence level two, not level one.
- The operand can be any of the aforementioned types (number, variable or subexpression), and will be evaluated together with `l2` under the action prescribed by `o2`.

**Demotion rule**:

- The partial result `l2` of precedence level two can be demoted to level one. Upon demotion, `l2` becomes the operand for precedence level one and will be evaluated together with `l1` under the action prescribed by `o1`.
- The demotion happens when either a level one operator (i.e., `+` or `-`) is hit or the end of the expression is reached. After demotion, `l2` and `o2` will be reset for following calculations.

```java
class Solution {
    public int calculate(String s) {
        if (s == null || s.length() == 0) return 0;
        Stack<Integer> stack = new Stack<>();
        int l1 = 0, o1 = 1;  // o1 => 1 : '+'; -1 : '-'
        int l2 = 1, o2 = 1;  // o2 => 1 : '*'; -1 : '/'
        int num = 0;
        for (int i = 0; i <= s.length(); i++) {
            char c = (i != s.length()) ? s.charAt(i) : '*';  // add last '*'
            if (c == ' ') continue;
            if (Character.isDigit(c)) {
                num = num * 10 + c - '0';
            } else if (c == '(') {
                stack.push(l1);                             // save states
                stack.push(o1);       
                stack.push(l2);
                stack.push(o2);
                l1 = 0; o1 = 1;                            // reset states
                l2 = 1; o2 = 1;
            } else {
                l2 = (o2 == 1) ? l2 * num : l2 / num;      // update num to l2
                num = 0;
                if (c == ')') {
                    num = l1 + o1 * l2;                    // save current res to num
                    o2 = stack.pop();
                    l2 = stack.pop();
                    o1 = stack.pop();
                    l1 = stack.pop();
                } else if (c == '*' || c == '/') {
                    o2 = (c == '*') ? 1 : -1;
                } else {
                    l1 = l1 + o1 * l2;                     // save l2 to l1
                    o1 = (c == '+') ? 1 : -1;
                    l2 = 1;
                    o2 = 1;
                }
            }
        }
        return l1 + o1 * l2;
    }
}
```

T: O(n)			S: O(n)

---

#### Recursion  

We could use recusive cal to process parentheses.

```java
class Solution {
    
    int i = 0;
    
    public int calculate(String s) {
        return cal(s);
    }
    
    private int cal(String s) {
        Stack<Integer> stack = new Stack<>();
        int num = 0;
        char sign = '+';
        for (; i <= s.length(); i++) {
            char c = (i != s.length()) ? s.charAt(i) : '+';
            if (c == ' ') continue;
            if (c == '(') {
                i++;
                num = cal(s);                   // get number of parentheses
            } else if (Character.isDigit(c)) {
                num = num * 10 + c - '0';
            } else {
                if (sign == '+') {
                    stack.push(num);
                } else if (sign == '-') {
                    stack.push(-num);
                } else if (sign == '*') {
                    stack.push(stack.pop() * num);
                } else {
                    stack.push(stack.pop() / num);
                }
                num = 0;
                sign = c;
                if (sign == ')') break;       // if we are at end of parentheses
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

T: O(n)			S: O(n)

---

###Infix to PostFix

The solution has 2 steps:

1. parse the input string and convert it to postfix notation.
2. evaluate the postfix string from step 1.

**Infix to postfix conversion**

converting a simple expression string that doesn't contain brackets to postfix is explained [here](http://scriptasylum.com/tutorials/infix_postfix/algorithms/infix-postfix/). You can imagine the expression between brackets as a new simple expression (which we know how to convert to postfix). So when we encounter opening bracket "(" push it to the top stack. When we encounter a closing bracket ")" keep popping from stack until we find the matching "(", here we are removing all operators that belong to the expression between brackets. Then pop the "(" from the stack.

One more thing to take into consideration, we don't want any operator to pop the "(" from the stack except the ")". We can handle this be assigning the "(" the lowest rank such that no operator can pop it.

**Evaluate postfix expression**

postfix evaluation is explained [here](http://scriptasylum.com/tutorials/infix_postfix/algorithms/postfix-evaluation/)

```java
class Solution {
    private int rank(char op) {
        switch(op) {
            case '+': return 1;
            case '-': return 1;
            case '*': return 2;
            case '/': return 2;
            default : return 0;  // for '('
        }
    }
    
    public int calculate(String s) {
        return evalPostfix(infixToPostfix(s));
    }
    
    private List<Object> infixToPostfix(String s) {
        List<Object> res = new ArrayList<>();
        Stack<Character> stack = new Stack<>();
        if (s == null || s.length() == 0) return res;
        stack.add('(');                     								// add ( to first
        int num = 0;
        boolean collect = false;            								// collect num
        boolean checkUnary = true;          								// check unary operator
        for (int i = 0; i <= s.length(); i++) {
            char c = (i != s.length()) ? s.charAt(i) : ')'; // add ) to last
            if (c == ' ') continue;
            if (checkUnary) {
                checkUnary = false;
                if (c == '+' || c == '-') {
                    res.add(0);
                }
            }
            if (Character.isDigit(c)) {
                collect = true;
                num = num * 10 + c - '0';
            } else {
                if (c == '(') {
                    checkUnary = true;            // check unary operator
                    stack.push(c);
                } else {
                    if (collect) {
                        collect = false;
                        res.add(num);
                        num = 0;
                    }
                    while (!stack.isEmpty() && rank(stack.peek()) >= rank(c)) {
                        char op = stack.pop();
                        if (op == '(') break;
                        res.add(op);
                    }
                    if (c != ')') {
                        stack.push(c);
                    }
                }
            }
        }
        return res;
    }
    
    private int evalPostfix(List<Object> list) {
        Stack<Integer> stack = new Stack<>();
        for (Object o : list) {
            if (o instanceof Integer) {
                stack.push((int) o);
            } else {
                char c = (char) o;
                int b = stack.pop();
                int a = stack.pop();
                if (c == '+') {
                    stack.push(a + b);
                } else if (c == '-') {
                    stack.push(a - b);
                } else if (c == '*') {
                    stack.push(a * b);
                } else {
                    stack.push(a / b);
                }
            }
        }
        return stack.pop();
    }
}
```

T: O(n)			S: O(n)