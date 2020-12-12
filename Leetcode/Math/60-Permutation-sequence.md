---
title: Medium | Permutation Sequence
tags:
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-05-13 21:49:48
---

The set `[1,2,3,...,*n*]` contains a total of *n*! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for *n* = 3:

1. `"123"`
2. `"132"`
3. `"213"`
4. `"231"`
5. `"312"`
6. `"321"`

Given *n* and *k*, return the *k*th permutation sequence.

[Leetcode](https://leetcode.com/problems/permutation-sequence/)

<!--more-->

**Example 1:**

```
Input: n = 3, k = 3
Output: "213"
```

**Example 2:**

```
Input: n = 4, k = 9
Output: "2314"
```

---

#### Tricky 

We could group permutations by factorial.

For example, n = 4.

When we consider the first char, there'll be `factorial = 3 * 2 * 1` permutations in the group.

When we consider the seconde char, there'll be `factorial = 2 * 1 ` permutations in the group.

So `int index = k / factorial`  is the index to the nums for current char.

`int k = k % factorial` is the remaining k for rest of chars.

---

#### Standard solution  

```java
class Solution {
    public String getPermutation(int n, int k) {
        if (n == 0) return "";
        int factorial = 1;
        for (int i = n - 1; i >= 1; i--) {
            factorial *= i;
        }
        List<Character> nums = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            nums.add((char)('1' + i));
        }
        k--;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int index = k / factorial;       // index of current number
            k = k % factorial;               // remaining k for the remaining numbers.
            sb.append(nums.get(index));
            nums.remove(index);
            if (i != n - 1) {
                factorial /= n - 1 - i;      // factorial group shrinks.
            }
        }
        return sb.toString();
    }
}
```

T: O(n)		S: O(n)

---

#### Summary 

In tricky.