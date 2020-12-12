---
title: Easy | Reorder Data in Log Files 937
tags:
  - tricky
categories:
  - Leetcode
  - Sort
date: 2019-12-03 23:38:57
---

You have an array of `logs`.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric *identifier*.  Then, either:

- Each word after the identifier will consist only of lowercase letters, or;
- Each word after the identifier will consist only of digits.

We will call these two varieties of logs *letter-logs* and *digit-logs*.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

[Leetcode](https://leetcode.com/problems/reorder-data-in-log-files/)

<!--more-->

**Example 1:**

```
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
```

**Constraints:**

1. `0 <= logs.length <= 100`
2. `3 <= logs[i].length <= 100`
3. `logs[i]` is guaranteed to have an identifier, and a word after the identifier.

---

#### Tricky 

* How to create comparator for Arrays.sort or Collections.sort

* When it comes to Java, the `Arrays.sort()` has two methods to sort an array.

  **It uses dual-pivot quicksort for primitives,** *which though better than a standard quicksort* **could still degrade into a quadratic running time.**

  For non-primitive types, it uses TimSort, *essetially a hybrid of merge sort and insertion sort, which makes it adapt to the test cases with a worst case run-time of* Θ(𝑛log𝑛)

  For that reason, *whenever you need a sorted array, it’s better to use a non-primitive if your array is huge and may contain* **nearly sorted sequences.**

---

#### My thoughts 

Create a comparator for sort logs.

---

#### Standard solution 

```java
class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Comparator<String> myComparator = new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                int i = s1.indexOf(" ");
                int j = s2.indexOf(" ");
                char c1 = s1.charAt(i + 1);
                char c2 = s2.charAt(j + 1);
                if (Character.isDigit(c1) && Character.isDigit(c2)) return 0;
                else if (Character.isDigit(c1)) return 1;
                else if (Character.isDigit(c2)) return -1;
                else {
                    String subS1 = s1.substring(i + 1);
                    String subS2 = s2.substring(j + 1);
                    int cmp = subS1.compareTo(subS2);
                    if (cmp == 0) {
                        cmp = s1.substring(0, i).compareTo(s2.substring(0, j));
                    }
                    return cmp;
                }
            }
        };
        Arrays.sort(logs, myComparator);
        return logs;
    }
}
```

T: O(n*logn) S: O(1)

---

#### Summary 

* For Primitive type, Collections#sort uses quicksort(). Time complexity is O(n*logn)
* For Non-primitive type, Collections#sort uses Timsort(), a hybrid of merge sort and insertion sort. Time complexity is O(n*logn). When N < 15, it will switch from merge sort to insertion sort.