---
title: KMP — Fast String Search Method
tags:
  - tricky
categories:
  - Summary
date: 2020-01-29 17:33:46
---

The key is to precompute some information about pattern string before performming search on text string.

The information about pattern is the **max length of common prefix and suffix for each char in pattern.**

Pattern: "a b a c a b a b"

next:      "0 0 0 1 0 1 2 3"

<!--more-->

`next[x]` means if `text[i] != pattern[x]` pattern fails matching at x position, pattern will go back to `next[x]` to rematch `text[i]`.

If x == 0, which means pattern string cannot go back any more, we give up matching `text[i]`, move forward to match next char in text. So i++.

---

#### KMP

```java
public static List<Integer> search(String s, String p) {
        List<Integer> res = new ArrayList<>();
        int m = s.length();
        int n = p.length();

        int[] next = new int[n + 1];
        for (int i = 1, j = 0; i < n; i++) {                            // starts at 1
            while (j > 0 && p.charAt(i) != p.charAt(j)) j = next[j];
            if (p.charAt(i) == p.charAt(j)) j++;
            next[i + 1] = j;    											// write next[] value to next pos
        }

        for (int i = 0, j = 0; i < m; i++) {
            while (j > 0 && s.charAt(i) != p.charAt(j)) j = next[j];
            if (s.charAt(i) == p.charAt(j)) j++;
            if (j == n) {
                res.add(i - n + 1);   // collect one match
                j = next[j];
            }
        }
        return res;
    }
```

T: O(N) 			S: O(N)

