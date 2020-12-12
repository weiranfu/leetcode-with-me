---
title: Hard | Palindrome Partition II 132	
tags:
  - tricky
categories:
  - Leetcode
  - DP	
date: 2020-05-27 21:01:31
---

Given a string *s*, partition *s* such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of *s*.

[Leetcode](https://leetcode.com/problems/palindrome-partitioning-ii/)

<!--more-->

**Example:**

```
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
```

**Follow up**

[Palindrome Partition III](https://leetcode.com/problems/palindrome-partitioning-iii/)

---

#### Tricky 

This is a follow up of [Palindrome Partition I](https://leetcode.com/problems/palindrome-partitioning/), which is solved by backtracking.

Here we could not use backtracking any more(because of LTE!). In *Palindrome Partition I* we could use backtracking because we need to find all possible cuts. However in this problem we only need to find `minCut`.

There're three appoarches.

1. **Backtracking with pruning —> LTE**. We explore each possible palindrome and backtracking to find minimum size one.
2. **DP**. We maintain a `int[] dp` to record current `minCut` of substring `s[:i]`. Try all possible palindrome in `s[:i]`, then `dp[i] = min{ dp[j] + 1 for j in [1, i] } if s[j:i] is a palindrome`.
3. **DP**. Use `boolean[][] isPalindrome` to record whether `s[j:i]` is a palindrome, which could speed up the approach 2.

---

#### First solution 

**LTE!!!!** Backtracking with pruning to search `minCut`

```java
class Solution {
    public int minCut(String s) {
        int[] min = new int[1];
        min[0] = Integer.MAX_VALUE;
        explore(0, s, 0, min);
        return min[0] - 1;
    }
    
    private void explore(int start, String s, int size, int[] min) {
        int n = s.length();
        if (size >= min[0]) return;
        if (start >= n) {
            min[0] = Math.min(min[0], size);
            return;
        }
        for (int i = n; i > start; i--) {
            if (isPalindrome(s, start, i)) {
                explore(i, s, size + 1, min);
            }
        }
    }
    
    private boolean isPalindrome(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left) == s.charAt(right - 1)) {
                left++;
                right--;
            } else {
                return false;
            }
        }
        return true;
    }
}
```

**LTE**

---

#### DP

Actually, we can determine a palindrome in O(n^2)

Use `boolean[][] isPalin` to record results of whether substring `s[i:j]` is a palindrome.

`isPalin[i][j] = (s.charAt(i) == s.charAt(j) && (j - i < 3 || isPalin[i + 1][j - 1]))`

可以用区间dp

**How to get the `minCut`?**

```java
if isPalin[1][i]:
	minCut[i] = 0
else:
	minCut[i] = min{ minCut[j] for j in [1, i-1] if isPalin[j+1][i]}
```

```java
class Solution {
    public int minCut(String s) {
        if (s == null || s.length() == 0) return 0;
        int n = s.length();
        int[] minCut = new int[n + 1];
        boolean[][] isPalin = new boolean[n + 1][n + 1];
        for (int i = 1; i <= n; i++) {
            isPalin[i][i] = true;
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 1, j = len; j <= n; i++, j++) {
                if (s.charAt(i - 1) == s.charAt(j - 1)) {
                    isPalin[i][j] = (j - i < 3) || isPalin[i + 1][j - 1];
                }
            }
        }
        for (int i = 2; i <= n; i++) {
            if (isPalin[1][i]) continue;
            int min = Integer.MAX_VALUE;
            for (int j = 1; j < i; j++) {
                if (isPalin[j + 1][i]) {
                    min = Math.min(min, minCut[j] + 1);
                }
            }
            minCut[i] = min;
        }
        return minCut[n];
    }
}
```

T: O(n^2)		S: O(n^2)

