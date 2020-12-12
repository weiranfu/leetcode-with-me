---
title: Medium | Fruit into Baskets 904
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-07-27 21:36:34
---

In a row of trees, the `i`-th tree produces fruit with type `tree[i]`.

You **start at any tree of your choice**, then repeatedly perform the following steps:

1. Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
2. Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

[Leetcode](https://leetcode.com/problems/fruit-into-baskets/)

<!--more-->

**Example 1:**

```
Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
```

**Example 2:**

```
Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
```

**Example 3:**

```
Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
```

**Example 4:**

```
Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
```

---

#### Two Pointers 

Find out the longest length of subarrays with at most 2 different numbers?

Loop all fruit `c` in `tree`,
Note that `a` and `b` are the last two different types of fruit that we met, `c` is the current fruit type,
so it's something like "....aaabbbc..."

**Case 1** `c == b`:
fruit `c` already in the basket,
and it's same as the last type of fruit
`cur += 1`
`count_b += 1`

**Case 2** `c == a`:
fruit `c` already in the basket,
but it's not same as the last type of fruit
`cur += 1`
`count_b = 1`
`a = b, b = c`

**Case 3** `c != b && c!= a`:
fruit `c` not in the basket,
`cur = count_b + 1`
`count_b = 1`
`a = b, b = c`

Of course, in each turn we need to update `res = max(res, cur)`

```java
class Solution {
    public int totalFruit(int[] tree) {
        int n = tree.length;
        int res = 0;
        int a = 0, b = 0;
        int cnt = 0, b_cnt = 0;
        for (int t : tree) {
            if (t == b) {
                cnt++;
                b_cnt++;
            } else if (t == a) {
                cnt++;
                a = b; b = t;
                b_cnt = 1;
            } else {
                cnt = b_cnt + 1;
                a = b; b = t;
                b_cnt = 1;
            }
            res = Math.max(res, cnt);
        }
        return res;
    }
}
```

T: O(n)			S: O(1)

---

#### Sliding Window

Find out the longest length of subarrays with at most 2 different numbers?

Solve with sliding window and maintain a hashmap `counter`, which count the number of element between the two pointers.

```java
class Solution {
    public int totalFruit(int[] tree) {
        int n = tree.length;
        int res = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0, j = 0; i < n; i++) {
            map.put(tree[i], map.getOrDefault(tree[i], 0) + 1);
            while (map.size() > 2) {
                map.put(tree[j], map.get(tree[j]) - 1);
                map.remove(tree[j], 0);
                j++;
            }
            res = Math.max(res, i - j + 1);
        }
        return res;
    }
}
```

T: O(n)			S: O(2)



