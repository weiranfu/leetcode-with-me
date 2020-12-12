---
title: Medium | Robot Bounded in Circle 1041
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-08-26 11:01:51
---

On an infinite plane, a robot initially stands at `(0, 0)` and faces north.  The robot can receive one of three instructions:

- `"G"`: go straight 1 unit;
- `"L"`: turn 90 degrees to the left;
- `"R"`: turn 90 degress to the right.

The robot performs the `instructions` given in order, and repeats them forever.

Return `true` if and only if there exists a circle in the plane such that the robot never leaves the circle.

[Leetcode](https://leetcode.com/problems/robot-bounded-in-circle/)

<!--more-->

**Example 1:**

```
Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
```

**Example 2:**

```
Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.
```

**Example 3:**

```
Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
```

---

#### First solution 

Starting at the origin and face north `(0,1)`, after one sequence of `instructions`,

1. if chopper return to the origin, he is obvious in an circle.
2. if chopper finishes with face not towards north,
   it will get back to the initial status in another one or three sequences.

![image](https://assets.leetcode.com/users/lee215/image_1557633739.png)

```java
class Solution {
    public boolean isRobotBounded(String instructions) {
        int x = 0, y = 0;
        char face = 'N';
        for (char c : instructions.toCharArray()) {
            if (c == 'G') {
                if (face == 'N') y++;
                else if (face == 'S') y--;
                else if (face == 'E') x++;
                else x--;
            } else if (c == 'L') {
                if (face == 'N') face = 'W';
                else if (face == 'W') face = 'S';
                else if (face == 'S') face = 'E';
                else face = 'N';
            } else if (c == 'R') {
                if (face == 'N') face = 'E';
                else if (face == 'E') face = 'S';
                else if (face == 'S') face = 'W';
                else face = 'N';
            }
        }
        return face != 'N' || (x == 0 && y == 0);
    }
}
```

T: O(n)		S: O(1)

---

#### Optimized

Let's use numbers from 0 to 3 to mark the directions: `north = 0`, `east = 1`, `south = 2`, `west = 3`. In the array `directions` we could store corresponding coordinates changes, *i.e.* `directions[0]` is to go north, `directions[1]` is to go east, `directions[2]` is to go south, and `directions[3]` is to go west.

```java
class Solution {
    public boolean isRobotBounded(String instructions) {
        int x = 0, y = 0, face = 0;
        int[][] moves = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (char c : instructions.toCharArray()) {
            if (c == 'R') {
                face = (face + 1) % 4;
            } else if (c == 'L') {
                face = (face + 3) % 4;
            } else {
                x += moves[face][0];
                y += moves[face][1];
            }
        }
        return face != 0 || (x == 0 && y == 0);
    }
}
```

T: O(n)		S: O(1)

