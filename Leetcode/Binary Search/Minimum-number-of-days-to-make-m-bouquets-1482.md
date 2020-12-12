---
title: Medium | Minimum Number of Days to Make m Bouquets 1482
tags:
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-06-14 20:03:51
---

Given an integer array `bloomDay`, an integer `m` and an integer `k`.

We need to make `m` bouquets. To make a bouquet, you need to use `k` **adjacent flowers** from the garden.

The garden consists of `n` flowers, the `ith` flower will bloom in the `bloomDay[i]` and then can be used in **exactly one** bouquet.

Return *the minimum number of days* you need to wait to be able to make `m` bouquets from the garden. If it is impossible to make `m` bouquets return **-1**.

[Leetcode](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/)

<!--more-->

**Example 1:**

```
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
```

**Example 2:**

```
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
```

**Example 3:**

```
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here's the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.
```

---

#### Tricky 

**We know that more flowers would bloom and more bouquets can be made as days move on.**

**We need to find a day that we could just make m bouquets —> Binary Search**

Then you could simply apply binary search on it, that is: find a mid day → validate if we can make k bouquests on that exact date → move to left or right part based on the validation → you are good to go

---

#### My thoughts 

Failed to solve.

---

#### Standard solution  

```java
class Solution {
    public int minDays(int[] bloomDay, int m, int k) {
        int n = bloomDay.length;
        if (k * m > n) return -1;
        int min = -1, max = -1;
        for (int day : bloomDay) {
            min = Math.min(min, day);
            max = Math.max(max, day);
        }
        int left = min;
        int right = max;              
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (check(mid, bloomDay, m, k)) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
    
    private boolean check(int day, int[] bloomDay, int m, int k) {
        int n = bloomDay.length;
        int flower = 0;
        int bouquet = 0;
        for (int i = 0; i < n; i++) {   // validate on [mid] day.
            if (bloomDay[i] > day) {
                flower = 0;
            } else if (++flower == k) {  // control the window
                bouquet++;
                flower = 0;
            }
        }
        return bouquet < m;
    }
}
```

T: O(nlog(max-min))			S: O(1)



