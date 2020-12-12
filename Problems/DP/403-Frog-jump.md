---
title: Hard | Frog Jump 403
tags:
  - tricky
categories:
  - Leetcode
  - DP	
date: 2020-01-18 19:48:27
---

A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was *k* units, then its next jump must be either *k* - 1, *k*, or *k* + 1 units. Note that the frog can only jump in the forward direction.

[Leetcode](https://leetcode.com/problems/frog-jump/)

<!--more-->

**Example 1:**

```
[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
```

**Example 2:**

```
[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
```

---

#### Tricky 

We must record the previous stones we jump from to current stone.

* DP

  Use `dp[i][j]` represent we jump from `stones[j]` to `stones[i]`. 

  The jump size is `stones[i] - stones[j]`

  How to find the next possible stones we can jump to?

  We can use Binary Search to search `stones + jump - 1`, `stones + jump` and `stones + jump + 1`

  ```java
  class Solution {
      public boolean canCross(int[] stones) {
          if (stones == null || stones.length == 0) return false;
          int n = stones.length;
          boolean[][] dp = new boolean[n][n];
          if (n == 1) return true;
          if (stones[1] - stones[0] == 1) dp[1][0] = true;
          for (int i = 1; i < n; i++) {
              for (int j = 0; j < i; j++) {
                  if (dp[i][j]) {
                      int stone = stones[i] - stones[j];
                      int k = Arrays.binarySearch(stones, i, n, stones[i] + stone - 1);
                      if (k > 0) dp[k][i] = true;
                      k = Arrays.binarySearch(stones, i, n, stones[i] + stone);
                      if (k > 0) dp[k][i] = true;
                      k = Arrays.binarySearch(stones, i, n, stones[i] + stone + 1);
                      if (k > 0) dp[k][i] = true;
                  }
                  if (i == n - 1 && dp[i][j]) return true; 
              }
          }
          return false;
      }
  }
  ```

  T: O(n^2 * logn)			S: O(n ^2)

* DP

  Use `dp[i][jump]` to represent we jump to `stones[i]` using `jump` steps.

  Since every jump, we can only increase one more jump step. So the total jump steps at `stones[i]` will not exceed `i`.

  These representation of states won't need to use Binary Search to find the next stones we will jump to.

  We can easily update the next states.

  for `dp[i][jump]`, we jump from `j` to `i` using `jump` steps. Then we can only jump to `j` using `jump - 1`, `jump`  or `jump + 1` steps.

  ```java
  int jump = stones[i] - stones[j]  jump steps from j to i.
  
  if dp[j][jump] == true || dp[j][jump + 1] == true || dp[j][jump - 1] == true,
  
  dp[i][jump] = true;
  ```

  ```java
  class Solution {
      public boolean canCross(int[] stones) {
          if (stones == null || stones.length == 0) return false;
          int n = stones.length;
          boolean[][] dp = new boolean[n][n];
          dp[0][0] = true;
          for (int i = 1; i < n; i++) {
              for (int j = 0; j < i; j++) {
                  int jump = stones[i] - stones[j];  // jump steps to i
                  if (jump > i) continue;            // jump steps exceed i
                	// jump steps to j
                  if (dp[j][jump]) dp[i][jump] = true;  
                	// jump - 1 steps to j
                  else if (jump - 1 >= 0 && jump - 1 <= j && dp[j][jump - 1]) 
                     dp[i][jump] = true;  
                	// jump + 1 steps to j
                  else if (jump + 1 <= j && dp[j][jump + 1]) dp[i][jump] = true;
                  if (i == n - 1 && dp[i][jump]) return true;
              }
          }
          return false;
      }
  }
  ```

  T：O(n^2)		S: O(n^2)

* Memorization

  We could use a Set to store all possible previous stones we jump from to this stone.

  Instead of store the index of stone, we store the value of stone using Map. Then we can avoid use Binary Search to find next stone we will jump to.

  ```java
  class Solution {
      public boolean canCross(int[] stones) {
          if (stones == null || stones.length == 0) return false;
          int n = stones.length;
          Map<Integer, Set<Integer>> map = new HashMap<>();
          for (int i = 0; i < n; i++) {
              map.put(stones[i], new HashSet<>());
          }
          map.get(0).add(0);
          for (int i = 0; i < n; i++) {
              for (int jump : map.get(stones[i])) {
                  for (int step = jump - 1; step <= jump + 1; step++) {
                      if (step > 0 && map.containsKey(stones[i] + step)) {
                          map.get(stones[i] + step).add(step);
                      }
                  }
              }
          }
          return map.get(stones[n - 1]).size() != 0;
      }
  }
  ```

  T: O(n^2)		S: O(n^2)

* DFS

  Use a set to store all possible stones to quick check whether we can jump to a stone.

  Use a Stack to perform DFS, try to search all possible jumps.

  We must store the last jump and value of stones together in Stack.

  We need pruning that the max jump steps at `stones[i]` will not exceed `i`.

  ```java
  class Solution {
      public boolean canCross(int[] stones) {
          if (stones == null || stones.length == 0) return false;
          int n = stones.length;
          Set<Integer> set = new HashSet<>();
          for (int i = 0; i < n; i++) {
            																									// steps won't exceed i
              if (i > 0 && stones[i] - stones[i - 1] > i) return false;
              set.add(stones[i]);
          }
          Stack<int[]> stack = new Stack<>();
          stack.push(new int[]{0, 0});
          while (!stack.isEmpty()) {
              int[] info = stack.pop();
              int stone = info[0];
              int jump = info[1];
              for (int k = jump - 1; k <= jump + 1; k++) {
                  if (k > 0 && set.contains(stone + k)) {
                      if (stone + k == stones[n - 1]) return true;      // search successful
                      stack.push(new int[]{stone + k, k});
                  }
              }
          }
          return false;
      }
  }
  ```

  T: O(n)		S: O(n)	