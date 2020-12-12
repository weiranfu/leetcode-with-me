---
title: Hard | Data Stream as Disjoint Intervals 352
tags:
  - common
  - tricky
categories:
  - Leetcode
  - TreeMap
date: 2020-06-26 21:02:37
---

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?

[Leetcode](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

<!--more-->

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

```
[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
```

---

#### Tricky 

* HashMap 

  Let's consider Interval `[ start, end ]` with length `len`,
  we save two end points into map: `map.put(start, len)` and `map.put(end, len)`
  When we add a new element into map, try to merge with its neighbors.

  add(): O(1)			getIntervals(): O(nlogn)

* TreeMap

  Let's consider Interval `[ start, end ]` with length `len`,

  we save start point into map: `map.put(start, end)`

  When we add a new element into map, we use `lowerKey()` and `higherKey()` to find its neighbor intervals and try to merge with them.

  add(): O(logn)	  getIntervals(): O(n)

  Since we only keep intervals in map rather than every points in map in HashMap solution, it will much faster in `getIntervals()`.

---

#### HashMap

```java
class SummaryRanges {
    
    Map<Integer, Integer> map = new HashMap<>();
    
    public void addNum(int val) {
        if (!map.containsKey(val)) {
            int left = map.containsKey(val - 1) ? map.get(val - 1) : 0;               // get left neighbor's length
            int right = map.containsKey(val + 1) ? map.get(val + 1) : 0;           // get right neighbor's length
            int sum = left + 1 + right;
            map.put(val, sum);
            if (left != 0) {
                map.put(val - left, sum);
            }
            if (right != 0) {
                map.put(val + right, sum);
            }
        }
    }
    
    public int[][] getIntervals() {
        List<int[]> list = new ArrayList<>();
        List<Integer> keys = new ArrayList<>(map.keySet());
        Collections.sort(keys);
        int end = -1;
        for (int i = 0; i < keys.size(); i++) {
            int key = keys.get(i);
            if (key > end) {                                       // find a new interval
                end = key + map.get(key) - 1;
                list.add(new int[]{key, end});
            }
        }
        int[][] res = new int[list.size()][2];
        for (int i = 0; i < res.length; i++) {
            res[i] = list.get(i);
        }
        return res;
    }
}
```

add(): O(1)

getIntervals(): O(nlogn)

---

#### TreeMap

```java
class SummaryRanges {

    TreeMap<Integer, Integer> map = new TreeMap<>();
    
    public void addNum(int val) {
        if (map.containsKey(val)) return;
        Integer l = map.lowerKey(val);
        Integer h = map.higherKey(val);
        if (l != null && h != null && map.get(l) + 1 == val && val + 1 == h) {
            map.put(l, map.get(h));
            map.remove(h);
        } else if (l != null && map.get(l) + 1 >= val) {
            map.put(l, Math.max(map.get(l), val));
        } else if (h != null && val + 1 == h) {
            map.put(val, map.get(h));
            map.remove(h);
        } else {
            map.put(val, val);
        }
    }
    
    public int[][] getIntervals() {
        List<int[]> list = new ArrayList<>();
        for (int key : map.keySet()) {
            list.add(new int[]{key, map.get(key)});
        }
        int[][] res = new int[list.size()][2];
        for (int i = 0; i < res.length; i++) {
            res[i] = list.get(i);
        }
        return res;
    }
}
```

add(): O(logn)

getIntervals: O(n)

