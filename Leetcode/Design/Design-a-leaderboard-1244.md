---
title: Medium | Design a LeaderBoard 1244
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Design
date: 2020-07-12 21:25:25
---

Design a Leaderboard class, which has 3 functions:

1. `addScore(playerId, score)`: Update the leaderboard by adding `score` to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given `score`.
2. `top(K)`: Return the score sum of the top `K` players.
3. `reset(playerId)`: Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.

Initially, the leaderboard is empty.

[Leetcode](https://leetcode.com/problems/design-a-leaderboard/)

<!--more-->

**Example 1:**

```
Input: 
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output: 
[null,null,null,null,null,null,73,null,null,null,141]

Explanation: 
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;
```

**Constraints:**

- `1 <= playerId, K <= 10000`
- It's guaranteed that `K` is less than or equal to the current number of players.
- `1 <= score <= 100`
- There will be at most `1000` function calls.

---

#### Tricky 

The operations are like the operations in Balanced Binary Tree.

1. So we could use TreeMap to implement, sorted based on the score.

   Use a HashMap to record the relationship between `id` and `score`.

   **Since there may be duplicate scores, we cannot use TreeSet!!!**

   ```java
   class Leaderboard {
       
       Map<Integer, Integer> map;
       TreeMap<Integer, Integer> rank;  // record score and duplicate count
   
       public Leaderboard() {
           map = new HashMap<>();
           rank = new TreeMap<>(Collections.reverseOrder());
       }
       
       public void addScore(int id, int score) {
           if (!map.containsKey(id)) {
               map.put(id, score);
               rank.put(score, rank.getOrDefault(score, 0) + 1);
           } else {
               int s = map.get(id);
               rank.put(s, rank.get(s) - 1);
               if (rank.get(s) == 0) rank.remove(s);
               s += score;
               map.put(id, s);
               rank.put(s, rank.getOrDefault(s, 0) + 1);
           }
       }
       
       public int top(int K) {
           int sum = 0;
           for (Integer s : rank.keySet()) {
               int cnt = rank.get(s);
               int min = Math.min(cnt, K);
               sum += s * min;
               K -= min;
               if (K == 0) break;
           }
           return sum;
       }
       
       public void reset(int id) {
           int s = map.get(id);
           rank.put(s, rank.get(s) - 1);
           if (rank.get(s) == 0) rank.remove(s);
           map.remove(id);
       }
   }
   ```

   T: O(nlogn)		S: O(n)

2. Weighted Segment Tree

   Although in the constraints, the `score` is only in `[0, 100]`, however we can add score to a player many times. It's not easy to find the upper bound of `score`.

   **So we need to create tree node dynamically.**

   Weighted Segment Tree can be used to find the top K largest items.

   In this problem, we need to find the sum of top K items. So we need to maintain not only `cnt` but also `sum` to get sum quickly.

   In `topK()` function, we need to determine whether the number of items in this interval is smaller than `k`, if it is we can just return `sum`.

   ```java
   class Leaderboard {
       class Node {
           int sum;
           int cnt;
           int l; int r;
           Node left; Node right;
       }
       
       Map<Integer, Integer> map = new HashMap<>();
       int maxn = 1000000;
       Node root = new Node();
       
       public void addScore(int id, int score) {
           if (!map.containsKey(id)) {
               map.put(id, score);
               update(score, true, 0, maxn, root);   
           } else {
               int s = map.get(id);
               update(s, false, 0, maxn, root);
               s += score;
               map.put(id, s);
               update(s, true, 0, maxn, root);
           }
       }
       
       public int top(int K) {
           return topK(K, 0, maxn, root);
       }
       
       public void reset(int id) {
           int s = map.get(id);
           map.remove(id);
           update(s, false, 0, maxn, root);
       }
       
       private void pushDown(Node n) {
           if (n.left == null) {
               n.left = new Node();
               n.right = new Node();
           }
       }
       private void pushUp(Node n) {
           n.cnt = n.left.cnt + n.right.cnt;
           n.sum = n.left.sum + n.right.sum;
       }
       
       private void update(int s, boolean add, int l, int r, Node n) {
           if (l == r) {
               if (add) {
                   n.cnt++;
                   n.sum += s;
               } else {
                   n.cnt--;
                   n.sum -= s;
               }
               return;
           }
           int mid = l + (r - l) / 2;
           
           pushDown(n);                            // create new node
           
           if (s <= mid) update(s, add, l, mid, n.left);
           else update(s, add, mid + 1, r, n.right);
           
           pushUp(n);                              // push up
       }
       private int topK(int K, int l, int r, Node n) {
           if (n.cnt <= K) {
               return n.sum;       // if K >= cnt, return sum of interval
           }
           if (l == r) {
               int min = Math.min(K, n.cnt);
               return min * l;     // return sum of min number of value
           }
           int mid = l + (r - l) / 2;
           int res = 0;
           res += topK(K, mid + 1, r, n.right);
           if (n.right.cnt < K) {
               res += topK(K - n.right.cnt, l, mid, n.left);
           }
           return res;
       }
   }
   ```

   