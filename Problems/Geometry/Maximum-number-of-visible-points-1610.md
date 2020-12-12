---
title: Medium | Maximum Number of Visible Points 1610
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Geometry
date: 2020-10-06 23:41:29
---

You are given an array `points`, an integer `angle`, and your `location`, where `location = [posx, posy]` and `points[i] = [xi, yi]` both denote **integral coordinates** on the X-Y plane.

Initially, you are facing directly east from your position. You **cannot move** from your position, but you can **rotate**. In other words, `posx` and `posy` cannot be changed. Your field of view in **degrees** is represented by `angle`, determining how wide you can see from any given view direction. Let `d` be the amount in degrees that you rotate counterclockwise. Then, your field of view is the **inclusive** range of angles `[d - angle/2, d + angle/2]`.

There can be multiple points at one coordinate. There may be points at your location, and you can always see these points regardless of your rotation. Points do not obstruct your vision to other points.

Return *the maximum number of points you can see*.

[Leetcode](https://leetcode.com/problems/maximum-number-of-visible-points/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/09/30/89a07e9b-00ab-4967-976a-c723b2aa8656.png)

```
Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
Output: 3
Explanation: The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.
```

**Example 2:**

```
Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
Output: 4
Explanation: All points can be made visible in your field of view, including the one at your location.
```

**Example 3:**

![img](https://assets.leetcode.com/uploads/2020/09/30/5010bfd3-86e6-465f-ac64-e9df941d2e49.png)

```
Input: points = [[1,0],[2,1]], angle = 13, location = [1,1]
Output: 1
Explanation: You can only see one of the two points, as shown above.
```

**Constraints:**

- `1 <= points.length <= 105`
- `points[i].length == 2`
- `location.length == 2`
- `0 <= angle < 360`
- `0 <= posx, posy, xi, yi <= 109`

---

#### Sliding Window  

Covert each point to an angle relative to original location.

Use `Math.atan2(dy, dx)` to get the `arctan(y/x)` angle.

How to handle cycle cases?

**Concatenate two cycles together. The latter cycle's angle is added by 360.**

```java
class Solution {
    public int visiblePoints(List<List<Integer>> points, int angle, List<Integer> location) {
        int n = points.size();
        List<Double> angles = new ArrayList<>();
        int same = 0;
        for (int i = 0; i < n; i++) {
            List<Integer> point = points.get(i);
            int dx = point.get(0) - location.get(0);
            int dy = point.get(1) - location.get(1);
            if (dx == 0 && dy == 0) same++;
            else {
                double theta = Math.atan2(dy, dx) * 180 / Math.PI; // get angle
                angles.add(theta);
            }
        }
        Collections.sort(angles);
        int cnt = 0;
        List<Double> list = new ArrayList<>(angles);
        for (double d : angles) {   // concatenate to handle cycles
            list.add(d + 360);
        }
        for (int i = 0, j = 0; i < list.size(); i++) {
            while (list.get(i) - list.get(j) > angle) j++;
            cnt = Math.max(cnt, i - j + 1);
        }
        return cnt + same;
    }
}
```

T: O(nlogn)			S: O(n)

