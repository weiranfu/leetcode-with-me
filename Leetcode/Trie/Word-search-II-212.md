---
title: Hard | Word Search II 212
tags:
  - tricky
  - oh-no
categories:
  - Leetcode
  - Trie
date: 2020-06-09 16:29:55
---

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

[Leetcode](https://leetcode.com/problems/word-search-ii/)

<!--more-->

**Example:**

```
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
```

**Note:**

1. All inputs are consist of lowercase letters `a-z`.
2. The values of `words` are distinct.

---

#### Tricky 

1. **Purely backtracking method.** For each word, we go through the graph and try to find a match.

   This is too slow. (brute force)

2. **Prefix search with Trie**. 

   **Use Trie simply as a dictionary to quickly find the match of words and prefixes**

#### Oh-no

Don't forget to reset board from `#` to original char. There're two position in the code we need to reset.

---

#### My thoughts 



---

#### Backtracking

This is brute force.

```java
class Solution {
    
    int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    
    public List<String> findWords(char[][] board, String[] words) {
        List<String> res = new ArrayList<>();
        int m = board.length;
        int n = board[0].length;
        for (String word : words) {
            outer:
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (board[i][j] == word.charAt(0)) {
                        if (search(i, j, 1, word, board)) {
                            res.add(word);
                            break outer;
                        }
                    }
                }
            }
        }
        return res;
    }
    
    private boolean search(int i, int j, int next, String word, char[][] board) {
        int m = board.length;
        int n = board[0].length;
        if (next == word.length())  {   
            return true;
        }
        char tmp = board[i][j];
        board[i][j] = '#';               // mark visited
        
        for (int[] dir : directions) {
            int x = i + dir[0];
            int y = j + dir[1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (board[x][y] == word.charAt(next)) {
                if (search(x, y, next + 1, word, board)) {
                    board[i][j] = tmp;    // reset board
                    return true;
                } 
            }
        }
        
        board[i][j] = tmp;                // reset board
        return false;
    }
}
```

T: O(len\*m\*n*depth).    `len` is number of words. `depth` is search depth.

S: O(depth)		stack length

---

#### Prefix search with Trie

Use Trie simply as a dictionary to quickly find the match of words and prefixes.

Since we are finding prefix of words in a graph, we could store the words in a Trie, which means some words have same prefix will be found in the graph together if possible. And if we know that there does not exist any match of word in the dictionary for a given prefix, then we would not need to further explore certain direction.

Optimize:

1. **Remove the matched words from the Trie.** 

   **If we successfully find a word, we need to mark the `Trie.isEnd = false`**. Because it is possible we enter the same subtree of Trie from different entry in the graph. If we don't mark the word as `isEnd = false`, we will collect that word multiple times. So we could use `List` instead of `set` to collect result.

2. **Gradually *prune* the nodes in Trie during the backtracking.**

   The idea is motivated by the fact that the time complexity of the overall algorithm sort of depends on the size of the Trie. For a leaf node in Trie, once we traverse it (*i.e.* find a matched word), we would no longer need to traverse it again. As a result, we could prune it out from the Trie.

   So we need to keep `parent Node` during backtracking.

   ![pic](https://leetcode.com/problems/word-search-ii/Figures/212/212_trie_prune.png)

   

```java
class Solution {
    class Node {
        Node[] links = new Node[26];
        int count;                     // count for children
        String word;
        boolean isEnd;
        public boolean isLeaf() {       // to determine leaf node
            return count == 0;
        }
    }
    
    int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    Node root = new Node();
    
    public List<String> findWords(char[][] board, String[] words) {
        for (String word : words) {
            Node curr = root;
            for (char c : word.toCharArray()) {
                if (curr.links[c - 'a'] == null) {
                    curr.links[c - 'a'] = new Node();
                    curr.count++;
                }
                curr = curr.links[c - 'a'];
            }
            curr.word = word;
            curr.isEnd = true;
        }
        List<String> res = new ArrayList<>();
        int m = board.length;
        int n = board[0].length;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (root.links[board[i][j] - 'a'] != null) { 
                    search(i, j, root.links[board[i][j] - 'a'], res, board, root);
                }
            }
        }
        return res;
    }
    
    private void search(int i, int j, Node next, List<String> res, char[][] board, Node parent) {
        int m = board.length;
        int n = board[0].length;
        
        char tmp = board[i][j];
        board[i][j] = '#';             // mark as visited
        
        if (next.isEnd) {              // collect word
            res.add(next.word);
            next.isEnd = false;        // only add this word once.
        }

        for (int[] dir : directions) {
            int x = i + dir[0];
            int y = j + dir[1];
            if (x < 0 || x >= m || y < 0 || y >= n) continue;
            if (board[x][y] == '#') continue;        // if visited
            if (next.links[board[x][y] - 'a'] != null) {
                search(x, y, next.links[board[x][y] - 'a'], res, board, next);
            }
        }
        
        board[i][j] = tmp;                     // reset board
        
        // Optimization: incrementally remove the leaf nodes
        if (next.isLeaf()) {
            parent.links[board[i][j] - 'a'] = null;
            parent.count--;
        }
    }
}
```

Time complexity: O( *M*(4⋅3^(*L*−1) ) ), where *M* is the number of cells in the board and *L* is the maximum length of words.

- It is tricky is calculate the exact number of steps that a backtracking algorithm would perform. We provide a upper bound of steps for the worst scenario for this problem. The algorithm loops over all the cells in the board, therefore we have *M* as a factor in the complexity formula. It then boils down to the *maximum* number of steps we would need for each starting cell *i.e.*4⋅3^(*L*−1).
- Assume the maximum length of word is L*L*, starting from a cell, initially we would have at most 4 directions to explore. Assume each direction is valid (*i.e.* worst case), during the following exploration, we have at most 3 neighbor cells (excluding the cell where we come from) to explore. As a result, we would traverse at most 4⋅3^(*L*−1) cells during the backtracking exploration.

Space complexity: O(N).       N is total number of letters in the Trie.

