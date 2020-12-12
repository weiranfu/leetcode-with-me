---
title: Medium | Maximum XOR of Two Numbers in an Array 421
tags:
  - tricky
categories:
  - Leetcode
  - Trie
date: 2020-06-20 01:04:50
---

Given a **non-empty** array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ *i*, *j* < *n*.

Could you do this in O(*n*) runtime?

[Leetcode](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

<!--more-->

**Example:**

```
Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
```

---

#### Tricky 

* Greedy + Trie + Two pointers DFS on Trie

  How to get the maximum XOR?

  We could view the nums in its binary format. 

  We want the higher order bits have as many `1` as possible when we XOR two nums. (**Greedy**)

  We could save all bit of a num in a Trie.

  We maintain two pointers to traversal on Trie. Each time we try to choose one `1` and `0` to achieve XOR `1`.



---

#### Greedy + Trie + Two pointers DFS

```java
class Solution {
    class Node {
        Node[] links = new Node[2];
        boolean isEnd;
        int value;
    }
    
    public int findMaximumXOR(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        
        Node root = new Node();
        for (int num : nums) {
            Node curr = root;
            for (int i = 31; i >= 0; i--) {
                int bit = (num >> i) & 1;
                if (curr.links[bit] == null) {
                    curr.links[bit] = new Node();
                }
                curr = curr.links[bit];
            }
            curr.isEnd = true;
            curr.value = num;
        }
        return dfs(root, root);
    }
    
    // try to get XOR 1 as much as we can
    private int dfs(Node n1, Node n2) {
        if (n1.isEnd) return n1.value ^ n2.value;
        if (n1.links[1] == null) {
            return dfs(n1.links[0], (n2.links[1] != null) ? n2.links[1] : n2.links[0]);
        } else if (n1.links[0] == null) {
            return dfs(n1.links[1], (n2.links[0] != null) ? n2.links[0] : n2.links[1]);
        } else if (n2.links[1] == null) {      // n1 has links[0] and links[1]
            return dfs(n1.links[1], n2.links[0]);
        } else if (n2.links[0] == null) {
            return dfs(n1.links[0], n2.links[1]);
        } else {                               // n1, n2 both have links[0] and links[1]
            return Math.max(dfs(n1.links[0], n2.links[1]), dfs(n1.links[1], n2.links[0]));
        }
    }
}
```

T: O(n)			S: O(1)

---

#### Bit manipulation + Prefix

```java
class Solution {
    public int findMaximumXOR(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        int n = nums.length;
        
        int max = 0;
        int mask = 0;
        for (int i = 31; i >= 0; i--) {
            // mask will grow like 1000 1100 1110 1111 
            mask = mask | (1 << i);
            
            Set<Integer> set = new HashSet<>();
            for (int num : nums) {
                set.add(num & mask); // add prefix
            }
            
            // possible greedy max we can get(add 1 to max)
            int greedy = max | (1 << i);
            for (int prefix : set) { 
                // another pair is (greedy ^ prefix)
                if (set.contains(greedy ^ prefix)) {
                    max = greedy;      
                    break;
                }
            }
            // if we can get greedy max, we will add 0 to max
        }
        return max;
    }
}
```

T: O(n)		S: O(n)



