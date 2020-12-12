---
title: Medium | Replace the Substring for Balanced String 1234
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-07-28 17:49:41
---

You are given a string containing only 4 kinds of characters `'Q',` `'W', 'E'` and `'R'`.

A string is said to be **balanced** if each of its characters appears `n/4` times where `n` is the length of the string.

Return the minimum length of the substring that can be replaced with **any** other string of the same length to make the original string `s` **balanced**.

Return 0 if the string is already **balanced**.

[Leetcode](https://leetcode.com/problems/replace-the-substring-for-balanced-string/)

<!--more-->

**Example 1:**

```
Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
```

**Example 2:**

```
Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
```

---

#### Sliding Window

1. Count the number of occurrences of each char in original string in `cnt[]`

2. Use `more[]` to record how many number each char's occurrences exceed `target = n / 4` occurrences.

   For example, in `"QQQQ"`, `cnt = [4, 0, 0, 0]` and `more = [3, -1, -1, -1]`

3. We don't care about the char that is less than target occurrences, we only care about the char that is more than target occurrences.(Because we need to replace it).

   In the example above, we only care about `Q`, cause its `more['Q'] = 3 > 0`

   So we use `k` to count how many that type of chars appearing in current window.

   In the example above, `k == 1`

   If `k == 0`, which means we have all that type of chars in the window, record the length and shrink the window.

```java
class Solution {
    public int balancedString(String s) {
        int n = s.length();
        int target = n / 4;
        int[] cnt = new int[4];
        for (int i = 0; i < n; i++) {
            int id = getId(s.charAt(i));
            cnt[id]++;
        }
        int[] more = new int[4];
        int k = 0;
        for (int i = 0; i < 4; i++) {
            more[i] = cnt[i] - target;
            if (more[i] > 0) k++;				// if more[i] > 0, this char will be replaced.
        }
        if (k == 0) return 0;
        int res = n;
        for (int i = 0, j = 0; i < n; i++) {
            int id = getId(s.charAt(i));
            more[id]--;
            if (more[id] == 0) k--;			// k-- if more[i] decreases to 0
            while (j <= i && k == 0) {
                res = Math.min(res, i - j + 1);
                int idx = getId(s.charAt(j));
                if (more[idx] == 0) k++;
                more[idx]++;
                j++;
            }
        }
        return res;
    }
    private int getId(char c) {
        if (c == 'Q') return 0;
        else if (c == 'W') return 1;
        else if (c == 'E') return 2;
        else return 3;
    }
}
```

T: O(n)			S: O(1)

