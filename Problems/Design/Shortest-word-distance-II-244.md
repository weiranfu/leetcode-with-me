---
title: Medium | Shortest Word Distance II
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Design
date: 2020-06-23 23:21:41
---

Design a class which receives a list of words in the constructor, and implements a method that takes two words *word1* and *word2* and return the shortest distance between these two words in the list. Your method will be called *repeatedly* many times with different parameters. 

[Leetcode](https://leetcode.com/problems/shortest-word-distance-ii/)

<!--more-->

**Example:**
Assume that words = `["practice", "makes", "perfect", "coding", "makes"]`.

```
Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
```

**Follow up:** 

[Shortest Word Distance I](https://aranne.github.io/2020/06/23/Sliding-window-maximum-239/#more)

[Shortest Word Distance III]([Shortest Word Distance III](https://aranne.github.io/2020/06/23/Shortest-word-distance-III-245/#more))

---

#### Tricky 

This is a follow up to *Shortest Word Distance* problem, in which we search one pass to find the min distance.

Here we store all occurrences in a map. When we want to find min distance between two words, we search two lists to find it, which takes O(m)	(m is the length of list)

---

#### Standard solution  

```java
class WordDistance {
    
    String[] words;
    Map<String, List<Integer>> map = new HashMap<>();

    public WordDistance(String[] words) {
        this.words = words;
        for (int i = 0; i < words.length; i++) {
            if (!map.containsKey(words[i])) {
                map.put(words[i], new ArrayList<>());
            }
            map.get(words[i]).add(i);
        }
    }
    
    public int shortest(String word1, String word2) {
        List<Integer> list1 = map.get(word1);
        List<Integer> list2 = map.get(word2);
        int i = 0, j = 0;
        int min = Integer.MAX_VALUE;
        while (i < list1.size() && j < list2.size()) {
            int a = list1.get(i);
            int b = list2.get(j);
            min = Math.min(min, Math.abs(a - b));
            if (a < b) {
                i++;
            } else {
                j++;
            }
        }
        return min;
    }
}
```

`initialize:` O(n)

`shortest()` O(m)		m is the length of list