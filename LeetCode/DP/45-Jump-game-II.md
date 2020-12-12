---
title: Hard | Jump Game 45
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-01-21 20:44:25
---

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

[Leetcode](https://leetcode.com/problems/jump-game-ii/)

<!--more-->

**Example:**

```
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

---

#### Tricky 

This is a greedy problem. Let's say the range of the current jump is [curBegin, curEnd]

curFarthest is the farthest point that all points in [curBegin, curEnd] can reach. 

Once the current point reaches curEnd, then trigger another jump (jump to the farthest point as we have found), set the new curEnd with curFarthest, then keep the above steps.

---

#### Standard solution  

```java
class Solution {
    public int jump(int[] nums) {
        int steps = 0;
        int farthest = 0;
        int end = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (i > farthest) return -1;
            if (i > end) {
                end = farthest;  // Update end point.
                steps++;
            }
            // Find farthest point.
            farthest = Math.max(farthest, nums[i] + i);
        }
        return steps;
    }
}
```

T: O(n)				S: O(1)

---

### BFS

We can also change this problem to a BFS problem, where nodes in level i are all the nodes that can be reached in i-1th jump. for example. 2 3 1 1 4 , is
2||
3 1||
1 4 ||

clearly, the minimum jump of 4 is 2 since 4 is in level 3.

---

#### Summary 

This is a typical greedy problem.