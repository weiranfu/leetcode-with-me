---
title: Easy | Majority of Elements 169
tags:
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-01-10 10:59:45
---

Given an array of size *n*, find the majority element. The majority element is the element that appears **more than** `⌊ n/2 ⌋` times.

You may assume that the array is non-empty and the majority element always exist in the array.

[Leetcode](https://leetcode.com/problems/majority-element/)

<!--more-->

**Example 1:**

```
Input: [3,2,3]
Output: 3
```

**Example 2:**

```
Input: [2,2,1,1,1,2,2]
Output: 2
```

**Follow up:** [Majority Element II](https://aranne.github.io/2020/06/22/Majority-element-II-229/#more)

---

#### Tricky 

The majority element is the element which appears more than n / 2.

The Moore Voting Algorithm:

We store the candidate and count for candidate. Whenever we find `count == 0`, we set candidate to current item. If we encounter `item == candidate`, `count++`, 

if we encounter `item != candidate`, `count—`.

This works because the majority candidate appears more than `n / 2`, so the count will greater than 0 in the end. If count == 0, which means there doesn't exist any majority element.

---

#### My thoughts 

Use a map to count each element.

---

#### Map 

```
class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int i : nums) {
            count.put(i, count.getOrDefault(i, 0) + 1);
            if (count.get(i) > nums.length / 2) {
                return i;
            }
        }
        return -1;
    }
}
```

T: O(n) 		S: O(n)

---

#### Sort 

Sort array, and return  item at index `len / 2`.

```java
class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }
}
```

T: O(nlogn) 		S: O(1)

---

#### Moore Voting Algorithm

Suppose there are nine elements in array **A**, and the round one is the majority.

![0_1477537808895_upload-f2ddd14f-9954-4025-b77a-40137c5abf06](https://leetcode.com/uploads/files/1477537810177-upload-f2ddd14f-9954-4025-b77a-40137c5abf06.png)

No matter in what order we select element from the array, we can only get two results

![0_1477537956098_upload-e3d23d8b-0d43-4f8f-ace1-065bd0928493](https://leetcode.com/uploads/files/1477537957428-upload-e3d23d8b-0d43-4f8f-ace1-065bd0928493.png)

```java
class Solution {
    public int majorityElement(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        int n = nums.length;
        int candidate = -1, cnt = 0;
        for (int a : nums) {
            if (candidate == a) {
                cnt++;
            } else if (cnt == 0) {
                candidate = a;
                cnt++;
            } else {
                cnt--;
            }
        }
        return candidate;
    }
}
```

T: O(n) 		S: O(1)
