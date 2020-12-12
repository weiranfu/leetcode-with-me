---
title: Medium | Zigzag Conversion 6
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - Array
date: 2020-01-22 16:19:47
---

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: `"PAHNAPLSIIGYIR"`

[Leetcode](https://leetcode.com/problems/zigzag-conversion/)

<!--more-->

**Example 1:**

```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

**Example 2:**

```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
```

---

#### Tricky 

We can use a flag `goDown` to indicate whether the zigzag is going down or going up.

The state changing condition is that we reach the top or bottom index.

#### Corner Case

If the number of rows is one, there is no any zigzag traversal. We just need to return the original string.

---

#### My thoughts 

Find the relationship of a char index in string and the level of lists it belongs to.

---

#### First solution 

```java
class Solution {
    public String convert(String s, int numRows) {
        StringBuilder[] zigzag = new StringBuilder[numRows];
        for (int i = 0; i < zigzag.length; ++i) {
            zigzag[i] = new StringBuilder();
        }
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            int index = getRowIndex(i, numRows);
            zigzag[index].append(c);
        }
        StringBuilder sb = new StringBuilder();
        for (StringBuilder level : zigzag) {
            sb.append(level);
        }
        return sb.toString();
    }
    private int getRowIndex(int index, int numRows) {
        if (numRows <= 2) return index % numRows;  // Corner case
        int pos = index % (2 * numRows - 2);
        if (pos > numRows - 1) {
            return 2 * (numRows - 1) - pos;
        } else {
            return pos;
        }
    }
}
```

T: O(n) 				S: O(n)

---

#### Use flag  

Use `goDown` flag to indicate whether the zigzag should go down or go up.

Only if we reach the top or bottom of zigzag, the change the flag.

```java
class Solution {
    public String convert(String s, int numRows) {
        // Corner case
        if (numRows == 1) return s;
        StringBuilder[] zigzag = new StringBuilder[numRows];
        for (int i = 0; i < zigzag.length; ++i) {
            zigzag[i] = new StringBuilder();
        }
        int i = 0, k = 0;
        boolean goDown = true;
        char[] cs = s.toCharArray();
        while (i < cs.length) {
            zigzag[k].append(cs[i++]);
            if (goDown) {
                k++;
            } else {
                k--;
            }
            if (k == numRows - 1 || k == 0) {
                goDown = !goDown;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (StringBuilder level : zigzag) {
            sb.append(level);
        }
        return sb.toString();
    }
}
```

T: O(n)			S: O(n)

---

#### Summary 

Use a flag to indicate zigzag traversal direction.