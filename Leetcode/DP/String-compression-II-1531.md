---
title: Hard | String Compression II 1531
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-07-26 18:41:12
---

[Run-length encoding](http://en.wikipedia.org/wiki/Run-length_encoding) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string `"aabccc"` we replace `"aa"` by `"a2"` and replace `"ccc"` by `"c3"`. Thus the compressed string becomes `"a2bc3"`.

Notice that in this problem, we are not adding `'1'` after single characters.

Given a string `s` and an integer `k`. You need to delete **at most** `k` characters from `s` such that the run-length encoded version of `s` has minimum length.

Find the *minimum length of the run-length encoded version of* `s` *after deleting at most* `k` *characters*.

[Leetcode](https://leetcode.com/problems/string-compression-ii/)

<!--more-->

**Example:**

```
Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
```

---

#### 4D-DP    **LTE**

Use `dp[i][k][c][cnt]` to represent min length of string at index `i`, delete `k` letters, ending color is `c`, ending color's count is `cnt`.

If we delete `s[i]`, keep previous color and cnt, total length doesn't change.

If we don't delete `s[i]`,

​		if previous color is same as `s[i]`, we append `s[i]`. color doesn't change, cnt + 1. Total length will increase 1 if previous cnt <= 1 || cnt == 9 || cnt == 99.

​		if previous color is different with `s[i]`, we append a new `s[i]`. Color will be `s[i]`, `cnt = 1`.

Total length will increase 1.

```java
if we delete s[i]:    
	dp[i][k][c1][j] = Math.min(dp[i][k][c1][j], dp[i - 1][k - 1][c1][j]);  // delete
else:
	if previous_color == s[i]:
			dp[i][k][c][j] = Math.min(dp[i][k][c][j], dp[i - 1][k][c][j - 1] + incre(j - 1));
  else:
			dp[i][k][c][1] = Math.min(dp[i][k][c][1], dp[i - 1][k][c1][j] + 1);
```

```java
class Solution {
    public int getLengthOfOptimalCompression(String s, int K) {
        int INF = 0x3f3f3f3f;
        int n = s.length();
        int[][][][] dp = new int[n + 1][K + 1][26][n + 1];
        for (int i = 0; i <= n; i++) {
            for (int k = 0; k <= K; k++) {
                for (int c = 0; c < 26; c++) {
                    Arrays.fill(dp[i][k][c], INF);
                }
            }
        }
        dp[0][0][s.charAt(0) - 'a'][0] = 0;
        for (int i = 1; i <= n; i++) {
            int c = s.charAt(i - 1) - 'a';
            for (int k = 0; k <= K; k++) {
                for (int c1 = 0; c1 < 26; c1++) {
                    for (int j = 0; j <= i; j++) {
                        if (k != 0) {					// delete
                            dp[i][k][c1][j] = Math.min(dp[i][k][c1][j], 
                                                       dp[i - 1][k - 1][c1][j]);  
                        }											// previous color is not same
                        if (c1 != c) dp[i][k][c][1] = Math.min(dp[i][k][c][1], 
                                                               dp[i - 1][k][c1][j] + 1);
                    }
                }
                for (int j = 1; j <= i; j++) { // previous color is same 
                    dp[i][k][c][j]  = Math.min(dp[i][k][c][j], 
                                               dp[i - 1][k][c][j - 1] + incre(j - 1));
                }
            }
        }
        int len = INF;
        for (int k = 0; k <= K; k++) {
            for (int c = 0; c < 26; c++) {
                for (int j = 0; j <= n; j++) {
                    len = Math.min(len, dp[n][k][c][j]);
                }
            }
        }
        return len;
    }
    private int incre(int cnt) {
        if (cnt <= 1 || cnt == 9 || cnt == 99) return 1;
        else return 0;
    }
}
```

T: O(n^2\*K).  (**LTE**)			S: O(n^2\*K)

---

#### Optimized: Top-down with memorization

Since we have calculated too much useless states in DP, we could perform Top-down search with memorization and positive transition.

So we only compute the state we need.

```java
class Solution {
    int INF = 0x3f3f3f3f;
    int[][][][] dp;
    int n, K;
    String s;
    
    public int getLengthOfOptimalCompression(String s, int K) {
        n = s.length();
        this.K = K;
        this.s = s;
        dp = new int[n + 1][K + 1][26][n + 1];
        for (int i = 0; i <= n; i++) {
            for (int k = 0; k <= K; k++) {
                for (int c = 0; c < 26; c++) {
                    Arrays.fill(dp[i][k][c], -1);
                }
            }
        }
        return search(0, 0, -1, 0);
    }
    private int search(int x, int delete, int c, int cnt) {
        if (c != -1 && dp[x][delete][c][cnt] != -1) return dp[x][delete][c][cnt];
        if (x >= n) return 0;
        int min = INF;								// choose delete
        if (delete < K) min = Math.min(min, search(x + 1, delete + 1, c, cnt));
        int curr = s.charAt(x) - 'a';
        if (curr != c) {						  // same char as previous
            min = Math.min(min, search(x + 1, delete, curr, 1) + 1); 
        } else {											// different char with previous
            min = Math.min(min, search(x + 1, delete, c, cnt + 1) + incre(cnt));
        }
        if (c != -1) dp[x][delete][c][cnt] = min;
        return min;
    }
    private int incre(int cnt) {
        if (cnt <= 1 || cnt == 9 || cnt == 99) return 1;
        else return 0;
    }
}
```

T: O(n^2\*k)			S: O(n)

---

#### Optimized: 2D-DP  

[Here](https://leetcode.com/problems/string-compression-ii/discuss/756022/C%2B%2B-Top-Down-DP-with-explanation-64ms-short-and-clear)

