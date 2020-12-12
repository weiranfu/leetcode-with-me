---
title: Medium | Count Sorted Vowel Strings 1641
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-11-21 15:55:22
---

Given an integer `n`, return *the number of strings of length* `n` *that consist only of vowels (*`a`*,* `e`*,* `i`*,* `o`*,* `u`*) and are **lexicographically sorted**.*

A string `s` is **lexicographically sorted** if for all valid `i`, `s[i]` is the same as or comes before `s[i+1]` in the alphabet.

[Leetcode](https://leetcode.com/problems/count-sorted-vowel-strings/)

<!--more-->

**Example 1:**

```
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
```

**Example 2:**

```
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
```

**Constraints:**

- `1 <= n <= 50` 

---

#### Brute Force 

```java
class Solution {
    public int countVowelStrings(int n) {
        return find(0, n);
    }
    private int find(int curr, int n) {
        if (n == 0) return 1;
        int sum = 0;
        for (int i = curr; i < 5; i++) {
            sum += find(i, n - 1);
        }
        return sum;
    }
}
```

- Time Complexity : O(*n^*4). At every level `i`, there are roughly `i^4` enumerations. The following figure illustrates the number of possible paths at level 2.

![img](https://leetcode.com/problems/count-sorted-vowel-strings/Figures/5555/timeComplexityBruteForce.png)

Since the maximum depth of recursion would be `n`, the time complexity to explore all the path would be roughly equal to O(n^4).

**This is a rough estimation**.

We could also say the upper bound of this algorithm is O(5^n) **Of course, O(5^n) is over counting. **

---

#### Standard solution  

The problem is a variant of finding [Combinations](https://en.wikipedia.org/wiki/Combination). Mathematically, the problem can be described as, given 5 vowels (let k = 5), find the number of combinations using *n* vowels. Also, we can repeat each of those vowels multiple times.

可重复元素，隔板法

一共有4个隔板，n+4 个位置

`C(n + 4, 4) = (n+4)*(n+3)*(n+2)*(n+1)/24`

```java
class Solution {
    public int countVowelStrings(int n) {
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) / 24;
    }
}
```

T: O(1)			S:  O(1)



