---
title: Medium | Add and Search Word 211
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Design
date: 2020-06-08 21:53:54
---

Design a data structure that supports the following two operations:

```
void addWord(word)
bool search(word)
```

search(word) can search a literal word or a regular expression string containing only letters `a-z` or `.`. A `.` means it can represent any one letter.

[Leetcode](https://leetcode.com/problems/add-and-search-word-data-structure-design/)

<!--more-->

**Example:**

```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```

**Note:**
You may assume that all words are consist of lowercase letters `a-z`.

---

#### Tricky 

Building a Trie to store all words. And search a word through the Trie.

We need to search all chars if we encounter `.`

---

#### First solution 

```java
class WordDictionary {
    class Node {
        Node[] children = new Node[26];    // 'a'-'z' & '.'
        boolean isEnd;
    }

    Node root;
    
    /** Initialize your data structure here. */
    public WordDictionary() {
        root = new Node();
    }
    
    /** Adds a word into the data structure. */
    public void addWord(String word) {
        Node curr = root;
        for (char c : word.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                curr.children[c - 'a'] = new Node();
            }
            curr = curr.children[c - 'a'];
        }
        curr.isEnd = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        return searchHelper(root, 0, word);
    }
    
    private boolean searchHelper(Node node, int index, String word) {
        int n = word.length();
        if (index == n) {
            return node.isEnd;
        }
        char c = word.charAt(index);
        if (c != '.') {
            if (node.children[c - 'a'] == null) {
                return false;
            } else {
                return searchHelper(node.children[c - 'a'], index + 1, word);
            }
        } else {
            for (int i = 0; i < 26; i++) {
                if (node.children[i] == null) continue;
                if (searchHelper(node.children[i], index + 1, word)) {
                    return true;
                }
            }
            return false;
        }
    }
}
```

Analysis:

`search()` takes O(26^k + len).  `k` means number of `.` in pattern string.

