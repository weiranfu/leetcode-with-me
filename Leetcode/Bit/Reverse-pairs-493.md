---
title: Hard | Reverse Pairs 493
tags:
  - common
  - tricky
categories:
  - Leetcode
  - BIT
date: 2020-07-31 20:32:01
---

Given an array `nums`, we call `(i, j)` an **important reverse pair** if `i < j` and `nums[i] > 2*nums[j]`.

You need to return the number of important reverse pairs in the given array.

[Leetcode](https://leetcode.com/problems/reverse-pairs/)

<!--more-->

**Example1:**

```
Input: [1,3,2,3,1]
Output: 2
```

**Example2:**

```
Input: [2,4,3,5,1]
Output: 3
```

**Follow up:** 

[Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

[Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)

[Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

---

#### Merge Sort and Count

During merge sort, we have two sorted array A and B.

We can easily count the number of pairs cross two arrays.

If we find `A[i] > 2 * B[j]`, then `A[i]` is larger than `B[mid+1], B[mid+2],...,B[j]`

And we find `(j - mid)` pairs for `A[i]`.

And increase `i` and continue to find `j` that `A[i] > 2 * B[j]` to compute the numbers.

```java
class Solution {
    int[] nums, tmp;
    
    public int reversePairs(int[] nums) {
        int n = nums.length;
        this.nums = nums;
        tmp = new int[n];
        return mergeCount(0, n - 1);
    }
    private int mergeCount(int l, int r) {
        if (l >= r) return 0;
        int mid = l + (r - l) / 2;
        int cnt = mergeCount(l, mid) + mergeCount(mid + 1, r);
        int j = mid + 1;
        for (int i = l; i <= mid; i++) {				// O(n) time complexity
            while (j <= r && nums[i] > nums[j] * 2L) j++; // 2L to avoid overflow
            cnt += j - mid - 1;
        }
        /* merge two array */
        int k = 0, i = l; j = mid + 1;
        while (i <= mid && j <= r) {
            if (nums[i] <= nums[j]) tmp[k++] = nums[i++];
            else tmp[k++] = nums[j++];
        }
        while (i <= mid) tmp[k++] = nums[i++];
        while (j <= r) tmp[k++] = nums[j++];
        for (i = l, j = 0; i <= r; i++, j++) nums[i] = tmp[j];
        return cnt;
    }
}
```

T: O(nlogn)			S: O(n)

---

#### BIT

This is typical problem can be solved by BIT.

We need to find how many `i` that `nums[i] > 2 * nums[j]` that `i < j`

Before we insert into BIT, we query how many `i` that is larger than `2 * nums[j]`

Then we insert `nums[j]` into BIT.

**So we need a reversed BIT to query larger elements.**

```java
class Solution {
    List<Long> list;
    int[] sum;
    int N;
    
    public int reversePairs(int[] nums) {
        int n = nums.length;
        list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add((long)nums[i]);
            list.add(nums[i] * 2L);
        }
        list = new ArrayList<>(new HashSet(list));
        Collections.sort(list);
        N = list.size();
        
        sum = new int[N + 1];
        
        int res = 0;
        for (int i = 0; i < n; i++) {
            int idx1 = find(2L * nums[i]);
            int idx2 = find((long)nums[i]);
            res += query(idx1 + 1);
            add(idx2);
        }
        return res;
    }
    private void add(int x) {
        for (int i = x; i > 0; i -= i & (-i)) {
            sum[i]++;
        }
    }
    private int query(int x) {
        int res = 0;
        for (int i = x; i <= N; i += i & (-i)) res += sum[i];
        return res;
    }
    private int find(long x) {
        int l = 0, r = N - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (list.get(mid) == x) return mid + 1;
            else if (list.get(mid) > x) r = mid - 1;
            else l = mid + 1;
        }
        return -1;
    }
}
```

T: O(nlogn)		S: O(n)



