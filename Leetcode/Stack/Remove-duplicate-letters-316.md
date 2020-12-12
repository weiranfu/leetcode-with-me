---
title: Hard | Remove Duplicate Letters 316
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-07-27 12:28:18
---

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

[Leetcode](https://leetcode.com/problems/remove-duplicate-letters/)

<!--more-->

**Example 1:**

```
Input: "bcabc"
Output: "abc"
```

**Example 2:**

```
Input: "cbacdcbc"
Output: "acdb"
```

**Example 3:**

```
Input: "abacb"
Output: "abc"
```

**Follow up:** 

[Remove K Digits](https://leetcode.com/problems/remove-k-digits/description/)

[Create Maximum Number](https://leetcode.com/problems/create-maximum-number/description/)

---

#### Stack 

First, given `"bcabc"`, the solution should be `"abc"`. If we think about this problem intuitively, you would sort of go from the beginning of the string and start removing one if there is still the same character left and a smaller character is after it. Given `"bcabc"`, when you see a `'b'`, keep it and continue with the search, then keep the following `'c'`, then we see an `'a'`. Now we get a chance to get a smaller lexi order, you can check if after `'a'`, there is still `'b'` and `'c'` or not. We indeed have them and `"abc"` will be our result.

Come to the implementation, we need some data structure to store the previous characters `'b'` and `'c'`, and we need to compare the current character with previous saved ones, and if there are multiple same characters, we prefer left ones. This calls for a stack.

After we decided to use stack, the implementation becomes clearer. From the intuition, we know that we need to know if there are still remaining characters left or not. So we need to iterate the array and save how many each characters are there. A visited array is also required since we want unique character in the solution. The line `while(!stack.isEmpty() && stack.peek() > c && count[stack.peek()-'a'] > 0)` checks that the queued character should be removed or not, like the `'b'` and `'c'` in the previous example. After removing the previous characters, push in the new char and mark the visited array.

If we don't have `visited[]`, we cannot handle the case in *Example 3*, `abacb`, when we meet the second `a`, we aren't allowed to remove previous `b`, otherwise we will get the wrong answer `acb` rather than `abc`.

```java
class Solution {
    public String removeDuplicateLetters(String s) {
        int n = s.length();
        int[] cnt = new int[27];
        for (int i = 0; i < n; i++) {
            cnt[s.charAt(i) - 'a']++;
        }
        boolean[] visited = new boolean[27];
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            int c = s.charAt(i) - 'a';
            cnt[c]--;											// decrease counter
            if (visited[c]) continue;			// don't consider visited char
            while (!stack.isEmpty() && stack.peek() > c && cnt[stack.peek()] > 0) {
                int prev = stack.pop();
                visited[prev] = false;		// mark as unvisited
            }
            stack.push(c);
            visited[c] = true;
        }
        StringBuilder sb = new StringBuilder();
        for (int c : stack) {
            sb.append((char)(c + 'a'));
        }
        return sb.toString();
    }
}
```

Time complexity: O(n), n is the number of chars in string.

Space complexity: O(n) worst case.



