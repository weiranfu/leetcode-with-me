---
title: DFA based KMP — Fast String Search Algorithm
tags:
  - tricky
categories:
  - Summary
date: 2020-01-29 11:32:13
---

#### DFA

We use Deterministic Finite Automata to help us to implement KMP algorithm.

The key is to find the max length of common prefix and suffix of the pattern.

<!--more-->

Every character is a state(from left to right chars forming a prefix)

If we find a match on char c, go to next state.

If we find a mismatch on char c, go back to a previous state and restart matching.

Construct the DFA:

Use X to store the suffix state.

The position of X means the max length of common prefix and suffix.

If the pattern is "abbab", X starts at i == 1, which means put "bbab"(suffix) into DFA machine.

After putting "bbab" into machine, X is at "b", which means max length of common prefix and suffix is "ab".

1. for each char at i in pattern string.(i starts at 1)

2. copy dfa[ , X] to dfa[ , i]  // mismatch

3. dfa[c, i] = i + 1            // match, moves forward to next state

4. X = dfa[c, X]                // put c into machine(update suffix to new suffix), update X to next state.

DFA diagram: for "abbab" pattern

![](./KMP-string-search-algorithm/IMG_2305.jpg)

#### KMP

```java
public class KMP {
    private static int[][] DFA(String pattern) {
        int n = pattern.length();
        int[][] dfa = new int[128][n];
        dfa[pattern.charAt(0)][0] = 1;
        int x = 0;
        for (int i = 1; i < n; i++) {      // Must start from 1. (suffix)
            for (int j = 0; j < 128; j++) {
                dfa[j][i] = dfa[j][x];
            }
            dfa[pattern.charAt(i)][i] = i + 1;
            x = dfa[pattern.charAt(i)][x];
        }
        return dfa;
    }

    public static int search(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int[][] dfa = DFA(pattern);
        int i = 0, j = 0;
        while (i < n && j < m) {
            j = dfa[text.charAt(i)][j];
            i++;
        }
        if (j == m) {         // if find
            return i - m;
        } else {              // not find
            return -1;
        }
    }
}
```

T: O(n)			S: O(n)