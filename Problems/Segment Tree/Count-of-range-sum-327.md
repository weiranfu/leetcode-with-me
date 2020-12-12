---
title: Hard | Count of Range Sum 327
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Segment Tree
date: 2020-06-26 02:33:19
---

Given an integer array `nums`, return the number of range sums that lie in `[lower, upper]` inclusive.
Range sum `S(i, j)` is defined as the sum of the elements in `nums` between indices `i` and `j` (`i` ≤ `j`), inclusive.

**Note:**
A naive algorithm of *O*(*n*2) is trivial. You MUST do better than that.

[Leetcode](https://leetcode.com/problems/count-of-range-sum/)

<!--more-->

**Example:**

```
Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
```

**Follow up:**  

[Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)

[Reverse Pairs](https://leetcode.com/problems/reverse-pairs/)

[Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

---

#### Tricky 

1. Brute Force

   ```java
   class Solution {
       public int countRangeSum(int[] nums, int lower, int upper) {
           int n = nums.length;
           long[] presum = new long[n + 1];
           int res = 0;
           for (int i = 1; i <= n; i++) {
               presum[i] = presum[i - 1] + nums[i - 1];
               for (int j = 0; j < i; j++) {
                   if (lower <= presum[i] - presum[j] && presum[i] - presum[j] <= upper) {
                       res++;
                   }
               }
           }
           return res;
       }
   }
   ```

   ​	T: O(n^2)			S: O(n)

2. TreeMap

   In solution 1, the second *for* loop is used to find the number of `j` that satisify:

   `lower <= presum[i] - presum[j] && presum[i] - presum[j] <= upper`  ==>

   `presum[i] - upper <= presum[j] <= presum[i] - lower`

   We need to find out how many `j` satisifies this condition.

   If we store the `presum[]` sorted, we can easily find the position of `presum[i] - upper` and `presum[i] - lower`. 

   So the number of satisified `j` will be `count(pos2 - pos1)`

   In C++, we could use `multiset`, which supports duplicate elements. MultiSet in c++ 这是一个支持重复元素的集合类，本质是一棵平衡树。

   ```c++
   class Solution {
   public:
       int countRangeSum(vector<int>& nums, int lower, int upper) {
           
           int n= nums.size();
           int64_t presum = 0;
           multiset<int64_t> S;
           S.insert(0);
           int ret = 0;
           for(int i=0;i<n;i++){
               presum += nums[i];
               ret += distance(S.lower_bound(presum-upper),S.upper_bound(presum-lower));
               S.insert(presum);
           }
           return ret;
       }        
   };
   ```

   T: O(nlogn)		S: O(n)

   In Java, there isn't some data structure like `multiset`, we can only use `TreeMap`.

   We could store duplicates as value in Map and traverse submap to collect the satisified presum.

   The time complexity could be O(n^2) in worst case.

   ```java
   class Solution {
       public int countRangeSum(int[] nums, int lower, int upper) {
           int n = nums.length;
           long[] presum = new long[n + 1];
           TreeMap<Long, Integer> map = new TreeMap<>();
           int res = 0;
           for (int i = 0; i <= n; i++) {
               if (i > 0) presum[i] = presum[i - 1] + nums[i - 1];
               for (int val : map.subMap(presum[i] - upper, true, presum[i] - lower, true).values()) {
                   res += val;
               }
               map.put(presum[i], map.getOrDefault(presum[i], 0) + 1);
           }
           return res;
       }
   }
   ```

   T: O(nlogn)			average!

3. Weighted Segment Tree

   We could get the API from the code above:

   `add(value)`: add a value into a data structure

   `query()`: query how many numbers of values in this range (**Range Query**)

   This is very close to Weighted Segment Tree!

```java
class Solution {
    
    int[] tree;
    int N;
    List<Long> list;
    
    public int countRangeSum(int[] nums, int lower, int upper) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        long[] preSum = new long[n + 1];       
        for (int i = 0; i < n; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
        }
        list = new ArrayList<>();
        for (int i = 0; i <= n; i++) {         // we need add preSum[0]
            list.add(preSum[i]);
            list.add(preSum[i] - upper); // discretize all possible values we will use
            list.add(preSum[i] - lower);
        }
        list = new ArrayList<>(new HashSet<>(list));
        Collections.sort(list);
        N = list.size();
        
        tree = new int[N << 2];
        
        int res = 0;
        for (int i = 0; i <= n; i++) {             // we need add preSum[0]
            int val = find(preSum[i]);
            int low = find(preSum[i] - upper);
            int high = find(preSum[i] - lower);
            res += query(low, high, 1, N, 1);
            add(val, 1, N, 1);
        }
        return res;
    }
    
    public void add(int value, int l, int r, int n) {
        if (l == r) {
            tree[n]++;
            return;
        }
        int mid = l + (r - l) / 2;
        if (value <= mid) {
            add(value, l, mid, n * 2);
        } else {
            add(value, mid + 1, r, n * 2 + 1);
        }
        
        tree[n] = tree[n * 2] + tree[n * 2 + 1];
    }
    
    public int query(int L, int R, int l, int r, int n) {
        if (L <= l && r <= R) {
            return tree[n];
        }
        int mid = l + (r - l) / 2;
        int res = 0;
        if (mid >= L) res += query(L, R, l, mid, n * 2);
        if (mid < R) res += query(L, R, mid + 1, r, n * 2 + 1);
        return res;
    }
    private int find(long x) {
        int l = 0, r = N - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (list.get(mid) == x) return mid + 1;
            else if (list.get(mid) > x) r = mid - 1;
            else l = mid + 1;
        }
        return -1;
    }
}
```

T: O(nlogn)			S: O(n)

4. Merge Sort Count

We could convert problem into *Find `i < j` that `lower <= preSum[j] - preSum[i] <= upper`*.

If we have two sorted array, we need to determine `j`  that 

`preSum[i] + lower <= preSum[j] <= preSum[i] + upper`

**So we could search two boundaries `j1` and `j2` that when `i` increases, `j1` and `j2` also increase.**

```java
int j1, j2, i;
j1 = j2 = mid + 1;
for (i = l; i <= mid; i++) {
  while (j1 <= r && preSum[j1] < preSum[i] + lower) j1++;
  while (j2 <= r && preSum[j2] <= preSum[i] + upper) j2++;
  cnt += j2 - j1;
}
```

```java
class Solution {
    long[] preSum, tmp;
    int lower, upper;
    
    public int countRangeSum(int[] nums, int lower, int upper) {
        this.lower = lower; this.upper = upper;
        int n = nums.length;
        preSum = new long[n + 1];
        tmp = new long[n + 1];
        for (int i = 0; i < n; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
        }
        return mergeCount(0, n);
    }
    private int mergeCount(int l, int r) {
        if (l >= r) return 0;
        int mid = l + (r - l) / 2;
        int cnt = mergeCount(l, mid) + mergeCount(mid + 1, r);
        
        int j1, j2, i;
        j1 = j2 = mid + 1;
        for (i = l; i <= mid; i++) {
            while (j1 <= r && preSum[j1] < preSum[i] + lower) j1++;
            while (j2 <= r && preSum[j2] <= preSum[i] + upper) j2++;
            cnt += j2 - j1;
        }
        /* merge starts */
        int k = 0, j = mid + 1;
        i = l;
        while (i <= mid && j <= r) {
            if (preSum[i] < preSum[j]) tmp[k++] = preSum[i++];
            else tmp[k++] = preSum[j++];
        }
        while (i <= mid) tmp[k++] = preSum[i++];
        while (j <= r) tmp[k++] = preSum[j++];
        for (i = l, j = 0; i <= r; i++, j++) preSum[i] = tmp[j];
        return cnt;
    }
}
```

T: O(nlogn)			S: O(n)