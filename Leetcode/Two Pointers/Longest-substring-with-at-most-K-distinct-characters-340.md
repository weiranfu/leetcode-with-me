---
title: Medium | Longest Substring with At Most K Distinct Characters 340
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-07-27 23:56:02
---

Given a string, find the length of the longest substring T that contains at most *k* distinct characters.

[Leetcode](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

<!--more-->

**Example 1:**

```
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
```

**Example 2:**

```
Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
```

---

#### Sliding Window 

Keep tracking the cnt of different chars.

```java
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int n = s.length();
        int[] cnt = new int[128];
        int res = 0;
        for (int i = 0, j = 0; i < n; i++) {
            if (cnt[s.charAt(i)] == 0) k--;
            cnt[s.charAt(i)]++;
            while (j <= i && k < 0) {
                cnt[s.charAt(j)]--;
                if (cnt[s.charAt(j)] == 0)  k++;
                j++;
            }
            res = Math.max(res, i - j + 1);
        }
        return res;
    }
}
```

T: O(n)		S: O(1)

---

#### Sliding Window II

**Follow up: The interviewer may say that the string is given as a steam. In this situation, we can't maintain a "left pointer" as the classical O(n) hashmap solution.**

We need to record the last occurrence of each char. When we have more than k dinstinct chars, we need to delete the oldest insertion char and update `j = Math.max(j, map.get(c) + 1)`

Here, we could use `LinkedHashMap<Character, Integer> ` to record the last occurrence of each char.

Since `LinkedHashMap` will maintain in order of insertion, we could easily find the oldest insertion char.

```java
class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        int n = s.length();
        LinkedHashMap<Character, Integer> map = new LinkedHashMap<>();
        int res = 0;
        for (int i = 0, j = 0; i < n; i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                map.remove(c);      // re-insert same key won't affect insertion order
            }                       // so we need to remove it and re-insert
            map.put(c, i);
            if (map.size() > k) {
                // get the first insertion key
                Character first = map.keySet().iterator().next();
                j = Math.max(j, map.get(first) + 1);
                map.remove(first);
            }
            res = Math.max(res, i - j + 1);
        }
        return res;
    }
}
```

```java
class CharStream {
    
    LinkedHashMap<Character, Integer> map;
    int k, id, left, int max;
    
    public CharStream(int k) {
        map = new LinkedHashMap<>();
        this.k = k;
        id = 0; left = 0; max = 0;
    }
    
    public int lengthOfLongestSubstringKDistinct(char in) {
        int pos = id++;
        if (map.containsKey(in)) {
            map.remove(in);         // re-insert same key won't affect insertion order
        }                           // so we need to remove it and re-insert
        map.put(in, pos);
        if (map.size() > k) {
            // get the first insertion key
            Character first = map.keySet().iterator().next();
            left = Math.max(left, map.get(first) + 1);
            map.remove(first);
        }
        max = Math.max(max, pos - left + 1);
        return max;
    }
}
```

T: O(n)			S: O(n)