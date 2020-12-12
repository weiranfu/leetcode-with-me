---
title: Easy | Most Common Word 819
tags:
  - common
  - corner case
categories:
  - Leetcode
  - String
date: 2019-11-26 22:20:10
---

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

[Leetcode](https://leetcode.com/problems/most-common-word/)

<!--more-->

**Example:**

```
Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
```

**Note:** 

- `1 <= paragraph.length <= 1000`.
- `0 <= banned.length <= 100`.
- `1 <= banned[i].length <= 10`.
- The answer is unique, and written in lowercase (even if its occurrences in `paragraph` may have uppercase symbols, and even if it is a proper noun.)
- `paragraph` only consists of letters, spaces, or the punctuation symbols `!?',;.`
- There are no hyphens or hyphenated words.
- Words only consist of letters, never apostrophes or other punctuation symbols.

---

#### Corner case

If there's only one word in paragraph, how can we spot it and change it from StringBuilder to String.

we can add `"."` to the tail of paragraph `paragraph += ".";` in order to spot one word without any non-letter character.

---

#### My thoughts 

Use a map to count how many times a word shows up.

---

#### First solution 

```java
class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> banlist = new HashSet<>();
        Map<String, Integer> count = new HashMap<>();
        for (String s : banned) {
            banlist.add(s);
        }
        String[] words = paragraph.toLowerCase().split("\\W+");
        int max = 0;
        String res = "";
        for (String s : words) {
            if (!banlist.contains(s)) {
                count.put(s, count.getOrDefault(s, 0) + 1);
                if (max < count.get(s)) {
                    max = count.get(s);
                    res = s;
                }
            }
        }
        return res;
    }
}
```

T: O(n) S: O(n)

---

#### Do not use split()

If we are not allowed to use `split()` function to parse word, we should we do?

Use `Character.isLetter(c)` to determine a char c is a letter or not.

```java
class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> banlist = new HashSet<>();
        Map<String, Integer> count = new HashMap<>();
        for (String s : banned) {
            banlist.add(s);
        }
        int max = 0;
        String res = "";
        StringBuilder words = new StringBuilder(); 
        // Corner case: if there's only one word, 
        // we can identify it to change it from StringBuilder to String.
        paragraph += "."; 
        for (char c : paragraph.toCharArray()) {
            if (Character.isLetter(c)) {
                words.append(c);
            } else if (words.length() > 0) {
                String word = words.toString().toLowerCase();
                if (!banlist.contains(word)) {
                    count.put(word, count.getOrDefault(word, 0) + 1);
                    if (max < count.get(word)) {
                        max = count.get(word);
                        res = word;
                    }
                }
                words.setLength(0);             // Clear StringBuilder.
            }
        }
        return res;
    }
}
```

T: O(n) S: O(n)

---

#### Summary

Use `Character.isLetter(c)` to determine a char c is a letter or not if we are not allowed to use `split()` to parse a string.