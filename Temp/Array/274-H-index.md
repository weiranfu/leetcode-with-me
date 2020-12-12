---
title: Medium | H-index 274
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - Array
date: 2019-07-21 11:19:07
---

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): "A scientist has index *h* if *h* of his/her *N* papers have **at least** *h* citations each, and the other *N − h* papers have **no more than** *h*citations each."

[Leetcode](https://leetcode.com/problems/h-index/)

<!--more-->

**Example:**

```
Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
```

**Note:** If there are several possible values for *h*, the maximum one is taken as the h-index.

---

#### Tricky 

This is a bucket sort problem. **If we care about how many times an item in array shows up, we could create a bucket array to record the times an item shows up. This bucket works like a hashmap.** 

H-index means h papers have at least h citations. Assume `n` is the total number of papers, so `h <= n`. 

We create `n+1` buckets, from `0` to `n`. **The index of bucket array corresponds to the sitations of a paper.** e.g. If a paper has 5 citations, then `bucket[5]++`.

We try to find the maximum h, so iterate from back to the front of the bucket array to find h (h <= n), whenever the total count exceeds the index of the bucket, `count >= i`, **meaning that we have the index number of papers that have reference greater than or equal to the index(citations), which will be our h-index result. **

#### Corner case 

**Find h papers in N papers which have at least h citations, there could be more than h papers have h citations.** (index *h* means if *h* of his/her *N* papers have **at least** *h* citations each, and the other *N − h* papers have **no more than** *h*citations each.) **There're two at least in this definition: At least h papers have at least h citations.** It's easy to miss this information.

e.g. citations = [3, 4, 4, 3, 1]. If 4 of total 5 papers have citations larger than or equal to 3, then h-index is 3. 

---

#### My thoughts 

Fail to solve.

---

#### First solution 

If citations is greater than total number of papers, use largerNum to count them. Their citations certainly larger than h-index.

```java
class Solution {
    public int hIndex(int[] citations) {
        int largerNum = 0;
        int count;
        int[] bucket = new int[citations.length + 1];
        for (int i = 0; i < citations.length; i += 1) {
            if (citations[i] <= citations.length) {
                bucket[citations[i]] += 1;            // throw it into the bucket.
            } else {
                largerNum += 1;
            }
        }
        count = largerNum;
        for (int i = bucket.length - 1; i >= 0; i -= 1) {
            count += bucket[i];
            if (count >= i) {
                return i;
            }
        }
        return 0;
    }
}
```

T: O(n), S:(n)

---

#### Optimized 

For any paper with larger number of reference than `n`, we could put in the `n`-th bucket.

```java
class Solution {
    public int hIndex(int[] citations) {
        int count = 0;
        int[] bucket = new int[citations.length + 1];
        for (int i = 0; i < citations.length; i += 1) {
            if (citations[i] <= citations.length) {
                bucket[citations[i]] += 1;            // throw it into the bucket.
            } else {
                bucket[bucket.length - 1] += 1;      // throw into last bucket.
            }
        }
        for (int i = bucket.length - 1; i >= 0; i -= 1) {
            count += bucket[i];
            if (count >= i) {
                return i;
            }
        }
        return 0;
    }
}
```

T: O(n), S:O(n)

---

#### Summary 

**If you want to record how many times an item in an array shows up, using bucket array (hashmap)!**

