---
title: Medium | Largest Number 179
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - Math
date: 2020-06-04 18:10:33
---

Given a list of non negative integers, arrange them such that they form the largest number.

[Leetcode](https://leetcode.com/problems/largest-number/)

<!--more-->

**Example 1:**

```
Input: [10,2]
Output: "210"
```

**Example 2:**

```
Input: [3,30,34,5,9]
Output: "9534330"
```

---

#### Tricky 

**How to get the most significant digit of an integer? We could convert the integer into String, then we could compare them begining with mostt significant digit.**

How to compare two String? `(String a, String b) -> (b + a).compareTo(a + b)`

#### Corner Case

Leading `0`. 

If `strs[0].equals("0") return "0"`

---

#### Standard solution  

```java
class Solution {
    public String largestNumber(int[] nums) {
        int n = nums.length;
        String[] strs = new String[n];
        for (int i = 0; i < n; i++) {
            strs[i] = String.valueOf(nums[i]);
        }
        Arrays.sort(strs, (s1, s2) -> (s2 + s1).compareTo(s1 + s2));
        if (strs[0].equals("0")) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            sb.append(s);
        }
        return sb.toString();
    }
}
```

T: O(nlogn)		S: O(n)



