---
title: Medium | People Whose List of Favorite Companies is Not a Subset of Another List
tags:
  - tricky
categories:
  - Leetcode
  - Set
date: 2020-05-18 15:56:01
---

Given the array `favoriteCompanies` where `favoriteCompanies[i]` is the list of favorites companies for the `ith` person (**indexed from 0**).

Return the indices of people whose list of favorite companies is not a **subset** of any other list of favorites companies. You must return the indices in increasing order.

[Leetcode](https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/)

<!--more-->

**Example 1:**

```
Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
Output: [0,1,4] 
Explanation: 
Person with index=2 has favoriteCompanies[2]=["google","facebook"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] corresponding to the person with index 0. 
Person with index=3 has favoriteCompanies[3]=["google"] which is a subset of favoriteCompanies[0]=["leetcode","google","facebook"] and favoriteCompanies[1]=["google","microsoft"]. 
Other lists of favorite companies are not a subset of another list, therefore, the answer is [0,1,4].
```

**Example 2:**

```
Input: favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
Output: [0,1] 
Explanation: In this case favoriteCompanies[2]=["facebook","google"] is a subset of favoriteCompanies[0]=["leetcode","google","facebook"], therefore, the answer is [0,1].
```

---

#### Tricky 

- **To check whether a set is a subset of another set, the easiest way is **

  `set1.contailsAll(set2)`. then `set2` is a subset of `set1`.

- When we want to break / continue the outer loop, we could use `break outer`, `continue outer`.

  ```java
  outer:
  for (int i = 0; i < n; i++) {
  	for (int j = 0; j < n; j++) {
  		if (condition) {
  			continue outer;
  		}
  	}
  }
  ```

---

#### My thoughts 

Brute force. Convert List of companies into a set. And check whether each set is a subset of another set.

---

#### First solution 

```java
class Solution {
    public List<Integer> peopleIndexes(List<List<String>> favoriteCompanies) {
        List<Integer> res = new ArrayList<>();
        if (favoriteCompanies == null || favoriteCompanies.size() == 0) return res;
        int size = favoriteCompanies.size();
        Set<String>[] sets = new Set[size];
        for (int i = 0; i < size; i++) {
            sets[i] = new HashSet<>(favoriteCompanies.get(i));
        }
        outer:
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (i != j && sets[j].containsAll(sets[i])) {
                    continue outer;
                }
            }
            res.add(i);
        }
        return res;
    }
}
```

Let
m = favoriteCompanies.size(),
a = average size of all companies list
b = average size of company names.

There needs `O(m * a * b)` time and O(m * a) space to create all sets, and there are `O(m ^ 2)` iterations due to the nested for loops, and each check for subset relation cost time `O(a)`. Therefore:

Time: `O(m * a * (m + b))`, space: `O(m * a)`.

---

#### Union Find

Typical union-find
for example:
`favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]`

it is actually a graph, each list of companies is a node.

```
	{lgf}     {gm}    {a}
    |  
  {gf}
	  |
	 {g}
```

with path compression, the root of each node can be found faster:

```
	{lgf}     {gm}    {a}
	/   \
 {gf}  {g}
```

In the end, we just need to return the index of the three roots of the graph.

```java
class Solution {
    public List<Integer> peopleIndexes(List<List<String>> favoriteCompanies) {
        List<Integer> res = new ArrayList<>();
        if (favoriteCompanies == null || favoriteCompanies.size() == 0) return res;
        int size = favoriteCompanies.size();
        Set<String>[] sets = new Set[size];
        for (int i = 0; i < size; i++) {
            sets[i] = new HashSet<>(favoriteCompanies.get(i));
        }
        int[] uf = new int[size];
        for (int i = 0; i < size; i++) {
            uf[i] = i;
        }
        for (int i = 0; i < size; i++) {
            for (int j = i + 1; j < size; j++) {
                int a = find(i, uf);
                int b = find(j, uf);
                if (a == b) continue;
                else if (sets[a].containsAll(sets[b])) {
                    uf[b] = a;
                } else if (sets[b].containsAll(sets[a])) {
                    uf[a] = b;
                }
            }
        }
        for (int i = 0; i < size; i++) {
            if (uf[i] == i) {
                res.add(i);
            }
        }
        return res;
    }
    private int find(int i, int[] uf) {
        while (uf[i] != i) {
            uf[i] = uf[uf[i]];
            i = uf[i];
        }
        return i;
    }
}
```

T: O(n^2)			S: O(n)