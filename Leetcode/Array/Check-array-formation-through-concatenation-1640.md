---
title: Easy | Check Array Formation Through Concatenation 1640
tags:
  - common
categories:
  - Leetcode
  - Array
date: 2020-11-21 15:39:51
---

You are given an array of **distinct** integers `arr` and an array of integer arrays `pieces`, where the integers in `pieces` are **distinct**. Your goal is to form `arr` by concatenating the arrays in `pieces` **in any order**. However, you are **not** allowed to reorder the integers in each array `pieces[i]`.

Return `true` *if it is possible* *to form the array* `arr` *from* `pieces`. Otherwise, return `false`.

[Leetcode](https://leetcode.com/problems/check-array-formation-through-concatenation/)

<!--more-->

**Example 1:**

```
Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].
```

**Example 2:**

```
Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]
```

**Constraints:**

- `1 <= pieces.length <= arr.length <= 100`
- `sum(pieces[i].length) == arr.length`
- `1 <= pieces[i].length <= arr.length`
- `1 <= arr[i], pieces[i][j] <= 100`
- The integers in `arr` are **distinct**.
- The integers in `pieces` are **distinct** (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).

---

#### Brute Force

The key is `arr` are **distinct** and `sum(pieces[i].length) == arr.length`, so all items in pieces should be also **distinct**. Then we can use the matching of first item in a piece to identify the next proper piece.

```java
class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        int n = arr.length, m = pieces.length;
        outer:
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i] == pieces[j][0]) {  //  find proper piece
                    for (int num : pieces[j]) {
                        if (arr[i] != num) return false;
                        i++;
                    }
                    i--;
                    continue outer;
                }
            }
            return false;
        }
        return true;
    }
}
```

T: O(n^2)			S: O(1)

---

#### Optimized

Use map to store the first item in a piece for quickly querying proper piece.

```java
class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        int n = arr.length, m = pieces.length;
        Map<Integer, int[]> map = new HashMap<>();
        for (int[] piece : pieces) {
            if (map.containsKey(piece[0])) return false;
            map.put(piece[0], piece);
        }
        for (int i = 0; i < n; i++) {
            if (!map.containsKey(arr[i])) return false;
            int[] piece = map.get(arr[i]);
            for (int num : piece) {
                if (arr[i] != num) return false;
                i++;
            }
            i--;
        }
        return true;
    }
}
```

T: O(1)		S:  O(n)

