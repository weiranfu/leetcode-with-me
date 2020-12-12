---
title: Easy | Shortest Word Distance 243
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-06-23 22:48:01
---

Given a list of words and two words *word1* and *word2*, return the shortest distance between these two words in the list.

[Leetcode](https://leetcode.com/problems/shortest-word-distance/)

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

[Shortest Word Distance II](https://aranne.github.io/2020/06/23/Shortest-word-distance-244/#more)

[Shortest Word Distance III](https://aranne.github.io/2020/06/23/Shortest-word-distance-III-245/#more)

---

#### Tricky 

* Store all lacations of a word in a list.

  Search two list(sorted) to find the min distance between them

* We could keep two pointers to track the most recent locations of `word1` and `word2`. Each time we find a  word, we will try to find another word.

---

#### First solution 

```java
class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        if (words == null || words.length == 0) return -1;
        if (word1.equals(word2)) return 0;
        int n = words.length;
        Map<String, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            if (!map.containsKey(words[i])) {
                map.put(words[i], new ArrayList<>());
            }
            map.get(words[i]).add(i);
        }
        List<Integer> list1 = map.get(word1);
        List<Integer> list2 = map.get(word2);
        int min = Integer.MAX_VALUE;
        int i = 0, j = 0;
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

T: O(n + m)			m: the size of locations of a word

S: O(n) 

---

#### Two pointers

```java
class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        if (words == null || words.length == 0) return -1;
        if (word1.equals(word2)) return 0;
        int n = words.length;
        int idx1 = -1, idx2 = -1;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (words[i].equals(word1)) {
                idx1 = i;
            } else if (words[i].equals(word2)) {
                idx2 = i;
            }
            if (idx1 != -1 && idx2 != -1) {
                min = Math.min(min, Math.abs(idx1 - idx2));
            }
        }
        return min;
    }
}
```

T: O(n)		S: O(1)

