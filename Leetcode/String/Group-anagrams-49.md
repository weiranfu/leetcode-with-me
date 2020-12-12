---
title: Medium | Group Anagrams 49
tags:
  - common
  - tricky
categories:
  - Leetcode
  - String
date: 2020-05-10 18:17:55
---

Given an array of strings, group anagrams together.

[Leetcode](https://leetcode.com/problems/group-anagrams/)

<!--more-->

**Example:**

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

**Note:**

- All inputs will be in lowercase.
- The order of your output does not matter.

---

#### Tricky 

Use sorted string as a key into map.

---

#### Standard solution  

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            char[] cs = s.toCharArray();
            Arrays.sort(cs);
            String sort_str = new String(cs);
            if (!map.containsKey(sort_str)) {
                map.put(sort_str, new ArrayList<>());
            }
            List<String> list = map.get(sort_str);
            list.add(s);
        }
        List<List<String>> res = new ArrayList<>();
        res.addAll(map.values());
        return res;
    }
}
```

T: O(n* mlogm)		S: O(n)