---
title: Hard | Reducing Dishes 1402
tags:
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-05-18 00:20:56
---

A chef has collected data on the `satisfaction` level of his `n` dishes. Chef can cook any dish in 1 unit of time.

*Like-time coefficient* of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level  i.e.  `time[i]`*`satisfaction[i]`

Return the maximum sum of *Like-time coefficient* that the chef can obtain after dishes preparation.

Dishes can be prepared in **any** order and the chef can discard some dishes to get this maximum value.

[Leetcode](https://leetcode.com/problems/reducing-dishes/)

<!--more-->

**Example 1:**

```
Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total Like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14). Each dish is prepared in one unit of time.
```

**Example 2:**

```
Input: satisfaction = [4,3,2]
Output: 20
Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
```

**Example 3:**

```
Input: satisfaction = [-1,-4,-5]
Output: 0
Explanation: People don't like the dishes. No dish is prepared.
```

---

#### Tricky 

* We will cock dish with small satisfaction, and leave the most satisfied dish in the end.  So `Arrays.sort()`.

* We choose the most satisfied dish first, everytime we add a new dish to the beginning of menu list, all dishes on the menu will be cooked one time unit later. (will increase `sum * 1`)

  So we only add dishes that `A[i] + sum > 0`.  `A[i]` could be negative if total is large enough.

---

#### Standard solution  

We use `sum` to record the sum all of dishes' satisfaction in the menu list.

```java
class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        if (satisfaction == null || satisfaction.length == 0) return 0;
        Arrays.sort(satisfaction);
        int n = satisfaction.length;
        int sum = 0;
        int res = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (sum + satisfaction[i] > 0) { // if we could add new dish to the head.
                res += sum + satisfaction[i];
                sum += satisfaction[i];
            }
        }
        return res;
    }
}
```

T: O(nlogn)			S: O(1)

---

#### Summary 

In tricky.