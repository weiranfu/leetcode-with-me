---
title: Medium | Restore IP Address
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-05-20 02:08:32
---

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

[Leetcode](https://leetcode.com/problems/restore-ip-addresses/)

<!--more-->

**Example:**

```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

---

#### Tricky 

This is a backtracking problem. We could try all possible decoding ways to restore IP.

We could try at most 3 index away. 

---

#### Standard solution  

```java
class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> res = new ArrayList<>();
        if (s == null || s.length() == 0) return res;
        getIp(0, new ArrayList<String>(), s, res);
        return res;
    }
    
    private void getIp(int idx, List<String> list, String s, List<String> res) {
        int n = s.length();
        if (list.size() == 4) {
            if (idx == n) {
                res.add(String.join(".", list));
            } 
            return;
        }
        for (int i = 1; i < 4; i++) {  
            if (idx + i > n) break;                 // try 3 index away.
            String ip = s.substring(idx, idx + i);
            if ((ip.charAt(0) == '0' && ip.length() > 1) // cann't start with '0'
                || (i == 3 && Integer.parseInt(ip) > 255)) continue;
            list.add(ip);
            getIp(idx + i, list, s, res);
            list.remove(list.size() - 1);
        }
    }
}
```

T: O(n)			S: O(n)

---

#### Brute Force

```java
static List<String> restoreIpAddresses(String s) {
	List<String> ans = new ArrayList<String>();
	int len = s.length();
	for (int i = 1; i <=3; ++i){  // first cut
		if (len-i > 9) continue;    		
		for (int j = i+1; j<=i+3; ++j){  //second cut
			if (len-j > 6) continue;    			
			for (int k = j+1; k<=j+3 && k<len; ++k){  // third cut
				int a,b,c,d;                // the four int's seperated by "."
				a = Integer.parseInt(s.substring(0,i));  
				b = Integer.parseInt(s.substring(i,j)); // notice that "01" can be parsed into 1. Need to deal with that later.
				c = Integer.parseInt(s.substring(j,k));
				d = Integer.parseInt(s.substring(k));
				if (a>255 || b>255 || c>255 || d>255) continue; 
				String ip = a+"."+b+"."+c+"."+d;
				if (ip.length()<len+3) continue;  // this is to reject those int's parsed from "01" or "00"-like substrings
				ans.add(ip);
			}
		}
	}
	return ans;
}
```

T: O(1)			S: O(1)

