---
title: Hard | Word Ladder II
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-05-26 23:57:27
---

Given two words (*beginWord* and *endWord*), and a dictionary's word list, find all shortest transformation sequence(s) from *beginWord* to *endWord*, such that:

1. Only one letter can be changed at a time
2. Each transformed word must exist in the word list. Note that *beginWord* is *not* a transformed word.

**Note:**

- Return an empty list if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume *beginWord* and *endWord* are non-empty and are not the same.

[Leetcode](https://leetcode.com/problems/word-ladder-ii/)

<!--more-->

**Example 1:**

```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
```

**Example 2:**

```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```

---

#### Tricky 

**BFS to search all possible neighbors of each word until we find the `endWord`.**

How to find neighbors? 

1. Iterate all words in `set` to check whether they're one char diff.
2. Change each char in `word` to get all possible words, then check `newWord` is in `set`.

Apparently, approach 2 will much faster.

In order to get all possible paths, we need to store `path` with `word` node.

In order not to consider the visited node in previous level, we need to remove nodes visited in current level.

---

#### First solution 

```java
class Solution {
    class Pair {
        String word;
        List<String> path;
        public Pair(String word, List<String> path) {this.word = word; this.path = path;}
    }
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        List<List<String>> res = new ArrayList<>();
        Set<String> set = new HashSet<>(wordList);
        if (!set.contains(endWord)) return res;
        set.remove(beginWord);        
        List<String> beginList = new ArrayList<>();
        beginList.add(beginWord);
        if (beginWord.equals(endWord)) {
            res.add(beginList);
            return res;
        }
        Queue<Pair> queue = new LinkedList<>();
        queue.add(new Pair(beginWord, beginList));
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<String> removeList = new ArrayList<>();
            while (size-- != 0) {
                Pair p = queue.poll();
                String currWord = p.word;
                List<String> currPath = p.path;
                if (currWord.equals(endWord)) {
                    res.add(currPath);
                    continue;
                }
                char[] word = currWord.toCharArray();
                for (int i = 0; i < word.length; i++) {
                    char old = word[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        word[i] = c;
                        String newWord = new String(word);
                        if (set.contains(newWord)) {
                          // we can't remove newWord right now, because there could be 
                          // other path uses this node.
                            removeList.add(newWord); 
                            List<String> newPath = new ArrayList<>(currPath);
                            newPath.add(newWord);
                            queue.add(new Pair(newWord, newPath));
                        }
                        word[i] = old;
                    }
                }
            }
            for (String s : removeList) {  // after exploring, remove nodes from set.
                set.remove(s);
            }
        }
        return res;
    }
}
```

T: O(V + E)		S: O(V)

---

#### Bidirectional BFS

The stop condition is `while (!q1.isEmpty() && !q2.isEmpty() && !meet)`

```java
class Solution {
    Map<String, List<String>> map;          // save each word's valid neighbors
    boolean forward = true;                 // save search direction
    
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        List<List<String>> res = new ArrayList<>();
        Set<String> words = new HashSet<>();
        for (String word : wordList) words.add(word);
        if (!words.contains(endWord)) return res;
        
        Set<String> q1 = new HashSet<>(), q2 = new HashSet<>();
        q1.add(beginWord); q2.add(endWord);
        words.remove(beginWord); words.remove(endWord);
        map = new HashMap<>();      
        
        boolean meet = false;
        while (!q1.isEmpty() && !q2.isEmpty() && !meet) { // not meet yet
            if (q1.size() > q2.size()) {
                Set<String> tmp = q1;
                q1 = q2;
                q2 = tmp;
                forward = !forward;     // change direction
            }
            Set<String> next = new HashSet<>();
            for (String s : q1) {
                char[] cs = s.toCharArray();
                for (int i = 0; i < cs.length; i++) {
                    char hold = cs[i];
                    for (int j = 0; j < 26; j++) {
                        cs[i] = (char)('a' + j);
                        String newS = new String(cs);
                        if (q2.contains(newS)) {        // q1 and q2 meets
                            meet = true;
                            addPath(s, newS);
                        } else if (!meet && words.contains(newS)) { // not meet yet 
                            next.add(newS);
                            addPath(s, newS);
                        }
                    }
                    cs[i] = hold;
                }
            }
            for (String s : next) {
                words.remove(s);
            }
            q1 = next;
        }
        if (!meet) return res;
        return retrievePath(beginWord, endWord);
    }
    private void addPath(String curr, String next) {
        if (forward) {
            if (!map.containsKey(curr)) {
                map.put(curr, new ArrayList<String>());
            }
            map.get(curr).add(next);
        } else {
            if (!map.containsKey(next)) {
                map.put(next, new ArrayList<String>());
            }
            map.get(next).add(curr);
        }
    }
    private List<List<String>> retrievePath(String s, String endWord) {
        List<List<String>> res = new ArrayList<>();
        if (!map.containsKey(s)) {
            if (!s.equals(endWord)) return res;
            List<String> list = new ArrayList<>();
            list.add(s);
            res.add(list);
            return res;
        }
        for (String next : map.get(s)) {
            List<List<String>> lists = retrievePath(next, endWord);
            for (List<String> list : lists) {
                list.add(0, s);
                res.add(list);
            }
        }
        return res;
    }
}
```

K = word.length() \* 26;

d = search distance

T: O(K^(d/2))					S: O(n)