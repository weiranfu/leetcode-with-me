---
title: Medium | Random Pick with Weight 528
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-09-01 21:21:19
---

Given an array of positive integers w. where `w[i]` describes the weight of `i``th` index (0-indexed).

We need to call the function `pickIndex()` which **randomly** returns an integer in the range `[0, w.length - 1]`. `pickIndex()` should return the integer proportional to its weight in the `w` array. For example, for `w = [1, 3]`, the probability of picking index `0` is `1 / (1 + 3) = 0.25` (i.e 25%) while the probability of picking index `1` is `3 / (1 + 3) = 0.75` (i.e 75%).

More formally, the probability of picking index `i` is `w[i] / sum(w)`.

[Leetcode](https://leetcode.com/problems/random-pick-with-weight/)

<!--more-->

**Example:**

```
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It's returning the second element (index = 1) that has probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It's returning the first element (index = 0) that has probability of 1/4.

Since this is a randomization problem, multiple answers are allowed so the following outputs can be considered correct :
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
```

**Constraints:**

- `1 <= w.length <= 10000`
- `1 <= w[i] <= 10^5`
- `pickIndex` will be called at most `10000` times.

---

#### Standard solution  

This reminds me the **Random scheduler for Process Scheduling in Operating System**

We could use accumulated weight(priority) to represents the possibility of each item.

And choose a random number from `[1, total_weight]`.

For example, `[1, 2, 4]` will convert to an accumulated array `[1, 3, 7]` => `[1,2,3,4,5,6,7]`

If `random <= 1`, we choose first item, else if `1 < random <= 3`, we choose second item, 

else if `3 < random <= 7`, we choose third item.

How to find the index of the item we choose, we could use **Binary Search** because the array is sorted.

```java
class Solution {
    
    int[] w;
    int n;
    Random random;

    public Solution(int[] w) {
        n = w.length;
        this.w = w;
        for (int i = 1; i < n; i++) {
            w[i] += w[i - 1];					// accumulated array
        }
        random = new Random();
    }
    
    public int pickIndex() {
        // get random number in [1, w[n - 1]]
        int rand = random.nextInt(w[n - 1]) + 1;
        int l = 0, r = n;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (w[mid] >= rand) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
}
```

T: O(nlogn)			S: O(1)			

