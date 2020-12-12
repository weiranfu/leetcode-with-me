---
title: Hard | Maximum Gap 164
tags:
  - tricky
categories:
  - Leetcode
  - Sort
date: 2020-06-03 20:43:18
---

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Try to solve it in linear time and space.

[Leetcode](https://leetcode.com/problems/maximum-gap/)

<!--more-->

**Example 1:**

```
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
```

**Example 2:**

```
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
```

---

#### Tricky 

We need to sort them and find the maximum gap.

**How to sort them in O(n)?  Use radix sort / bucket sort**.

* Radix sort:

  Cause we are sorting integers, we could use radix sort base on each digit.

* Bucket sort:

  We only care about the minimum gap, so we could try to put each integers into bucket except for max and min value.

  According to Pigeonhole principle, if we put `n - 2` elements into `n - 1` buckets, there must exist one bucket empty. So the maximum gap must come from two buckets, rather than come from within a bucket.

---

#### My thoughts 

Failed to solve.

---

#### Radix Sort

Sort integers base on digits.

```java
class Solution {
    public int maximumGap(int[] nums) {
        if (nums == null || nums.length < 2) return 0;
        int n = nums.length;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, nums[i]);
        }
        int[] tmp = new int[n];
        int base = 1;
        while (max != 0) {
            int[] count = new int[10];
            for (int i = 0; i < n; i++) {
                int digit = nums[i] / base % 10;    // get current digit.
                count[digit]++;
            }
            for (int i = 1; i < 10; i++) {
                count[i] += count[i - 1];
            }
            for (int i = n - 1; i >= 0; i--) {      // sort base on digit.
                int digit = nums[i] / base % 10;
                int pos = count[digit] - 1;
                tmp[pos] = nums[i];
                count[digit]--;
            }
            for (int i = 0; i < n; i++) {
                nums[i] = tmp[i];
            }
            max = max / 10;
            base = base * 10;
        }
        int res = Integer.MIN_VALUE;
        for (int i = 1; i < n; i++) {
            res = Math.max(res, nums[i] - nums[i - 1]);
        }
        return res;
    }
}
```

T: O(n)		S: O(n)

---

#### Bucket sort

We only need to record the max and min value in each buckets, then we could get the max gap between buckets.

```java
class Solution {
    public int maximumGap(int[] nums) {
        if (nums == null || nums.length < 2) return 0;
        int n = nums.length;
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, nums[i]);
            min = Math.min(min, nums[i]);
        }
        int d = max - min;
        if (d == 0) return 0;                        // corner case.
        int[] minBuckets = new int[n - 1];           // n - 1 buckets for n - 2 integers
        int[] maxBuckets = new int[n - 1];
        Arrays.fill(minBuckets, Integer.MAX_VALUE);
        Arrays.fill(maxBuckets, Integer.MIN_VALUE);
        
        for (int i : nums) {
            if (i == min || i == max) continue;      // don't throw max/min into buckets.
            int pos = (int) ((double) (i - min) / d * (n - 2));  // get index of bucket.
            minBuckets[pos] = Math.min(minBuckets[pos], i);
            maxBuckets[pos] = Math.max(maxBuckets[pos], i);
        }
        int res = Integer.MIN_VALUE;
        int prev = min;
        for (int i = 0; i < n - 1; i++) {
            if (minBuckets[i] == Integer.MAX_VALUE && maxBuckets[i] == Integer.MIN_VALUE) continue;
            res = Math.max(res, minBuckets[i] - prev);         // get max gap
            prev = maxBuckets[i];
        }
        res = Math.max(res, max - prev);              
        return res;
    }
}
```

T: O(n)			S: O(n)

---

#### Summary 

Sorting integers based on digits could achieve O(n) time complexity.