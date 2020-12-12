---
title: Easy | Reverse vowels of a string 345
tags:
  - common
  - Oh-shit
  - implement
categories:
  - Leetcode
  - String
date: 2019-08-06 18:17:40
---

Write a function that takes a string as input and reverse only the vowels of a string.

[Leetcode](https://leetcode.com/problems/reverse-vowels-of-a-string/)

<!--more-->

**Example 1:**

```
Input: "hello"
Output: "holle"
```

**Example 2:**

```
Input: "leetcode"
Output: "leotcede"
```

**Note:**
The vowels does not include the letter "y".

Vowels can be uppercase or lowercase.

---

#### Implement

when we want to determine whether a character is in a string, use `s.contains(string b)`

```java
String s = "aeiou";
Character c = 'a';
s.contains(c + ""); // Contains can only be applied to string.
```

#### Oh-Shit

When we use `while` loop, don't forget to increase the iterator. 

---

#### My thoughts 

Using two pointers to find vowels.

---

#### First solution 

```java
class Solution {
    public String reverseVowels(String s) {
        char[] cs = s.toCharArray();
        int left = 0;
        int right = s.length() - 1;
        while (left <= right) {
            if (isVowel(cs[left])) {
                while (!isVowel(cs[right]) && left <= right) {
                    right -= 1;
                }
                char temp = cs[left];
                cs[left] = cs[right];
                cs[right] = temp;
                right -= 1;        // Don't forget!
            }
            left += 1;
        }
        return new String(cs);
    }
    
    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
              || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'; 
    }
}
```

T: O(n), S: O(n)

---

#### Optimized 

* Using `Character.toLowerCase()` to optimize `isVowel()` method.
* `while (left < right)` is more organized.
  * First to find right position
  * Then to switch each other

```java
class Solution {
    public String reverseVowels(String s) {
        if (s.length() == 0 || s == null) {
            return s;
        }
        char[] cs = s.toCharArray();
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            while (left < right && !isVowel(cs[left])) {
                left += 1;
            }
            while (left < right && !isVowel(cs[right])) {
                right -= 1;
            }
            char temp = cs[left];
            cs[left] = cs[right];
            cs[right] = temp;
            right -= 1;
            left += 1;
        }
        return new String(cs);
    }
    
    private boolean isVowel(char c1) {
        char c = Character.toLowerCase(c1);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
```

T: O(n), S: O(n)

---

#### Second Solution

Use `string.contains()` methods to indicate whether this char is a vowel.

`String vowels = "aeiouAEIOU"`

```java
class Solution {
    public String reverseVowels(String s) {
        if (s.length() == 0 || s == null) {
            return s;
        }
        String vowels = "aeiouAEIOU";
        char[] cs = s.toCharArray();
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            while (left < right && !vowels.contains(cs[left] + "")) {
                left += 1;
            }
            while (left < right && !vowels.contains(cs[right] + "")) {
                right -= 1;
            }
            char temp = cs[left];
            cs[left] = cs[right];
            cs[right] = temp;
            right -= 1;
            left += 1;
        }
        return new String(cs);
    }
}
```

T: O(n), S: O(n)

---

#### Summary 

Using two pointers to switch.