---
title: Medium | Find Servers that Handled Most Number of Requests 1606
tags:
  - common
  - tricky
categories:
  - Leetcode
  - TreeMap
date: 2020-10-07 00:57:41
---

You have `k` servers numbered from `0` to `k-1` that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but **cannot handle more than one request at a time**. The requests are assigned to servers according to a specific algorithm:

- The `ith` (0-indexed) request arrives.
- If all servers are busy, the request is dropped (not handled at all).
- If the `(i % k)th` server is available, assign the request to that server.
- Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the `ith` server is busy, try to assign the request to the `(i+1)th` server, then the `(i+2)th` server, and so on.

You are given a **strictly increasing** array `arrival` of positive integers, where `arrival[i]` represents the arrival time of the `ith` request, and another array `load`, where `load[i]` represents the load of the `ith` request (the time it takes to complete). Your goal is to find the **busiest server(s)**. A server is considered **busiest** if it handled the most number of requests successfully among all the servers.

Return *a list containing the IDs (0-indexed) of the **busiest server(s)***. You may return the IDs in any order.

[Leetcode](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/)

<!--more-->

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/09/08/load-1.png)

```
Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
Output: [1] 
Explanation:
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.
```

---

#### PriorityQueue + TreeMap  

Since we need to find the next available server starts at `i % k`, we can use TreeMap.

`treeset.ceiling(i % k)`

If we cann't find it, the server will be `treeset.fisrt()`.

```java
class Solution {
    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {
        int n = arrival.length;
        int[] cnt = new int[k];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        TreeSet<Integer> set = new TreeSet<>();
        for (int i = 0; i < k; i++) set.add(i);
        for (int i = 0; i < n; i++) {
            while (!pq.isEmpty() && pq.peek()[0] <= arrival[i]) set.add(pq.poll()[1]);
            if (set.size() == 0) continue;          // all busy
            Integer server = set.ceiling(i % k);
            if (server == null) server = set.first();
            cnt[server]++;
            pq.add(new int[]{arrival[i] + load[i], server});
            set.remove(server);
        }
        int max = 0;
        for (int i = 0; i < k; i++) {
            max = Math.max(max, cnt[i]);
        }
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            if (cnt[i] == max) res.add(i);
        }
        return res;
    }
}
```

T: (nlogn)			S: O(n)

