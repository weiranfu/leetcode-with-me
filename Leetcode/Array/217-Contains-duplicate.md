---
title: Easy | Contains duplicate 217
tags:
  - common
  - Oh-shit
categories:
  - Leetcode
  - Array
date: 2019-07-22 11:08:11
---

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

[Leetcode](https://leetcode.com/problems/contains-duplicate/)

<!--more-->

**Example 1:**

```
Input: [1,2,3,1]
Output: true
```

**Example 2:**

```
Input: [1,2,3,4]
Output: false
```

**Example 3:**

```
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
```

---

#### Oh-Shit

When we compare two adjacent items in an array, mind the index in *for* loop.

e.g. *for* loop is end at `i < array.length - 1` instead of `i < array.length`.

 ```java
for (int i = 0; i < array.length - 1; i += 1) {
    if (array[i] == array[i + 1]) {
        return true;
    }
}
return false;
 ```

---

#### First solution 

Use HashMap.

```java 
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> integers = new HashMap<>();
        for (int n : nums) {
            if (!integers.containsKey(n)) {
                integers.put(n, 1);
            } else {
                integers.put(n, integers.get(n) + 1);
            }
        }
        for (int n : nums) {
            if (integers.get(n) > 1) {
                return true;
            }
        }
        return false;
    }
}
```

T: O(n) (not sure)

---

#### Optimized 

* we could sort the array first, and check if there're two adjacent items.

  ```java
  class Solution {
      public boolean containsDuplicate(int[] nums) {
          Arrays.sort(nums);
          for (int i = 0; i < nums.length - 1; i += 1) {
              if (nums[i + 1] == nums[i]) {
                  return true;
              }
          }
          return false;
      }
  }
  ```

  T: O(n*logn) 

* HashMap is too slow, try to use HashSet.

  If HashSet.size() is smaller than nums.length, then nums has duplicates.

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int n : nums) {
            numSet.add(n);
        }
        return nums.length != numSet.size();
    }
}
```

​      T: O(n), S: O(n)

---

#### Summary 

HashSet has the lowest time complexity to find duplicates.