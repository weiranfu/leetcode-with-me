---
title: Medium | Bulls and cows 299
tags:
  - tricky
  - Oh-shit
categories:
  - Leetcode
  - Array
date: 2019-07-19 10:08:32
---

You are playing the following [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows) game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use `A` to indicate the bulls and `B` to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

<!--more-->

**Example 1:**

```
Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
```

**Example 2:**

```
Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
```

**Note:** You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

---

#### Tricky 

**How to record digits? Using a 10 length array to store!**

Its position represents its value. e.g. 7 should store at nums[7].

In this case, to get same digit in two strings, we could suppose that

if the digit is from secret, `nums[digit] += 1;`

if the digit is from guess, `nums[digit] -= 1;`

if `nums[digit] == 0`, then indicates this digit has same numbers in both strings. 

#### Oh-shit

When output a string containing both integers and characters, we could use 

`return 5 + "A"`    // This will turn out "5A"

However if we write

`return 5 + 'A'  `  // This will cannot run, because int cannot be converted to character.

---

#### My thoughts 

Failed to solve.

---

#### First solution 

```java
class Solution {
    public String getHint(String secret, String guess) {
        int bulls = 0;
        int cows = 0;
        int[] nums = new int[10];        // default value is 0;
        for (int i = 0; i < secret.length(); i += 1) {
            int s = Character.getNumericValue(secret.charAt(i)); // convert '3' to 3
            int g = Character.getNumericValue(guess.charAt(i));
            if (s == g) {
                bulls += 1;
            } else {
                if (nums[s] < 0) {
                    cows += 1;
                }
                nums[s] += 1;
                if (nums[g] > 0) {
                    cows += 1;
                }
                nums[g] -= 1;
            }
        }
        return bulls + "A" + cows + "B";
    }
}
```

T: O(n) S: O(1)

---

#### Standard solution 

Using two 10-length array to store digits from secret and guess.

```java
class Solution {
    public String getHint(String secret, String guess) {
        int bulls = 0;
        int cows = 0;
        int[] secretcount = new int[10];
        int[] guesscount = new int[10];
        for (int i = 0; i < secret.length(); i += 1) {
            char s = secret.charAt(i);
            char g = guess.charAt(i);
            if (s == g) {
                bulls += 1;
            } else {
                secretcount[s - '0'] += 1;
                guesscount[g - '0'] += 1;
            }
        }
        for (int i = 0; i < 10; i += 1) {
            cows += Math.min(secretcount[i], guesscount[i]);
        }
        return bulls + "A" + cows + "B";
    }
}
```

T: O(n) S:O(1)

---

#### Optimized 

Algorithms: Hashmap?

Speed: 

When we convert a character into an integer, we use

**`'5' - '0'`** instead of `Character.getNumbericValue('5')`

---

#### Summary 

When we need to record the digits showing up in a string,

use a 10-length array to store them. 

5 should be stored at nums[5].