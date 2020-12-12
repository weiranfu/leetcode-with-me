---
title: Medium | Range Sum Query - Mutable 307
tags:
  - tricky
categories:
  - Leetcode
  - Segment Tree
date: 2020-06-18 07:04:55
---

Given an integer array *nums*, find the sum of the elements between indices *i* and *j* (*i* ≤ *j*), inclusive.

The *update(i, val)* function modifies *nums* by updating the element at index *i* to *val*.

[Leetcode](https://leetcode.com/problems/range-sum-query-mutable/)

<!--more-->

**Example:**

```
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
```

**Note:**

1. The array is only modifiable by the *update* function.
2. You may assume the number of calls to *update* and *sumRange* function is distributed evenly.

**Follow up:** 

[Range Sum Query - Immutable](https://aranne.github.io/2020/06/18/Range-sum-query-immutable-303/#more)	

[Range Sum Query - Mutable](https://aranne.github.io/2020/06/18/Range-sum-query-mutable-307/#more)

[Range Sum Query 2D - Immutable](https://aranne.github.io/2020/06/18/Range-sum-query-2D-immutable/#more)

[Range Sum Query 2D - Mutable](https://aranne.github.io/2020/06/18/Range-sum-query-2D-mutable-308/#more)

---

#### Tricky 

* Segment Tree

* Binary Index Tree (Fenwick Tree)

  BIT is 1 based array.

---

#### Segment Tree

```java
class NumArray {
    
    int[] tree;
    int[] nums;

    public NumArray(int[] nums) {
        int n = nums.length;
        this.nums = nums;
        tree = new int[n << 2];
        build(0, n - 1, 0);
    }
    
    private void build(int l, int r, int rt) {
        if (l == r) {
            tree[rt] = nums[l];
            return;
        }
        int mid = l + (r - l) / 2;
        build(l, mid, rt * 2 + 1);
        build(mid + 1, r, rt * 2 + 2);
        
        tree[rt] = tree[rt * 2 + 1] + tree[rt * 2 + 2];
    }
    
    public void update(int i, int val) {
        update(i, val, 0, nums.length - 1, 0);
    }
    
    private void update(int i, int val, int l, int r, int rt) {
        if (l == r) {
            tree[rt] = val;
            nums[i] = val;
            return;
        }
        int mid = l + (r - l) / 2;
        if (i <= mid) {
            update(i, val, l, mid, rt * 2 + 1);
        } else {
            update(i, val, mid + 1, r, rt * 2 + 2);
        }
        
        tree[rt] = tree[rt * 2 + 1] + tree[rt * 2 + 2];
    }
    
    public int sumRange(int i, int j) {
        return sum(i, j, 0, nums.length - 1, 0);
    }
    
    private int sum(int L, int R, int l, int r, int rt) {
        if (L <= l && r <= R) {
            return tree[rt];
        }
        int mid = l + (r - l) / 2;
        int ans = 0;
        if (mid >= L) ans += sum(L, R, l, mid, rt * 2 + 1);
        if (mid < R) ans += sum(L, R, mid + 1, r, rt * 2 + 2);
        return ans;
    }
}
```

T: O(logn)			S: O(n)

---

#### Binary Index Tree 

BIT is 1 based, so we need to move array one step right.

```java
class NumArray {
    
    int[] sum;
    int[] nums;

    public NumArray(int[] nums) {
        int n = nums.length;
        this.nums = nums;
        sum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            add(i + 1, nums[i]);         // one step right
        }
    }
    
    public void add(int i, int delta) {
        while (i < sum.length) {
            sum[i] += delta;
            i += lowbit(i);
        }
    }
    
    private int query(int i) {
        int res = 0;
        while (i > 0) {
            res += sum[i];
            i -= lowbit(i);
        }
        return res;
    }
    
    public void update(int i, int val) {
        int delta = val - nums[i];
        nums[i] = val;
        add(i + 1, delta);               // one step right
    }
    
    public int sumRange(int i, int j) {
        return query(j + 1) - query(i);  // one step right
    }
    
    private int lowbit(int x) {
        return x & (-x);
    }
}
```

T: O(logn)		S: O(n)

