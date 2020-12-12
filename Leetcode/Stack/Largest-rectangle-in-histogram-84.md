---
title: Hard | Largest Rectangle in Histogram 84
tags:
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-05-19 06:18:51

---

Given *n* non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
![img](https://assets.leetcode.com/uploads/2018/10/12/histogram.png)
Above is a histogram where width of each bar is 1, given height = `[2,1,5,6,2,3]`.

![img](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)
The largest rectangle is shown in the shaded area, which has area = `10` unit.

[Leetcode](https://leetcode.com/problems/largest-rectangle-in-histogram/)

<!--more-->

**Example:**

```
Input: [2,1,5,6,2,3]
Output: 10
```

**Follow up:** [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

---

#### Brute Force

Scan from left to right, the height of ractangle is stricted by the min height of all possible bars.

For each bar, we scan from left to right to find the minH.

```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int max = 0;
        for (int i = 0; i < n; i++) {
            int minH = heights[i];
            for (int j = i; j < n; j++) {
                minH = Math.min(minH, heights[j]);
                max = Math.max(max, minH * (j - i + 1));
            }
        }
        return max;
    }
}
```

T: O(n^2)		S: O(1)

---

#### Standard solution  

The stack maintain the indexes of buildings with ascending height. 

**If the new building `heights[i]` is smaller than the building at the top of stack `heights[stack.peek()]`, we find the right boundary of a rectangle. Then we could try to calculate the area of this rectangle in the stack. We need to save the index of building in the stack.**

**How to get the left boundary? If the new building `heights[i]` is not adjacent to the top stack building, the left boundary is the index on the top of stack `stack.peek()`.**

So the width of rectangle will be `i - stack.peek() - 1`. 

If stack is empty, left boundary will be 0, the width will be `i`. (which means all the building between 0 and i are greater than `heights[i]`).

**Continue pop out buildings whose height is greater than new building `heights[i]` until buildings left in stack is shorter than new building.**

**In the end, if there're buildings left in the stack after adding all buildings(which means the heights of these left buildings are in ascending order), we add a building with heigth 0 to pop out all the left buildings in the stack.** 

```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        if (heights == null || heights.length == 0) return 0;
        int n = heights.length;
        int max = 0;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i <= n; i++) {
            // we need to add 0 finally to compute the lowest wall's area
            int curr = i == n ? 0 : heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] > curr) {
                int H = heights[stack.pop()];
              	// the empty stack's idx is -1 for computing distance
                int idx = stack.isEmpty() ? -1 : stack.peek(); 
                max = Math.max(max, H * (i - idx - 1));
            }
            stack.push(i);
        }
        return max;
    }
}
```

T: O(n)			S: O(n)
