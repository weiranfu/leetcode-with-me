---
title: Easy | String Compression 443
tags:
  - common
  - tricky
categories:
  - Leetcode
  - String
date: 2020-08-25 22:19:48
---

Given an array of characters, compress it [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm).

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a **character** (not int) of length 1.

After you are done **modifying the input array in-place**, return the new length of the array.

Could you solve it using only O(1) extra space?

[Leetcode](https://leetcode.com/problems/string-compression/)

<!--more-->

**Example 1:**

```
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
```

**Example 2:**

```
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
```

---

#### Standard solution  

```java
class Solution {
    int curr = 1;
    
    public int compress(char[] chars) {
        int n = chars.length;
        char prev = chars[0];
        int count = 1;
        for (int i = 1; i < n; i++) {
            if (chars[i] != prev) {
                if (count != 1) parseInt(count, chars);
                chars[curr++] = chars[i];
                prev = chars[i];
                count = 1;
            } else {
                count++;
            }
        }
        if (count != 1) parseInt(count, chars);
        return curr;
    }
    
    private void parseInt(int count, char[] chars) {
      	// convert int to String for reverse processing
        String s = String.valueOf(count);  
        for (int i = 0; i < s.length(); i++) {
            chars[curr++] = s.charAt(i);
        }
    }
}
```

T: O(n)			S: O(1)

