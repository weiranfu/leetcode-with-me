---
title: Medium | Shuffle an Array 384
tags:
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-06-10 00:19:17
---

Shuffle a set of numbers without duplicates.

[Leetcode](https://leetcode.com/problems/shuffle-an-array/)

<!--more-->

**Example:**

```
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
```

---

#### Tricky 

[Shuffle Algorithm]([https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle](https://en.wikipedia.org/wiki/Fisher–Yates_shuffle))

When we are at `nums[0]`, choose an item `nums[i]` from [0, n] and exchange `nums[0]` with `nums[i]`

When we are at `nums[1]`, choose an item `nums[i]` from [1, n] and exchange `nums[1]` with `nums[i]`

And so on...

---

#### Standard solution  

```java
class Solution {
    
    int[] original;
    Random random = new Random();

    public Solution(int[] nums) {
        original = nums;
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return original;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        int n = original.length;
        int[] nums = Arrays.copyOf(original, n);         // copy an array
        for (int i = 0; i < n; i++) {
            int rand = i + random.nextInt(n - i);        // get rand int from [i, n]
            int tmp = nums[i];
            nums[i] = nums[rand];
            nums[rand] = tmp;
        }
        return nums;
    }
}
```

T: O(n)

---

#### Summary 

