---
title: Hard | Minimize Max Distance to Gas Station 774
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Binary Search
date: 2020-06-28 15:04:26
---

On a horizontal number line, we have gas stations at positions `stations[0], stations[1], ..., stations[N-1]`, where `N = stations.length`.

Now, we add `K` more gas stations so that **D**, the maximum distance between adjacent gas stations, is minimized.

Return the smallest possible value of **D**.

[Leetcode](https://leetcode.com/problems/minimize-max-distance-to-gas-station/)

<!--more-->

**Example:**

```
Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
Output: 0.500000
```

**Note:**

1. `stations.length` will be an integer in range `[10, 2000]`.
2. `stations[i]` will be an integer in range `[0, 10^8]`.
3. `K` will be an integer in range `[1, 10^6]`.
4. Answers within `10^-6` of the true value will be accepted as correct.

---

#### Tricky 

#### Approach #1: Dynamic Programming [Memory Limit Exceeded]

**Intuition**

Let `dp[n][k]` be the answer for adding `k` more gas stations to the first `n` intervals of stations. We can develop a recurrence expressing `dp[n][k]` in terms of `dp[x][y]` with smaller `(x, y)`.

**Algorithm**

Say the `i`th interval is `deltas[i] = stations[i+1] - stations[i]`. We want to find `dp[n+1][k]` as a recursion. We can put `x` gas stations in the `n+1`th interval for a best distance of `deltas[n+1] / (x+1)`, then the rest of the intervals can be solved with an answer of `dp[n][k-x]`. The answer is the minimum of these over all `x`.

From this recursion, we can develop a dynamic programming solution.

```java
class Solution {
    public double minmaxGasDist(int[] stations, int K) {
        int N = stations.length;
        double[] deltas = new double[N-1];
        for (int i = 0; i < N-1; ++i)
            deltas[i] = stations[i+1] - stations[i];

        double[][] dp = new double[N-1][K+1];
        //dp[i][j] = answer for deltas[:i+1] when adding j gas stations
        for (int i = 0; i <= K; ++i)
            dp[0][i] = deltas[0] / (i+1);

        for (int p = 1; p < N-1; ++p)
            for (int k = 0; k <= K; ++k) {
                double bns = 999999999;
                for (int x = 0; x <= k; ++x)
                    bns = Math.min(bns, Math.max(deltas[p] / (x+1), dp[p-1][k-x]));
                dp[p][k] = bns;
            }

        return dp[N-2][K];
    }
}
```

**Complexity Analysis**

- Time Complexity: O(N K^2), where N*N* is the length of `stations`.
- Space Complexity: O(N K), the size of `dp`.

#### Approach #2: Brute Force [Time Limit Exceeded]

**Intuition**

As in *Approach #1*, let's look at `deltas`, the distances between adjacent gas stations.

Let's repeatedly add a gas station to the current largest interval, so that we add `K` of them total. This greedy approach is correct because if we left it alone, then our answer never goes down from that point on.

**Algorithm**

To find the largest current interval, we keep track of how many parts `count[i]` the `i`th (original) interval has become. (For example, if we added 2 gas stations to it total, there will be 3 parts.) The new largest interval on this section of road will be `deltas[i] / count[i]`.

```java
class Solution {
    public double minmaxGasDist(int[] stations, int K) {
        int N = stations.length;
        double[] deltas = new double[N-1];
        for (int i = 0; i < N-1; ++i)
            deltas[i] = stations[i+1] - stations[i];

        int[] count = new int[N-1];
        Arrays.fill(count, 1);

        for (int k = 0; k < K; ++k) {
            // Find interval with largest part
            int best = 0;
            for (int i = 0; i < N-1; ++i)
                if (deltas[i] / count[i] > deltas[best] / count[best])
                    best = i;

            // Add gas station to best interval
            count[best]++;
        }

        double ans = 0;
        for (int i = 0; i < N-1; ++i)
            ans = Math.max(ans, deltas[i] / count[i]);

        return ans;
    }
}
```

**Complexity Analysis**

- Time Complexity: O(N K), where N*N* is the length of `stations`.
- Space Complexity: O(N)*O*(*N*), the size of `deltas` and `count`.

#### Approach #3: Heap [Time Limit Exceeded]

**Intuition**

Following the intuition of *Approach #2*, if we are taking a repeated maximum, we can replace this with a heap data structure, which performs repeated maximum more efficiently.

**Algorithm**

As in *Approach #2*, let's repeatedly add a gas station to the next larget interval `K` times. We use a heap to know which interval is largest. In Python, we use a negative priority to simulate a max heap with a min heap.

```java
class Solution {
    public double minmaxGasDist(int[] stations, int K) {
        int N = stations.length;
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((a, b) ->
            (double)b[0]/b[1] < (double)a[0]/a[1] ? -1 : 1);
        for (int i = 0; i < N-1; ++i)
            pq.add(new int[]{stations[i+1] - stations[i], 1});

        for (int k = 0; k < K; ++k) {
            int[] node = pq.poll();
            node[1]++;
            pq.add(node);
        }

        int[] node = pq.poll();
        return (double)node[0] / node[1];
    }
}
```

**Complexity Analysis**

Let N*N* be the length of stations, and K*K* be the number of gas stations to add.

- Time Complexity: O*(*N*+*K*log*N)
  - First of all, we scan the stations to obtain a list of intervals between each adjacent stations.
  - Then it takes another O(N)*O*(*N*) to build a heap out of the list of intervals.
  - Finally, we repeatedly pop out an element and push in a new element into the heap, which takes O(\log N)*O*(log*N*) respectively. In total, we repeat this step for K*K* times (*i.e.* to add K*K* gas stations).
  - To sum up, the overall time complexity of the algorithm is O*(*N*)+*O*(*N*)+*O*(*K*⋅log*N*)=*O*(*N*+*K*⋅log*N).
- Space Complexity: O(N)*O*(*N*), the size of `deltas` and `count`.

#### Approach #4: Binary Search [Accepted]

**Intuition**

Let's ask `possible(D)`: with `K` (or less) gas stations, can we make every adjacent distance between gas stations at most `D`? This function is monotone, so we can apply a binary search to find D^{\text{*}}*D**.

**Algorithm**

More specifically, there exists some `D*` (the answer) for which `possible(d) = False` when `d < D*` and `possible(d) = True` when `d > D*`. Binary searching a monotone function is a typical technique, so let's focus on the function `possible(D)`.

When we have some interval like `X = stations[i+1] - stations[i]`, we'll need to use `X/D` gas stations to ensure every subinterval has size less than `D`. This is independent of other intervals, so in total we'll need to use ∑*i*⌊X/Di⌋ gas stations. If this is at most `K`, then it is possible to make every adjacent distance between gas stations at most `D`.

```java
class Solution {
    public double minmaxGasDist(int[] stations, int K) {
        int n = stations.length;
        double max = stations[1] - stations[0];
        for (int i = 0; i < n - 1; i++) {
            max = Math.max(max, stations[i + 1] - stations[i]);
        }
        double l = 0, r = max;
        while (l + 1e-8 < r) {
            double mid = l + (r - l) / 2;
            if (check(stations, K, mid)) {
                r = mid;
            } else {
                l = mid;
            }
        }
        return l;
    }
    
    public boolean check(int[] stations, int K, double max) {
        int n = stations.length;
        int cnt = 0;
        for (int i = 0; i < n - 1; i++) {
            cnt += (int)(stations[i + 1] - stations[i]) / max;
        }
        return cnt <= K;
    }
}
```

**Complexity Analysis**

- Time Complexity: O*(*N*log*W*), where N*N* is the length of `stations`, and W = max distance.
- Space Complexity: O(1) in additional space complexity.

