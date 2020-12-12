---
title: Medium | Corporate Flight Bookings 1109 
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Prefix
date: 2020-08-01 16:39:13
---

There are `n` flights, and they are labeled from `1` to `n`.

We have a list of flight bookings.  The `i`-th booking `bookings[i] = [i, j, k]` means that we booked `k` seats from flights labeled `i` to `j` inclusive.

Return an array `answer` of length `n`, representing the number of seats booked on each flight in order of their label.

[Leetcode](https://leetcode.com/problems/corporate-flight-bookings/)

<!--more-->

**Example 1:**

```
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
```

**Constraints:**

- `1 <= bookings.length <= 20000`
- `1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000`
- `1 <= bookings[i][2] <= 10000`

---

#### 差分数组 

```java
class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] res = new int[n];
        int[] B = new int[n + 2];
        for (int[] book : bookings) {
            int l = book[0], r = book[1], k = book[2];
            B[l] += k;
            B[r + 1] -= k;
        }
        for (int i = 1; i <= n; i++) {
            B[i] += B[i - 1];
            res[i - 1] = B[i];
        }
        return res;
    }
}
```

T: O(n)			S: O(n)



