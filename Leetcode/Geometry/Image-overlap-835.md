---
title: Medium | Image Overlap 835
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Geometry
date: 2020-10-28 23:43:08
---

You are given two images `img1` and `img2` both of size `n x n`, represented as binary, square matrices of the same size. (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the *overlap* of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does **not** include any kind of rotation.)

What is the largest possible overlap?

[Leetcode](https://leetcode.com/problems/image-overlap/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/09/09/overlap1.jpg)

![](https://assets.leetcode.com/uploads/2020/09/09/overlap_step1.jpg)

![](https://assets.leetcode.com/uploads/2020/09/09/overlap_step2.jpg)

```
Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We slide img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3. (Shown in red)
```

**Constraints:**

- `n == img1.length`
- `n == img1[i].length`
- `n == img2.length`
- `n == img2[i].length`
- `1 <= n <= 30`
- `img1[i][j]` is `0` or `1`.
- `img2[i][j]` is `0` or `1`.

---

#### Brute Force

Try all possible shifting way, move the `img1` around by shifting up, down, left, right.

Then count how many overlapping cells.

```java
class Solution {
    int[][] img1, img2;
    int n;
    public int largestOverlap(int[][] img1, int[][] img2) {
        n = img1.length;
        this.img1 = img1;
        this.img2 = img2;
        int max = 0;
        for (int i = -n + 1; i < n; i++) {
            for (int j = -n + 1; j < n; j++) {
                max = Math.max(max, overlap(i, j));
            }
        }
        return max;
    }
    public int overlap(int rowOffset, int colOffset) {
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i + rowOffset < 0 || i + rowOffset >= n || j + colOffset < 0 || j + colOffset >= n) continue;
                if (img2[i][j] == 1 && img1[i + rowOffset][j + colOffset] == 1) cnt++;
            }
        }
        return cnt;
    }
}
```

T:  O(n^4)			S: O(1)

---

#### Count shifting ways

We can assume all possible shifting ways are shifting down some steps and then shifting right some steps.

Note that the steps can be negative.

So we can scan two images and for two points which `(i, j) (x, y)` both are 1, and then we can say we are shifting image1 from `(i, j)` to `(x, y)` by shifting `x - i` steps down and `y - j` steps right.

So the shifting ways are `[(x - i), (y - j)]`.

How to represent this shifting way?

1. **Use String or encoding it to an integer**
2. **Use two dimentional map.**

1. Use String to represent the shifting way.

   ```java
   class Solution {
       public int largestOverlap(int[][] img1, int[][] img2) {
           int n = img1.length;
           Map<String, Integer> count = new HashMap<>();
           int max = 0;
           for (int i = 0; i < n; i++) {
               for (int j = 0; j < n; j++) {
                   if (img1[i][j] == 0) continue;
                   for (int x = 0; x < n; x++) {
                       for (int y = 0; y < n; y++) {
                           if (img2[x][y] == 0) continue;
                           String s = (x - i) + ":" + (y - j);
                           count.put(s, count.getOrDefault(s, 0) + 1);
                           max = Math.max(max, count.get(s));
                       }
                   }
               }
           }
           return max;
       }
   }
   ```

   T: O(n^4)		S: O(n^4)

2. Use encoding to integer to represent shifting way.

   Since the length of image is smaller than 30, we can use `row * 100 + col` to encode the `row` and `col`.

   ```java
   class Solution {
       public int largestOverlap(int[][] img1, int[][] img2) {
           int n = img1.length;
           Map<Integer, Integer> count = new HashMap<>();
           int max = 0;
           for (int i = 0; i < n; i++) {
               for (int j = 0; j < n; j++) {
                   if (img1[i][j] == 0) continue;
                   for (int x = 0; x < n; x++) {
                       for (int y = 0; y < n; y++) {
                           if (img2[x][y] == 0) continue;
                           int index = (x - i) * 100 + y - j;
                           count.put(index, count.getOrDefault(index, 0) + 1);
                           max = Math.max(max, count.get(index));
                       }
                   }
               }
           }
           return max;
       }
   }
   ```

   T: O(n^4)		S: O(1)

3. Use two dimentional map.

   We use `count[][]` to count the number of cells using shifting way `count[x - i][y - j]`

   ```java
   class Solution {
       public int largestOverlap(int[][] img1, int[][] img2) {
           int n = img1.length;
           int[][] count = new int[2 * n][2 * n];
           for (int i = 0; i < n; i++) {
               for (int j = 0; j < n; j++) {
                   if (img1[i][j] == 0) continue;
                   for (int x = 0; x < n; x++) {
                       for (int y = 0; y < n; y++) {
                           if (img2[x][y] == 0) continue;
                           count[x - i + n][y - j + n]++;
                       }
                   }
               }
           }
           int max = 0;
           for (int[] row : count) {
               for (int v : row) {
                   max = Math.max(max, v);
               }
           }
           return max;
       }
   }
   ```

   T: O(n^4)		S: O(1)

