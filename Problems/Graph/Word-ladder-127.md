---
title: Medium | Word Ladder 127
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-05-26 22:44:52
---

Given two words (*beginWord* and *endWord*), and a dictionary's word list, find the length of shortest transformation sequence from *beginWord* to *endWord*, such that:

1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list.

**Note:**

- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume *beginWord* and *endWord* are non-empty and are not the same.

[Leetcode](https://leetcode.com/problems/word-ladder/)

<!--more-->

**Example 1:**

```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
```

**Example 2:**

```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```

**Follow up:** [Word Ladder II](https://aranne.github.io/2020/05/26/126-Word-ladder/#more)

---

#### Tricky 

**The first intuition for this problem is to build a graph whose nodes represent strings and edges connect strings that are only 1 character apart, and then we apply BFS from the startWord node.** If we find the endWord, we return the level count of the bfs. This intuition is correct, but there are some places that we can save time.

1. When we build adjacency list graph, we don't use two loops to check every pair of string to see if they are 1 character apart. Instead, we make changes to current string to obtain all the strings we can reach from current node, and see if it is in the wordList. Thus, there are currentString.length() * 25 case we need to check for every node. This is faster when the wordList set is large, since the check-every-pair method need wordList.size() * currentString.length() for each node. Otherwise, your may exceed the running time limit.

2. For the strings we visited, we remove it from the wordList. This way we don't need to mark visited using another HashSet or something.

3. Actually, we don't even need to build the adjacency list graph explicitly using a HashMap<String, ArrayList>, since we keep all the nodes we can reach in the queue of each level of BFS. This can be seen as the keys of the HashMap are the strings that in the queue, and values are the strings that satisfy the 1 character apart in the wordList. Thus, we avoid the time cost of build map for those nodes we don't need to visit.

---

#### My thoughts 

BFS. Maintain a queue to bfs all possible strings until we find `endWord`.

When we check whether two words can transform, we go through all words in `set` to see whether each pair is one char apart. (**This is slow!!!**) 

---

#### BFS

We only consider all words `currWord` can transform to, then it will be much faster than go through all words in `set`. (because the set size could be very large)

```java
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> set = new HashSet<>(wordList);
        if (!set.contains(endWord)) return 0;
        if (beginWord.equals(endWord)) return 0;
        set.remove(beginWord);
        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord);
        int level = 0;
        while (!queue.isEmpty()) {
            level++;
            int size = queue.size();
            while (size-- != 0) {
                String currWord = queue.poll();
                char[] word = currWord.toCharArray();
                for (int i = 0; i < word.length; i++) {   // change each chars 
                    char old = word[i];
                    for (char c = 'a'; c <= 'z'; c++) {   // all possible changes
                        word[i] = c;
                        String newWord = new String(word);
                        if (newWord.equals(endWord)) {
                            return level + 1;
                        }
                        if (set.contains(newWord)) {
                            set.remove(newWord);
                            queue.add(newWord);
                        }
                    }
                    word[i] = old;
                }
            }
        }
        return 0;
    }
}
```

T: O(V + E) 			S: O(V)

---

#### Two-ends BFS

**If we know the start point and end point, we could perform Two-ends BFS to search faster!!!**

`q1` and `q2` is the frontier queue of two-ends BFS.

If `q1.size() < q2.size()`, we perform BFS on `q1`, otherwise we perform BFS on `q2`.

When we BFS on `q1` to search a word that is already in `q2`, we find the smallest path!

The end condition is that `while (!q1.size() && !q2.size())`, which means if either `q1` or `q2` becomes empty, we cannot continue BFS any more.

```java
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> words = new HashSet<>();
        for (String s : wordList) words.add(s);
        if (!words.contains(endWord)) return 0;
        Set<String> q1 = new HashSet<>(), q2 = new HashSet<>();
        q1.add(beginWord); q2.add(endWord);
        words.remove(beginWord); words.remove(endWord);
        int cnt = 0;
        while (!q1.isEmpty() && !q2.isEmpty()) {
            cnt++;
            if (q1.size() > q2.size()) {   // change search direction
                Set<String> tmp = q1;
                q1 = q2;
                q2 = tmp;
            }
            Set<String> next = new HashSet<>();
            for (String s : q1) {
                char[] cs = s.toCharArray();
                for (int i = 0; i < s.length(); i++) {
                    char hold = cs[i];
                    for (int j = 0; j < 26; j++) {
                        cs[i] = (char)('a' + j);
                        String newS = new String(cs);
                        if (q2.contains(newS)) {  // Two-ends BFS meets
                            return cnt + 1;
                        }
                        if (words.contains(newS)) {
                            words.remove(newS);
                            next.add(newS);
                        }
                    }
                    cs[i] = hold;                 // restore original char
                }
            }
            q1 = next;
        }
        return 0;
    }
}
```

回到双向BFS的话题中来。写出code只是第一步，提升逼格还是在分析复杂度上面。[Wikipedia](https://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/Bidirectional_search)上有很好的解释，我就直接复制过来吧。

> in a simplified model of search problem complexity in which both searches expand a [tree](https://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/Tree_(graph_theory)) with [branching factor](https://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/Branching_factor) *b*, and the distance from start to goal is *d*, each of the two searches has complexity ![[公式]](https://www.zhihu.com/equation?tex=O%28b%5E%7Bd%2F2%7D%29)(in [Big O notation](https://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/Big_O_notation)), and the sum of these two search times is much less than the ![[公式]](https://www.zhihu.com/equation?tex=O%28b%5Ed%29)) complexity that would result from a single search from the beginning to the goal.

其中的branch factor指的是展开树里，每一个节点的孩子的个数，也就是每一个元素可能到达的新的元素的个数。例如在一个只能上下左右移动的迷宫里，branch factor就是4，在这个Word Ladder里，每个word的branch factor就是word.size()*25。