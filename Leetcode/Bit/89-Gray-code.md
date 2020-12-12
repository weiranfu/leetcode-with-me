---
title: Medium | Gray Code 89
tags:
  - tricky
categories:
  - Leetcode
  - Bit
date: 2020-05-19 23:37:11
---

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer *n* representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0. A gray code sequence of n has size = 2^n.

[Leetcode](https://leetcode.com/problems/gray-code/)

<!--more-->

**Example 1:**

```
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
```

**Example 2:**

```
Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
```

---

#### Tricky 

When n=3, we can get the result based on n=2.         00,01,11,10

000

001

011

010

110

111

101

100

The middle two numbers only differ at their highest bit, while the rest numbers of part two are exactly symmetric of part one.

---

#### First solution 

Use a map to store previous result list. And add one bit to the previous of results.

```java
class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> list = new ArrayList<>();
        list.add(0);
        Map<Integer, List<Integer>> map = new HashMap<>();
        map.put(0, list);
        for (int i = 1; i <= n; i++) {
            List<Integer> preCodes = map.get(i - 1);
            List<Integer> newCodes = new ArrayList<>(preCodes);
            int base = (1 << (i - 1));
            for (int j = preCodes.size() - 1; j >= 0; j--) {
                newCodes.add(base + preCodes.get(j));
            }
            map.put(i, newCodes);
        }
        return map.get(n);
    }
}
```

T: O(n^2)			S: O(n)		

---

#### Optimized: 

Don't need to use a map to store previous results. We can get previous results easily.

Use `list.get(j) | (1 << i)` to add one bit to the head of results.

```java
class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> list = new ArrayList<>();
        list.add(0);
        for (int i = 0; i < n; i++) {
            int size = list.size();
            for (int j = size - 1; j >= 0; j--) {
                list.add(list.get(j) | (1 << i));
            }
        }
        return list;
    }
}
```

T: O(n^2)		S: O(1)



