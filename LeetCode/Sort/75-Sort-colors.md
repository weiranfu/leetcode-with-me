---
title: Medium | Sort Colors 75
tags:
  - tricky
categories:
  - Leetcode
  - Sort
date: 2020-05-15 21:13:10
---

Given an array with *n* objects colored red, white or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

[Leetcode](https://leetcode.com/problems/sort-colors/)

<!--more-->

**Example:**

```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Follow up:** Could you come up with a one-pass algorithm using only constant space?

---

#### Tricky 

* Two pass algorithm: counting sort

* One pass algorithm: [dutch partitioning problem](https://en.wikipedia.org/wiki/Dutch_national_flag_problem) We are classifying the array into four groups: red, white, unclassified, and blue. And keep pointers for red, white, blue.

  If encounter red, swap(red, white). If encounter blue, swap(white, blue).

---

#### My thoughts 

Counting sort: First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

---

#### One-pass 

```java
class Solution {
    public void sortColors(int[] nums) {
        if (nums == null || nums.length == 0) return;
        int n = nums.length;
        int red = 0;
        int white = 0;
        for (int num : nums) {
            if (num == 0) red++;
            else if (num == 1) white++;
        }
        for (int i = 0; i < n; i++) {
            if (red > 0) {
                nums[i] = 0;
                red--;
            } else if (white > 0) {
                nums[i] = 1;
                white--;
            } else {
                nums[i] = 2;
            }
        }
    }
}
```

T: O(n)		S: O(1)

---

#### Two-pass

We are classifying the array into four groups: red, white, unclassified, and blue. Initially we group all elements into unclassified. We iterate from the beginning as long as the white pointer is less than the blue pointer.

If the white pointer is red color(nums[white] == 0), we swap with the red pointer(which is white color) and move both white and red pointer forward. If the pointer is white (nums[white] == 1), the element is already in correct place, so we don't have to swap, just move the white pointer forward. If the white pointer is blue, we swap with the latest unclassified element(which is pointed by blue).

```java
class Solution {
    public void sortColors(int[] nums) {
        if (nums == null || nums.length == 0) return;
        int n = nums.length;
        int red = 0;
        int white = 0;
        int blue = n - 1;
        while (white <= blue) {
            if (nums[white] == 0) { // if meets red
                swap(red, white, nums);  // swap white one 
                red++;
                white++;
            } else if (nums[white] == 2) { // if meets blue 
                swap(white, blue, nums);   // swap unclassified one
                blue--;
            } else {                  // if meets white
                white++;
            }
        }
    }
    
    private void swap(int i, int j,  int[] nums) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
```

T: O(n)			S: O(1)

