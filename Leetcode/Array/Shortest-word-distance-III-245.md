---
title: Medium | Shortest Word Distance III 245
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-06-23 23:42:59
---

Given a list of words and two words *word1* and *word2*, return the shortest distance between these two words in the list.

*word1* and *word2* may be the same and they represent two individual words in the list.

[Leetcode](https://leetcode.com/problems/shortest-word-distance-iii/)

<!--more-->

**Example:**
Assume that words = `["practice", "makes", "perfect", "coding", "makes"]`.

```
Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
```

**Follow up:** 

[Shortest Word Distance I](https://aranne.github.io/2020/06/23/Sliding-window-maximum-239/#more)

[Shortest Word Distance II](https://aranne.github.io/2020/06/23/Shortest-word-distance-244/#more)

---

#### Tricky 

When two words are the same, we use `idx1` to record previous position and `idx2` to record current position.

---

#### Standard solution  

```java
class Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        if (words == null || words.length == 0) return -1;
        int idx1 = -1, idx2 = -1;
        int min = Integer.MAX_VALUE;
        boolean same = word1.equals(word2);
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1)) {
                if (same) {
                    idx1 = idx2;
                    idx2 = i;
                } else {
                    idx1 = i;
                }
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