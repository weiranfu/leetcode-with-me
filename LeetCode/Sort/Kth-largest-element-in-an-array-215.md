---
title: Medium | Kth Largest Element in an Array 215
tags:
  - tricky
categories:
  - Leetcode
  - Sort
date: 2020-06-11 17:46:29
---

Find the **k**th largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

[Leetcode](https://leetcode.com/problems/kth-largest-element-in-an-array/)

<!--more-->

**Example 1:**

```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

**Example 2:**

```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```

**Note:**
You may assume k is always valid, 1 ≤ k ≤ array's length.

---

#### Tricky 

We could use **Shuffle + Quick select** to find Kth largest element.

We use partition method in quick sort to partition elements in array and return pivot index.

If pivot index equals `nums.length - k`, then we have successfully partitioned the array.

---

#### Sort

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        if (nums == null || nums.length == 0) return -1;
        int n = nums.length;
        nums = Arrays.stream(nums).boxed().sorted().mapToInt(i -> i).toArray();
        return nums[n - k];
    }
}
```

T: O(nlogn)		S: O(1)

---

#### Priority Queue

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        if (nums == null || nums.length == 0) return -1;
        int n = nums.length;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i : nums) {
            pq.add(i);
            if (pq.size() > k) {
                pq.poll();
            }
        }
        return pq.poll();
    }
}
```

T: O(nlogk)			S: O(n)

---

#### QuickSort with Partition

Original partition function's time complexity is O(nlogn) on average. But for worst case that **all elements are same or array is sorted already, the time complexity will be O(n^2)**

**So we use `Random` to swap a random element with last element and use this as a pivot to achieve O(n) time complexity**

```java
class Solution {
    Random random;
    int k, n;
    
    public int findKthLargest(int[] nums, int k) {
        random = new Random();
        this.k = k;
        n = nums.length;
        return quickSort(nums, 0, n - 1, k);
    }
    
    private int quickSort(int[] A, int l, int r, int k) {
        if (l == r) return A[l];
				// randomly choose an element to swap with last element
        int rand = l + random.nextInt(r - l + 1);  
        swap(A, r, rand);
        int pivot = A[r];
        int i = l;
        for (int j = l; j <= r - 1; j++) {
            if (A[j] <= pivot) {
                swap(A, i, j);
                i++;
            }
        }
        swap(A, i, r);                             
        
      	// [l,i-1][i][i+1,r]
        if (i == n - k) return A[i];				// find target
        else if (i < n - k) return quickSort(A, i + 1, r, k);
        else return quickSort(A, l, i - 1, k);
    }
    
    private void swap(int[] nums, int a, int b) {
        int tmp = nums[a];
        nums[a] = nums[b];
        nums[b] = tmp;
    }
}
```

T: O(n)			S: O(1)