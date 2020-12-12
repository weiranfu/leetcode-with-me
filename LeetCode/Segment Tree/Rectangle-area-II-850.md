---
title: Hard | Rectangle Area II 850
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Segment Tree
date: 2020-10-04 21:00:31
---

We are given a list of (axis-aligned) `rectangles`.  Each `rectangle[i] = [x1, y1, x2, y2] `, where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the `i`th rectangle.

Find the total area covered by all `rectangles` in the plane.  Since the answer may be too large, **return it modulo 10^9 + 7**.

![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png)

[Leetcode](https://leetcode.com/problems/rectangle-area-ii/)

<!--more-->

**Example 1:**

```
Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
```

**Example 2:**

```
Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
```

**Note:**

- `1 <= rectangles.length <= 200`
- `rectanges[i].length = 4`
- `0 <= rectangles[i][j] <= 10^9`
- The total area covered by all rectangles will never exceed `2^63 - 1` and thus will fit in a 64-bit signed integer.

---

#### Brute Force (Sweep Line) 

Use TreeMap to store intervals and merge intervals during sweeping lines of same x.

**Note that TreeMap uses compareTo instead of hashCode for containsKey/get/remove operations**

```java
class Solution {
    public int rectangleArea(int[][] rectangles) {
        int mod = (int)1e9 + 7;
        List<int[]> lines = new ArrayList<>();
        for (int[] rectangle : rectangles) {
            int x1 = rectangle[0], y1 = rectangle[1];
            int x2 = rectangle[2], y2 = rectangle[3];
            int[] line1 = new int[]{x1, y1, y2, 1};
            int[] line2 = new int[]{x2, y1, y2, 0};
            lines.add(line1);
            lines.add(line2);
        }
        Collections.sort(lines, (a, b) -> a[0] - b[0]);
        // int[] -> {y1, y2}
        // TreeMap uses compareTo instead of hashCode for containsKey/get/remove operations
        TreeMap<int[], Integer> map = new TreeMap<>((a, b) -> {
            if (a[0] != b[0]) return a[0] - b[0];
            else return a[1] - b[1];
        });
        
        long area = 0;
        int preX = -1;
        int i = 0, N = lines.size();
        while (i < N) {
            int X = lines.get(i)[0];
            long sumY = 0;
            int s = -1, curr = -1;
            for (int[] range : map.keySet()) {     // merge intervals
                if (range[0] > curr) {
                    if (s != -1) sumY += curr - s;
                    curr = range[1];
                    s = range[0];
                } else {
                    curr = Math.max(curr, range[1]);
                }
            }
            if (s != -1) sumY += curr - s;
            if (preX != -1) area = (area + sumY * (X - preX)) % mod;
            preX = X;
            while (i < N && lines.get(i)[0] == X) {
                int[] line = lines.get(i++);
                int y1 = line[1], y2 = line[2], in = line[3];
                int[] interval = new int[]{y1, y2};
                if (in == 1) {
                    map.put(interval, map.getOrDefault(interval, 0) + 1);
                } else {
                    map.put(interval, map.get(interval) - 1);
                    if (map.get(interval) == 0) map.remove(interval);
                }
            }
        }
        return (int)area;
    }
}
```

T: O(n^2)			S: O(n)

---

#### Segment Tree

We can use segment tree to sweep line.

**Note that the length of interval is the delta of two positions, `length = pos.get(r + 1) - pos.get(l)`**

Then `tree[rt].coverL = tree[rt * 2].coverL + tree[rt * 2 + 1]`

So when we want to add a new interval `[l, r]`, we need to add `update(l, r - 1)`

```java
class Solution {
    class Node {
        int cover; // cover times
        int coverL;// cover length
    }
    
    int N;
    List<Integer> pos;
    Node[] tree;
    int mod = (int)1e9 + 7;
    
    public int rectangleArea(int[][] rectangles) {
        List<int[]> lines = new ArrayList<>();
        pos = new ArrayList<>();
        for (int[] rectangle : rectangles) {
            int x1 = rectangle[0], y1 = rectangle[1];
            int x2 = rectangle[2], y2 = rectangle[3];
            int[] line1 = new int[]{x1, y1, y2, 1};
            int[] line2 = new int[]{x2, y1, y2, 0};
            lines.add(line1);
            lines.add(line2);
            pos.add(y1);
            pos.add(y2);
        }
        pos = new ArrayList<>(new HashSet<>(pos));
        Collections.sort(pos);
        N = pos.size();
        
        tree = new Node[N << 2];
        for (int i = 0; i < tree.length; i++) tree[i] = new Node();
        
        Collections.sort(lines, (a, b) -> a[0] - b[0]);
        long area = 0;
        int preX = -1;
        int i = 0, n = lines.size();
        while (i < n) {
            int X = lines.get(i)[0];
            if (preX != -1) area = (area + (long)tree[1].coverL * (X - preX)) % mod;
            preX = X;
            while (i < n && lines.get(i)[0] == X) {
                int[] line = lines.get(i++);
                int y1 = line[1], y2 = line[2], in = line[3];
                int Y1 = find(y1), Y2 = find(y2);
                if (in == 1) {
                    update(Y1, Y2 - 1, 1, N, 1, 1);   // index is [Y1, Y2 - 1]
                } else {
                    update(Y1, Y2 - 1, 1, N, 1, -1);  
                }
            }
        }
        return (int)area;
    }
    
    private void pushUp(int l, int r, int rt) {
        if (tree[rt].cover > 0) {
            tree[rt].coverL = pos.get(r) - pos.get(l - 1);
        } else {
            if (l == r) tree[rt].coverL = 0;
            else tree[rt].coverL = tree[rt * 2].coverL + tree[rt * 2 + 1].coverL;
        }
    }
    
    private void update(int L, int R, int l, int r, int rt, int c) {
        if (L <= l && r <= R) {
            tree[rt].cover += c;
            pushUp(l, r, rt);
            return;
        }
        int mid = l + (r - l) / 2;
        if (mid >= L) update(L, R, l, mid, rt * 2, c);
        if (mid < R) update(L, R, mid + 1, r, rt * 2 + 1, c);
        pushUp(l, r, rt);
    }
    
    private int find(int x) {
        int l = 0, r = N - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (pos.get(mid) == x) return mid + 1;
            else if (pos.get(mid) < x) l = mid + 1;
            else r = mid - 1;
        }
        return -1;
    }
}
```

T: O(nlogn)			S: O(n)  



