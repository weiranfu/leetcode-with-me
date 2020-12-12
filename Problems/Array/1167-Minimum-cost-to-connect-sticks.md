---
title: Medium | Minimum Cost to Connect Sticks 1167
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2019-12-24 21:45:55
---

You have some `sticks` with positive integer lengths.

You can connect any two sticks of lengths `X` and `Y` into one stick by paying a cost of `X + Y`.  You perform this action until there is one stick remaining.

Return the minimum cost of connecting all the given `sticks` into one stick in this way.

[Leetcode](https://leetcode.com/problems/minimum-cost-to-connect-sticks/)

<!--more-->

**Example 1:**

```
Input: sticks = [2,4,3]
Output: 14
```

**Example 2:**

```
Input: sticks = [1,8,3,5]
Output: 30
```

**Constraints:**

- `1 <= sticks.length <= 10^4`
- `1 <= sticks[i] <= 10^4`

---

#### Tricky 

How to get two smallest items in an array? Use a priority queue!

---

#### First solution 

Use a priority queue to store items, and add the connected stick into priority queue after combining.

```java
class Solution {
    public int connectSticks(int[] sticks) {
        if (sticks.length == 1) return 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i : sticks) {
            pq.offer(i);
        }
        int sum = 0;
        while (!pq.isEmpty()) {
            int x = pq.poll();
            int y = pq.poll();
            sum += x + y;
            if (pq.isEmpty()) break;
            pq.offer(x + y);
        }
        return sum;
    }
}
```

T: O(n*logn) S: O(n)

---

#### Optimized 

We always achieve two items in pq to combine. if there's only one item in pq, we finish combining.

```java
class Solution {
    public int connectSticks(int[] sticks) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i : sticks) {
            pq.offer(i);
        }
        int sum = 0;
        while (pq.size() > 1) {
            int x = pq.poll();
            int y = pq.poll();
            sum += x + y;
            pq.offer(x + y);
        }
        return sum;
    }
}
```

T: O(n*logn) S: O(n)

---

#### Summary 

When we want to get min value from an array, we could use priority queue.