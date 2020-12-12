---
title: Easy | Pascal's Triangle II 119
tags:
  - common
  - implement
categories:
  - Leetcode
  - Array
date: 2020-05-24 20:30:37
---

Given a non-negative index *k* where *k* ≤ 33, return the *k*th index row of the Pascal's triangle.

[Leetcode](https://leetcode.com/problems/pascals-triangle-ii/)

<!--more-->

Note that the row index starts from 0.

![img](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
In Pascal's triangle, each number is the sum of the two numbers directly above it.

**Example:**

```
Input: 3
Output: [1,3,3,1]
```

**Follow up:**

Could you optimize your algorithm to use only *O*(*k*) extra space?

---

#### Implement

How to set the value in a list?

`list.set(j, list.get(j) + list.get(j + 1))`

---

#### My thoughts 

Each time add a `1` into list, and set the rest of to a sum of contiguous values.

---

#### Standard solution  

```java
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < rowIndex + 1; i++) {
            res.add(0, 1);
            for (int j = 1; j < res.size() - 1; j++) {
                res.set(j, res.get(j) + res.get(j + 1));
            }
        }
        return res;
    }
}
```

T: O(k)			S: O(k)		

