---
title: Medium | Determine If Two Strings Are Close 1657
categories:
  - LeetCode
  - String
date: 2020-12-13 22:11:14
---

# Determine If Two Strings Are Close 1657

Two strings are considered **close** if you can attain one from the other using the following operations:

- Operation 1: Swap any two existing characters.
  - For example, `abcde -> aecdb`
- Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
  - For example, `aacabb -> bbcbaa` (all `a`'s turn into `b`'s, and all `b`'s turn into `a`'s)

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return `true` *if* `word1` *and* `word2` *are **close**, and* `false` *otherwise.*

[Leetcode](https://leetcode.com/problems/determine-if-two-strings-are-close/)

<!--more-->

**Example 1:**

```
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
```

**Example 2:**

```
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
```

**Constraints:**

- `1 <= word1.length, word2.length <= 105`
- `word1` and `word2` contain only lowercase English letters.

---

#### Standard Solution

The operation1 means that the position of each char doesn't matter.

The operation2 means that the frequency pattern of two strings must be same.

**Overall, the chars occur in `word1` must occur in `word2`, or vice versa. Because we can only swap or change existing chars.**

**What is frequency pattern?**

For example, 

```java
String 1 = "aabaacczp"        String 2="bbzbbaacp"
Frequency in string1 :                         Frequency in string2 :
	  a->4                                                b->4
		b->1                                                a->2
		c->2                                                z->1
		z->1                                                c->1
		p->1                                                p->1
		
see in String 1 count array ->   1, 1, 1, 2, 4 =>sorted order
and in String 2 count array ->   1, 1, 1, 2, 4 =>sorted order
```

So we could use two maps to count the frequency of chars in two words.

How can we make sure that chars occur in `word1` must occur in `word2` or vice versa?

We can check `if (cnt1[i] != cnt2[i] && cnt1[i] * cnt2[i] == 0)`.

```java
class Solution {
    public boolean closeStrings(String word1, String word2) {
        int l1 = word1.length(), l2 = word2.length();
        if (l1 != l2) return false;
        int[] cnt1 = new int[26], cnt2 = new int[26];
        for (char c1 : word1.toCharArray()) {
            cnt1[c1 - 'a']++;
        }
        for (char c2 : word2.toCharArray()) {
            cnt2[c2 - 'a']++;
        }
        for (int i = 0; i < 26; i++) {
            // this char occurs in word1 but doesn't occur in word2
            if (cnt1[i] != cnt2[i] && cnt1[i] * cnt2[i] == 0) return false;
        }
        Arrays.sort(cnt1);
        Arrays.sort(cnt2);
        for (int i = 0; i < 26; i++) {
            if (cnt1[i] != cnt2[i]) return false;
        }
        return true;
    }
}
```

T: O(n)		S:  O(1)



