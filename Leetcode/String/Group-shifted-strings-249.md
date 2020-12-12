---
title: Medium | Group Shifted Strings 249
tags:
  - tricky
categories:
  - Leetcode
  - String
date: 2020-06-24 15:10:20
---

Given a string, we can "shift" each of its letter to its successive letter, for example: `"abc" -> "bcd"`. We can keep "shifting" which forms the sequence:

```
"abc" -> "bcd" -> ... -> "xyz"
```

Given a list of **non-empty** strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

[Leetcode](https://leetcode.com/problems/group-shifted-strings/)

<!--more-->

**Example:**

```
Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
```

---

#### Tricky 

We could shift all strings to `a` based at index 0.

How to process the overflow of lowercase letter?   Add 26!!

```java
cs[j] = (char)(cs[j] - delta);
if (cs[j] < 'a') {
  cs[j] = (char)(cs[j] + 26);
}
```

---

#### Standard solution  

```java
class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        List<List<String>> res = new ArrayList<>();
        int n = strings.length;
        Map<String, List<String>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String s = strings[i];
            char[] cs = s.toCharArray();
            int delta = cs[0] - 'a';
            for (int j = 0; j < cs.length; j++) {
                cs[j] = (char)(cs[j] - delta);
                if (cs[j] < 'a') {
                    cs[j] = (char)(cs[j] + 26);
                }
            }
            String key = new String(cs);
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(strings[i]);
        }
        for (String key : map.keySet()) {
            res.add(map.get(key));
        }
        return res;
    }
}
```

T: O(n * len)			S: O(n)

