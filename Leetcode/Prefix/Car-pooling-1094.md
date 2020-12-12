---
title: Medium | Car Pooling 1094	
tags:
  - tricky
categories:
  - Leetcode
  - Prefix
date: 2020-01-25 14:49:45
---

You are driving a vehicle that has `capacity` empty seats initially available for passengers.  The vehicle **only** drives east (ie. it **cannot** turn around and drive west.)

Given a list of `trips`, `trip[i] = [num_passengers, start_location, end_location]` contains information about the `i`-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return `true` if and only if it is possible to pick up and drop off all passengers for all the given trips. 

[Leetcode](https://leetcode.com/problems/car-pooling/)

<!--more-->

**Example 1:**

```
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
```

**Example 2:**

```
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
```

**Constraints:**

1. `trips.length <= 1000`
2. `trips[i].length == 3`
3. `1 <= trips[i][0] <= 100`
4. `0 <= trips[i][1] < trips[i][2] <= 1000`
5. `1 <= capacity <= 100000`

**Follow up**

[Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/)

---

#### Tricky 

We need to see one trip as a whole part, rather then time point.

Sort these trips by start time or end time.

Or we can use a TreeMap.

---

#### Optimized

We don't need to create two arrays in order to sort by start and end. For each trip, we can create two trips, one trip contains start time, the other trip contains end time.

```java
class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int m = trips.length;
        int n = trips[0].length;
        int[][] times = new int[m * 2][3];
        int i = 0;
        for (int[] trip : trips) {
            times[i++] = new int[]{trip[0], trip[1], 1};  // 1 means start
            times[i++] = new int[]{trip[0], trip[2], 0};  // 0 means end
        }
        Arrays.sort(times, (a, b) -> {
            if (a[1] != b[1]) {
                return a[1] - b[1];
            } else {
                return a[2] - b[2];   // end is ahead of start.
            }
        });
        int curr = 0, max = 0;
        for (int[] time : times) {
            if (time[2] == 1) {
                curr += time[0];
                max = Math.max(max, curr);
            } else {
                curr -= time[0];
            }
        }
        return max <= capacity;
    }
}
```

T: O(NlogN)			S: O(n)

---

#### Optimized Cont. (TreeMap)

Since we store these trips by time(start time and end time), we can use a TreeMap to store them.

For a time point, if we pick up passengers, we add passengers. And if we drop off passengers, we decrease passengers.

```java
class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int m = trips.length;
        int n = trips[0].length;
        Map<Integer, Integer> map = new TreeMap<>();
        for (int[] trip : trips) {
            map.put(trip[1], map.getOrDefault(trip[1], 0) + trip[0]); // plus passengers
            map.put(trip[2], map.getOrDefault(trip[2], 0) - trip[0]); // minus passenger
        }
        int max = 0, curr = 0;
        for (int time : map.keySet()) {
            curr += map.get(time);
            max = Math.max(max, curr);
        }
        return max <= capacity;
    }
}
```

T: O(NlogN)		S: O(n)

---

#### 差分数组

加入一个trip即是在区间 `[l, r]`加上人数，统计差分数组后的人数最大值

```java
class Solution {
    int N = 1010;
    int[] B = new int[N];
    
    public boolean carPooling(int[][] trips, int capacity) {
        for (int[] trip : trips) {
            int l = trip[1] + 1, r = trip[2], c = trip[0];
            add(l, r, c);
        }
        int res = 0;
        for (int i = 1; i < N; i++) {
            B[i] += B[i - 1];
            res = Math.max(res, B[i]);
        }
        return res <= capacity;
    }
    private void add(int l, int r, int c) {
        B[l] += c;
        B[r + 1] -= c;
    }
}
```

T: O(n)			S: O(len)

---

#### Summary 

* Consider a trip as a whole part, sort them by time(start time and end time).

  Or we can use a TreeMap to store them.

* If the time has a max value, we can consider a trip as discrete time point. And store time point with passengers at a time array.