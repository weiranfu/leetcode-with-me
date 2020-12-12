---
title: Hard | Find a Value of a Mysterious Function Closest to Target 1521
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-07-19 13:42:02
---

![img](https://assets.leetcode.com/uploads/2020/07/09/change.png)

Winston was given the above mysterious function `func`. He has an integer array `arr` and an integer `target` and he wants to find the values `l` and `r` that make the value `|func(arr, l, r) - target|` minimum possible.

Return *the minimum possible value* of `|func(arr, l, r) - target|`.

Notice that `func` should be called with the values `l` and `r` where `0 <= l, r < arr.length`.

[Leetcode](https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/)

<!--more-->

**Example 1:**

```
Input: arr = [9,12,3,7,15], target = 5
Output: 2
Explanation: Calling func with all the pairs of [l,r] = [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]], Winston got the following results [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0]. The value closest to 5 is 7 and 3, thus the minimum difference is 2.
```

**Constraints:**

- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 10^6`
- `0 <= target <= 10^7`

**Follow up:** 

[Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/)

---

#### 1. Segment Tree

We're asking the bitwise AND of many intervals of an array. We could use segment tree to compute the bitwise AND of intervals and achieve the min value.

We need to initialize the tree node to `(1 << 31) - 1`.

```java
class Solution {
    int INF = 0x3f3f3f3f;
    int N = 100010;
    int[] tree = new int[N << 2];
    int[] arr;
    int target;
    int min = INF;
    
    public int closestToTarget(int[] arr, int target) {
        int n = arr.length;
        this.arr = arr;
        this.target = target;
        Arrays.fill(tree, (1 << 31) - 1);					// initialize
        for (int i = 0; i < n; i++) {
            add(i, 0, N, 0);
        }
        return min;
    }
    private void add(int x, int l, int r, int n) {
        if (l == r) {
            tree[n] = arr[x];
            min = Math.min(min, Math.abs(tree[n] - target)); // get min value
            return;
        }
        int mid = l + (r - l) / 2;
        if (x <= mid) {
            add(x, l, mid, 2 * n + 1);
        } else {
            add(x, mid + 1, r, 2 * n + 2);
        }
        tree[n] = (tree[2 * n + 1] & tree[2 * n + 2]);  // & two subtrees
        min = Math.min(min, Math.abs(tree[n] - target));// get min value
    }
}
```

T: O(nlogn)		S: O(n)

---

#### 2. Binary Search

We could simplify the `abs(fun - target)` into

`min(fun)` if `fun > target`

`max(fun)` if `fun < target`

**For a interval [l, r], if we fix l bound the bitwise AND of [l, r] is monotic**

Because we can only decrease the value of bitwise AND from `1` to `0`

So as `r` increases, `fun` will become less.

However we need to get the bitwise AND of an interval in O(1), then we can perform BinarySearch

Use Sparse Table to get AND of an interval in O(1)

Then we could use Binary Search to find the `min(fun) > target`.

And the next value will be the `max(fun) > target`.

---

#### Optimized

If we keep the preSum of bitwise value of `A[i]` in a list, 

`A[0], A[0]&A[1], A[0]&A[1]&A[2], ..., A[0]&A[1]&..&A[i]`, every time we consider a new item `A[i+1]`

we just need to do a bitwise AND with all preSum value in the list and add `A[i + 1]` into list.

On a first glance, it seems size of list is O(n), and therefore to calculate one dp needs O(n) time. Looping all dps will give O(n^2) time. But actually, size(dp) <= 32, the maxium number of bits in a int variable. This because: All the elements (in the order of above sequence) in list is non-increasing by flipping 1 bits to 0 from A[i]. Since there are at most 32 1s in A[i]. Thus the size of the set is <= 32.

**So we use a Set instead of list to remove duplicate result.**

```java
class Solution {
    public int closestToTarget(int[] arr, int target) {
        int n = arr.length;
        Set<Integer> set = new HashSet<>();
        int min = Integer.MAX_VALUE;
        for (int a : arr) {
            Set<Integer> newSet = new HashSet<>();
            for (int b : set) {
                newSet.add(b & a);
            }
            newSet.add(a);
            for (int b : newSet) {
                min = Math.min(min, Math.abs(b - target));
            }
            set = newSet;
        }
        return min;
    }
}
```

T: O(n)			S: O(n)

