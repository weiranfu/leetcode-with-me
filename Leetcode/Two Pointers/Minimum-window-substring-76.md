---
title: Hard | Minimum Window Substring 76
tags:
  - tricky
categories:
  - Leetcode
  - Two Pointers
date: 2020-05-16 18:30:44
---

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

[Leetcode](https://leetcode.com/problems/minimum-window-substring/)

<!--more-->

**Example:**

```
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
```

**Note:**

- If there is no such window in S that covers all characters in T, return the empty string `""`.
- If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

---

#### Tricky 

For most substring problem, we are given a string and need to find a substring of it which satisfy some restrictions. A general way is to use a hashmap assisted with two pointers. The template is given below.

```java
int findSubstring(string s){
        vector<int> map(128,0);
        int counter; // check whether the substring is valid
        int begin=0, end=0; //two pointers, one point to tail and one  head
        int d; //the length of substring

        for() { /* initialize the hash map here */ }

        while(end<s.size()){

            if(map[s[end++]]-- ?){  /* modify counter here */ }

            while(/* counter condition */){ 
                 
                 /* update d here if finding minimum*/

                //increase begin to make it invalid/valid again
                
                if(map[s[begin++]]++ ?){ /*modify counter here*/ }
            }  

            /* update d here if finding maximum*/
        }
        return d;
  }
```

**One thing needs to be mentioned is that when asked to find maximum substring, we should update maximum after the inner while loop to guarantee that the substring is valid. On the other hand, when asked to find minimum substring, we should update minimum inside the inner while loop.**

---

#### My thoughts 

Failed to solve.

---

#### Standard solution  

Use `cnt` to count number of unique chars in string `t`.

`cnt == 0` means we have collect all chars in the window.

```java
class Solution {
    public String minWindow(String s, String t) {
        int m = s.length(), n = t.length();
        int[] map = new int[128];
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (map[t.charAt(i)] == 0) {
                cnt++;
            }
            map[t.charAt(i)]++;
        }
        int min = m + 1;
        int l = -1, r = -1;
        for (int i = 0, j = 0; i < m; i++) {
            map[s.charAt(i)]--;
            if (map[s.charAt(i)] == 0) {
                cnt--;
            }
            while (j <= i && cnt == 0) {		// we collect all chars in the window
                if (min > i - j + 1) {
                    min = i - j + 1;
                    l = j; r = i;
                }
                if (map[s.charAt(j)] == 0) {
                    cnt++;
                }
                map[s.charAt(j)]++;
                j++;
            }
        }
        return min == m + 1 ? "" : s.substring(l, r + 1);
    }
}
```

T: O(n)		S: O(1)

---

#### Summary 

In tricky.