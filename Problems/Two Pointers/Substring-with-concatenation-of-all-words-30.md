---
title: Hard | Substring with Concatenation of All Words 30
tags:
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-06-01 17:31:14
---

You are given a string, **s**, and a list of words, **words**, that are all of the same length. Find all starting indices of substring(s) in **s** that is a concatenation of each word in **words** exactly once and without any intervening characters.

[Leetcode](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)

<!--more-->

**Example 1:**

```
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
```

**Example 2:**

```
Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
```

---

#### Tricky 

**The key is to search one word each time with different starting position.**

```java
for (int s = 0; s < len; s++) { 									// search with different starting pos.
  /* sliding window [j, i], each time search one word. */
	for (int i = s, j = s; i <= n - len; i += len) {
    
  }
}
```

Use two Map to record the occurrence of words. One for target words, one for collection of substrings.

If we find a word with isn't in target map, we need to clear map and move one word forward.

---

#### Sliding Window  

```java
class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> res = new ArrayList<>();
        if (words == null || words.length == 0) return res;
        int n = s.length(), len = words[0].length();
        int total = words.length;
        Map<String, Integer> targetMap = new HashMap<>();
        for (String word : words) {
            targetMap.put(word, targetMap.getOrDefault(word, 0) + 1);
        }
        for (int start = 0; start < len; start++) {
            Map<String, Integer> map = new HashMap<>();
            int cnt = 0;       												// cnt number of words in window
            /* sliding window [j, i], each time search one word. */
            for (int i = start, j = start; i <= n - len; i += len) {   
                String str = s.substring(i, i + len);
                if (!targetMap.containsKey(str)) {      // if word isn't in target map.
                    map.clear();
                    j = i + len;
                    cnt = 0;
                } else {
                    map.put(str, map.getOrDefault(str, 0) + 1);
                    cnt++;															// shrink window
                    while (j <= i && map.get(str) > targetMap.get(str)) {
                        String tmp = s.substring(j, j + len);
                        map.put(tmp, map.get(tmp) - 1);
                        cnt--;
                        j += len;
                    }
                    if (cnt == total) {
                        res.add(j);
                    }
                }
            }
        }
        return res;
    }
}
```

T: O(n)		S: O(n)



