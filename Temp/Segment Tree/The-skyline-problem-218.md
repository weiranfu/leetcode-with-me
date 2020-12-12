---
title: Hard | The Skyline Problem 218
tags:
  - tricky
categories:
  - Leetcode
  - Segment Tree
date: 2020-06-18 02:47:34
---

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are **given the locations and height of all the buildings** as shown on a cityscape photo (Figure A), write a program to **output the skyline** formed by these buildings collectively (Figure B).

![Buildings](https://assets.leetcode.com/uploads/2018/10/22/skyline1.png) 

[Leetcode](https://leetcode.com/problems/the-skyline-problem/)

<!--more-->

![Skyline Contour](https://assets.leetcode.com/uploads/2018/10/22/skyline2.png)

The geometric information of each building is represented by a triplet of integers `[Li, Ri, Hi]`, where `Li` and `Ri` are the x coordinates of the left and right edge of the ith building, respectively, and `Hi` is its height. It is guaranteed that `0 ≤ Li, Ri ≤ INT_MAX`, `0 < Hi ≤ INT_MAX`, and `Ri - Li > 0`. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: `[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] `.

The output is a list of "**key points**" (red dots in Figure B) in the format of `[ [x1,y1], [x2, y2], [x3, y3], ... ]` that uniquely defines a skyline. **A key point is the left endpoint of a horizontal line segment**. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:`[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]`.

**Notes:**

- The number of buildings in any input list is guaranteed to be in the range `[0, 10000]`.
- The input list is already sorted in ascending order by the left x position `Li`.
- The output list must be sorted by the x position.
- There must be no consecutive horizontal lines of equal height in the output skyline. For instance, `[...[2 3], [4 5], [7 5], [11 5], [12 7]...]` is not acceptable; the three lines of height 5 should be merged into one in the final output as such: `[...[2 3], [4 5], [12 7], ...]`

---

#### Tricky 

* Segment Tree:

  Store building boundaries in `Line` and scan them from left to right.

  Use `cover` to represent cover times, and `coverL` to represent cover length.

  Compress the coordinations of buildings. Use two map `rank` and `rankToL` to map the relationship between `rank index` and `height`.

  The length in each node is the delta length. 

  `tree[rt].L = (l == 0) ? 0 : rankToL.get(l) - rankToL.get(l - 1);  // delta length`

* Priority Queue

  Scan lines from left to right.

  Store lines' height into pq when it enters and remove its height from pq when it leaves.

  `remove()` takes O(n)

* TreeMap

  In order to reduce `remove` time complexity, we use TreeMap to store `height` as key and cover time as value. 

  If `map.get(height) == 0`, we need to remove this height from TreeMap.

---

#### Segment Tree 

```java
class Solution {
    class Line {
        int x;
        int y;
        boolean in;     // in or out of this line
        public Line(int x, int y, boolean in) {
            this.x = x;
            this.y = y;
            this.in = in;
        }
    }
    class Node {
        int cover;   // cover times
        int L;       // length of this interval
        int coverL;  // cover length of this interval
    }
    
    Map<Integer, Integer> rank;  // coordinations compression
    Map<Integer, Integer> rankToL;// map rank to length
    int rankN;                   // size of rank
    Node[] tree;
    
    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<List<Integer>> res = new ArrayList<>();
        
        rank = new HashMap<>();
        rankToL = new HashMap<>();
        List<Integer> pos = new ArrayList<>();
        
        int n = buildings.length;
        Line[] lines = new Line[n * 2];
        for (int i = 0; i < n; i++) {
            int[] building = buildings[i];
            lines[i * 2] = new Line(building[0], building[2], true);
            lines[i * 2 + 1] = new Line(building[1], building[2], false);
            pos.add(building[2]);
        }
        
        // coordinations compression
        pos = new ArrayList<>(new HashSet<>(pos));
        pos.add(0);                                 // add 0 height
        Collections.sort(pos);
        for (int i = 0; i < pos.size(); i++) {
            rank.put(pos.get(i), i);
            rankToL.put(i, pos.get(i));
        }
        
        // build tree
        rankN = rank.size();
        tree = new Node[rankN << 2];
        for (int i = 0; i < tree.length; i++) {
            tree[i] = new Node();
        }
        build(0, rankN - 1, 0);
        
        // sort lines
        Arrays.sort(lines, (l1, l2) -> l1.x - l2.x);
        
        int i = 0;
        int N = lines.length;
        int preH = 0;
        while (i < N) {
            int X = lines[i].x;
            while (i < N && lines[i].x == X) {       // for a same X position
                if (lines[i].in) {                    // Line in
                    cover(0, rank.get(lines[i].y), 0, rankN - 1, 0);
                } else {                              // Line out
                    unCover(0, rank.get(lines[i].y), 0, rankN - 1, 0);
                }
                i++;
            }
            if (tree[0].coverL != preH) {           // if height changes
                res.add(new ArrayList<>(Arrays.asList(X, tree[0].coverL)));
            }
            preH = tree[0].coverL;
        }
        return res;
    }
    
    private void build(int l, int r, int rt) {
        if (l == r) {
            tree[rt].L = (l == 0) ? 0 : rankToL.get(l) - rankToL.get(l - 1);  // delta length
            return;
        }
        int mid = l + (r - l) / 2;
        build(l, mid, rt * 2 + 1);
        build(mid + 1, r, rt * 2 + 2);
        
        tree[rt].L = tree[rt * 2 + 1].L + tree[rt * 2 + 2].L;
    }
    
    private void pushUp(int rt) {
        if (tree[rt].cover > 0) {
            tree[rt].coverL = tree[rt].L;
        } else {
            tree[rt].coverL = tree[rt * 2 + 1].coverL + tree[rt * 2 + 2].coverL;
        }
    }
    
    private void cover(int L, int R, int l, int r, int rt) {
        if (L <= l && r <= R) {
            if (tree[rt].cover == 0) {
                tree[rt].coverL = tree[rt].L;
            }
            tree[rt].cover++;
            return;
        }
        int mid = l + (r - l) / 2;
        if (mid >= L) cover(L, R, l, mid, rt * 2 + 1);
        if (mid < R) cover(L, R, mid + 1, r, rt * 2 + 2);
        
        pushUp(rt);
    }
    
    private void unCover(int L, int R, int l, int r, int rt) {
        if (L <= l && r <= R) {
            tree[rt].cover--;
            if (tree[rt].cover == 0) {
                if (l == r) {              // if rt is leaf
                    tree[rt].coverL = 0;
                } else {
                    tree[rt].coverL = tree[rt * 2 + 1].coverL + tree[rt * 2 + 2].coverL;
                }
            }
            return;
        }
        int mid = l + (r - l) / 2;
        if (mid >= L) unCover(L, R, l, mid, rt * 2 + 1);
        if (mid < R) unCover(L, R, mid + 1, r, rt * 2 + 2);
        
        pushUp(rt);
    }
    
}
```

T: O(nlogn)

---

#### Priority Queue

Scan lines from left to right.

Store the height in a priority queue.

When a line enters, we add its height into pq, and when a line leaves, we remove its height from pq.

**We must add a zero height into pq.**

```java
class Solution {
    class Line {
        int x;
        int y;
        boolean in;
        public Line(int x, int y, boolean in) {
            this.x = x;
            this.y = y;
            this.in = in;
        }
    }
    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<List<Integer>> res = new ArrayList<>();
        
        int n = buildings.length;
        Line[] lines = new Line[n * 2];
        for (int i = 0; i < n; i++) {
            int[] building = buildings[i];
            lines[i * 2] = new Line(building[0], building[2], true);
            lines[i * 2 + 1] = new Line(building[1], building[2], false);
        }
        
        Arrays.sort(lines, (l1, l2) -> l1.x - l2.x);
        
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        pq.add(0);                                // add 0 height
        int preH = 0;
        int i = 0;
        int N = lines.length;
        while (i < N) {
            int X = lines[i].x;
            while (i < N && lines[i].x == X) {
                if (lines[i].in) {
                    pq.add(lines[i].y);
                } else {
                    pq.remove(lines[i].y);
                }
                i++;
            }
            if (pq.peek() != preH) {
                res.add(new ArrayList<>(Arrays.asList(X, pq.peek())));
            }
            preH = pq.peek();
        }
        return res;
    }
}
```

T: O(n^2)		The `pq.remove()` takes O(n)

S: O(n)

---

#### TreeMap

Since `pq.remove()` takes O(n), we can use TreeMap to reduce `remove` operation to O(logn).

TreeMap stores the height of line and the times of covering.

If `map.get(height) == 0`, we remove the height from map.

```java
class Solution {
    class Line {
        int x;
        int y;
        boolean in;
        public Line(int x, int y, boolean in) {
            this.x = x;
            this.y = y;
            this.in = in;
        }
    }
    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<List<Integer>> res = new ArrayList<>();
        
        int n = buildings.length;
        Line[] lines = new Line[n * 2];
        for (int i = 0; i < n; i++) {
            int[] building = buildings[i];
            lines[i * 2] = new Line(building[0], building[2], true);
            lines[i * 2 + 1] = new Line(building[1], building[2], false);
        }
        
        Arrays.sort(lines, (l1, l2) -> l1.x - l2.x);
        
        TreeMap<Integer, Integer> map = new TreeMap<>((a, b) -> b - a);
        map.put(0, 0);                                // add 0 height
        int preH = 0;
        int i = 0;
        int N = lines.length;
        while (i < N) {
            int X = lines[i].x;
            while (i < N && lines[i].x == X) {
                if (lines[i].in) {
                    map.put(lines[i].y, map.getOrDefault(lines[i].y, 0) + 1);
                } else {
                    map.put(lines[i].y, map.getOrDefault(lines[i].y, 0) - 1);
                    if (map.get(lines[i].y) == 0) {     // all lines leave
                        map.remove(lines[i].y);
                    }
                }
                i++;
            }
            if (map.firstKey() != preH) {
                res.add(new ArrayList<>(Arrays.asList(X, map.firstKey())));
            }
            preH = map.firstKey();
        }
        return res;
    }
}
```

T: O(logn)		S: O(n)



