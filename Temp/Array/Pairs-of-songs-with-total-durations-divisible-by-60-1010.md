---
title: Easy | Pairs of Songs with Total Durations Divisible by 60 1010
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-08-26 12:27:55
---

In a list of songs, the `i`-th song has a duration of `time[i]` seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by `60`.  Formally, we want the number of indices `i`, `j` such that `i < j` with `(time[i] + time[j]) % 60 == 0`.

[Leetcode](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)

<!--more-->

**Example 1:**

```
Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
```

**Example 2:**

```
Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
```

**Note:**

- `1 <= time.length <= 60000`
- `1 <= time[i] <= 500`

---

#### Standard solution  

We can save the remainder of each `time[i]` into a map.

And find pairs `remainder1 + remainder2 == 60` in the map.

```java
class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        int n = time.length;
        int[] map = new int[60];
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            int remainder = time[i] % 60;
            int target = (60 - remainder) % 60;
            if (map[target] != 0) {
                cnt += map[target];
            }
            map[remainder]++;
        }
        return cnt;
    }
}
```

T: O(n)		S: O(1)

