---
title: Hard | Maximum Number of Non-overlapping Substrings 1520
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Greedy
date: 2020-07-19 15:59:49
---

Given a string `s` of lowercase letters, you need to find the maximum number of **non-empty** substrings of `s` that meet the following conditions:

1. The substrings do not overlap, that is for any two substrings `s[i..j]` and `s[k..l]`, either `j < k` or `i > l` is true.
2. A substring that contains a certain character `c` must also contain all occurrences of `c`.

Find *the maximum number of substrings that meet the above conditions*. If there are multiple solutions with the same number of substrings, *return the one with minimum total length.* It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in **any** order.

[Leetcode](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/)

<!--more-->

**Example 1:**

```
Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.
```

**Example 2:**

```
Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.
```

**Constraints:**

- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters.

**Follow up**

[Partition Labels](https://leetcode.com/problems/partition-labels/)

---

#### Greedy

1. Firstly we need to find the maximum occurrence of each letter in `s`.

   Since there're 26 letters, we could store `min` and `max` index in `min[26]` and `max[26]`

2. Then we need to make sure that if a char `c` appears in a string, all other occurrences of `c` should be included.

   So we need to check all chars other than `c` in `[min[c], max[c]]` and try to extend the interval merging with intervals of other chars.

   For example, `abeeaabb` we have `min['a'] = 0, max['a'] = 6`, `min[b] = 1, max[b] = 8`

   So the merged interval for `a` will be `[0, 8]`, for `b` will be `[0, 8]`, for `e` will be `[2, 3]`

3. Then we need to choose from these merged intervals as many as we can without overlapping.

   At this time, if two intervals are overlapped, which means interval A is included by interval B.

   It is impossible for two intervals being intersacted.

   **it's impossible for any two valid substrings to overlap unless one is inside another.**

   So we could perform **Greedy** to add small length intervals before larger ones.

   **If we find an interval include a shorter interval, we won't choose it and choose the shorter one.**

```java
class Solution {
    public List<String> maxNumOfSubstrings(String s) {
        int n = s.length();
        int[] max = new int[26]; int[] min = new int[26];
        Arrays.fill(min, -1); Arrays.fill(max, -1);
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (min[c - 'a'] == -1) {
                min[c - 'a'] = i;
            }
            max[c - 'a'] = i;
        }
        List<int[]> list = new ArrayList<>();
        // merge intervals
        for (int i = 0; i < 26; i++) {
            if (min[i] == -1) continue;
            int l = min[i], r = max[i];
            boolean valid = true;
            for (int j = l; j <= r; j++) {         // check each chars in [l, r]
                if (min[s.charAt(j) - 'a'] < l) {  // only merge intervals that begin point > l
                    valid = false;
                    break;
                }
                r = Math.max(r, max[s.charAt(j) - 'a']);
            }
            if (valid) {
                list.add(new int[]{l, r});
            }
        }
        // Since merged intervals can only include each other rather than intersect,
        // we could sort by end point of interval
        Collections.sort(list, (a, b) -> a[1] - b[1]);
        List<String> res = new ArrayList<>();
        int end = -1;
        for (int i = 0; i < list.size(); i++) {
            int[] range = list.get(i);
            if (range[0] > end) {
                res.add(s.substring(range[0], range[1] + 1));
                end = range[1];
            } 
        }
        return res;
    }
}
```

T: O(n)			Since there're at most 26 letters, the time complexity is O(n)

S: O(1)