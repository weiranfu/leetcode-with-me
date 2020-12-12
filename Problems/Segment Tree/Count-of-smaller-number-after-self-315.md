---
title: Hard | Count of Smaller Number after Self 315
tags:
  - tricky
categories:
  - Leetcode
  - Segment Tree
date: 2020-06-25 21:37:14
---

You are given an integer array *nums* and you have to return a new *counts* array. The *counts* array has the property where `counts[i]` is the number of smaller elements to the right of `nums[i]`.

[Leetcode](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

<!--more-->

**Example:**

```
Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
```

**Follow up**

[Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

[Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)

[Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

---

#### Merge sort

Divide array into `[l, mid]` `[mid + 1, r]`

1. Divide array into two parts [l, mid] [mid+1, r]
2. Count the number of pairs in left part and right part
3. Count the number of pairs with one member in left part other member in right part.
4. return the total count

How to count 3?
**We need sort the array in descending order, because during the steps merging two sorted array, If we find `A[i] > B[j]`, then A[i] > all of them `B[j]`, `B[j+1]`,….`B[r]`**

So we can add result to `cnt[A[i]] += r - j + 1` and `i++`

**To record the result, we need to keep the index of each number in the original array. So instead of sort the number in nums, we sort the indexes of each number.**

```java
class Solution {
    
    int[] A, tmp;
    int[] indices;
    int[] cnt;
    
    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        A = nums;
        tmp = new int[n];
        cnt = new int[n];
        indices = new int[n];
        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }
        mergeSort(0, n - 1);
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; i++) res.add(cnt[i]);
        return res;
    }
    
    private void mergeSort(int l, int r) {
        if (l >= r) return;
        int mid = l + (r - l) / 2;

        mergeSort(l, mid);    // count left & right part
        mergeSort(mid + 1, r);

        int k = 0, i = l, j = mid + 1;
        while (i <= mid && j <= r) {
            if (A[indices[i]] <= A[indices[j]]) tmp[k++] = indices[j++];
            else {
                cnt[indices[i]] += r - j + 1;       // count cross pairs  
                tmp[k++] = indices[i++];
            }
        }
        while (i <= mid) tmp[k++] = indices[i++];
        while (j <= r) tmp[k++] = indices[j++];
        for (i = l, j = 0; i <= r; i++, j++) indices[i] = tmp[j];
    }
}
```

T: O(nlogn)			S: O(n)

------

#### Binary Index Tree

Scan from right to left and count number of smaller elements.

```java
class Solution {
    int N;
    int[] sum;
    List<Integer> list;
    
    public List<Integer> countSmaller(int[] nums) {
        List<Integer> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        int n = nums.length;
        list = new ArrayList<>();
        for (int num : nums) list.add(num);
        list = new ArrayList<>(new HashSet<>(list));
        Collections.sort(list);
        N = list.size();
        
        sum = new int[N + 1];
        for (int i = n - 1; i >= 0; i--) {
            int idx = find(nums[i]);
            int count = query(idx - 1);    // query in range (0, idx - 1)
            res.add(count);
            add(idx);
        }
        Collections.reverse(res);
        return res;
    }
    
    private int find(int x) {
        int l = 0, r = N - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (list.get(mid) == x) return mid + 1;		// return idx + 1
            else if (list.get(mid) < x) l = mid + 1;
            else r = mid - 1;
        }
        return -1;
    }
    private void add(int x) {
        for (int i = x; i <= N; i += i & (-i)) {
            sum[i]++;
        }
    }
    private int query(int x) {
        int res = 0;
        for (int i = x; i > 0; i -= i & (-i)) {
            res += sum[i];
        }
        return res;
    }
}
```

T: O(nlogn)			S: O(n)

---

#### Segment Tree

权值线段树+离散化

We want to know the number of `nums` that smaller than a num. 

The data structure that provides `add a new num`, `query count of nums in a range ` just like a balanced binary tree or weighted segment tree with discretization.

We can query in range `[0, num - 1]` to get the count number. Save `cnt` in tree node.

```java
class Solution {
    
    int[] tree;
    int N;
    List<Integer> list;
    
    public List<Integer> countSmaller(int[] nums) {
        List<Integer> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        list = new ArrayList<>();
        int n = nums.length;
        for (int num : nums) list.add(num);
        list = new ArrayList<>(new HashSet<>(list));
        Collections.sort(list);
        N = list.size();
        
        tree = new int[N << 2];
        
        for (int i = n - 1; i >= 0; i--) {
            int idx = find(nums[i]);
            int count = query(idx - 1, 0, N, 0);// query count in range [0, idx - 1]
            res.add(count);
            add(idx, 0, N, 0);                // add this value
        }
        Collections.reverse(res);
        return res;
    }
    
    public void add(int idx, int l, int r, int n) {
        if (l == r) {
            tree[n]++;
            return;
        }
        int mid = l + (r - l) / 2;
        if (idx <= mid) {
            add(idx, l, mid, n * 2 + 1);
        } else {
            add(idx, mid + 1, r, n * 2 + 2);
        }
        
        tree[n] = tree[n * 2 + 1] + tree[n * 2 + 2];
    }
    
    public int query(int idx, int l, int r, int n) {  // query in range [0, idx]
        if (r <= idx) {
            return tree[n];
        }
        int mid = l + (r - l) / 2;
        int res = query(idx, l, mid, n * 2 + 1);
        if (mid < idx) res += query(idx, mid + 1, r, n * 2 + 2);
        return res;
    }
    
    private int find(int x) {
        int l = 0, r = N - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (list.get(mid) == x) return mid + 1; // return idx + 1
            else if (list.get(mid) > x) r = mid - 1;
            else l = mid + 1;
        }
        return -1;
    }
}
```

T: O(nlogn)		S: O(n)

