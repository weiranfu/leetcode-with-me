---
title: Medium | Advantage Shuffle 870
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-08-26 15:47:13
---

Given two arrays `A` and `B` of equal size, the *advantage of A with respect to B* is the number of indices `i` for which `A[i] > B[i]`.

Return **any** permutation of `A` that maximizes its advantage with respect to `B`.

[Leetcode](https://leetcode.com/problems/advantage-shuffle/)

<!--more-->

**Example 1:**

```
Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
```

**Example 2:**

```
Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
```

**Note:**

1. `1 <= A.length = B.length <= 10000`
2. `0 <= A[i] <= 10^9`
3. `0 <= B[i] <= 10^9`

---

#### Sort 

Sort `A` and `B`. And compare the smallest items of `A` and `B`.

If `A[i] > B[i]`, keep the order.

If `A[i] <= B[i]`, move `A[i]` to the end of array.

Since we cannot modify the order of `B`, we could sort the indices of `B` and change back the order of result according to the indices.

```java
class Solution {
    public int[] advantageCount(int[] A, int[] B) {
        int n = A.length;
        int[] indices = new int[n];
        for (int i = 0; i < n; i++) indices[i] = i;
        Arrays.sort(A); 
        indices = Arrays.stream(indices)
                        .boxed()
                        .sorted((a, b) -> B[a] - B[b]) // sorted indices based on B
                        .mapToInt(i -> i)
                        .toArray();
        int[] a = new int[n];
        int l = 0, r = n - 1;
        int i = 0, j = 0;
        while (l <= r) {
            if (A[i] > B[indices[j]]) {
                a[l++] = A[i++];
                j++;
            } else {
                a[r--] = A[i++];
            }
        }
        int[] res = new int[n];
        for (i = 0; i < n; i++) {
            int index = indices[i];
            res[index] = a[i];
        }
        return res;
    }
}
```

T: O(nlogn)			S: O(n)

2. Linked List

We could sort `B` with indices using a Linked List.

```java
class Solution {
    public int[] advantageCount(int[] A, int[] B) {
        int n = A.length;
        Arrays.sort(A);
        LinkedList<int[]> list = new LinkedList<>();
        for (int i = 0; i < n; i++) list.addLast(new int[]{B[i], i});
        Collections.sort(list, (a, b) -> a[0] - b[0]);
        int[] res = new int[n];
        int curr = 0;
        while (!list.isEmpty()) {
            int[] info = list.peekFirst();
            int idx = info[1], val = info[0];
            if (A[curr] > val) {
                res[idx] = A[curr++];
                list.pollFirst();
            } else {
                int index = list.pollLast()[1];
                res[index] = A[curr++];
            }
        }
        return res;
    }
}
```

T:  O(nlogn)		S: O(n)

---

#### TreeMap  

Count elements in `A` to a map `m`.
For each element in `B`, find the least bigger element in map `m`.
Otherwise, we'll take the smallest element.
Then we update the `m`.

```java
class Solution {
    public int[] advantageCount(int[] A, int[] B) {
        int n = A.length;
        TreeMap<Integer, Integer> map = new TreeMap<>();
        for (int i = 0; i < n; i++) map.put(A[i], map.getOrDefault(A[i], 0) + 1);
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            Integer high = map.higherKey(B[i]);
            if (high == null) high = map.firstKey();
            res[i] = high;
            map.put(high, map.get(high) - 1);
            if (map.get(high) == 0) map.remove(high);
        }
        return res;
    }
}
```

T: O(nlogn)			S: O(n)

