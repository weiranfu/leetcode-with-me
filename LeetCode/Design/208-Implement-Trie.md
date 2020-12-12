---
title: Medium | Implement Trie 208
tags:
  - tricky
categories:
  - Leetcode
  - Design
date: 2020-06-08 17:02:35
---

Implement a trie with `insert`, `search`, and `startsWith` methods.

[Leetcode](https://leetcode.com/problems/implement-trie-prefix-tree/)

<!--more-->

**Example:**

```
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
```

---

#### Tricky

Note to set the end of word `isEnd = true`

---

#### Standard solution  

```java
class Trie {
    class Node {
        Node[] children = new Node[128];
        boolean isEnd;
    }
    
    Node root;
    
    /** Initialize your data structure here. */
    public Trie() {
        root = new Node();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        Node curr = root;
        for (char c : word.toCharArray()) {
            if (curr.children[c] == null) {
                curr.children[c] = new Node();
            }
            curr = curr.children[c];
        }
        curr.isEnd = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        Node curr = root;
        for (char c : word.toCharArray()) {
            if (curr.children[c] == null) {
                return false;
            }
            curr = curr.children[c];
        }
        return curr.isEnd;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        Node curr = root;
        for (char c : prefix.toCharArray()) {
            if (curr.children[c] == null) {
                return false;
            }
            curr = curr.children[c];
        }
        return true;
    }
}
```



