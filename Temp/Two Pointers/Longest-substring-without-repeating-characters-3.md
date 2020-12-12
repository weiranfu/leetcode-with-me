---
title: Medium | Longest Substring Without Repeating Characters 3
tags:
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2019-10-30 21:20:46
---

Given a string, find the length of the **longest substring** without repeating characters.

[Leetcode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

<!--more-->

**Example 1:**

```
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

**Example 2:**

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Follow up**

[Longest Substring with At Most K Distinct Characters 340](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)

---

#### Tricky 

This is a sliding window problem. We need to find the longest substring without repeating.

When we add a new char into window, we must try to shrink the left boundary of window until there's no repeating chars in the window.

Then record the length of current window.

---

#### Sliding Window 

Use `int[] map = new int[128]` to count occurence of each char.

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) return 0;
        int n = s.length();
        int[] cnt = new int[128];
        int res = 0;
        for (int i = 0, j = 0; i < n; i++) {
            cnt[s.charAt(i)]++;
            while (j <= i && cnt[s.charAt(i)] > 1) {
                cnt[s.charAt(j)]--;
                j++;
            }
            res = Math.max(res, i - j + 1);
        }
        return res;
    }
}
```

T: O(n) 			S: O(1)

---

#### Sliding Window II

Use `map` to record the last occurrence of a char.

If we find current char has appeared before, we can just set `j` to `last_pos + 1`.

We need to make sure that `j` will not go back. `j = Math.max(j, last_pos + 1)`

For example: Consider the input: `"tmsmfdut"` for the case when `i = s.length()-1`. Here, `j= 2`.
if you just use , `map.get(s.charAt(i))+1`, then `j` will be set to 1 and it will give wrong answer.

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) return 0;
        int n = s.length();
        int[] map = new int[128];
        Arrays.fill(map, -1);
        int res = 0;
        for (int i = 0, j = 0; i < n; i++) {
            if (map[s.charAt(i)] != -1) {
                j = Math.max(j, map[s.charAt(i)] + 1); // move forward j
            }
            map[s.charAt(i)] = i;       // record pos
            res = Math.max(res, i - j + 1);
        }
        return res;
    }
}
```

T: O(n)		S: O(1)