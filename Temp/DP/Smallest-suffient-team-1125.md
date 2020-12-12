---
title: Hard | Smallest Suffient Team 1125
tags:
  - common
  - tricky
categories:
  - Leetcode
  - DP	
date: 2020-07-12 11:57:47
---

In a project, you have a list of required skills `req_skills`, and a list of `people`.  The i-th person `people[i]` contains a list of skills that person has.

Consider a *sufficient team*: a set of people such that for every required skill in `req_skills`, there is at least one person in the team who has that skill.  We can represent these teams by the index of each person: for example, `team = [0, 1, 3]` represents the people with skills `people[0]`, `people[1]`, and `people[3]`.

Return **any** sufficient team of the smallest possible size, represented by the index of each person.

You may return the answer in any order.  It is guaranteed an answer exists.

[Leetcode](https://leetcode.com/problems/smallest-sufficient-team/)

<!--more-->

**Example 1:**

```
Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
```

**Example 2:**

```
Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
```

**Constraints:**

- `1 <= req_skills.length <= 16`
- `1 <= people.length <= 60`
- `1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16`
- Elements of `req_skills` and `people[i]` are (respectively) distinct.
- `req_skills[i][j], people[i][j][k]` are lowercase English letters.
- Every skill in `people[i]` is a skill in `req_skills`.
- It is guaranteed a sufficient team exists.

---

#### Tricky 

This is a typical DP with bitmask problem.

We can use `dp[s]` to represent the min count of people to form the state `s`.

1. We enumerate all possible states of skills and try to DP transit.

   Since people's skill may overlap with each other, we cannot use **Positive Transition** of DP but instead **Negative Transition** of DP.

   If the next state is different from current state, we find a new state and try to transit.

   We use `edgeTo[s][0]` to store the previous state to `s` and `edgeTo[s][1]` to store the previous people we add. 

   ```java
   class Solution {
       public int[] smallestSufficientTeam(String[] skills, List<List<String>> people) {
           int n = skills.length;
           Map<String, Integer> map = new HashMap<>();
           for (int i = 0; i < n; i++) {
               map.put(skills[i], i);
           }
           
           int[] dp = new int[1 << n];
           int[][] edgeTo = new int[1 << n][2];
           Arrays.fill(dp, 0x3f3f3f3f);
           dp[0] = 0;
           int[] peoSkills = new int[people.size()];
           for (int i = 0; i < people.size(); i++) {
               int s = 0;
               for (String skill : people.get(i)) {
                   s |= 1 << map.get(skill);
               }
               peoSkills[i] = s;
           }
           for (int s = 0; s < 1 << n; s++) {
               for (int i = 0; i < people.size(); i++) {
                   int k = s | peoSkills[i];
                   if (k != s) {
                       if (dp[k] > dp[s] + 1) {
                           dp[k] = dp[s] + 1;
                           edgeTo[k][0] = s;
                           edgeTo[k][1] = i;
                       }
                   }
               }
           }
           int[] res = new int[dp[(1 << n) - 1]];
           int i = 0;
           int curr = (1 << n) - 1;
           while (curr != 0) {
               res[i++] = edgeTo[curr][1];
               curr = edgeTo[curr][0];
           }
           return res;
       }
   }
   ```

   T: O(2^n\*m)			S: O(2^n)

2. We enumerate people to find a state to transit from (**Positive Transition**)

   So we can calculate `skillset` in the *for* loop

   ```java
   class Solution {
       public int[] smallestSufficientTeam(String[] skills, List<List<String>> people) {
           int n = skills.length;
           Map<String, Integer> map = new HashMap<>();
           for (int i = 0; i < n; i++) {
               map.put(skills[i], i);
           }
           
           int[] dp = new int[1 << n];
           int[][] edgeTo = new int[1 << n][2];
           Arrays.fill(dp, 0x3f3f3f3f);
           dp[0] = 0;
           for (int i = 0; i < people.size(); i++) {
               int skillset = 0;
               for (String skill : people.get(i)) {
                   skillset |= 1 << map.get(skill);     // get skillset
               }
               for (int s = 0; s < 1 << n; s++) {
                   int k = s | skillset;
                   if (k != s) {                        // try to transit
                       if (dp[k] > dp[s] + 1) {
                           dp[k] = dp[s] + 1;
                           edgeTo[k][0] = s;
                           edgeTo[k][1] = i;
                       }
                   }
               }
           }
           int[] res = new int[dp[(1 << n) - 1]];
           int i = 0;
           int curr = (1 << n) - 1;
           while (curr != 0) {
               res[i++] = edgeTo[curr][1];
               curr = edgeTo[curr][0];
           }
           return res;
       }
   }
   ```

   T: O(m\*2^n)			S: O(2^n)

---

#### DFS

We enumerate peoples's skill state and try to combine them with all achieved states in dp. If we combine them to get a new state, we transit state.

**In this algorithm, we don't need to enumberate all states but just enumerate all available states in DP which can be much faster.**

We can use Map to store states, cnt, previous state and peoples's index.

```java
class Solution {
    public int[] smallestSufficientTeam(String[] skills, List<List<String>> people) {
        int n = skills.length;
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(skills[i], i);
        }
        
        Map<Integer, int[]> dp = new HashMap<>();
        dp.put(0, new int[]{0, -1, -1});     // cnt, previous state, people's index
        
        for (int i = 0; i < people.size(); i++) {
            int skillset = 0;
            for (String skill : people.get(i)) {
                skillset |= 1 << map.get(skill);
            }
            List<int[]> modified = new ArrayList<>(); // avoid concurrent modification
            for (int s : dp.keySet()) {
                int k = s | skillset;
                if (k != s) {
                    modified.add(new int[]{s, k});
                }
            }
            for (int[] m : modified) {
                int s = m[0];
                int k = m[1];
                if (!dp.containsKey(k) 
                    || dp.containsKey(k) && dp.get(k)[0] > dp.get(s)[0] + 1) {
                    dp.put(k, new int[]{dp.get(s)[0] + 1, s, i});
                }
            }
        }
        int[] info = dp.get((1 << n) - 1);
        int[] res = new int[info[0]];
        int i = 0;
        int curr = (1 << n) - 1;
        while (curr != 0) {
            res[i++] = info[2];
            curr = info[1];
            info = dp.get(curr);
        }
        return res;
    }
}
```

T: O()