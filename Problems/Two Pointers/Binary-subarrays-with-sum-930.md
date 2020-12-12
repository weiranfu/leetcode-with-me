---
title: Medium | Binary Subarray with Sum 930
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-07-28 16:57:20
---

In an array `A` of `0`s and `1`s, how many **non-empty** subarrays have sum `S`?

[Leetcode](https://leetcode.com/problems/binary-subarrays-with-sum/)

<!--more-->

**Example 1:**

```
Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
```

**Follow up**

[Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)

---

#### Sliding Window

Just like the problem [Subarrays with exactly K Distinct Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

We could use a third `upper` pointer to shrink the window.

The number of subarrays ending with `A[i]` is `res += upper - j + 1`

If `sum > S`, we could shrink window from `upper` and update `j = upper`

```java
class Solution {
    public int numSubarraysWithSum(int[] A, int S) {
        int n = A.length;
        int sum = 0, upper = 0;
        int res = 0;
        for (int i = 0, j = 0; i < n; i++) {
            if (A[i] == 1) sum++;
            while (sum > S) {
                if (A[upper] == 1) {
                    sum--;
                }
                upper++;
                j = upper;			// update j to upper
            }
            if (sum == S) {
                while (upper < i && A[upper] == 0) {
                    upper++;
                }
                if (upper <= i) res += upper - j + 1; // corner case: upper > i
            }
        }
        return res;
    }
}
```

T: O(n)			S: O(n)

---

#### Convert to *At most S* problem

We could convert problem to *Findind number of subarrays with at most S sum*

`wihtSum(S) = atMostS(S) - atMostS(S - 1)`

```java
class Solution {
    public int numSubarraysWithSum(int[] A, int S) {
        return atMostS(A, S) - atMostS(A, S - 1);
    }
    private int atMostS(int[] A, int S) {
        int n = A.length;
        int sum = 0, res = 0;
        for (int i = 0, j = 0; i < n; i++) {
            if (A[i] == 1) sum++;
            while (j <= i && sum > S) {
                if (A[j] == 1) sum--;
                j++;
            }
            res += i - j + 1;
        }
        return res;
    }
}
```

T: O(n)		S: O(n)

