---
title: Medium | Friend Circles 547
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Union Find
date: 2020-08-25 22:52:09
---

There are **N** students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a **direct** friend of B, and B is a **direct** friend of C, then A is an **indirect** friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a **N\*N** matrix **M** representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are **direct** friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

[Leetcode](https://leetcode.com/problems/friend-circles/)

<!--more-->

**Example 1:**

```
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
```

**Example 2:**

```
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
```

**Constraints:**

- `1 <= N <= 200`
- `M[i][i] == 1`
- `M[i][j] == M[j][i]`

---

#### Union Find

Union students into groups and maintain the number of groups.

```java
class Solution {
    int[] uf;
    
    public int findCircleNum(int[][] M) {
        int N = M.length;
        uf = new int[N];
        int cnt = N;
        for (int i = 0; i < N; i++) uf[i] = i;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (M[i][j] == 1) {
                    int x = find(i), y = find(j);
                    if (x != y) {		// if not in a group
                        uf[x] = y;
                        cnt--;
                    }
                }
            }
        }
        return cnt;
    }
    
    private int find(int x) {
        if (uf[x] != x) {
            uf[x] = find(uf[x]);
        }
        return uf[x];
    }
}
```

T: O(n^2\*A(1))		S: O(n)

---

#### DFS

We could perform DFS to find all connected friends.

Use `visited[]` to record the visited friend.

```java
class Solution {
    public int findCircleNum(int[][] M) {
        int N = M.length;
        boolean[] visited = new boolean[N];
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                cnt++;
                visited[i] = true;
                dfs(i, visited, M);
            }
        }
        return cnt;
    }
    private void dfs(int x, boolean[] visited, int[][] M) {
        int N = M.length;
        for (int i = 0; i < N; i++) {
            if (!visited[i] && M[x][i] == 1) {
                visited[i] = true;
                dfs(i, visited, M);
            }
        }
    }
}
```

T: O(n^2)			S: O(n)