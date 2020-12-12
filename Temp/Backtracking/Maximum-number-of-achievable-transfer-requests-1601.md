---
title: Hard | Maximum Number of Achievable Transfer Requests 1601
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-09-28 21:56:13
---

We have `n` buildings numbered from `0` to `n - 1`. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.

You are given an array `requests` where `requests[i] = [fromi, toi]` represents an employee's request to transfer from building `fromi` to building `toi`.

**All buildings are full**, so a list of requests is achievable only if for each building, the **net change in employee transfers is zero**. This means the number of employees **leaving** is **equal** to the number of employees **moving in**. For example if `n = 3` and two employees are leaving building `0`, one is leaving building `1`, and one is leaving building `2`, there should be two employees moving to building `0`, one employee moving to building `1`, and one employee moving to building `2`.

Return *the maximum number of achievable requests*.

[Leetcode](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/09/10/move1.jpg)

```
Input: n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
Output: 5
Explantion: Let's see the requests:
From building 0 we have employees x and y and both want to move to building 1.
From building 1 we have employees a and b and they want to move to buildings 2 and 0 respectively.
From building 2 we have employee z and they want to move to building 0.
From building 3 we have employee c and they want to move to building 4.
From building 4 we don't have any requests.
We can achieve the requests of users x and b by swapping their places.
We can achieve the requests of users y, a and z by swapping the places in the 3 buildings.
```

**Example 2:**

![img](https://assets.leetcode.com/uploads/2020/09/10/move2.jpg)

```
Input: n = 3, requests = [[0,0],[1,2],[2,1]]
Output: 3
Explantion: Let's see the requests:
From building 0 we have employee x and they want to stay in the same building 0.
From building 1 we have employee y and they want to move to building 2.
From building 2 we have employee z and they want to move to building 1.
We can achieve all the requests. 
```

**Constraints:**

- `1 <= n <= 20`
- `1 <= requests.length <= 16`
- `requests[i].length == 2`
- `0 <= fromi, toi < n`

**Follow up:** 

---

#### Brute force

Since there're only at most `16` requests, we could try all combinations of achievable requests.

**Each request has two states: satisified or not satisified**

So there're totally `2^16` combinations of states of requests.

Try all of them and record the employee moving count into `cnt[]`, then check if all building's `cnt[i] == 0`.

Note that there's a prunning of state: `if (Integer.bitCount(s) <= max) continue;`

```java
class Solution {
    public int maximumRequests(int n, int[][] requests) {
        int[] cnt = new int[n];
        int m = requests.length;
        int max = 0;
        for (int s = 0; s < 1 << m; s++) {
            if (Integer.bitCount(s) <= max) continue; // prunning!!
            Arrays.fill(cnt, 0);
            for (int i = 0; i < m; i++) {
                if ((s >> i & 1) == 0) continue;
                int a = requests[i][0], b = requests[i][1];
                cnt[a]--; cnt[b]++;
            }
            boolean valid = true;
            for (int i = 0; i < n && valid; i++) {
                valid &= cnt[i] == 0;
            }
            if (valid) max = Math.max(max, Integer.bitCount(s));
        }
        return max;
    }
}
```

T: O(n\*2^m)			S: O(n)

---

#### DFS

DFS with backtracking is a little bit faster because of prunning.

We can choose whether we satisify the `i`th request or not.

```java
class Solution {
    int n, m;
    int[] cnt;
    int max;
    int[][] requests;
    
    public int maximumRequests(int n, int[][] requests) {
        this.requests = requests;
        this.n = n;
        m = requests.length;
        cnt = new int[n];
        max = 0;
        dfs(0, 0);
        return max;
    }
    private void dfs(int index, int count) {
        if (index == m) {
            boolean valid = true;
            for (int i = 0; i < n && valid; i++) {
                valid &= cnt[i] == 0;
            }
            if (valid) max = Math.max(max, count);
            return;
        }
        int a = requests[index][0], b = requests[index][1];
        cnt[a]--; cnt[b]++;
        dfs(index + 1, count + 1);
        cnt[a]++; cnt[b]--;
        dfs(index + 1, count);
    }
}
```

T: O(n\*2^m)			S: O(2^m)

