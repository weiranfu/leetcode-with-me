---
title: Easy | Happy Number 202
tags:
  - common
categories:
  - Leetcode
  - Linked List
date: 2020-06-06 15:35:02
---

Write an algorithm to determine if a number `n` is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1. Those numbers for which this process **ends in 1** are happy numbers.

Return True if `n` is a happy number, and False if not.

[Leetcode](https://leetcode.com/problems/happy-number/)

<!--more-->

**Example:** 

```
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

---

#### Tricky 

The key is to find a cycle during the process we find a happy number.

* Detect cycle with a HashSet
* Fast/slow pointers

---

#### HashSet

```java
class Solution {
    public boolean isHappy(int n) {
        if (n <= 0) return false;
        Set<Integer> seen = new HashSet<>();
        int start = n;
        while (start != 1) {
            if (seen.contains(start)) {
                return false;
            }
            seen.add(start);
            start = getNext(start);
        }
        return true;
    }
    
    private int getNext(int n) {
        int sum = 0;
        while (n != 0) {
            int d = n % 10;
            sum += d * d;
            n /= 10;
        }
        return sum;
    }
 }
```

Analysis:

* Time Complexity: `O(243⋅3+logn+loglogn+logloglogn)... = O(logn).`

  The `getNext` costs O(logn). 

  To work out the *total* time complexity, we'll need to think carefully about how many numbers are in the chain, and how big they are.

  We determined above that once a number is below 243, it is impossible for it to go back up above 243. Therefore, based on our very shallow analysis we know for *sure* that once a number is below 243, it is impossible for it to take more than another 243 steps to terminate. Each of these numbers has at most 3 digits. With a little more analysis, we could replace the 243 with the length of the longest number chain below 243, however because the constant doesn't matter anyway, we won't worry about it.

  For an `n` above 243, we need to consider the cost of each number in the chain that is above 243. With a little math, we can show that in the worst case, these costs will be `O(243⋅3+logn+loglogn+logloglogn)...`. Luckily for us, the `O*(logn)` is the dominating part, and the others are all tiny in comparison (collectively, they add up to less than log*n*), so we can ignore them.

* Space Complexity: O(logn)

  Closely related to the time complexity, and is a measure of what numbers we're putting in the HashSet, and how big they are. For a large enough n, the most space will be taken by n itself.

  We can optimize to O*(243⋅3)=*O(1) easily by only saving numbers in the set that are less than 243, as we have already shown that for numbers that are higher, it's impossible to get back to them anyway.

---

#### Fast/slow pointers

We could use fast/slow pointers to detect cycle.

`fast` pointer is ahead of `slow` pointer.

```java
class Solution {
    public boolean isHappy(int n) {
        if (n <= 0) return false;
        int slow = n;
        int fast = getNext(n);
        while (fast != 1) {
            if (fast == slow) {
                return false;
            }
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }
        return true;
    }
    
    private int getNext(int n) {
        int sum = 0;
        while (n != 0) {
            int d = n % 10;
            sum += d * d;
            n /= 10;
        }
        return sum;
    }
 }
```

T: O(logn)			S: O(1)

---

#### Standard solution  



---

#### Summary 

