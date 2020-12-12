---
title: Medium | Reverse words in a string 151
tags:
  - tricky
  - corner case
categories:
  - Leetcode
  - String
date: 2019-07-29 21:55:40
---

Given an input string, reverse the string word by word.

[Leetcode](https://leetcode.com/problems/reverse-words-in-a-string/)

<!--more-->

**Example 1:**

```
Input: "the sky is blue"
Output: "blue is sky the"
```

**Example 2:**

```
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

**Example 3:**

```
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

**Note:**

- A word is defined as a sequence of non-space characters.
- Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.

---

#### Tricky 

To reverse something, we could define a `reverse()` methods.

We could use two pointers to finger out the word to reverse.

#### Corner Case

1. There are whitespaces before the string.
2. There are whitespaces between the words.
3. There are whitespaces after the string.
4. How to eliminate the last `' '` after the string.
5. Need to reverse the last word.

---

#### My thoughts 

1. Reverse the whole string.
2. Reverse each word.
3. Skip all the whitespaces.
4. Remove the last `' '`.

---

#### First solution 

Fail to solve.

---

#### Standard solution 

```java
class Solution {
    public static String reverseWords(String s) {
        char[] cs = s.toCharArray();
        reverse(cs, 0, cs.length);         // Reverse the whole string.
        int start = 0;
        int end = 0;
        for (int i = 0; i < cs.length; i += 1) {
            if (cs[i] != ' ') {            // if cs[i] is in word.
                cs[end] = cs[i];
                end += 1;
            } else if (i > 0 && cs[i - 1] != ' ') {       // Skip whitespaces.
                reverse(cs, start, end);
                if (end < cs.length) {         // end could be out of array range.
                    cs[end] = ' ';
                    end += 1;
                    start = end;
                }
            }
        }
        reverse(cs, start, end);// reverse the last word if it ends without whitespaces.
        if (end > 0 && cs[end - 1] == ' ') {   // Remove the last ' ' and end could be 0
            return new String(cs, 0, end - 1);    
        }
        return new String(cs, 0, end);
    }

    public static void reverse(char[] c, int start, int end) {
        while (start < end) {          // The reverse interval is [start, end).
            char temp = c[start];
            c[start] = c[end - 1];
            c[end - 1] = temp;
            start += 1;
            end -= 1;
        }
    }
}
```

T: O(n) (not sure).  S: O(1)

---

#### Second Solution

Using built-in library. `.substring()` to get word from back to the front, then store it in a new StringBuilder.

Every word begins with `' '`.

```java
public class Solution {
  public String reverseWords(String s) {
        StringBuilder sb = new StringBuilder();   // To store the reverse string.
        int n = s.length();
        int i = n - 1;
        while(i >= 0) {                // From back to front of the string.
            if (s.charAt(i) == ' ') {
                i -= 1; 
                continue;              // Skip all the whitespaces.
            }
            int j = i;                 // To finger out a word.
            while(j >= 0 && s.charAt(j) != ' ') {
                j -= 1;
            }
            sb.append(" ");            // Word begins with ' '
            sb.append(s.substring(j + 1, i + 1));       // Get the word in [j + 1, i + 1)
            i = j - 1;
        }
        if (sb.length() > 0) {     // If there's a word, we must delete its ' ' in front of it.
            sb.deleteCharAt(0);
        }
        return sb.toString();   
    }
}
```

T: O(n). S: O(n)

---

#### Using built-in method

Use `.trim()`, `split()` method.

`\s` is a regex class for any kind of whitespace (space, tab, newline, etc). Since Java uses `\` as an escape character in strings (e.g. for newlines: "\n"), we need to escape the escape character ;-) So it becomes `\\s`. The `+` means one or more of them.

```java
public class Solution {
  public String reverseWords(String s) {
    String[] parts = s.trim().split("\\s+");     
    StringBuilder sb = new StringBuilder();
    for (int i = parts.length - 1; i > 0; i -= 1) {
        sb.append(parts[i]);
        sb.append(' ');
    }
    return sb.append(parts[0]).toString();
  }
}
```

Or we could use built-in `reverse()` method.

`Collections.reverse()` is used to reverse a list.

`Arrays.asList(array)` **returns a list view of an array, not a new list, ****

**so we could change the original array as a list.**

`String.join()` will returns a string with array joined by String `" "`.

```java
public class Solution {
  public String reverseWords(String s) {
    String[] words = s.trim().split(" +");  // escape more ' '
    Collections.reverse(Arrays.asList(words)); 
    return String.join(" ", words);       // join must be string " ", not ' '           
  }
}
```

---

#### Summary 

So many corner cases need to mind:

* string could be empty.
* when start the string reverse.
* when end the string reverse.