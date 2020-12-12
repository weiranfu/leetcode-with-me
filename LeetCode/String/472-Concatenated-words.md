---
title: Hard | Concatenated Words 472
tags:
  - tricky
categories:
  - Leetcode
  - String
date: 2019-12-16 21:37:03
---

Given a list of words (**without duplicates**), please write a program that returns all concatenated words in the given list of words. A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

[Leetcode](https://leetcode.com/problems/concatenated-words/)

<!--more-->

**Example:**

```
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
```

**Note:**

1. The number of elements of the given array will not exceed `10,000 `
2. The length sum of elements in the given array will not exceed `600,000`. 
3. All the input string will only include lower case letters.
4. The returned elements order does not matter.

---

#### Tricky 

Using recursion. `concatWord(string)` means this string has at least two concatenated words in list.

Consider all index `i` in a string, `prefix = string.substring(0, i); suffix = string.substring(i);`

if `prefix` is in the list, there're two situations. One is `suffix` is also in list, the other one is suffix contains at least two words in list which means `concatWord(suffix) is true`.

---

#### Standard solution

Recursion.

```java
class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        List<String> res = new ArrayList<>();
        Set<String> dict = new HashSet<>();
        int min = Integer.MAX_VALUE;
        for (String word : words) {
            if (word.length() == 0) continue;
            dict.add(word);
            min = Math.min(min, word.length()); // Minimum length of word.
        }
        for (String word : words) {
            if (concatWord(word, dict, min)) {
                res.add(word);
            }
        }
        return res;
    }
    
    private boolean concatWord(String word, Set<String> dict, int min) {
        for (int i = min; i <= word.length() - min; i += 1) {
            if (dict.contains(word.substring(0, i))) { 
//If prefix is in dict, suffix is also in dict or suffix has at least two words in list.
                if (dict.contains(word.substring(i)) || concatWord(word.substring(i), dict, min)) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

T: O(n* len(word)^2)  S: O(n)

---

#### DP

for each word, consider `substring[i:]`. If `substring[i:] has a word[i:j] and substring[j:]`, then `dp[i] = true;`.

We need to remove string from dictionary before we find concatWord, because a string should have at least two words in dict. So after removing string from dict, the situation that string has only one word in dict is avoided.

```java
class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        List<String> res = new ArrayList<>();
        Set<String> dict = new HashSet<>();
        for (String word : words) {
            if (word.length() == 0) continue;
            dict.add(word);
        }
        for (String word : words) {
            if (word.length() == 0) continue;
            dict.remove(word);
            if (concatWord(word, dict)) {
                res.add(word);
            }
            dict.add(word);
        }
        return res;
    }
    
    private boolean concatWord(String word, Set<String> dict) {
        boolean[] dp = new boolean[word.length() + 1];
        dp[word.length()] = true;
        for (int i = word.length() - 1; i >= 0; i -= 1) {
            for (int j = i + 1; j <= word.length(); j += 1) {
                if (dp[j] && dict.contains(word.substring(i, j))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }
}
```

T: O(n* len(word)^2) S: O(len(word))

---

#### Trie 

We could also use Trie to store words.

```java
class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        List<String> res = new ArrayList<>();
        TrieNode root = new TrieNode();
        for (String word : words) {
            insertWord(word, root);
        }
        for (String word : words) {
            if (concatWord(word.toCharArray(), 0, root, 0)) {
                res.add(word);
            }
        }
        return res;
    }
    public boolean concatWord(char[] word, int index, TrieNode root, int count) {
        TrieNode n = root;
        for (int i = index; i < word.length; i += 1) {
            if (!n.contains(word[i])) {
                return false;
            }
            n = n.get(word[i]);
            if (n.isEnd) {
                // Collect this word as a concatenate word, we need to check left chars.
                if (i != word.length - 1 && concatWord(word, i + 1, root, count + 1)) { 
                    return true;
                }
                // Or we don't collect this word, let the loop continue.
            } 
        }
        return count >= 1 && n.isEnd; // Last word + at least one word
    }
    
    
    public void insertWord(String word, TrieNode root) {
        TrieNode n = root;
        for (char c : word.toCharArray()) {
            if (!n.contains(c)) {
                n.put(c, new TrieNode());
            }
            n = n.get(c);
        }
        n.isEnd = true;
    }
    
    
    class TrieNode {
        TrieNode[] childs;
        boolean isEnd;
        public TrieNode() {
            childs = new TrieNode[26];
        }
        public boolean contains(char ch) {
            return childs[ch - 'a'] != null;
        }
        public TrieNode get(char ch) {
            return childs[ch - 'a'];
        }
        public void put(char ch, TrieNode n) {
            childs[ch - 'a'] = n;
        }
    }
}
```

Don't know the time complexity….

---

#### Summary 

The recurion way might use DP with memorization to reduce time complexity...