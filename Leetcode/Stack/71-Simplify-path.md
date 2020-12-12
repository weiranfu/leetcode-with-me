---
title: Medium | Simplify Path 71
tags:
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-05-15 17:16:33
---

Given an **absolute path** for a file (Unix-style), simplify it. Or in other words, convert it to the **canonical path**.

In a UNIX-style file system, a period `.` refers to the current directory. Furthermore, a double period `..` moves the directory up a level.

Note that the returned canonical path must always begin with a slash `/`, and there must be only a single slash `/` between two directory names. The last directory name (if it exists) **must not** end with a trailing `/`. Also, the canonical path must be the **shortest**string representing the absolute path.

[Leetcode](https://leetcode.com/problems/simplify-path/)

<!--more-->

**Example 1:**

```
Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
```

**Example 2:**

```
Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
```

**Example 3:**

```
Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
```

**Example 4:**

```
Input: "/a/./b/../../c/"
Output: "/c"
```

**Example 5:**

```
Input: "/a/../../b/../c//.//"
Output: "/c"
```

**Example 6:**

```
Input: "/a//b////c/d//././/.."
Output: "/a/b/c"
```

---

#### Tricky 

1. How to store the previous state of subdir's name? (when meeting `".."` we need to move up a level)

   One obvious idea is to use a Linked List to store the previous state.

   However the easiest one is to use **Stack**!

2. When processing String to extract parts of it, we could use `s.split("/")`.

---

#### My thoughts 

Use stack to store previous state.

When we encounter `'/'`, we need to process the chars we have collected and add them to Stack.

```java
class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        for (char ch : path.toCharArray()) {
            if (ch == '/') {              
                getSubDir(sb, stack);      // process chars
                sb = new StringBuilder();
            } else {
                sb.append(ch);             // collect chars
            }
        }
        getSubDir(sb, stack);          // process remaining chars
        
        sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.insert(0, stack.pop());
            sb.insert(0, "/");
        }
        if (sb.length() == 0) {
            sb.append("/");
        }
        return sb.toString();
    }
    
    private void getSubDir(StringBuilder sb, Stack<String> stack) {
        String s = sb.toString();
        if (s.length() == 0 || s.equals(".")) {
            return;
        } else if (s.equals("..")) {
            if (!stack.isEmpty()) {
                stack.pop();
            }
        } else {
            stack.push(s);
        }
    }
}
```

T: O(n)		S: O(n)

---

#### Optimized

Use `s.split("/")` to simplify the extracting of name of subdirectories.

```java
class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<>();
        for (String name : path.split("/")) {
            if (name.equals("") || name.equals(".")) continue;
            if (name.equals("..")) {
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            } else {
                stack.push(name);
            }
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.insert(0, stack.pop());
            sb.insert(0, "/");
        }
        if (sb.length() == 0) {
            sb.append("/");
        }
        return sb.toString();
    }
}
```

T: O(n)			S: O(n)

