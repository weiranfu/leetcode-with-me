---
title: Medium | K Closest Points to Origin 973
tags:
  - tricky
categories:
  - Leetcode
  - Sort
date: 2019-11-26 23:28:14
---

We have a list of `points` on the plane.  Find the `K` closest points to the origin `(0, 0)`.

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

[Leetcode](https://leetcode.com/problems/k-closest-points-to-origin/)

<!--more-->

**Example 1:**

```
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
```

**Example 2:**

```
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
```

---

#### Tricky 

* Define a comparator for PriorityQueue or Arrays.sort

  `PriorityQueue<int[]> pq = `

  ​       `         new PriorityQueue<>((a, b) -> a[0]*a[0] + a[1]*a[1] - b[0]*b[0] - b[1]*b[1]);`

  `Arrays.sort(points, Comparator.comparing(p -> p[0] * p[0] + p[1] * p[1]));`

* We can implement quick sort to achieve O(n) rather than use priority queue for O(n*lgK) 

---

#### My thoughts 

Use PriorityQueue to get K smallest distance points.

---

#### First solution 

```java
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0]*a[0] + a[1]*a[1] - b[0]*b[0] - b[1]*b[1]);
        for (int[] point : points) {
            pq.offer(point);
        }
        int size = Math.min(K, pq.size());
        int[][] res = new int[size][2];
        for (int i = 0; i < size; i += 1) {
            res[i] = pq.poll();
        }
        return res;
    }
}
```

T: O(n*lgN) S: O(n)

---

#### Optimized 

If we change this priority queue to Max Heap, we just need to keep priority queue in size K.

We poll out larger one and keep K smallest one in priority queue.

Then time complexity will be O(n*lgK)!

```java
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[0]*b[0] + b[1]*b[1] - a[0]*a[0] - a[1]*a[1]);
        for (int[] point : points) {
            pq.offer(point);
            if (pq.size() > K) {
                pq.poll();
            }
        }
        int size = Math.min(K, pq.size());
        int[][] res = new int[size][2];
        for (int i = size - 1; i >= 0 ; i -= 1) {
            res[i] = pq.poll();
        }
        return res;
    }
}
```

T: O(n*lgK) S: O(K)

---

#### Arrays.sort()

Use `Arrays.sort()` to sort all points and get smallest K points.

```java
public int[][] kClosest(int[][] points, int K) {
        Arrays.sort(points, Comparator.comparing(p -> p[0] * p[0] + p[1] * p[1]));
        return Arrays.copyOfRange(points, 0, K);
    }
```

T: O(n*lgn) S: O(n)

---

#### Quick Sort

`Arrays.sort()` is O(n*lgn), so can implement quick sort to get O(n) time complexity.

```java
class Solution {
    public int [][] kClosest(int [][] points, int K){
        if (K == 0 || points.length == 0) return new int [][]{};
        int start = 0;
        int end = points.length - 1;
        while (start < end){
            int pos = partition(points, start, end);
            if (pos > K) end = pos - 1;
            else if (pos < K) start = pos + 1;
            else break;
        }
        return Arrays.copyOfRange(points, 0, K);
    }
    
    public int partition(int [][] points, int low, int high){
        int i = low;
        int [] pivot = points[high];
        for (int j = low; j < high; j++){
            if (compare(points[j], pivot) >= 0) swap(points, i++, j);
        }
        swap(points, i, high);
        return i;
    }
    
    public void swap(int [][] points, int i, int j){
        int [] temp = points[i];
        points[i] = points[j];
        points[j] = temp;
    }
    public int compare(int [] p1, int [] p2){
        return p2[0] * p2[0] + p2[1] * p2[1] - p1[0] * p1[0] - p1[1] * p1[1];
    }
}
```

T: O(n) S: O(n)

---

#### Summary 

We can implement quick sort to get O(n) time complexity rather than using priority queue for O(n*lgn).