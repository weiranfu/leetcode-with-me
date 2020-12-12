---
title: Medium | Repeated DNA Sequences 187
tags:
  - tricky
categories:
  - Leetcode
  - String
date: 2020-06-04 22:39:38
---

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

[Leetcode](https://leetcode.com/problems/repeated-dna-sequences/)

<!--more-->

**Example:**

```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
```

---

#### Tricky 

Linear-time window slice O(*L*) is easy stupid, just take a substring. Overall that would result in O((*N*−*L*)*L*) time complexity and huge space consumption in the case of large sequences.

Constant-time slice O(1) is where the fun starts, because the way you choose will show your actual background. There are two ways to proceed:

- Rabin-Karp = constant-time slice using rolling hash algorithm.
- Bit manipulation = constant-time slice using bitmasks.

---

#### My thoughts 

Stupid windown slice O((N-L)L) approach.

---

#### First solution 

```java
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int L = 10, n = s.length();
        if (n <= L) return new ArrayList<String>();
        Set<String> res = new HashSet<>();
        Set<String> seen = new HashSet<>();
        for (int i = 0; i <= n - L; i++) {
            String str = s.substring(i, i + L);
            if (seen.contains(str)) {
                res.add(str);
            } else {
                seen.add(str);
            }
        }
        return new ArrayList<>(res);
    }
}
```

T: O((N-L)L)		S: O(N-L)

---

#### Rabin-Karp Algorithm

**The idea is to slice over the string and to compute the hash of the sequence in the sliding window, both in a constant time.[Rabin-Karp Algorithm]([https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm](https://en.wikipedia.org/wiki/Rabin–Karp_algorithm))**

Let's use string `AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT` as an example. First, convert string to integer array:

 `'A' -> 0, 'C' -> 1, 'G' -> 2, 'T' -> 3`

`AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT` -> `00000111110000011111100000222333`. Time to compute hash for the first sequence of length L: `0000011111`. The sequence could be considered as a number in a [numeral system](https://en.wikipedia.org/wiki/Numeral_system) with the base 4 and hashed as

![{\displaystyle H=c_{1}a^{k-1}+c_{2}a^{k-2}+c_{3}a^{k-3}+...+c_{k}a^{0},}](https://wikimedia.org/api/rest_v1/media/math/render/svg/1a0d49f64002250b24941225db5208363ad10a66)

Removing and adding characters simply involves adding or subtracting the first or last term.

Add a new item `ck+1` using [Rolling Hash](https://en.wikipedia.org/wiki/Rolling_hash) means `h1 = h0 * a - c1*a^k + ck+1`.

```java
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int L = 10, n = s.length();
        if (n <= L) return new ArrayList<String>();
        // rolling hash parameters: base 4
        int base = 4, basePow = (int)Math.pow(base, L);
        // convert string to array of integers
        Map<Character, Integer> toInt = new HashMap<>();
        toInt.put('A', 0);
        toInt.put('C', 1);
        toInt.put('G', 2);
        toInt.put('T', 3);
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = toInt.get(s.charAt(i));
        }
        
        Set<String> res = new HashSet<>();
        Set<Integer> seen = new HashSet<>();
        int hash = 0;
        for (int i = 0; i <= n - L; i++) {
            // compute hash of the current sequence in O(1) time
            if (i == 0) {
                // compute hash of the first sequence in O(L) time
                for (int j = 0; j < L; j++) {
                    hash = hash * base + nums[j];
                }
            } else {
                hash = hash * base - nums[i - 1] * basePow + nums[i + L - 1];
            }
            if (seen.contains(hash)) {
                res.add(s.substring(i, i + L));
            } else {
                seen.add(hash);
            }
        }
        return new ArrayList<>(res);
    }
}
```

T: O(N-L)		S: O(N-L)

---

#### Bitmask  

**The idea is to slice over the string and to compute the bitmask of the sequence in the sliding window, both in a constant time.**

As for Rabin-Karp, let's start from conversion of string to 2-bits integer array:

`A -> 0 = 00,  C -> 1 = 01, G -> 2 = 10, T -> 3 = 11`

`GAAAAACCCCCAAAAACCCCCCAAAAAGGGTTT` -> `200000111110000011111100000222333`.

When we need to compute the bitmask of a substring like rolling hash, we need

1. Do left shift tto free the last two bits: `bitmask <<= 2`

2. Save current digit into last two bits: `bitmask |= nums[i]`

3. Remove two leading bits, which means to set 2L bit and (2L + 1) bit to zero.

   Let's use bitwise trick to unset n-th bit: `bitmask &= ~(1 << n)`.

   * `1 << n` is to set n-th bit equal to 1.
   * `~(1 << n)` is to set n-th bit equal to 0, and all lower bits to 1.
   * `bitmask &= ~(1 << n)` is to set n-th bit of bitmask equal to 0.

```java
class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int L = 10, n = s.length();
        if (n <= L) return new ArrayList<String>();
        
        Map<Character, Integer> toInt = new HashMap<>();
        toInt.put('A', 0);
        toInt.put('C', 1);
        toInt.put('G', 2);
        toInt.put('T', 3);
        
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = toInt.get(s.charAt(i));
        }
        
        Set<Integer> seen = new HashSet<>();
        Set<String> res = new HashSet<>();
        int bitmask = 0;
        for (int i = 0; i <= n - L; i++) {
            if (i == 0) {
                for (int j = 0; j < L; j++) {
                    bitmask <<= 2;
                    bitmask |= nums[j];
                }
            } else {
                // left shift to free the last 2 bit
                bitmask <<= 2;
                // add a new 2-bits number in the last two bits
                bitmask |= nums[i + L - 1];
                // unset first two bits: 2L-bit and (2L + 1)-bit
                bitmask &= ~(3 << 2 * L);    // 3 means 11 in binary
            }
            if (seen.contains(bitmask)) {
                res.add(s.substring(i, i + L));
            } else {
                seen.add(bitmask);
            }
        }
        return new ArrayList<>(res);
    }
}
```

T: O(N-L)		S: O(N-L)

---

#### Summary 

Two ways to converse string to integer.

* Hash
* Bitmask