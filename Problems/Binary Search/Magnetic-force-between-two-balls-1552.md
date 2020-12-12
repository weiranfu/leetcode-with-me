---
title: Medium | Magnetic Force Between Two Balls 1552
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-08-20 09:30:37
---

In universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has `n` empty baskets, the `ith` basket is at `position[i]`, Morty has `m` balls and needs to distribute the balls into the baskets such that the **minimum magnetic force** between any two balls is **maximum**.

Rick stated that magnetic force between two different balls at positions `x` and `y` is `|x - y|`.

Given the integer array `position` and the integer `m`. Return *the required force*.

[Leetcode](https://leetcode.com/problems/magnetic-force-between-two-balls/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/08/11/q3v1.jpg)

```
Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
```

**Constraints:**

- `n == position.length`
- `2 <= n <= 10^5`
- `1 <= position[i] <= 10^9`
- All integers in `position` are **distinct**.
- `2 <= m <= position.length`

---

#### Binary Search 

We can use binary search to find the answer.

Define function `count(d)` that counts the number of balls can be placed in to baskets, under the condition that the minimum distance between any two balls is `d`.

We want to find the maximum `d` such that `count(d) == m`.

- If the `count(d) > m` , we have too many balls placed, so `d` is too small.
- If the `count(d) < m` , we don't have enough balls placed, so `d` is too large.

Since `count(d)` is monotonically decreasing with respect to `d`, we can use binary search to find the optimal `d`.

```java
class Solution {
    public int maxDistance(int[] position, int m) {
        int n = position.length;
      	Arrays.sort(position);
        int l = 1, r = Integer.MAX_VALUE;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (check(mid, m, position)) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l - 1;
    }
    private boolean check(int f, int m, int[] arr) {
        int n = arr.length;
        int prev = arr[0];
        int cnt = 1;
        for (int i = 1; i < n; i++) {
            if (arr[i] - prev >= f) {
                cnt++;
                if (cnt >= m) return true;
                prev = arr[i];
            }
        }
        return false;
    }
}
```

T: O(nlogn)			S: O(1)

---

#### Optimized



---

#### Standard solution  



