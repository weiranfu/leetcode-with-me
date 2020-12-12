---
title: Hard | Alien Dictionary 269
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-10-20 23:51:43
---

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of **non-empty** words from the dictionary, where **words are sorted lexicographically by the rules of this new language**. Derive the order of letters in this language.

[Leetcode](https://leetcode.com/problems/alien-dictionary/)

<!--more-->

**Example 1:**

```
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
```

**Example 2:**

```
Input:
[
  "z",
  "x"
]

Output: "zx"
```

**Example 3:**

```
Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
```

**Note:**

- You may assume all letters are in lowercase.
- If the order is invalid, return an empty string.
- There may be multiple valid order of letters, return any one of them is fine.

---

#### Topological Sort + BFS

**STEP 1: Initialize**
for each letter in each word `indegree[letter] = 0;`

**STEP 2: Build Graph and Record the edge**
for each edge (cur node, nex node) `graph.insert(cur, nex)`
for each nex node `indegree[nex]++;`

**STEP 3: Topological Sort**
use queue, push all nodes which indegree is 0;
use BFS start to iterate the whole graph.

**STEP 4: Tell if cyclic**
compare the result with indegree `if exists indegree[c] > 0`

**Edge case: **

**1. handle duplicate paths**

**2. invalid input: previous string is longer than current one and `prev.startsWith(curr)` **

**`zbc, zb`**

```java
class Solution {
    public String alienOrder(String[] words) {
        if (words == null || words.length == 0) return "";
        int n = words.length;
        Set<Integer>[] g = new Set[26];
        for (int i = 0; i < 26; i++) g[i] = new HashSet<>();
        int[] indegree = new int[26];
        Arrays.fill(indegree, -1);
        for (String word : words) {
            for (char c : word.toCharArray()) {
                indegree[c - 'a'] = 0;
            }
        }
        for (int i = 1; i < n; i++) {
            String prev = words[i - 1], curr = words[i];
            int len = Math.min(prev.length(), curr.length());
            if (prev.length() > curr.length() && prev.startsWith(curr)) return "";   // egde case: "abc" is before "ab" => invalid
            for (int j = 0; j < len; j++) {
                char c1 = prev.charAt(j), c2 = curr.charAt(j);
                if (c1 != c2) {
                    if (!g[c1 - 'a'].contains(c2 - 'a'))  {      // don't add duplicate path
                        g[c1 - 'a'].add(c2 - 'a');
                        indegree[c2 - 'a']++;
                    }
                    break;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < 26; i++) {
            if (indegree[i] == 0) q.add(i);
        }
        while (!q.isEmpty()) {
            int u = q.poll();
            sb.append((char)('a' + u));
            for (int v : g[u]) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    q.add(v);
                }
            }
        }
        for (int i = 0; i < 26; i++) {
            if (indegree[i] > 0) return "";
        }
        return sb.toString();
    }
}
```

T: O(n*len)			S: O(1)

---

#### Topological Sort + DFS

Same idea but with DFS implementation.

```java
class Solution {
    Set<Integer>[] g;   // handle duplicate paths
    StringBuilder sb;
    int[] visited;
    
    public String alienOrder(String[] words) {
        if (words == null || words.length == 0) return "";
        int n = words.length;
        g = new Set[26];
        for (int i = 0; i < 26; i++) g[i] = new HashSet<>();
        for (int i = 1; i < n; i++) {
            String prev = words[i - 1], curr = words[i];
            int len = Math.min(prev.length(), curr.length());
            if (prev.length() > curr.length() && prev.startsWith(curr)) return "";   // egde case: "abc" is before "ab" => invalid
            for (int j = 0; j < len; j++) {
                char c1 = prev.charAt(j), c2 = curr.charAt(j);
                if (c1 != c2) {
                    g[c1 - 'a'].add(c2 - 'a');
                    break;
                }
            }
        }
        sb = new StringBuilder();
        visited = new int[26];
        Arrays.fill(visited, -1);
        for (String word : words) {
            for (char c : word.toCharArray()) {
                visited[c - 'a'] = 0;
            }
        }
        for (int i = 0; i < 26; i++) {
            if (visited[i] == 0) {
                if(!dfs(i)) return "";
            }
        }
        return sb.reverse().toString();
    }
    
    private boolean dfs(int u) {
        visited[u] = 1;
        for (int v : g[u]) {
            if (visited[v] == 0) {
                if(!dfs(v)) return false;
            } else if (visited[v] == 1) return false;
        }
        sb.append((char)('a' + u));
        visited[u] = 2;
        return true;
    }
}
```

T: O(n*len)			S: O(1)

