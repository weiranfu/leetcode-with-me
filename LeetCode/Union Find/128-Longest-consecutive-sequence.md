---
title: Hard | Longest Consecutive Sequence 128
tags:
  - tricky
categories:
  - Leetcode
  - Union Find
date: 2020-05-27 07:31:22
---

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(*n*) complexity.

[Leetcode](https://leetcode.com/problems/longest-consecutive-sequence/)

<!--more-->

**Example:**

```
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

---

#### Tricky 

Although the integers in `nums` varies from small number to a large number, we cannot union them directly.

**However, we could see their indices as a node to union.** For example, we union `4` at position `1` with `1` at position `3`, then node `1` and `3` are unioned.

We need  a HashMap to map `numns[i]` to its index `i`.

We also need a size array `int[] size` to record each node's size.

---

#### Union Find

We add a new `nums[i]`, try to union `nums[i] + 1` and `nums[i] - 1`

```java
class Solution {
    int[] uf;
    int[] size;
    
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        uf = new int[n];
        size = new int[n];
        Map<Integer, Integer> map = new HashMap<>(); // map nums[i] to index i.
        int res = 1;
        for (int i = 0; i < n; i++) {
            if (map.containsKey(nums[i])) continue;
            map.put(nums[i], i);
            uf[i] = i;
            size[i] = 1;
            if (map.containsKey(nums[i] - 1)) {
                int index = map.get(nums[i] - 1);
                int p1 = find(index);
                int p2 = find(i);
                uf[p2] = p1;
                size[p1] += size[p2];
                res = Math.max(res, size[p1]);
            }
            if (map.containsKey(nums[i] + 1)) {
                int index = map.get(nums[i] + 1);
                int p1 = find(index);
                int p2 = find(i);
                uf[p2] = p1;
                size[p1] += size[p2];
                res = Math.max(res, size[p1]);
            }
        }
        return res;
    }
    
    private int find(int i) {    // ONLY when we initialize uf[i] = i,
        while (i != uf[i])  {    // we could write find() like this.
            uf[i] = uf[uf[i]];
            i = uf[i];
        }
        return i;
    }
}
```

T: O(n)		S: O(n)

---

#### Two boundaries

We will use HashMap. The key thing is to keep track of the sequence length and store that in the boundary points of the sequence. For example, as a result, for sequence {1, 2, 3, 4, 5}, map.get(1) and map.get(5) should both return 5.

Whenever a new element **n** is inserted into the map, do two things:

1. See if **n - 1** and **n + 1** exist in the map, and if so, it means there is an existing sequence next to **n**. Variables **left** and **right** will be the length of those two sequences, while **0** means there is no sequence and **n** will be the boundary point later. Store **(left + right + 1)** as the associated value to key **n** into the map.
2. Use **left** and **right** to locate the other end of the sequences to the left and right of **n** respectively, and replace the value with the new length.

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        Map<Integer, Integer>  map = new HashMap<>();
        int res = 0;
        for (int num : nums) {
            if (map.containsKey(num)) continue;
            int left = (map.containsKey(num - 1)) ? map.get(num - 1) : 0; // find left boundary
            int right = (map.containsKey(num + 1)) ? map.get(num + 1) : 0;
            int sum = 1 + left + right;
            map.put(num, sum);
            res = Math.max(res, sum);
            map.put(num - left, sum);    // extend boundary
            map.put(num + right, sum);
        }
        return res;
    }
}
```

T: O(n)		S: O(n)

---

#### Removing nums

Try to removing a `num` and its neighboring numbers. Use a `set` to indicate whether it has been removed.

If we want to remove left nums, we check `set` whether it contains `num[i] - 1`.

If we want to remove right nums, we check `set` whether it contains `nums[i] + 1`.

Use `res` to record max removing length.

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            int count = 1;
            int num = nums[i];
            while (set.contains(--num)) {  // look left
                set.remove(num);
                count++;
            }
            num = nums[i];
            while (set.contains(++num)) {  // look right
                set.remove(num);
                count++;
            }
            res = Math.max(res, count);
        }
        return res;
    }
}
```

T: O(n)		S: O(n)

