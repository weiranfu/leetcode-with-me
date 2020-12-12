---
title: Medium | Contains Duplicate III 220
tags:
  - tricky
  - oh-no
categories:
  - Leetcode
  - TreeMap
date: 2020-06-18 18:26:20
---

Given an array of integers, find out whether there are two distinct indices *i* and *j* in the array such that the **absolute** difference between **nums[i]** and **nums[j]** is at most *t* and the **absolute** difference between *i* and *j* is at most *k*.

[Leetcode](https://leetcode.com/problems/contains-duplicate-iii/)

<!--more-->

**Example 1:**

```
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
```

**Example 2:**

```
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
```

**Example 3:**

```
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
```

---

#### Tricky

1. TreeMap

   This problem requires us to find i*i* and j*j* such that the following conditions are satisfied:

   1. `|i - j| <= k`
   2. `|nums[i] - nums[j]| <= t`

   * If elements in the window are maintained in sorted order, we can apply binary search twice to check if [Condition 2](https://leetcode.com/problems/contains-duplicate-iii/solution/#condition-2) is satisfied.

   * By utilizing self-balancing Binary Search Tree, one can keep the window ordered at all times with logarithmic time `insert` and `delete`.

   Unfortunately, the window is unsorted. A common mistake here is attempting to maintain a sorted array. Although searching in a sorted array costs only logarithmic time, keeping the order of the elements after `insert` and `delete` operation is not as efficient

   To gain an actual speedup, we need a *dynamic* data structure that supports faster `insert`, `search` and `delete`. Self-balancing Binary Search Tree (BST) is the right data structure. 

   So with balanced BST, we could easily find the *smallest* item that is greater than or equal to `key` and find the *largest* item that is smaller than or equal to `key`.

   Then we could check Condition 2 is satisfied.

2. Bucket sort

   In order to check that for a given element `x` is there an item in the window that is within the range of `[x - t, x + t]`

   Inspired by `bucket sort`, we could maintain buckets `[0, t], [t + 1, 2t], ...`

   For a given item `x`, we need to check its own buckets, previous and next buckets to find some item in range `[x - t, x + t]`.

   Since there're atmost one item in each bucket, we could use HashMap to represent the bucket with bucket id as key, item as value.

#### Oh-no

We need to mind the overflow.

If we want to check `nums[i] - floor <= t`, we could use `nums[i] <= t + floor` to avoid overflow.

---

#### My thoughts 

Failed to solve.

---

#### TreeMap

```java
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (nums == null || nums.length == 0) return false;
        int n = nums.length;
        TreeSet<Integer> set = new TreeSet<>();
        int left = 0;
        for (int i = 0; i < n; i++) {
            if (i - left > k) {
                set.remove(nums[left++]);
            }
            Integer floor = set.floor(nums[i]);
            Integer ceiling = set.ceiling(nums[i]);
            // nums[i] - floor <= t (in case for overflow)
            // so we write nums[i] <= t + floor
            if (floor != null && nums[i] <= t + floor) return true; 
            if (ceiling != null && ceiling <= t + nums[i]) return true;
            set.add(nums[i]);
        }
        return false;
    }
}
```

T: O(nlogk)			S: O(n)

---

#### Bucket

```java
class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (nums == null || nums.length == 0) return false;
        if (t < 0) return false;
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        int left = 0;
        int width = t + 1;
        for (int i = 0; i < n; i++) {
            if (i - left > k) {
                int preId = getId(nums[left++], width);
                map.remove(preId);
            }
            int id = getId(nums[i], width);
            if (map.containsKey(id)) return true;
            if (map.containsKey(id + 1) && map.get(id + 1) <= t + nums[i]) return true;
            if (map.containsKey(id - 1) && nums[i] <= t + map.get(id - 1)) return true;
            map.put(id, nums[i]);
        }
        return false;
    }
    
    private int getId(int x, int width) {
        return (x > 0) ? x / width : x / width - 1;
    }
}
```

T: O(n)			S: O(n)

