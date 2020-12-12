---
title: Medium | Kth Smallest Element in a Sorted Matrix 378
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-06-26 14:15:12
---

Given a *n* x *n* matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

[Leetcode](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

<!--more-->

**Example:**

```
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
```

---

#### Tricky 

* Breadth First Search

  We can see the smallest corner is at top left corner and the largest corner is at the bottom right corner.

  So we could perform BFS to find the Kth smallest element. Each time we search out neighbors.

* Merge K sorted List

  Since the `m` rows are sorted, we could just pretend to merge these `m` sorted rows to find the Kth smallest element. We keep `m` pointers to `m` rows' head, and add them into a Priority Queue. Each time we poll out a smallest one, we add its successor into priority queue.

* Binary Search

  Since each row and column of the matrix is sorted, is it possible to use **Binary Search** to find the Kth smallest number?

  The biggest problem to use **Binary Search** in this case is that we don’t have a straightforward sorted array, instead we have a matrix. As we remember, in **Binary Search**, we calculate the middle index of the search space (‘1’ to ‘N’) and see if our required number is pointed out by the middle index; if not we either search in the lower half or the upper half. In a sorted matrix, we can’t really find a middle. Even if we do consider some index as middle, it is not straightforward to find the search space containing numbers bigger or smaller than the number pointed out by the middle index.

  An alternate could be to apply the **Binary Search** on the “number range” instead of the “index range”. As we know that the smallest number of our matrix is at the top left corner and the biggest number is at the bottom lower corner. These two number can represent the “range” i.e., the `start` and the `end` for the **Binary Search**. Here is how our algorithm will work:

  1. Start the **Binary Search** with `start = matrix[0][0]` and `end = matrix[n-1][n-1]`.
  2. Find `middle` of the `start` and the `end`. This `middle` number is NOT necessarily an element in the matrix.
  3. Count all the numbers smaller than or equal to `middle` in the matrix. As the matrix is sorted, we can do this in O(N).
  4. While counting, we can keep track of the “smallest number greater than the `middle`” (let’s call it `n1`) and at the same time the “biggest number less than or equal to the `middle`” (let’s call it `n2`). These two numbers will be used to adjust the "number range" for the **Binary Search** in the next iteration.
  5. If the count is equal to ‘K’, `n1` will be our required number as it is the “biggest number less than or equal to the `middle`”, and is definitely present in the matrix.
  6. If the count is less than ‘K’, we can update `start = n2` to search in the higher part of the matrix and if the count is greater than ‘K’, we can update `end = n1` to search in the lower part of the matrix in the next iteration.

---

#### BFS

```java
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        if (matrix == null || matrix.length == 0) return -1;
        int m = matrix.length;
        int n = matrix[0].length;
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> matrix[a[0]][a[1]] - matrix[b[0]][b[1]]);
        queue.add(new int[]{0, 0});
        int[][] moves = {{0, 1}, {1, 0}};
        boolean[][] visited = new boolean[m][n];
        int cnt = 0;
        while (!queue.isEmpty()) {
            int[] info = queue.poll();
            int i = info[0];
            int j = info[1];
            cnt++;
            if (cnt == k) return matrix[i][j];
            for (int[] move : moves) {
                int x = i + move[0];
                int y = j + move[1];
                if (x >= m || y >= n || visited[x][y]) continue;
                visited[x][y] = true;               // mark true when adding into queue
                queue.add(new int[]{x, y});
            }
        }
        return -1;
    }
}
```

T: O(klog(Math.max(m, n)))			S: O(mn)

---

#### Merge K sorted list

```java
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        if (matrix == null || matrix.length == 0) return -1;
        int m = matrix.length;
        int n = matrix[0].length;
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> matrix[a[0]][a[1]] - matrix[b[0]][b[1]]);
        for (int i = 0; i < m; i++) {
            queue.add(new int[]{i, 0});
        }
        int cnt = 0;
        while (!queue.isEmpty()) {
            int[] info = queue.poll();
            int i = info[0];
            int j = info[1];
            cnt++;
            if (cnt == k) return matrix[i][j];
            if (j + 1 < n) queue.add(new int[]{i, j + 1});
        }
        return -1;
    }
}
```

T: O(m + klogm)		S: O(m)

---

#### Binary Search

```java
class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        if (matrix == null || matrix.length == 0) return -1;
        int m = matrix.length;
        int n = matrix[0].length;
        int l = matrix[0][0], r = matrix[m - 1][n - 1];
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int[] info = count(matrix, mid);
            if (info[0] == k) return info[1];
            else if (info[0] < k) {
                l = info[2];           // higher
            } else if (info[0] > k) {
                r = info[1] - 1;       // lower - 1
            }
        }
        return l;
    }
    
    public int[] count(int[][] matrix, int val) {
        int[] res = new int[3];
        int m = matrix.length;
        int n = matrix[0].length;
        int count = 0;
        int i = m - 1, j = 0;
        int lower = Integer.MIN_VALUE, higher = Integer.MAX_VALUE;
        while (i >= 0 && j < n) {
            if (matrix[i][j] <= val) {
                lower = Math.max(lower, matrix[i][j]);
                count += i + 1;
                j++;
            } else {
                higher = Math.min(higher, matrix[i][j]);
                i--;
            }
        }
        res[0] = count;
        res[1] = lower;
        res[2] = higher;
        return res;
    }
}
```

- Time Complexity: *O*(*N*×*l**o**g*(Max−Min))
  - Let's think about the time complexity in terms of the normal binary search algorithm. For a one-dimensional binary search over an array with N*N* elements, the complexity comes out to be O(log(N)).
  - For our scenario, we are kind of defining our binary search space in terms of the minimum and the maximum numbers in the array. Going by this idea, the complexity for our binary search should be *O*(*l**o**g*(Max−Min)) where Max is the maximum element in the array and likewise, Min is the minimum element.
- Space Complexity: O(1)

