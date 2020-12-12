---
title: Easy | Most Visited Sector in a Circular Track 1560
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Prefix
date: 2020-08-28 22:17:52
---

Given an integer `n` and an integer array `rounds`. We have a circular track which consists of `n` sectors labeled from `1` to `n`. A marathon will be held on this track, the marathon consists of `m` rounds. The `ith` round starts at sector `rounds[i - 1]` and ends at sector `rounds[i]`. For example, round 1 starts at sector `rounds[0]` and ends at sector `rounds[1]`

Return *an array of the most visited sectors* sorted in **ascending** order.

Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example).

[Leetcode](https://leetcode.com/problems/most-visited-sector-in-a-circular-track/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/08/14/tmp.jpg)

```
Input: n = 4, rounds = [1,3,1,2]
Output: [1,2]
Explanation: The marathon starts at sector 1. The order of the visited sectors is as follows:
1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round 3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors. Sectors 3 and 4 are visited only once.
```

---

#### Standard solution  

Prefix array. （差分数组）

Consider the interval `[x, y]`

`x <= y, a[x]++, a[y + 1]--`

`x > y, a[x]++, a[n + 1]--, a[1]++, a[y + 1]--`

```java
class Solution {
    int n;
    int[] a;
    public List<Integer> mostVisited(int n, int[] rounds) {
        this.n = n;
        a = new int[n + 2];
        int s = rounds[0];
        for (int i = 1; i < rounds.length; i++) {
            add(s, rounds[i]);
            s = rounds[i] + 1;
        }
        int max = 0;
        for (int i = 1; i <= n; i++) {
            a[i] += a[i - 1];
            max = Math.max(max, a[i]);
        }
        List<Integer> res = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (a[i] == max) res.add(i);
        }
        return res;
    }
    private void add(int x, int y) {
        if (x <= y) {
            a[x]++; a[y + 1]--;
        } else {
            a[x]++; a[n + 1]--;
            a[1]++; a[y + 1]--;
        }
    }
}
```

T: O(n)		S: O(n)

---

#### Check start and end

Like a clock, check first and last
pay attention if count cross a circle;

details of thoughts: let fr = arr[0] (first), to = arr[m -1] (last);
1, when fr <= to, cnt for each node [..., n, n+1(fr), n+1, ..., n + 1(to), n, n, ...]
2, when fr > to, cnt for each node [n+1, n+1, ..., n + 1(to), n, ... , n, n+1(fr), n+1, ..., n + 1]
3, You may find that you don't worry about the value of n, n could be 0, 1, 2, 3, ..., whatever it is won't influence the result. You just need to check whether it is model 1 or 2 based on fr and to.

```java
   public List<Integer> mostVisited(int n, int[] rounds) {
        int len = rounds.length, fr = rounds[0], to = rounds[len - 1];
        List<Integer> res = new ArrayList<>();
        if (to >= fr) {     // no circle, such as [1,3,1,2]
            for (int i = fr; i <= to; i++) res.add(i);
        } else {            // cross a circle, such as [2,3,2,1]
            for (int i = 1; i <= n; i++) {
                if (i == to + 1) i = fr;
                res.add(i);
            }
        }
        return res;
    }
```

T: O(n)			S: O(1)