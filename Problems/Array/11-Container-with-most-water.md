---
title: Medium | Container with most water 11
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2019-07-25 00:58:58
---

Given *n* non-negative integers *a1*, *a2*, ..., *an* , where each represents a point at coordinate (*i*, *ai*). *n* vertical lines are drawn such that the two endpoints of line *i* is at (*i*, *ai*) and (*i*, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

**Note:** You may not slant the container and *n* is at least 2.

[Leetcode](https://leetcode.com/problems/container-with-most-water/)

<!--more-->

![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49. 

**Example:**

```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

---

#### Tricky 

**Two pointer approach**

To find max volume, there're two variables `length` and `height`. length = right - left`, `height = min(right, left)`. 

I put `left = 0`, `right = array.length - 1`, so `length` will be maximum at first, 

From now on, `length` must become less because these two pointers will move closer.

So if I want a larger volume, I need to find a heigher boundary.

In this way, we could assume that we only have just *one* variables now. (because `length` is bound to be less).

---

#### First solution 

```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int volume = volume(height, left, right);
        while (left < right) {
            if (height[left] < height[right]) {
                left = left + 1;
                if (volume(height, left, right) > volume) {
                    volume = volume(height, left, right);
                }
            } else {
                right = right - 1;
                if (volume(height, left, right) > volume) {
                    volume = volume(height, left, right);
                }
            }
        }
        return volume;
    }
    
    public static int volume(int[] height, int left, int right) {
        return (right - left) * Math.min(height[left], height[right]);
    }
}
```

T: O(n), S: O(1)

---

#### Optimized 

1. If - else could be optimized.

   put the re-new of `volume` out of the if-else.

2. Volume is compared with new volume itself.

   so use `volume = max(volume, ...)` instead.

```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int h = Math.min(height[left], height[right]);
        int volume = (right - left) * h;
        while (left < right) {
            if (height[left] < height[right]) {
                left = left + 1;
            } else {
                right = right - 1;
            }
            h = Math.min(height[left], height[right]);
            volume = Math.max(volume, (right - left) * h); 
        }
        return volume;
    }
}
```

T: O(n), S: O(1)

---

#### Summary 

Using two pointer approach to make `length ` become less and less.

Two variables problem become one variable problem!