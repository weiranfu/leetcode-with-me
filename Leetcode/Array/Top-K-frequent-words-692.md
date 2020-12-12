---
title: Medium | Top K Frequent Words 692
tags:
  - common
categories:
  - Leetcode
  - Array
date: 2020-01-01 21:36:52
---

Given a non-empty list of words, return the *k* most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

[Leetcode](https://leetcode.com/problems/top-k-frequent-words/)

<!--more-->

**Example 1:**

```
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
```

**Example 2:**

```
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
```

**Note:**

1. You may assume *k* is always valid, 1 ≤ *k* ≤ number of unique elements.
2. Input words contain only lowercase letters.

---

#### My thoughts 

Use a priority queue to store top k frequency strings.

Use a map to store frequency of each string.

---

#### First solution 

When we define the Comparator for priority queue, we can use Map outside of the function. 

```java
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> count = new HashMap<>();
        for (String word : words) {
            count.put(word, count.getOrDefault(word, 0) + 1);
        }
        PriorityQueue<String> pq = new PriorityQueue<>((s1, s2) -> {
            if (count.get(s1) != count.get(s2)) {
                return count.get(s1) - count.get(s2);
            } else {
                return s2.compareTo(s1);
            }
        });
        for (String word : count.keySet()) {
            pq.offer(word);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        List<String> res = new ArrayList<>();
        while (!pq.isEmpty()) {
            res.add(pq.poll());
        }
        Collections.reverse(res);
        return res;
    }
}
```

T: O(n*logK) 			S: O(n)

---

#### Bucket Sort

Beacause there're N strings, the frequency of each string should between 1 and N.

So we could create N buckets corresponding the frequency.

And iterate buckets backwards to get top K strings.

```java
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        int n = words.length;
        Map<String, Integer> map = new HashMap<>();
        for(String word : words) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        int N = map.size();
        int size = n - N + 1;  // max possible occurrence of a word
        List<String>[] buckets = new List[size + 1];
        for (int i = 0; i <= size; i++) buckets[i] = new ArrayList<String>();
        for (String word : map.keySet()) {
            buckets[map.get(word)].add(word);
        }
        // Sort each bucket.
        for (List<String> bucket : buckets) {
            Collections.sort(bucket);
        }
        // get k frequent words
        List<String> res = new LinkedList<>();
        for (int i = size; i >= 0; i--) {
            for (String s : buckets[i]) {
                res.add(s);
                if (res.size() == k) {
                    return res;
                }
            }
        }
        return res;
    } 
}
```

T: O(n + m + n(log(n/m)))  m is num of buckets

S: O(n + m)

---

#### Summary 

Use buckets to store items according to its frequency.

Sort bucket can use `Collections.sort` or `Trie`. 