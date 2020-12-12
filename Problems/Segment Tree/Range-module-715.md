---
title: Hard | Range Module 715
tags:
  - tricky
categories:
  - Leetcode
  - Segment Tree
date: 2020-06-16 15:08:17
---

A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

`addRange(int left, int right)` Adds the half-open interval `[left, right)`, tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval `[left, right)` that are not already tracked.

`queryRange(int left, int right)` Returns true if and only if every real number in the interval `[left, right)` is currently being tracked.

`removeRange(int left, int right)` Stops tracking every real number currently being tracked in the interval `[left, right)`.

[Leetcode](https://leetcode.com/problems/range-module/)

<!--more-->

**Example 1:**

```
addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
```

**Note:**

A half open interval `[left, right)` denotes all real numbers `left <= x < right`.

`0 < left < right < 10^9` in all calls to `addRange, queryRange, removeRange`.

The total number of calls to `addRange` in a single test case is at most `1000`.

The total number of calls to `queryRange` in a single test case is at most `5000`.

The total number of calls to `removeRange` in a single test case is at most `1000`.

---

#### Tricky 

* Segment Tree: use `boolean status` to control whether this interval is covered.

  Mind `pushUp()` and `pushDown()` functions.

  If we want to add smaller interval and the whole interval is covered, we must return immediately.

  When we query a smaller interval and the whole interval is true, we must return true immediately.

  When we add a whole interval, we need to reset its children to null.

  When we remove a whole interval, we need to reset its children to null.

* Brute Force: Use a list to store all intervals. 

  Find a right place to insert new interval in order to keep sorted.

  `add()` and `remove()` will take O(n) to find a place a add or remove an interval.

  `query()` will use binary search to find a overlapped interval.

* TreeMap

  In order to find overlapped ranges more effiently, we could use TreeMap to store left as key, right as value.

  TreeMap can sort the intervals.

---

#### Segment Tree

```java
class RangeModule {
    
    class Node {
        int start;
        int end;
        boolean cover;
        Node left;
        Node right;
        public Node(int s, int e) {
            start = s;
            end = e;
        }
    }
    
    Node root;

    public RangeModule() {
        root = new Node(0, (int)1e9);
    }
  	
  	public void addRange(int left, int right) {
        update(root, left, right - 1, true);
    }
    
    public boolean queryRange(int left, int right) {
        return query(root, left, right - 1);
    }
    
    public void removeRange(int left, int right) {
        update(root, left, right - 1, false);
    }
    
    private void pushUp(Node node) {
        node.cover = node.left.cover && node.right.cover;
    }
    
    private void pushDown(Node node) {
        int mid = node.start + (node.end - node.start) / 2;
        
        if (node.left == null) {                     // create new children
            node.left = new Node(node.start, mid);
            node.right = new Node(mid + 1, node.end);
        }
        if (node.cover) {                           // if cover, push down
            node.left.cover = true;
            node.right.cover = true;
        }
    }
    
    private void update(Node node, int L, int R, boolean b) {
        if (L <= node.start && node.end <= R) {
            node.cover = b;
            node.left = null;                           // remove children
            node.right = null;
            return;
        }
        
        if (b && node.cover) return;                 // stops smaller range add
        
        int mid = node.start + (node.end - node.start) / 2;
        
        pushDown(node);
        
        if (mid >= L) update(node.left, L, R, b);
        if (mid < R) update(node.right, L, R, b);
        
        pushUp(node);
    }
    
    private boolean query(Node node, int L, int R) {
        if (L <= node.start && node.end <= R) {
            return node.cover;
        }
        
        if (node.cover) return true;                    // stops smaller range query
        
        int mid = node.start + (node.end - node.start) / 2;
        if (node.left == null) {
            return node.cover;
        }
        boolean ans = true;
        if (mid >= L) ans = ans && query(node.left, L, R);
        if (mid < R) ans = ans && query(node.right, L, R);
        return ans;
    }
}
```

T: O(logn)			S: O(n)

---

#### List + Binary Search 

Find a right place to insert new interval in order to keep sorted.

`add()` and `remove()` will take O(n) to find a place a add or remove an interval.

`query()` will use binary search to find a overlapped interval.

```java
class RangeModule {
    class Pair {
        int start;
        int end;
        public Pair(int s, int e) {
            start = s;
            end = e;
        }
    }
    
    List<Pair> ranges;

    public RangeModule() {
        ranges = new ArrayList<>();
    }
    
    public void addRange(int left, int right) {
        List<Pair> newRanges = new ArrayList<>();
        
        boolean inserted = false;
        for (Pair p : ranges) {
            if (p.end < left) {
                newRanges.add(p);
            } else if (p.start <= right) {
                left = Math.min(left, p.start);
                right = Math.max(right, p.end);
            } else {
                if (!inserted) {
                    newRanges.add(new Pair(left, right));
                    inserted = true;
                }
                newRanges.add(p);
            }
        }
        if (!inserted) {
            newRanges.add(new Pair(left, right));
        }
        
        ranges = newRanges;
    }
    
    public boolean queryRange(int left, int right) {
        int l = 0, r = ranges.size();
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (ranges.get(mid).end < left) {
                l = mid + 1;
            } else if (ranges.get(mid).start >= right) {
                r = mid;
            } else {
                return ranges.get(mid).start <= left && ranges.get(mid).end >= right;
            }
        }
        return false;
    }
    
    public void removeRange(int left, int right) {
        List<Pair> newRanges = new ArrayList<>();
        for (Pair p : ranges) {
            if (p.end <= left || p.start >= right) {
                newRanges.add(p);
            } else {
                if (p.start < left) {
                    newRanges.add(new Pair(p.start, left));
                }
                if (p.end > right) {
                    newRanges.add(new Pair(right, p.end));
                }
            }
        }
        ranges = newRanges;
    }
}
```

`add(), remove()`  O(n)

`remove()` O(logn)

---

#### TreeMap

in `remove()`, we need to change `end` before `start`.

```java
if (end != null && map.get(end) > right) { // we need to change end before start
  map.put(right, map.get(end));          // if start == end
}
if (start != null && map.get(start) > left) {
  map.put(start, left);
}
```

if `start == end`, for example

we have range [1, 10], and we want to remove range[4, 6]

if we modify `start` before `end`,

range will be [1, 4] and we cannot add range [6, 10]

```java
class RangeModule {
    
    TreeMap<Integer, Integer> map;

    public RangeModule() {
        map = new TreeMap<>();
    }
    
    public void addRange(int left, int right) {
        Integer start = map.floorKey(left);            
        Integer end = map.floorKey(right);
        
        if (start != null && map.get(start) >= left) {
            left = start;
        }
        if (end != null && map.get(end) > right) {
            right = map.get(end);
        }
        map.put(left, right);
        
        map.subMap(left, false, right, false).clear(); // clear map from left to right.
    }
    
    public boolean queryRange(int left, int right) {
        Integer start = map.floorKey(left);
        if (start == null) return false;
        return map.get(start) >= right;
    }
    
    public void removeRange(int left, int right) {
        Integer start = map.floorKey(left);
        Integer end = map.floorKey(right);
        
        if (end != null && map.get(end) > right) { // we need to change end before start
            map.put(right, map.get(end));          // if start == end
        }
        if (start != null && map.get(start) > left) {
            map.put(start, left);
        }
        
        map.subMap(left, true, right, false).clear(); // clear map from left to right
    }
}
```

`add()`, `remove()`: O(mlogn)        m is the length of sumMap

`query()`: O(logn)



