---
title: Easy | First unique character in a string 387
tags:
  - common
  - Oh-shit
categories:
  - Leetcode
  - String
date: 2019-07-28 14:58:09
---

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

[Leetcode](https://leetcode.com/problems/first-unique-character-in-a-string/)

<!--more-->

**Examples:**

```
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```

**Note:** You may assume the string contain only lowercase letters.

---

#### Oh-Shit 

When we want to increment a character `'a'`, **we cannot use `'a' + 1`, because this will become an integer not a char!** Instead, we can use:

`(char) ('a' + 1)` to cast int to char.

---

#### My thoughts 

Build a dictionary of 26 characters.

Then look up in the dictionary to find unique chars.

Finally compare them index to find the minimum one.

---

#### First solution 

```java
class Solution {
    public int firstUniqChar(String s) {
        int[] characters = new int[26];
        int uniqueIndex = Integer.MAX_VALUE;
        // Store in the dictionary.
        for (int i = 0; i < s.length(); i += 1) {
            characters[s.charAt(i) - 'a'] += 1;
        }
        // Looking for first unique char.
        for (int i = 0; i < characters.length; i += 1) {
            if (characters[i] == 1) {
                char c = (char) ('a' + i);        // Cast int to char.
                uniqueIndex = Math.min(uniqueIndex, s.indexOf(Character.toString(c)));
            }
        }
        if (uniqueIndex == Integer.MAX_VALUE) {
            return -1;
        }
        return uniqueIndex;
    }
}
```

T: O(n) S: O(1)

---

#### Standard solution 

After we build a characters dictionary int[26], **we could loop the string again from front to back to find unique char** other than look up in the dictionary to find unique chars and then find the minimum index of them.

```java
class Solution {
    public int firstUniqChar(String s) {
        int[] characters = new int[26];
        for (int i = 0; i < s.length(); i += 1) {
            characters[s.charAt(i) - 'a'] += 1;
        }
        for (int i = 0; i < s.length(); i += 1) {
            if (characters[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
}
```

T: O(n), S: O(1)

---

#### Third Solution (Better)

Using built-in method `indexOf` and `lastindexOf`.

All possible solution is between `'a'` and `'z'`.

```java
class Solution {
    public int firstUniqChar(String s) {
        if(s == null || s.isEmpty()) return -1;
        int min = Integer.MAX_VALUE;
        // Loop in 'a' and 'z'.
        for(char c = 'a'; c <= 'z'; c++) {
            int first = s.indexOf(c);
            int last = s.lastIndexOf(c);
            
            if(first != -1 && first == last) {
                min = Math.min(min, first);
            }
        }
        return min == Integer.MAX_VALUE ? -1 : min;
    }
}
```

Because `indexOf()` could be O(n), `for` loop time complexity is O(1),

So total time complexity is O(n).

And this will be faster than two methods above, because these two methods use `charAt()` built-in methods which will take some time.

---

#### Using HashMap

This will be slower than second solution using a 26 long dictionary.

```java
class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> charMap = new HashMap<>();
        for (int i = 0; i < s.length(); i += 1) {
            char c = s.charAt(i);
            charMap.put(c, charMap.getOrDefault(c, 0) + 1);
        }
        for (int i = 0; i < s.length(); i += 1) {
            if (charMap.get(s.charAt(i)) == 1) {
                return i;
            }
        }
        return -1;
    }
}
```

T: O(n), S: O(1)

---

#### Summary 

Reduce using the built-in methods to save time.