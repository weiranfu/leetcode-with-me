---
title: Medium | Remove K Digits 402
tags:
  - common
  - tricky
  - corner case
categories:
  - Leetcode
  - Stack
date: 2020-07-27 14:26:36
---

Given a non-negative integer *num* represented as a string, remove *k* digits from the number so that the new number is the smallest possible.

**Note:**

- The length of *num* is less than 10002 and will be ≥ *k*.
- The given *num* does not contain any leading zero.

[Leetcode](https://leetcode.com/problems/remove-k-digits/)

<!--more-->

**Example 1:**

```
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
```

**Example 2:**

```
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
```

**Example 3:**

```
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
```

**Follow up:** 

[Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

---

#### Stack 

Keep an increasing stack and remove as many greater chars as possible.

Corner case:

1. If there's K left after adding all items into Stack, we can pop out items while K > 0.

2. We need to remove leading `0` in the stack.

```java
class Solution {
    public String removeKdigits(String num, int k) {
        int n = num.length();
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            int c = num.charAt(i) - '0';
            while (!stack.isEmpty() && stack.peek() > c && k > 0) {
                stack.pop();
                k--;
            }
            stack.push(c);
        }
        while (k-- > 0) {		// there's K left.
            stack.pop();
        }
        StringBuilder sb = new StringBuilder();
        boolean leadingZero = true;
        for (int c : stack) {
            if (leadingZero && c == 0) continue; // remove leading zero
            leadingZero = false;
            sb.append(c);
        }
        return sb.length() == 0 ? "0" : sb.toString();
    }
}
```

T: O(n)			S: O(n)