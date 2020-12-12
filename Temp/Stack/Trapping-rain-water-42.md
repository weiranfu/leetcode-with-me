---
title: Hard | Trapping Rain Water 42
tags:
  - tricky
categories:
  - Leetcode
  - Stack
date: 2019-12-20 19:06:08
---

Given *n* non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

[Leetcode](https://leetcode.com/problems/trapping-rain-water/)

<!--more-->

![img](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. **Thanks Marcos** for contributing this image!

**Example:**

```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

---

#### Tricky 

This is a bucket problem. 

How can we trap water? The only situation is that we always move the side with smaller height of bucket and trap water if height goes down.

Keep track left and right height of a bucket and compute the sum accumulatively.

---

#### Brute Force

- Initialize `ans`= 0
- Iterate the array from left to right:
  - Initialize max_left=0 and max_right=0
  - Iterate from the current element to the beginning of array updating:
    - `max_left=max⁡(max_left, height[j])`
  - Iterate from the current element to the end of array updating:
    - `max_right=max⁡(max_right, height[j])`
  - Add `min⁡(max_left, max_right) − height[i]` to `ans`

```java
class Solution {
    public int trap(int[] height) {
        int sum = 0;
        for (int i = 0; i < height.length; i += 1) {
            int maxLeft = 0, maxRight = 0;
            for (int j = i; j >= 0; j -= 1) {
                maxLeft = Math.max(maxLeft, height[j]);
            }
            for (int j = i; j < height.length; j += 1) {
                maxRight = Math.max(maxRight, height[j]);
            }
            sum += Math.min(maxLeft, maxRight) - height[i];
        }
        return sum;
    }
}
```

T: O(n^2) S: O(1)

---

#### DP

Using DP to optimize brute force solution. As we compute max left and right height many times in brute force, we can use array to store these max heights.

`maxLeft[i] = Math.max(maxLeft[i - 1], height[i]);`

```java
class Solution {
    public int trap(int[] height) {
        int size = height.length;
        if (size == 0) return 0;
        int sum = 0;
        int[] maxLeft = new int[size];
        int[] maxRight = new int[size];
        maxLeft[0] = height[0];
        for (int i = 1; i < size; i += 1) {
            maxLeft[i] = Math.max(maxLeft[i - 1], height[i]);
        }
        maxRight[size - 1] = height[size - 1];
        for (int i = size - 2; i >= 0; i -= 1) {
            maxRight[i] = Math.max(maxRight[i + 1], height[i]);
        }
        for (int i = 0; i < height.length; i += 1) {
            sum += Math.min(maxLeft[i], maxRight[i]) - height[i];
        }
        return sum;
    }
}
```

T: O(n) S: O(n)

---

#### Two Pointers

Using two pointers. And keep track of left max height and right max height.

If left max height < right max height, which means the bucket height is at left, then if next height is smaller than left max height, `sum += left max height - next height`.

```java
class Solution {
    public int trap(int[] height) {
        if (height.length < 3) return 0;
        int left = 0, right = height.length - 1;
        int maxLeft = height[left], maxRight = height[right];
        int sum = 0;
        while (left < right) {
            if (maxLeft < maxRight) {
                left += 1;
                if (height[left] < maxLeft) {
                    sum += maxLeft - height[left];
                }
                maxLeft = Math.max(maxLeft, height[left]);
            } else {
                right -= 1;
                if (height[right] < maxRight) {
                    sum += maxRight - height[right];
                }
                maxRight = Math.max(maxRight, height[right]);
            }
        }
        return sum;
    }
}
```

T: O(n) S: O(1)

---

#### Stack

![image.png](https://pic.leetcode-cn.com/37fccd915f959c2046ffc1ab2b0a1e4d921869337d8d5d4aa218886ab0bf7c8a-image.png)

Monotonic Decreasing Stack.

When we meet a higher wall, we pop out walls and compute the area.

The lower bound of area is `height[stack.pop()]`

The upper bound of area is `int H = Math.min(height[i], height[stack.peek()]);`

The distance is `int d = i - stack.peek() - 1;`

The area is `res += d * (H - lowH);`

```java
class Solution {
    public int trap(int[] height) {
        if (height == null || height.length == 0) return 0;
        int n = height.length;
        Stack<Integer> stack = new Stack<>();
        int res = 0;
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && height[stack.peek()] < height[i]) {
                int lowH = height[stack.pop()];		// lower bound
                if (!stack.isEmpty()) {
                    int H = Math.min(height[i], height[stack.peek()]);// upper bound
                    int d = i - stack.peek() - 1;
                    res += d * (H - lowH);
                }
            }
            stack.push(i);
        }
        return res;
    }
}
```

T: O(n)

S: O(n)

---

#### Summary 

How to compute sum of trapped water is key to this problem.