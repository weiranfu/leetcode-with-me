---
title: Medium | Prison Cells After N Days 957
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2019-12-23 02:44:02
---

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

- If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
- Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: `cells[i] == 1` if the `i`-th cell is occupied, else `cells[i] == 0`.

Given the initial state of the prison, return the state of the prison after `N` days (and `N`such changes described above.)

[Leetcode](https://leetcode.com/problems/prison-cells-after-n-days/)

<!--more-->

**Example 1:**

```
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
```

**Example 2:**

```
Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
```

**Note:**

1. `cells.length == 8`
2. `cells[i]` is in `{0, 1}`
3. `1 <= N <= 10^9`

---

#### Tricky 

Under this rule to change cells, there will be a loop.

We can find the repeat cycle using a map.

---

#### My thoughts 

Intuitely, I didn't find that there's a repeat cycle during cells changing with day.

If N becomes very very large, there'll be TLE error.

```java
class Solution {
    public int[] prisonAfterNDays(int[] cells, int N) {
        int size = cells.length;
        while (N-- > 0) {
            int[] tmp = new int[size];
            for (int i = 1; i < size - 1; i += 1) {
                if (cells[i - 1] == cells[i + 1]) {
                    tmp[i] = 1;
                } else {
                    tmp[i] = 0;
                }
             } 
             cells = tmp;
        }
        return cells;
    }
}
```

T: O(n*len) S: O(len)

---

#### Optimized 

Find the repeat cycle firstly, then we could reduce N by repeat cycle.

```java
class Solution {
    public int[] prisonAfterNDays(int[] cells, int N) {
		if (cells == null || cells.length == 0 || N <= 0) return cells;
        boolean hasCycle = false;
        int cycle = 0;
        HashSet<String> set = new HashSet<>(); 
        for (int i = 0; i < N; i++) {
            int[] next = nextDay(cells);
            String key = Arrays.toString(next);
            if(!set.contains(key)){ //store cell state
                set.add(key);
                cycle++;
            } else { //hit a cycle
                hasCycle = true;
                break;
            }
            cells = next;
        }
        if (hasCycle) {
            N = N % cycle;
            for (int i = 0; i < N; i++){
                cells = nextDay(cells);
            }   
        }
        return cells;
    }
    
    private int[] nextDay(int[] cells) {
        int[] tmp = new int[cells.length];
        for(int i = 1; i < cells.length - 1; i++){
            tmp[i] = cells[i-1] == cells[i+1] ? 1 : 0;
        }
        return tmp;
    }
}
```

T: O(k\* min(N, 2^k)) S: O(k)

---

#### Bitmask

Use bitmask to store state of cells, then we can store them in Map to detect cycle.

Use `state = ~((state >> 1)^(state << 1))`  to get the XOR of neighbors.

Use `state |= mask` to set `0` and `n-1` to 0 in order to remove leading `1`s set by `~` operator.

```java
class Solution {
    public int[] prisonAfterNDays(int[] cells, int N) {
        if (N == 0) return cells;
        int n = cells.length;
        int state = 0;
        for (int i = 0; i < n; i++) {
            if (cells[i] == 1) {
                state |= 1 << i;
            }
        }
        int mask = 0;
        for (int i = 1; i < n - 1; i++) {
            mask |= 1 << i;
        }
        
        Map<Integer, Integer> map = new HashMap<>();
        boolean noCycle = true;
        while (N != 0) {
            if (!map.containsKey(state) && noCycle) {
                map.put(state, N);
            } else if (noCycle) {
                noCycle = false;
                N = N % (map.get(state) - N);
                if (N == 0) break;                      // corner case
            }
            state = ~((state >> 1) ^ (state << 1));     // left and right are same
            state &= mask;                              // add 0 to tail and head
            N--;                                        // and remove leading 1 cause by ~
        }
        int[] res = new int[n];
        int i = 0;
        while (state != 0) {
            res[i++] = (state & 1) == 1 ? 1 : 0;
            state >>= 1;
        }
        return res;
    }
}
```

T: O(min(N, 2^k))			S: O(2^k)