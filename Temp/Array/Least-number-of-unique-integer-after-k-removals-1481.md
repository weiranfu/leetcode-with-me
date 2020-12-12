---
title: Medium | Least Number of Unique Integer after K Removals 1481
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-06-14 17:30:51
---

Given an array of integers `arr` and an integer `k`. Find the *least number of unique integers* after removing **exactly** `k` elements**.**

[Leetcode](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/)

<!--more-->

**Example 1:**

```
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
```

Example 2:

```
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
```

---

#### Tricky 

We need to sort map count by values. (TreeMap can only sort by key not values.)

---

#### First solution 

Collections.sort() on map.values()

```java
class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : arr) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        List<Integer> list = new ArrayList<>();
        list.addAll(map.values());              // add all values.
        Collections.sort(list);                 // sort by values.
        int count = 0;                          // count removals.
        while (k > 0) {
            k -= list.get(count);
            count++;
        }
        if (k < 0) count--;
        return list.size() - count;
    }
}
```

T: O(nlogn)			S: O(n)

---

#### Optimized

Use `int[] occurrence` to store the occurrence since max occurrence < arr.length.

From small to big, deduct from `k` the multiplication with the number of elements of same occurrence, check if reaching `0`, then deduct the correponding unique count `remaining`.

```java
class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        int n = arr.length;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : arr) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        int[] count = new int[n + 1];   // count occurrence
        for (int v : map.values()) {
            count[v]++;
        }
        int res = map.size();
        int occur = 1;                 // least occurrence.
        while (k > 0) {
            int cnt = count[occur];
            if (k - cnt * occur <= 0) {
                res -= k / occur;        // try to deduct on same key.
                break;
            }
            k -= cnt * occur;
            res -= cnt;
            occur++;
        }
        return res;
    }
}
```

T: O(n)			S: O(n)



