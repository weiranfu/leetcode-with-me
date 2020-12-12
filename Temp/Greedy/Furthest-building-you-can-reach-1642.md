---
title: Medium | Furthest Building You Can Reach 1642
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-11-21 17:22:59
---

You are given an integer array `heights` representing the heights of buildings, some `bricks`, and some `ladders`.

You start your journey from building `0` and move to the next building by possibly using bricks or ladders.

While moving from building `i` to building `i+1` (**0-indexed**),

- If the current building's height is **greater than or equal** to the next building's height, you do **not** need a ladder or bricks.
- If the current building's height is **less than** the next building's height, you can either use **one ladder** or `(h[i+1] - h[i])` **bricks**.

*Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.*

[Leetcode](https://leetcode.com/problems/furthest-building-you-can-reach/)

<!--more-->

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/27/q4.gif)

```
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
```

**Constraints:**

- `1 <= heights.length <= 105`
- `1 <= heights[i] <= 106`
- `0 <= bricks <= 109`
- `0 <= ladders <= heights.length`

---

#### Binary Search 

Let's say there're `n` buildings, our optimal decision is to choose to use `ladders` for most highest buildings as much as possible, and use `bricks` for lower buildings.

And if we know the furthest distance we can reach, we can easily check whether we can really reach there.

We can sort these buildings and check `ladders` and `bricks`.

So we can **binary search** the max distance and check the reachability.

```java
class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        int n = heights.length;
        int l = 0, r = n;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (check(mid, heights, bricks, ladders)) l = mid + 1;
            else r = mid;
        }
        return l - 1;
    }
    private boolean check(int mid, int[] heights, int bricks, int ladders) {
        List<Integer> list = new ArrayList<>();
        int sum = 0;
        for (int i = 0; i < mid; i++) {
            if (heights[i] >= heights[i + 1]) continue;
            int diff = heights[i + 1] - heights[i];
            sum += diff;
            list.add(diff);
        }
        Collections.sort(list);     // sort diff of buildings
        int i;
        for (i = list.size() - 1; i >= 0 && ladders != 0; i--) {
            sum -= list.get(i);
            ladders--;
        }
        if (i == -1) return true;    // climb all the buildings
        if (sum <= bricks) return true; // use bricks to climb buildings
        return false;
    }
}
```

T: O(n\*logn\*logn)		S: O(n)

---

#### PriorityQueue

We keep a priority queue and store the max height difference in it.

If the size of priority queue exceeds `ladders`, which means we cannot use all ladders to climb max `ladders` diff height, we must use `bricks` to climb the smallest diff height.
Then we pop out the smallest difference, and reduce `bricks`.
If `bricks < 0`, we can't make this move, then we return current index `i`.
If we can reach the last building, we return `A.length - 1`.

```java
class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        int n = heights.length;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 1; i < n; i++) {
            int diff = heights[i] - heights[i - 1];
            if (diff <= 0) continue;
            pq.add(diff);
            if (pq.size() > ladders) {
                bricks -= pq.poll();
                if (bricks < 0) return i - 1;
            }
        }
        return n - 1;
    }
}
```

T: O(nlogn)		S: O(n)

