---
title: Medium | Statistics from a Large Sample 1093
tags:
  - implement
categories:
  - Leetcode
  - Math
date: 2019-12-24 01:56:37
---

We sampled integers between `0` and `255`, and stored the results in an array `count`:  `count[k]` is the number of integers we sampled equal to `k`.

Return the minimum, maximum, mean, median, and mode of the sample respectively, as an array of **floating point numbers**.  The mode is guaranteed to be unique.

[Leetcode](https://leetcode.com/problems/statistics-from-a-large-sample/)

<!--more-->

*(Recall that the median of a sample is:*

- *The middle element, if the elements of the sample were sorted and the number of elements is odd;*
- *The average of the middle two elements, if the elements of the sample were sorted and the number of elements is even.)*

 

**Example 1:**

```
Input: count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
```

**Example 2:**

```
Input: count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,4.00000,2.18182,2.00000,1.00000]
```

**Constraints:**

1. `count.length == 256`
2. `1 <= sum(count) <= 10^9`
3. The mode of the sample that count represents is unique.
4. Answers within `10^-5` of the true value will be accepted as correct.

---

#### Implement

How to compute median is key.

Whatever the number of data is even or odd, we can compute median use two medians.

`m1 = (total + 1) / 2`, `m2 = (total / 2) + 1`.

`median = (m1 + m2) / 2` 

---

#### First solution 

Just to find lower bound of median then find the upper bound of median.

```java
class Solution {
    public double[] sampleStats(int[] count) {
        double[] res = new double[5];
        double mode = 0, max = 0, min = -1, mean = 0, median =0;
        int total = 0;
        for (int i = 0; i < count.length; i++) {
            total += count[i];
        }
        double sum = 0;
        int time = 0;
        for (int i = 0; i < count.length; i++) {
            if (count[i] != 0) {
                sum += i * count[i];
                if (min == -1) min = i; // Just change min once.
                max = i;
                if (count[i] > time) {
                    time = count[i];
                    mode = i;
                }
            }
        }
        mean = sum / total;
        int half = 0;
        int i = 0;
        while (i < count.length) {
            if (count[i] != 0) {
                half += count[i];
                if (total % 2 == 0) {
                    if (half >= total / 2) {
                        break;
                    }
                } else {
                    if (half >= (total / 2) + 1) {
                        break;
                    }
                }
            }
            i++;
        }
        if (total % 2 != 0) {
            median = i;
        } else {
            if (half > total / 2) {
                median = i;
            } else {
                int j = i + 1;
                while (j < count.length) {
                    if (count[j] != 0) {
                        break;
                    }
                    j++;
                }
                median = (double) (i + j) / 2;
            }
        }
        res[0] = min; res[1] = max; res[2] = mean; res[3] = median; res[4] = mode;
        return res;
    }
}
```

T: O(n) S: O(1)

---

#### Optimized 

Using `m1 = (total + 1) / 2`, `m2 = (total / 2) + 1`.

`median = (m1 + m2) / 2` to compute median

```java
    public double[] sampleStats(int[] count) {
        double[] res = new double[5];
        double max = 0, min = -1, mean = 0, median =0;
        int mode = 0;
        int total = 0;
        for (int i = 0; i < count.length; i++) {
            total += count[i];
        }
        double sum = 0;
        for (int i = 0; i < count.length; i++) {
            if (count[i] != 0) {
                sum += i * count[i];
                if (min == -1) min = i; // Just change min once.
                max = i;
                if (count[i] > count[mode]) {
                    mode = i;
                }
            }
        }
        mean = sum / total;
        int m1 = (total + 1) / 2;
        int m2 = total / 2 + 1;
        for (int i = 0, cnt = 0; i < count.length; i++) {
            if (cnt < m1 && cnt + count[i] >= m1) { // The moment cnt goes over m1.
                median += i / 2.0d; // Add half m1 to median.
            }
            if (cnt < m2 && cnt + count[i] >= m2) { // The moment cnt goes over m2.
                median += i / 2.0d; // Add half m2 to median.
            }
            cnt += count[i];
            if (cnt >= m2) break;
        }
        res[0] = min; res[1] = max; res[2] = mean; res[3] = median; res[4] = mode;
        return res;
    }
} 
```

T: O(n) S: O(1)

---

#### Summary 

Whatever the number of data is even or odd, we can compute median use two medians.

`m1 = (total + 1) / 2`, `m2 = (total / 2) + 1`.

`median = (m1 + m2) / 2` 