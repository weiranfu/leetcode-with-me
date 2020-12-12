---
title: Medium | Longest Increasing Subsequences 300
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-06-24 21:54:55
---

Given an unsorted array of integers, find the length of longest increasing subsequence.

The algorithm should run in O(n^2) complexity. Could you improve it to O(nlogn) time complexity?

[Leetcode](https://leetcode.com/problems/longest-increasing-subsequence/)

<!--more-->

**Example:**

```
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
```

**Follow up:** 

[Number of Longest Increasing Subsequences](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)

---

#### Tricky 

* DP

   `dp[i]` means if we use `nums[i]` as the last element in this subsequences the longest length we could achieve.

  We need to traverse from `[0, j - 1]` to find max.

* Greedy + Binary Search:

  `tails` is an array storing the smallest tail of all increasing subsequences with length `i+1` in `tails[i]`.
  For example, say we have `nums = [4,5,6,3]`, then all the available increasing subsequences are:

  ```
  len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
  len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
  len = 3   :      [4, 5, 6]            => tails[2] = 6
  ```

  We always update the number at tail to be smaller one in same length (Greedy!)

  We can easily prove that tails is a increasing array, because we only store the smallest tail for each length. Therefore it is possible to do a binary search in tails array to find the one needs update.

  Each time we only do one of the two:
  
  ```
  (1) if x is larger than all tails, append it, increase the size by 1
(2) if tails[i-1] < x <= tails[i], update tails[i]
  ```
  
  Doing so will maintain the tails invariant. The the final answer is just the size.
  
* BIT

   维护一个权值数组，以dp[i] 为值，nums[i] 为坐标

   当我们要求dp[i]时，我们要找 nums[j] < nums[i] 中 dp[j] 最大的

   这就转化成了区间最值问题 + 单点更新

   在权值数组中，如果有重复的nums[i], 可以直接更新dp[i]. 因为后面更新的 nums[i] 的 LIS 一定是更长的

   因为区间最值从最左侧开始，可以用BIT，否则应用Segment Tree

   因为单点更新是越来越大，所以在更新max时可以用BIT

* 

   ```
   
   ```

---

#### Brute Force

There're two choices when considering a `num[i]`, take it or not take it.

```java
public class Solution {

    public int lengthOfLIS(int[] nums) {
        return lengthofLIS(nums, Integer.MIN_VALUE, 0);
    }

    public int lengthofLIS(int[] nums, int prev, int curpos) {
        if (curpos == nums.length) {
            return 0;
        }
        int taken = 0;
        if (nums[curpos] > prev) {
            taken = 1 + lengthofLIS(nums, nums[curpos], curpos + 1);
        }
        int nottaken = lengthofLIS(nums, prev, curpos + 1);
        return Math.max(taken, nottaken);
    }
}
```

T: O(2^n)		size of recursion tree will be 2^n

S: O(n^2)        memo array size

---

#### DP 

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = 1;
        int res = 1;
        for (int i = 1; i < n; i++) {
            int max = Integer.MIN_VALUE;
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    max = Math.max(max, dp[j] + 1);
                }
            }
            dp[i] = (max == Integer.MIN_VALUE) ? 1 : max;
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}
```

T: O(n^2)			S: O(n)

---

#### Binary Search

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        int[] tails = new int[n];
        int len = 0;
        for (int i = 0; i < n; i++) {
            int l = 0, r = len;
            while (l < r) {
                int mid = l + (r - l) / 2;
                if (tails[mid] >= nums[i]) {
                    r = mid;
                } else {
                    l = mid + 1;
                }
            }
            tails[l] = nums[i];
            if (l == len) {
                len++;
            }
        }
        return len;
    }
}
```

T: O(nlogn)		S: O(n)

---

#### Optimized

We could use `Arrays.binarySearch()` to search the right place to insert into.

Arrays.binarySearch() method returns index of the search key, if it is contained in the array, else it returns `(-(insertion point) - 1)`. The insertion point is the point at which the key would be inserted into the array: the index of the first element greater than the key, or a.length if all elements in the array are less than the specified key.

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        int[] tails = new int[n];
        int len = 0;
        for (int i = 0; i < n; i++) {
            int pos = Arrays.binarySearch(tails, 0, len, nums[i]);
            if (pos < 0) {
                pos = -(pos + 1);
            }
            tails[pos] = nums[i];
            if (pos == len) {
                len++;
            }
        }
        return len;
    }
}
```

T: O(nlogn)			S: O(n)

---

#### BIT

```java
class Solution {
    int N;
    int[] bit;
    List<Integer> list;    
    
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        list = new ArrayList<>();
        for (int a : nums) {
            list.add(a);
        }
        list = new ArrayList<>(new HashSet<>(list));
        Collections.sort(list);
        N = list.size();
        
        bit = new int[N + 1];
        int res = 1;
        for (int a : nums) {
            int idx = find(a);
            int max = getmax(idx - 1);
            add(idx, max + 1);
            res = Math.max(res, max + 1);
        }
        return res;
    }
    private void add(int x, int v) {
        for (int i = x; i <= N; i += lowbit(i)) {
            bit[i] = Math.max(bit[i], v);
        }
    }
    private int getmax(int x) {
        int res = 0;
        for (int i = x; i > 0; i -= lowbit(i)) {
            res = Math.max(res, bit[i]);
        }
        return res;
    }
    private int find(int x) {
        return Collections.binarySearch(list, x) + 1;     // BIT start from 1
    }
    private int lowbit(int x) {return x & (-x);}
}
```

T: O(nlogn)		S: O(n)