---
title: Easy | Rotate array 189
tags:
  - tricky
  - corner case
  - Oh-shit
categories:
  - Leetcode
  - Array
date: 2019-07-18 23:00:51
---

Given an array, rotate the array to the right by *k* steps, where *k* is non-negative.

<!--more-->

**Example 1:**

```
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**

```
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

---

**Tricky**

1. Rotate an array. This likes a mirror, e.g [1, 2, 3, 4, 5] rotate k = 2.

* We first reverse whole array. We get [5, 4, 3, 2, 1]
* Then reverse the first k items in new array. We get [4, 5, 3, 2, 1]
* Lastly reverse the remaining items in the array. We get [4, 5, 1, 2, 3]

2. Cyclic Replacements.

**Corner Case** 

`k = k % nums.length`

Using `%` to deal with the situation where k > nums.length

**Oh-Shit** 

When we use *while* loop, we usually forget add the pointers.

```java
while (condition) {
    first += 1;
    last += 1;
}
```

---

**My thoughts** 

Brute solution: move the last item to front of array and move left items one step back.

then do this k times.

---

**First solution** 

```java
class Solution {
    public void rotate(int[] nums, int k) {
        int size = nums.length;
        for (int i = 0; i < k; i += 1) {
            int lastItem = nums[size - 1];
            for (int j = size - 2; j >= 0; j -= 1) {
                nums[j + 1] = nums[j];
            }
            nums[0] = lastItem;
        }
    }
}
```

Time: O(kn) Space: O(1)

---

**Standard solution** 

```java
class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length; 
        if (k == 0) {
            return;
        }
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }
    
    public void reverse(int[] nums, int first, int last) {
        while (first < last) {
            int temp = nums[last];
            nums[last] = nums[first];
            nums[first] = temp;
            first += 1;
            last -= 1;
        }
    }
}
```

T: O(n) S: O(1)

---

#### Cyclic Replacement

We can directly place every number of the array at its required correct position. But if we do that, we will destroy the original element. Thus, we need to store the number being replaced in a `temp` variable. Then, we can place the replaced number(`temp`) at its correct position and so on, n times, where n is the length of array.

But, there could be a problem with this method, if `n % k == 0`, while picking up numbers to be placed at the correct position, we will eventually reach the number from which we originally started. Thus, in such a case, when we hit the original number's index again, we start the same process with the number following it.

```
nums: [1, 2, 3, 4, 5, 6]
k: 2
```

![Rotate Array](https://leetcode.com/media/original_images/189_Rotate_Array.png)

```java
class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        int cnt = 0;
        int start = 0;
        while (cnt < n) {
            int curr = start;
            int prev = nums[curr];
            do {
                curr = (curr + k) % n;
                int tmp = nums[curr];
                nums[curr] = prev;
                prev = tmp;
                cnt++;
            } while (curr != start);
            start++;
        }
    }
}
```

T: O(n)		S: O(1)

---

**Summary** 

Rotate an array is like a mirror.

Just need to reverse array three times.