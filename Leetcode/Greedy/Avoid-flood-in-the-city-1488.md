---
title: Medium | Avoid Flood in the City 1488
tags:
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-06-21 15:50:43
---

Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the `nth` lake, the `nth` lake becomes full of water. If it rains over a lake which is **full of water**, there will be a **flood**. Your goal is to avoid the flood in any lake.

Given an integer array `rains` where:

- `rains[i] > 0` means there will be rains over the `rains[i]` lake.
- `rains[i] == 0` means there are no rains this day and you can choose **one lake** this day and **dry it**.

Return *an array ans* where:

- `ans.length == rains.length`
- `ans[i] == -1` if `rains[i] > 0`.
- `ans[i]` is the lake you choose to dry in the `ith` day if `rains[i] == 0`.

If there are multiple valid answers return **any** of them. If it is impossible to avoid flood return **an empty array**.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes. (see example 4)

[Leetcode](https://leetcode.com/problems/avoid-flood-in-the-city/)

<!--more-->

**Example 1:**

```
Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.
```

**Example 2:**

```
Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
```

**Example 3:**

```
Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.
```

**Example 4:**

```
Input: rains = [69,0,0,0,69]
Output: [-1,69,1,1,-1]
Explanation: Any solution on one of the forms [-1,69,x,y,-1], [-1,x,69,y,-1] or [-1,x,y,69,-1] is acceptable where 1 <= x,y <= 10^9
```

**Example 5:**

```
Input: rains = [10,20,20]
Output: []
Explanation: It will rain over lake 20 two consecutive days. There is no chance to dry any lake.
```

---

#### Tricky 

When drying a lake #L, it is only useful to dry it if it is FULL already. Otherwise its of no use.

Which lake to dry on a day when there is no rain, can not be determined without knowing the rain sequence that is coming next.

1. We must dry the previous one between two rains on a same lake as soon as possible(**Greedy**)

   So if there're multiple pairs waiting for drying, we want to dry the earliest one.

   We could record the day of next rain on same lake in `next[]` and add `next[i]` into priority queue.

   If we meet a 0, we pop out the earliest day rain from pq and dry it.

2. If we want to dry the previous one of two rains on a same lake, we need to know the nearest 0 days to dry it.(**Greedy**). 

   So we could save the position of 0 days in a TreeMap and use `map.hight(pos)` to search nearest 0.

---

#### Next  + Priority Queue

```java
class Solution {
    public int[] avoidFlood(int[] rains) {
        int n = rains.length;
        int[] res = new int[n];
        Map<Integer, Integer> map = new HashMap<>();
        int[] next = new int[n];
        Arrays.fill(next, -1);
        for (int i = n - 1; i >= 0; i--) {
            if (rains[i] == 0) continue;
            if (map.containsKey(rains[i])) {
                next[i] = map.get(rains[i]);
            }
            map.put(rains[i], i);
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            if (rains[i] == 0) {
                if (pq.isEmpty()) {
                    res[i] = 1;
                } else {
                    int[] info = pq.poll();
                    int lake = info[1];
                    set.remove(lake);
                    res[i] = lake;
                }
            } else {
                if (set.contains(rains[i])) return new int[0];
                set.add(rains[i]);
                res[i] = -1;
                if (next[i] != -1) {
                    pq.add(new int[]{next[i], rains[i]});  // sort by next day
                }
            }
        }
        return res;
    }
}
```

T: O(nlogm)					m: number of pairs waiting for drying

S: O(n)

---

#### TreeMap to save 0 pos

```java
class Solution {
    public int[] avoidFlood(int[] rains) {
        int n = rains.length;
        Map<Integer, Integer> lakes = new HashMap<>();
        TreeSet<Integer> canfix = new TreeSet<>();
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            if (rains[i] == 0) {
                res[i] = 1;
                canfix.add(i);        									// add position of 0
            } else {
                if (lakes.containsKey(rains[i])) {
                    int pos = lakes.get(rains[i]);
                    Integer fix = canfix.higher(pos);   // search nearest 0
                    if (fix == null) return new int[0];
                    canfix.remove(fix);
                    res[fix] = rains[i];
                }
                lakes.put(rains[i], i);
                res[i] = -1;
            }
        }
        return res;
    }
}
```

T: O(n\*logm)				m: number of 0

S: O(n)

