---
title: Hard | Minimum Possible Integer After at Most K Adjacent Swaps on Digits 1505
tags:
  - common
  - tricky
categories:
  - Leetcode
  - BIT
date: 2020-07-05 14:26:21
---

Given a string `num` representing **the digits** of a very large integer and an integer `k`.

You are allowed to swap any two adjacent digits of the integer **at most** `k` times.

Return *the minimum integer* you can obtain also as a string.

[Leetcode](https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/)

<!--more-->

**Example 1:**

```
Input: num = "4321", k = 4
Output: "1342"
Explanation: The steps to obtain the minimum integer from 4321 with 4 adjacent swaps are shown.
```

**Example 2:**

```
Input: num = "100", k = 1
Output: "010"
Explanation: It's ok for the output to have leading zeros, but the input is guaranteed not to have any leading zeros.
```

**Example 3:**

```
Input: num = "36789", k = 1000
Output: "36789"
Explanation: We can keep the number without any swaps.
```

**Constraints:**

- `1 <= num.length <= 30000`
- `num` contains **digits** only and doesn't have **leading zeros**.
- `1 <= k <= 10^9`

---

#### Tricky 

We try to put smallest digit on the least significant digit in K swaps.

* Brute Force: bubble sort

  Find the the smallest digit at most K steps away, and bubble sort it to the least significant digit.

  ```java
  class Solution {
      public String minInteger(String num, int k) {
          if (num == null || num.length() == 0) return num;
          char[] cs = num.toCharArray();
          int n = num.length();
          for (int i = 0; i < n && k > 0; i++) {
              int curr = i;
              for (int j = curr + 1; j < n && j - i <= k; j++) {
                  if (cs[j] < cs[curr]) {
                      curr = j;
                  }
              }
              k -= curr - i;
              char tmp = cs[curr];
              for (int j = curr; j > i; j--) {
                  cs[j] = cs[j - 1];
              }
              cs[i] = tmp;
          }
          return new String(cs);
      }
  }
  ```

  T: O(n^2)			S: O(n)

* Binary Index Tree

  We need to keep track the position of each digit in `num`. However after swapping some digits, the position of other digits might change. For example,

  ```java
  4312 -> 1432     4,3's pos don't change. 2's pos changes.
  ```

  1. 前某段数的下标全都+1      （BIT 是要用到差分）
2. 求当前数的下标
  
经典问题：可以用BIT或Segment Tree
  
  当选择用BIT时，要用差分实现给某一段数+1
  
  `[i, j]` `sum[i] += 1, sum[j + 1] -= 1`
  
   我们这里要给`[1, p-1]` +1. So `add(1, 1), add(p, -1)` 
  
  ```java
  class Solution {
      int n;
      int[] sum;
      private int lowbit(int i) {return i & (-i);}
      private void add(int x, int v) {
          for (int i = x; i <= n; i += lowbit(i)) sum[i] += v;
      }
      private int query(int x) {
          int res = 0;
          for (int i = x; i > 0; i -= lowbit(i)) res += sum[i];
          return res;
      }
      
      public String minInteger(String num, int k) {
          if (num == null || num.length() == 0) return num;
          Deque<Integer>[] pos = new Deque[10];  // save all pos of current digit
          for (int i = 0; i < 10; i++) {
              pos[i] = new ArrayDeque<>();
          }
          n = num.length();
          sum = new int[n + 1];
          for (int i = 0; i < n; i++) {
              pos[num.charAt(i) - '0'].addLast(i + 1);   // BIT starts with 1
          }
          
          StringBuilder res = new StringBuilder();
          for (int i = 1; i <= n; i++) {
              for (int j = 0; j < 10; j++) {              // try all digits
                  if (pos[j].isEmpty()) continue;         // all used
                  int t = pos[j].peekFirst();             // get next closest digit
                  int p = t + query(t);                   // query(p) 是坐标偏移量
                  if (p - i <= k) {
                      k -= p - i;
                      pos[j].pollFirst();
                      res.append(j);
                      add(1, 1);              // add all 1 in [1, t-1]    
                      add(t, -1);                
                      break;
                  }   
              }
          }
          return res.toString();
      }
}
  ```
  
  T: O(nlogn)			S: O(n)

