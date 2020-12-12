---
title: Hard | K Empty Slots 683
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-07-29 11:13:21
---

You have `N` bulbs in a row numbered from `1` to `N`. Initially, all the bulbs are turned off. We turn on exactly one bulb everyday until all bulbs are on after `N` days.

You are given an array `bulbs` of length `N` where `bulbs[i] = x` means that on the `(i+1)th` day, we will turn on the bulb at position `x` where `i` is `0-indexed` and `x` is `1-indexed.`

Given an integer `K`, find out the **minimum day number** such that there exists two **turned on** bulbs that have **exactly** `K` bulbs between them that are **all turned off**.

If there isn't such day, return `-1`.

[Leetcode](https://leetcode.com/problems/k-empty-slots/)

<!--more-->

**Example 1:**

```
Input: 
bulbs: [1,3,2]
K: 1
Output: 2
Explanation:
On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
We return 2 because on the second day, there were two on bulbs with one off bulb between them.
```

---

#### Check by Date

Suppose we are opening bulbs in the order of days.

On `i`th day, we open a bulb at `bulbs[i-1]` pos.

We want to know the previous open bulb's pos and latter open bulb's pos.

If `pos - prev - 1 == K || latter - pos - 1 == K`, we find a K length empty slots and return current day.

1. TreeSet

   We could use TreeSet to store the position of each open bulb.

   `set.lower(pos)` and `set.higher(pos)` will help us to find the pos of previous and latter open bulbs' pos.

   ```java
   class Solution {
       public int kEmptySlots(int[] bulbs, int K) {
           int n = bulbs.length;
           TreeSet<Integer> set =  new TreeSet<>();
           for (int day = 1; day <= n; day++) {
               int pos = bulbs[day - 1];
               set.add(pos);
               Integer lower = set.lower(pos);
               if (lower != null && pos - lower - 1 == K) return day;
               Integer higher = set.higher(pos);
               if (higher != null && higher - pos - 1 == K) return day; 
           }
           return -1;
       }
   }
   ```

   T: O(nlogn)			S: O(n)

2. BIT

   On `i`th day, we open a bulb at `bulbs[i-1]` pos.

   We need to an `open[]` array to record whether a bulb is open to help determine the boundary of K slots.

   `int pos = bulbs[day - 1], left = pos - K - 1, right = pos + K + 1;`

   We need to check three pos and cnt the number of open bulbs.

   ```java
   int cnt = query(pos);
   if (left >= 1 && open[left] && query(left) + 1 == cnt) return day;
   if (right <= n && open[right] && query(right) == cnt + 1) return day;
   ```

   ```java
   class Solution {
       int n;
       int[] sum;
       
       public int kEmptySlots(int[] bulbs, int K) {
           n = bulbs.length;
           sum = new int[n + 1];
           boolean[] open = new boolean[n + 1];
           for (int day = 1; day <= n; day++) {
               int pos = bulbs[day - 1], left = pos - K - 1, right = pos + K + 1;
               add(pos);
               open[pos] = true;
               
               int cnt = query(pos);
               if (left >= 1 && open[left] && query(left) + 1 == cnt) return day;
               if (right <= n && open[right] && query(right) == cnt + 1) return day;
           }
           return -1;
       }
       
       private void add(int x) {
           for (int i = x; i <= n; i += i & -i) {
               sum[i]++;
           }
       }
       private int query(int x) {
           int res = 0;
           for (int i = x; i > 0; i -= i & -i) res += sum[i];
           return res;
       }
   }
   ```

   T: O(nlogn)		S: O(n)

---

#### Check by Pos

We could convert the `bulbs[]` into `days[]`, which `days[i]` means the bulbs at position `i` will open at `days[i]`.

**Sliding Window**

We could keep a sliding window `[l, r]` with size `K`. All bulbs in this range `[l, r]` should open later than `max(days[l], days[r])`.

So we check all days `i` in between `[l, r]` that `days[i] > max(days[l], days[r])`.

**If we find `days[i] < max(days[l], days[r])`, we could reset window to `l = i, r = l + K + 1` because bulb at `i` will open earlier than all bulbs between `[l, i]`.**

If we find `i == r`, we find a valid window and record the days `res = min(res, max(days[l], days[r]))`

```java
class Solution {
    public int kEmptySlots(int[] bulbs, int K) {
        int n = bulbs.length;
        int[] days = new int[n];
        for (int day = 0; day < n; day++) {
            days[bulbs[day] - 1] = day + 1;
        }
        int res = n + 1;
        for (int i = 0, l = 0, r = K + 1; i < n && r < n; i++) {
            if (days[i] < Math.max(days[l], days[r]) || i == r) { // move window
                if (i == r) res = Math.min(res, Math.max(days[l], days[r]));
                l = i;
                r = l + K + 1;
            }
        }
        return res == n + 1 ? -1 : res;
    }
}
```

T: O(n)			S: O(n)

