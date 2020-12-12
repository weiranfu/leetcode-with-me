---
title: Hard | Best Meeting Point 296
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-01-02 21:35:48
---

A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using [Manhattan Distance](http://en.wikipedia.org/wiki/Taxicab_geometry), where distance(p1, p2) = `|p2.x - p1.x| + |p2.y - p1.y|`.

[Leetcode](https://leetcode.com/problems/best-meeting-point/)

<!--more-->

**Example:**

```
Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.
```

---

#### Tricky 

**Conclusion: The Median Minimizes the Sum of Absolute Deviations**.



**1. Let's start from the 1-dimension case**

Suppose we have n people living on a straight street and they want to find somewhere to meet. The total distance is

![enter image description here](https://latex.codecogs.com/gif.latex?%5Csum_i%7B%7Cx_i-m%7C%7D)

where ![enter image description here](https://latex.codecogs.com/gif.latex?x_i) is the location of each house and ![enter image description here](https://latex.codecogs.com/gif.latex?m)
is the meeting point. To minimize this problem, take the derivative of this equation. Each term will give you

- 1, if ![enter image description here](https://latex.codecogs.com/gif.latex?m%20%3E%20x_i)
- -1, if ![enter image description here](https://latex.codecogs.com/gif.latex?m%20%3C%20x_i)

To reach the minimum, the derivative must be 0. To make the derivative 0, the number of 1s and -1s must equal.

- If n is even, then m must be located between the middle two locations (Any locations between them will give you the minimum, **not necessarily** the median).
- If n is odd, then m must be located on the middle one house. That's the median.

**2. Then we can discuss the 2-dimension case**

Let's write down the equation directly.

![enter image description here](https://latex.codecogs.com/gif.latex?%5Csum_i%20%7Cx_i-m%7C+%7Cy_i-n%7C)

So this time, we have two variables - m and n. Recall what you've learned in multiple variables calculus. To find the minimum, we need to take the partial derivatives for the equation. And each partial derivative (or we can say, each dimension) will give you the same result as the 1-D case.

**3. So we can even solve the problem in any dimension**

Because every dimension is independent to each other. Do every dimension as 1-D case.

---

#### My thoughts 

Because every dimension is independent to each other. So do every dimension as 1-D case.

Get the median of each dimension's points values.

---

#### First solution 

In order to get median more easier, we need to get coordinate in order.

So we need two loops to get `xList` and `yList`.

```java
class Solution {
    public int minTotalDistance(int[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        List<Integer> xList = new ArrayList<>();
        List<Integer> yList = new ArrayList<>();
        int m = grid.length, n = grid[0].length;
        // Get sorted (x, y) lists.
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    xList.add(i);
                }
            }
        }
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) {
                if (grid[i][j] == 1) {
                    yList.add(j);
                }
            }
        }
        int xMin = getMin(xList);
        int yMin = getMin(yList);
        return xMin + yMin;
    }
    
    private int getMin(List<Integer> list) {
        int size = list.size();
        int median;
        if (size % 2 == 0) {
            median = (list.get(size / 2) + list.get(size / 2 - 1)) / 2; 
        } else {
            median = list.get(size / 2);
        }
        int sum = 0;
        for (int i = 0; i < size; i++) {
            sum += Math.abs(list.get(i) - median);
        }
        return sum;
    }
}
```

T: O(mn)		S: O(mn)

---

#### Optimized 

We can use 

`m1 = list.get(size / 2)`;  `m2 = list.get((size - 1) / 2);`

`median = (m1 + m2) / 2`  to calculate the median.

```java
class Solution {
    public int minTotalDistance(int[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        List<Integer> xList = new ArrayList<>();
        List<Integer> yList = new ArrayList<>();
        int m = grid.length, n = grid[0].length;
        // Get sorted (x, y) lists.
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    xList.add(i);
                }
            }
        }
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) {
                if (grid[i][j] == 1) {
                    yList.add(j);
                }
            }
        }
        int xMin = getMin(xList);
        int yMin = getMin(yList);
        return xMin + yMin;
    }
    
    private int getMin(List<Integer> list) {
        int size = list.size();
        int m1 = list.get(size / 2);
        int m2 = list.get((size - 1) / 2);
        int median = (m1 + m2) / 2;
        int sum = 0;
        for (int i = 0; i < size; i++) {
            sum += Math.abs(list.get(i) - median);
        }
        return sum;
    }
}
```

T: O(mn)		S: O(mn)

---

#### Summary 

* **The Median Minimizes the Sum of Absolute Deviations**.

* Iterate in two directions to get x or y coordinates in order.
* `median = (m1 + m2) / 2`. `m1 = list.get(size / 2), m2 = list.get((size - 1) / 2)`

