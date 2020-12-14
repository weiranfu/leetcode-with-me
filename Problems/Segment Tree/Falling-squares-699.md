---
title: Hard | Falling Squares 699
tags:
  - tricky
categories:
  - Leetcode
  - Segment Tree
date: 2020-06-17 17:33:16
---

On an infinite number line (x-axis), we drop given squares in the order they are given.

The `i`-th square dropped (`positions[i] = (left, side_length)`) is a square with the left-most point being `positions[i][0]` and sidelength `positions[i][1]`.

The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently landed squares. We wait for each square to stick before dropping the next.

The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch (either the number line or another square). Squares dropped adjacent to each other will not stick together prematurely.

Return a list `ans` of heights. Each height `ans[i]` represents the current highest height of any square we have dropped, after dropping squares represented by `positions[0], positions[1], ..., positions[i]`.

[Leetcode](https://leetcode.com/problems/falling-squares/)

<!--more-->

**Example 1:**

```
Input: [[1, 2], [2, 3], [6, 1]]
Output: [2, 5, 5]
Explanation:
```

![](https://cdn.jsdelivr.net/gh/weiranfu/image-hosting@main/img/leetcode/falling-squares-699.png)

---

#### Tricky 

* Segment Tree.

  We need to compress the coordinations of squares. So we have to discretize the input coordinations.

  For example, a square [x1 = 1, y1 = 2, h = 2], another square [x2 = 2, y2 = 4, h = 4].

  ​													  XXXXXXXXXXXXX

  ​													  XXXXXXXXXXXXX

  ​		        height = 2    XXXXXX   XXXXXXXXXXXXX   height = 4

  ​									  XXXXXX   XXXXXXXXXXXXX

  index ———0 ———1——— 2——— 3 ———4

  **If we want to update two squares [1, 2] and [2, 4], it looks like that two squares stick to each other, they both use point `2` **.

  However, the problem says: "Squares dropped adjacent to each other will not stick together prematurely."

  **So we have to represent a square `[x, y]` using point `x, x + 1, ..., y - 1`**

  Square[1, 2] uses point `1`. Square[2, 4] uses point `2` and `3`.

  So we add `square[0]` and `square[0] + square[1] - 1` as two edges into list.

  总的来说，就是加入这个square的时候，右边界要减1. 因为当两个square相邻的时候，相邻点是不能算成有覆盖的。

  Since the range of square's coordinations is huge, we need to compress the coordination, known as discretizing coordinations.

  [离散化坐标](https://blog.csdn.net/zezzezzez/article/details/80230026)

  离散化有特殊情况，如果本身不相邻的两个square离散化后相邻了，可能parent节点产生影响。

  通常在两个值相差1的点中间插入一个新点来避免此情况。

  1. Add square edge into list.
  2. remove duplicates
  3. sort
  4. map original edge into **new index in list + 1**. (using binary search)

  ```java
  private Map<Integer, Integer> coorCompression(int[][] positions) {
          Map<Integer, Integer> rank = new HashMap<>();
          List<Integer> pos = new ArrayList<>();
          for (int[] square : positions) {
              pos.add(square[0]);
              pos.add(square[0] + square[1] - 1);      // represent square x,x+1,..,y-1
          }
          pos = new ArrayList<>(new HashSet<>(pos));  // remove duplicates
          Collections.sort(pos);                      // sort
          for (int i = 0; i < pos.size(); i++) {
              rank.put(pos.get(i), i);                // map to new index
          }
          return rank;
      }
  ```

  Using map to build the segment tree. `N = map.size()`

  `Node[] tree = new Node[N<<2]`            The size of tree node is `4 * N`

  **Before we add a new square, we need to query the max height `maxH` in that range, then update all node's height to `maxH + newH`**

  ```java
  for (int[] square : positions) {
              int x = rank.get(square[0]);
              int y = rank.get(square[0] + square[1] - 1);
              int h = query(x, y, 0, N - 1, 0);          // query max height
              update(x, y, h + square[1], 0, N - 1, 0);  // update to new height
              max = Math.max(max, h + square[1]);
              res.add(max);
          }
  ```

* TreeMap

---

#### Segment Tree

Compress the coordinations since the range of square's coordinations is huge.

**Before we add a new square, we need to query the max height `maxH` in that range, then update all node's height to `maxH + newH`**

```java
class Solution {
    class Node {
        int h;
        int lazy;
    }
    Node[] tree;
    List<Integer> pos;
    int N;
    
    public List<Integer> fallingSquares(int[][] positions) {     
        pos = new ArrayList<>();
        for (int[] square : positions) {
            pos.add(square[0]);
            pos.add(square[0] + square[1] - 1);   // avoid neighbor covering
        }
        pos = new ArrayList<>(new HashSet<>(pos));  // remove duplicates
        Collections.sort(pos);   
        N = pos.size();
        
        tree = new Node[N << 2];
        for (int i = 0; i < tree.length; i++) tree[i] = new Node();
        
        List<Integer> res = new ArrayList<>();
        int max = 0;
        for (int[] square : positions) {
            int x = find(square[0]);
            int y = find(square[0] + square[1] - 1);
            int h = query(x, y, 1, N, 1);
            update(x, y, h + square[1], 1, N, 1);
            max = Math.max(max, h + square[1]);
            res.add(max);
        }
        return res;
    }
    
    private void pushUp(int rt) {
        tree[rt].h = Math.max(tree[rt * 2].h, tree[rt * 2 + 1].h);
    }
    
    private void pushDown(int rt) {
        if (tree[rt].lazy != 0) {
            tree[rt * 2].lazy = tree[rt].lazy;
            tree[rt * 2 + 1].lazy = tree[rt].lazy;
            tree[rt * 2].h = tree[rt].lazy;
            tree[rt * 2 + 1].h = tree[rt].lazy;
            tree[rt].lazy = 0;
        }
    }
    
    private void update(int L, int R, int h, int l, int r, int rt) {
        if (L <= l && r <= R) {
            tree[rt].h = h;
            tree[rt].lazy = h;
            return;
        }
        int mid = l + (r - l) / 2;
        pushDown(rt);
        if (mid >= L) update(L, R, h, l, mid, rt * 2);
        if (mid < R) update(L, R, h, mid + 1, r, rt * 2 + 1);
        pushUp(rt);
    }
    
    private int query(int L, int R, int l, int r, int rt) {
        if (L <= l && r <= R) {
            return tree[rt].h;
        }
        int mid = l + (r - l) / 2;
        pushDown(rt);
        int ans = 0;
        if (mid >= L) ans = Math.max(ans, query(L, R, l, mid, rt * 2));
        if (mid < R) ans = Math.max(ans, query(L, R, mid + 1, r, rt * 2 + 1));
        return ans;
    }
    
    private int find(int x) {
        int l = 0, r = N - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (pos.get(mid) == x) return mid + 1; // return index + 1
            else if (pos.get(mid) < x) l = mid + 1;
            else r = mid - 1;
        } 
        return -1;
    }
}
```

T: O(logn)		S: O(n)

---

#### Brute Force

Keep all intervals in a list.

Everytime we add a new interval, we check the max height in range [l, r], and add a new interval with height `height + maxH` into list.

```java
class Solution {
    class Interval {
        int start;
        int end;
        int height;
        public Interval(int s, int e, int h) {
            start = s;
            end = e;
            height = h;
        }
    }
    
    public List<Integer> fallingSquares(int[][] positions) {
        List<Integer> ans = new ArrayList<>();
        List<Interval> intervals = new ArrayList<>();
        int max = 0;
        for (int[] square : positions) {
            int start = square[0];
            int end = square[0] + square[1];
            int height = square[1];
            int maxH = 0;
            for (Interval interval : intervals) {
                if (interval.start >= end || interval.end <= start) continue;
                maxH = Math.max(maxH, interval.height);
            }
          	int newHeight = maxH + height;
            intervals.add(new Interval(start, end, newHeight));
            max = Math.max(max, newHeight);
            ans.add(max);
        }
        return ans;
    }
}
```

T: O(n^2)			S: O(n)

---

#### TreeMap

[Range Module](https://aranne.github.io/2020/06/16/Range-module-715/#more)

Save `Pair(left, right)` as key and `height` as value into TreeMap.

If we want  to add a new range[left, right].

```
Pair start = map.lowerKey(p1);
Pair end = map.lowerKey(p2);
```

1. Modify the `end` interval if it intersects with `[left, right]`
2. Modify the `start` interval if it intersects with `[left, right]`
3. Seach in `subMap = map.subMap(p1, true, p2, false)` to find max height
4. clear all intervals in range `[left, right]`
5. put new range into map

```java
class Solution {
    class Pair {
        int left;
        int right;
        public Pair(int l, int r) {
            left = l;
            right = r;
        }
        public String toString() {
            return left +","+right;
        }
    }
    public List<Integer> fallingSquares(int[][] positions) {
        List<Integer> res = new ArrayList<>();
        TreeMap<Pair, Integer> map = new TreeMap<>((a, b) -> a.left - b.left);
        int max = 0;
        
        for (int[] square : positions) {
            int left = square[0];
            int right = square[0] + square[1];
            int height = square[1];
            Pair p1 = new Pair(left, 0);
            Pair p2 = new Pair(right, 0);
            
            int maxH = 0;
            Pair start = map.lowerKey(p1);
            Pair end = map.lowerKey(p2);
            
            if (end != null && end.right > right) { // change end before start
                int h = map.get(end);
                int r = end.right;
                maxH = Math.max(maxH, h);       // compare with intersact range
                map.put(new Pair(right, r), h);
            }
            if (start != null && start.right > left) {
                int h = map.get(start);   
                int l = start.left;
                maxH = Math.max(maxH, h);  
                map.put(new Pair(l, left), h);
            }
            
            Map<Pair, Integer> submap = map.subMap(p1, true, p2, false);
            for (Pair key : submap.keySet()) {
                maxH = Math.max(maxH, map.get(key));
            }
            submap.clear();                     // remove intervals in range
            
            int newH = height + maxH;
            map.put(new Pair(left, right), newH);    // put new range
            
            max = Math.max(max, newH);
            res.add(max);
        } 
        return res;
    }
}
```

T: O(nlogn)		S: O(n)



