---
title: Medium | H-index-II 275
tags:
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2019-07-21 20:01:09
---

Given an array of citations **sorted in ascending order** (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): "A scientist has index *h* if *h* of his/her *N* papers have **at least** *h* citations each, and the other *N − h* papers have **no more than** *h* citations each."

[Leetcode](https://leetcode.com/problems/h-index-ii/)

<!--more-->

**Example:**

```
Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
```

**Note:**

If there are several possible values for *h*, the maximum one is taken as the h-index.

**Follow up:**

- This is a follow up problem to [H-Index](https://aranne.github.io/2019/07/21/274-H-index/), where `citations` is now guaranteed to be sorted in ascending order.
- Could you solve it in logarithmic time complexity?

---

#### Tricky 

The target varies during binary search.

---

#### Standard solution 

```java
class Solution {
    public int hIndex(int[] citations) {
        if (citations == null || citations.length == 0) return 0;
        int n = citations.length;
        int l = 0, r = n;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (citations[mid] >= n - mid) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return n - l;
    }
}
```

T: O(logn), S:O(1)

---

#### Summary 

To search total count in a unsorted array, we use bucket sort to get count in O(n), like in Problem H-index 274.

To search total count in a sorted array, we use binary search because count can be got if we know the index.