---
title: Medium | Divide Array in Sets of K Consecutive Numbers 1296
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2019-12-22 16:55:46
---

Given an array of integers `nums` and a positive integer `k`, find whether it's possible to divide this array into sets of `k` consecutive numbers
Return `True` if its possible otherwise return `False`.

[Leetcode](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/)

<!--more-->

**Example 1:**

```
Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
```

**Example 2:**

```
Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
```

**Example 3:**

```
Input: nums = [3,3,2,2,1,1], k = 3
Output: true
```

**Example 4:**

```
Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
```

---

#### Tricky 

How to make sure that we find consecutive numbers from the smallest one?

* Sort `nums` firstly.
* Use `TreeMap`.

---

#### First solution 

Sort `nums` firstly, then we start at smallest item, change its consecutive nums to `-1`.

```java
class Solution {
    public boolean isPossibleDivide(int[] nums, int k) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; i += 1) {
            if (nums[i] < 0) continue;
            int target = nums[i] + 1;
            int count = 1;
            for (int j = i + 1; j < nums.length; j += 1) {
                if (count == k) {
                    break;
                }
                if (nums[j] == target) {
                    target += 1;
                    count += 1;
                    nums[j] = -1;
                }
            }
        }
        int pair = 0;
        for (int i = 0; i < nums.length; i += 1) {
            if (nums[i] != -1) {
                pair += 1;
            }
        }
        return pair * k == nums.length;
    }
}
```

T: O(n^2) S: O(1)

---

#### Sort and HashMap

We sort nums firstly, then use HashMap to store occurrence of each num.

```java
class Solution {
    public boolean isPossibleDivide(int[] nums, int k) {
        Arrays.sort(nums);
        Map<Integer, Integer> map = new HashMap<>();
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        for (int n : nums) {
            if (map.get(n) <= 0) continue;
            for (int i = 0; i < k; i += 1) {
                if (!map.containsKey(n + i) || map.get(n + i) <= 0) {
                    return false;
                } else {
                    map.put(n + i, map.get(n + i) - 1);
                }
            }
        }
        return true;
    }
}
```

T: O(nLogn) S: O(n)

---

#### TreeMap

We don't need to sort nums, TreeMap will do this for us.

```java
class Solution {
    public boolean isPossibleDivide(int[] nums, int k) {
        if (nums.length % k != 0) return false; // For the case that they're not pairs.
        Map<Integer, Integer> map = new TreeMap<>();
        for (int n : nums) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
        // Because this is a keySet, so there might not be any duplicate int n.
        for (int n : map.keySet()) { 
            int pairs = map.get(n);
            if (pairs <= 0) continue;
            System.out.println(n);
            for (int i = 0; i < k; i += 1) {
                if (!map.containsKey(n + i) || map.get(n + i) <= 0) {
                    return false;
                } else {
                    // We need to remove duplicate pairs.
                    map.put(n + i, map.get(n + i) - pairs);  
                }
            }
        }
        return true;
    }
}
```

T: O(nLogn) S: O(n)

---

#### Summary 

How to make sure that we find consecutive numbers from the smallest one?

- Sort `nums` firstly.
- Use `TreeMap`.