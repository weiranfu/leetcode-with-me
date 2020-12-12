---
title: Medium | Maximum Number of Occurrences of a Substring 1297
tags:
  - tricky
categories:
  - Leetcode
  - String
date: 2019-12-22 20:16:47
---

Given a string `s`, return the maximum number of ocurrences of **any**substring under the following rules:

- The number of unique characters in the substring must be less than or equal to `maxLetters`.
- The substring size must be between `minSize` and `maxSize` inclusive.

[Leetcode](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/)

<!--more-->

**Example 1:**

```
Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
```

**Example 2:**

```
Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
```

**Example 3:**

```
Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output: 3
```

**Example 4:**

```
Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output: 0
```

**Constraints:**

- `1 <= s.length <= 10^5`
- `1 <= maxLetters <= 26`
- `1 <= minSize <= maxSize <= min(26, s.length)`
- `s` only contains lowercase English letters.

---

#### Tricky 

When considering the occurrence of substrings, we only need to check substrings with `minSize` and `letters < maxLetters`. Because any substring greater than that size would only at most add a new distinct letter, which means since substring greater than minSize satisfies `letters < maxLetters` will have less or equal frequency with the minSize substring.

So we don't need to consider substring with `size > minSize`, this problem then is simplified to a fixed window size problem with length `minSize`. 

---

#### My thoughts 

Brute force. Check all possible length substrings with `letters < maxLetters`.

---

#### First solution 

Sliding window with size between `minSize` and `maxSize`.

```java
class Solution {
    public int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
        int[] map;
        StringBuilder sb;
        char[] chars = s.toCharArray();
        Map<String, Integer> freq = new HashMap<>();
        int max = 0;
        for (int i = 0; i < s.length(); i += 1) {
            int count = 0;
            int len = 0;
            map = new int[26];
            sb = new StringBuilder();
            int k = i;
            while (k < s.length()) {
                if (map[chars[k] - 'a'] == 0) {
                    count += 1;
                }
                sb.append(chars[k]);
                map[chars[k] - 'a'] += 1;
                len += 1;
                k += 1;
                if (len <= maxSize && count <= maxLetters) {
                    if (len >= minSize) {
                        freq.put(sb.toString(), freq.getOrDefault(sb.toString(), 0) + 1);
                        max = Math.max(max, freq.get(sb.toString()));
                    }
                } else {
                    break;
                }
            }
        }
        return max;
    }
}
```

T: O(n^2) S: O(n^2)

---

#### Optimized 

As explained in Tricky, we only need to consider substring with `length == minSize` and `letters < maxLetters`. So the sliding window size is minSize.

```java
class Solution {
    public int maxFreq(String s, int maxLetters, int minSize, int maxSize) {
        int max = 0;
        char[] chars = s.toCharArray();
        Map<String, Integer> occur = new HashMap<>();
        int[] count = new int[128];
        int l = 0, r = 0, letters = 0;
        while (r < chars.length) {
            if (count[chars[r]] == 0) {
                letters++;
            }
            count[chars[r]]++;
            r++;
            while (letters > maxLetters || r - l > minSize) {
                count[chars[l]]--;
                if (count[chars[l]] == 0) {
                    letters--;
                }
                l++;
            }
            if (r - l == minSize) {
                String sub = s.substring(l, r);
                occur.put(sub, occur.getOrDefault(sub, 0) + 1);
                max = Math.max(max, occur.get(sub));
            }
        }
        return max;
    }
}
```

T: O(n) S: O(n)

---

#### Summary 

All substrings satisfy `letters <= maxLetters`. The substring with `length == minSize` must have greater or equal frequency than that of substring with longer size.