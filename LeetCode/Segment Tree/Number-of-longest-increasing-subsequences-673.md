---
title: Hard | Number of Longest Increasing Subsequences 673
tags:
  - tricky
categories:
  - Leetcode
  - Segment Tree
date: 2020-06-25 15:43:55
---

Given an unsorted array of integers, find the number of longest increasing subsequence.

[Leetcode](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)

<!--more-->

**Example 1:**

```
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
```

**Example 2:**

```
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
```

---

#### Tricky 

* DP

  Suppose for sequences ending at `nums[i]`, we knew the length `dp[i]` of the longest sequence, and the number `count[i]` of such sequences with that length.

  For every `j < i` with `A[j] < A[i]`, we might append `A[i]` to a longest subsequence ending at `A[j]`. It means that we have demonstrated `count[j]` subsequences of length `length[j] + 1`.

  Now, if those sequences are longer than `length[i]`, then we know we have `count[j]` sequences of this length. If these sequences are equal in length to `length[i]`, then we know that there are now `count[j]` additional sequences to be counted of that length (ie. `count[i] += count[j]`).
  
* Segment Tree

  Suppose we knew for each length `L`, the number of sequences with length `L` ending in `x`. Then when considering the next element of `nums`, updating our knowledge hinges on knowing the number of sequences with length `L-1` ending in `y < x`. This type of query over an interval is a natural fit for using some sort of tree.

  We can use Segment Tree to achieve this goal. To query in range `y < x` and store the max length in each node.

  When merging two nodes, we only care about the one has larger length. If they have same length, then we add up their count.

  Before we add a num into Segment Tree, we need to query in range `[0, num - 1]` to get the max length and count. Then add `max length + 1` and `count` into Segment Tree.

---

#### DP 

We could collect number of max length in the DP loops.

```java
class Solution {
    public int findNumberOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];  // length of LPS
        int[] cnt = new int[n];
        Arrays.fill(dp, 1);
        Arrays.fill(cnt, 1);
        int max = 0;
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    if (dp[j] + 1 > dp[i]) {   // if we find longer one
                        dp[i] = dp[j] + 1;
                        cnt[i] = cnt[j];      // update cnt
                    } else if (dp[j] + 1 == dp[i]) { 
                        cnt[i] += cnt[j];     // collect cnt
                    }
                }
            }
            if (dp[i] > max) {
                max = dp[i];
                res = cnt[i];
            } else if (dp[i] == max) {
                res += cnt[i];
            }
        }
        return res;
    }
}
```

T: O(n^2)			S: O(n)

---

#### Segment Tree 

```java
class Solution {
    class Node {
        Value val;
    }
    
    class Value {
        int len;
        int cnt;
        public Value(int l, int c) {
            len = l; cnt = c;
        }
    }
    
    Node[] tree;
    int N;
    Map<Integer, Integer> rank;
    
    public int findNumberOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        List<Integer> list = new ArrayList<>();
        for (int num : nums) {
            list.add(num);
        }
        list = new ArrayList<>(new HashSet<>(list));  // remove duplicates
        Collections.sort(list);                       // sort
        N = list.size();
        rank = new HashMap<>();
        for (int i = 0; i < N; i++) {
            rank.put(list.get(i), i + 1);       // move one step right
        }
        N = N + 1;
        tree = new Node[N << 2];
        for (int i = 0; i < tree.length; i++) {
            tree[i] = new Node();
            tree[i].val = new Value(0, 1);     // initialize value for query
        }
        
        for (int i = 0; i < nums.length; i++) {
            int idx = rank.get(nums[i]);
            Value v = query(idx - 1, 0, N - 1, 0);  // query in range [0, idx - 1]
            add(idx, new Value(v.len + 1, v.cnt), 0, N - 1, 0);
        }
        return tree[0].val.cnt;
    }
    
    public void add(int idx, Value val, int l, int r, int rt) {
        if (l == r) {
            tree[rt].val = merge(tree[rt].val, val);
            return;
        }
        int mid = l + (r - l) / 2;
        if (idx <= mid) {
            add(idx, val, l, mid, rt * 2 + 1);
        } else {
            add(idx, val, mid + 1, r, rt * 2 + 2);
        }
        
        tree[rt].val = merge(tree[rt * 2 + 1].val, tree[rt * 2 + 2].val);
    }
    
    public Value merge(Value val1, Value val2) {
        if (val1.len == val2.len) {
            if (val1.len == 0) return new Value(0, 1);     // if one node is not used.
            return new Value(val1.len, val1.cnt + val2.cnt);
        } else if (val1.len > val2.len) {
            return val1;
        } else {
            return val2;
        }
    }
    
    public Value query(int idx, int l, int r, int rt) {
        if (r <= idx) {
            return tree[rt].val;
        }
        Value res = new Value(0, 0);
        int mid = l + (r - l) / 2;
        Value left = query(idx, l, mid, rt * 2 + 1);
        res = merge(res, left);
        if (mid < idx) {
            Value right = query(idx, mid + 1, r, rt * 2 + 2);
            res = merge(res, right);
        }
        
        return res;
    }
}
```

T: O(nlogn)			S: O(n)