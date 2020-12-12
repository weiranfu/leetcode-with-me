---
title: Hard | Design Search Autocomplete System 642
tags:
  - tricky
categories:
  - Leetcode
  - Design
date: 2019-12-27 21:15:12
---

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character `'#'`). For **each character** they type **except '#'**, you need to return the **top 3** historical hot sentences that have prefix the same as the part of sentence already typed. 

[Leetcode](https://leetcode.com/problems/design-search-autocomplete-system/)

<!--more-->

Here are the specific rules:

1. The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
2. The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
3. If less than 3 hot sentences exist, then just return as many as you can.
4. When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

Your job is to implement the following functions:

The constructor function:

`AutocompleteSystem(String[] sentences, int[] times):` This is the constructor. The input is **historical data**. `Sentences` is a string array consists of previously typed sentences. `Times` is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

`List<String> input(char c):` The input `c` is the next character typed by the user. The character will only be lower-case letters (`'a'` to `'z'`), blank space (`' '`) or a special character (`'#'`). Also, the previously typed sentence should be recorded in your system. The output will be the **top 3** historical hot sentences that have prefix the same as the part of sentence already typed.

 

**Example:**
**Operation:** AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
`"i love you"` : `5` times
`"island"` : `3` times
`"ironman"` : `2` times
`"i love leetcode"` : `2` times
Now, the user begins another search:

**Operation:** input('i')
**Output:** ["i love you", "island","i love leetcode"]
**Explanation:**
There are four sentences that have prefix `"i"`. Among them, "ironman" and "i love leetcode" have same hot degree. Since `' '` has ASCII code 32 and `'r'` has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

**Operation:** input(' ')
**Output:** ["i love you","i love leetcode"]
**Explanation:**
There are only two sentences that have prefix `"i "`.

**Operation:** input('a')
**Output:** []
**Explanation:**
There are no sentences that have prefix `"i a"`.

**Operation:** input('#')
**Output:** []
**Explanation:**
The user finished the input, the sentence `"i a"` should be saved as a historical sentence in system. And the following input will be counted as a new search.

**Note:**

1. The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
2. The number of **complete sentences** that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
3. Please use double-quote instead of single-quote when you write test cases even for a character input.
4. Please remember to **RESET** your class variables declared in class AutocompleteSystem, as static/class variables are **persisted across multiple test cases**. Please see [here](https://leetcode.com/faq/#different-output) for more details.

---

#### Tricky 

We use Trie to store input lines.

1. **Use DFS to collect all possible histories and sort them.** So we only need to store `String` and `times` in the last Node of an input line.
2. Keep a *hot history list* in each node. **We need to store the End Node in list for comparing based on String and times. When we input a new line, we need to record the visited nodes. After finishing inputing, we have to update all visited nodes' *hot history list***.

---

#### First solution

How to implement `input()` ?

Keep a `StringBuilder` and `curr` Node to track current input status.

When we encounter `#`, we store `sb.toString()` into End Node.

If we encounter an `null` node, create a new Node at `curr` and return empty list.

```java
class AutocompleteSystem {
    class Node {
        Node[] children = new Node[27];    // a-z + ' '
        int times;      // only save in last Node
        String line;    // only save in last Node
    }
    
    Node root;
    Node curr;          // current node when input
    StringBuilder sb;   // already input string

    public AutocompleteSystem(String[] sentences, int[] times) {
        root = new Node();
        curr = root;
        sb = new StringBuilder();
        for (int i = 0; i < sentences.length; i++) {
            addLine(sentences[i], times[i]);   
        }
    }
    
    private void addLine(String line, int times) {
        Node node = root;
        for (char c : line.toCharArray()) {
            int idx = (c == ' ') ? 26 : c - 'a';
            if (node.children[idx] == null) {
                node.children[idx] = new Node();
            }
            node = node.children[idx];
        }
        node.line = line;
        node.times += times;
    }
    
    public List<String> input(char c) {
        List<String> res = new ArrayList<>();
        if (c == '#') {
            curr.line = sb.toString();
            curr.times++;
            sb = new StringBuilder();          // clear input
            curr = root;                       // reset curr
            return res;
        }
        sb.append(c);
        int idx = (c == ' ') ? 26 : c - 'a'; 
        if (curr.children[idx] == null) {      // doesn't have this char
            curr.children[idx] = new Node();
            curr = curr.children[idx];
            return res;
        }
        curr = curr.children[idx];
        List<Node> list = new ArrayList<>();
        collect(curr, list);
        
        Collections.sort(list, (a, b) -> {
            if (a.times != b.times) {
                return b.times - a.times;
            } else {
                return a.line.compareTo(b.line);
            }
        });
        
        for (int i = 0; i < 3 && i < list.size(); i++) {
            res.add(list.get(i).line);
        }
        return res;
    }
    
    private void collect(Node n, List<Node> list) {
        if (n.times > 0) {                   // if find a sentence
            list.add(n);
        }
        for (int i = 0; i < 27; i++) {
            if (n.children[i] == null) continue;
            collect(n.children[i], list);
        }
    }
}
```

Analysis:

* `AutocompleteSystem()` takes O(k\*len) time. We need to iterate over `len` sentences each of average length `k`, to create the trie for the given set of sentences.
* `input()` takes O(27^depth + mlogm) time. Here `depth` means the depth we recursively call when we collecting histories. `m` indicating the length of collected histories.

---

#### Optimized 

Using DFS to collect all histories can be too slow.

So we could maintain a *hot history list* in each Node. **We need to store the End Node in list for comparing based on String and times.**

**When we input a new line, we need to record the visited nodes. After finishing inputing, we have to update all visited nodes' *hot history list***.

To implement `input`, we keep `Node curr`, `StringBuilder sb` and `List<Node> visited` to store the input status.

```java
class AutocompleteSystem {
    class Node {
        Node[] children = new Node[27];         // a-z + ' '
        int times;                              // only save in last Node
        String line;                            // only save in last Node
        List<Node> hotList = new ArrayList<>(); // store End Node as hot histories
    }
    
    Node root;
    Node curr;          // current node when input
    StringBuilder sb;   // already input string
    List<Node> visited; // visited node waiting for updating

    public AutocompleteSystem(String[] sentences, int[] times) {
        root = new Node();
        curr = root;
        sb = new StringBuilder();
        visited = new ArrayList<>();
        for (int i = 0; i < sentences.length; i++) {
            addLine(sentences[i], times[i]);   
        }
    }
    
    private void addLine(String line, int times) {
        Node node = root;
        
        List<Node> visited = new ArrayList<>(); // visited list
        for (char c : line.toCharArray()) {
            int idx = (c == ' ') ? 26 : c - 'a';
            if (node.children[idx] == null) {
                node.children[idx] = new Node();
            }
            node = node.children[idx];
            visited.add(node);
        }
        node.line = line;
        node.times += times;
        
        for (Node n : visited) {              // update hot list
            update(n, node);
        }
    }
    
    public List<String> input(char c) {
        List<String> res = new ArrayList<>();
        if (c == '#') {
            curr.line = sb.toString();
            curr.times++;
            for (Node n : visited) {
                update(n, curr);
            }
            sb = new StringBuilder();          // clear input
            curr = root;                       // reset curr
            visited = new ArrayList<>();       // clear visited
            return res;
        }
        sb.append(c);
        int idx = (c == ' ') ? 26 : c - 'a'; 
        if (curr.children[idx] == null) {      // doesn't have this char
            curr.children[idx] = new Node();
            curr = curr.children[idx];
            visited.add(curr);
            return res;
        }
        curr = curr.children[idx];
        visited.add(curr);
        
        for (Node n : curr.hotList) {
            res.add(n.line);
        }
        return res;
    }
    
    private void update(Node curr, Node target) {  // update hot list
        if (!curr.hotList.contains(target)) {
            curr.hotList.add(target);
        }
        
        Collections.sort(curr.hotList, (a, b) -> {
            if (a.times != b.times) {
                return b.times - a.times;
            } else {
                return a.line.compareTo(b.line);
            }
        });
        
        if (curr.hotList.size() > 3) {
            curr.hotList.remove(curr.hotList.size() - 1);
        }
    }
}
```

Analysis:

- `AutocompleteSystem()` takes O(k\*len) time. We need to iterate over `len` sentences each of average length `k`, to create the trie for the given set of sentences.
- `input()` takes amortized O(1) time. Since the *hot history list* is size of 3, we only need to update *hot history list* when we input `#`.

