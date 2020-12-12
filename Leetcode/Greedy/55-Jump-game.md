---
title: Medium | Jump game 55
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2019-07-23 11:26:52
---

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

[Leetcode](https://leetcode.com/problems/jump-game/)

<!--more-->

**Example 1:**

```
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
```

**Follow up:**

[Jump Game II](https://aranne.github.io/2020/01/21/45-Jump-game-II/)

---

#### Tricky

This is a greedy problem.

We should consider the max index we could reach when traverse the array.

`max = Math.max(max, i + nums[i])`

The condition we can continue to traverse is that `i < nums.length && i <= max`.

---

#### Standard 

```java
class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length == 0) return false;
        int n = nums.length;
        int max = 0;
        for (int i = 0 ; i < n && i <= max; i++) {
            max = Math.max(max, i + nums[i]);
        }
        return max >= n - 1;
    }
}
```

T: O(n), S: O(1)

---

#### Summary 

Greedy: select the locally optimum in the hope of reaching global optimum.

