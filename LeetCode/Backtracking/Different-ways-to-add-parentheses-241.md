---
title: Medium | Different Ways to Add Parentheses 241
tags:
  - tricky
categories:
  - Leetcode
  - Backtracking
date: 2020-06-23 21:30:54
---

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are `+`, `-` and `*`.

[Leetcode](https://leetcode.com/problems/different-ways-to-add-parentheses/)

<!--more-->

**Example 1:**

```
Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
```

**Example 2:**

```
Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
```

**Follow up:** [Unique Binary Tree II](https://leetcode.com/problems/unique-binary-search-trees-ii/)

---

#### Tricky 

This is a typical [Catalan Number](https://www.cnblogs.com/Morning-Glory/p/11747744.html) problem. We need to try each element to form the result.

For each operator in the list, we compute all possible results for entries to the left of that operator, which is `List<Integer> left`, and also all possible results for entries to the right of that operator, namely `List<Integer> right`, and combine the results.

Since the original input is a string, we need to preprocess the string to get all correct numbers and operators.

We could also use DP to reduce some recalculation.

---

#### Backtracking 

```java
class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        if (input == null || input.length() == 0) return new ArrayList<>();
        int n = input.length();
        List<String> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int j = i;
            while (j < n && Character.isDigit(input.charAt(j))) {
                j++;
            }
            list.add(input.substring(i, j));
            if (j < n ) list.add(input.substring(j, j + 1));
            i = j;
        }
        n = list.size();
        return helper(0, n - 1, list);
    }
    
    private List<Integer> helper(int low, int high, List<String> s) {
        List<Integer> list = new ArrayList<>();
        if (low == high) {
            list.add(Integer.parseInt(s.get(low)));
            return list;
        }
        for (int i = low; i <= high - 2; i += 2) {
            List<Integer> left = helper(low, i, s);      // left part
            List<Integer> right = helper(i + 2, high, s);// right part
            for (int a : left) {
                for (int b : right) {
                    int c = 0;
                    if (s.get(i + 1).equals("+")) {
                        c = a + b;
                    } else if (s.get(i + 1).equals("-")) {
                        c = a - b;
                    } else if (s.get(i + 1).equals("*")) {
                        c = a * b;
                    }
                    list.add(c);
                }
            }
        }
        return list;
    }
}
```

Not sure about the time complexity

---

#### DP

```java
public List<Integer> diffWaysToCompute(String input) {
    List<Integer> result=new ArrayList<>();
    if(input==null||input.length()==0)  return result;
    List<String> ops=new ArrayList<>();
    for(int i=0; i<input.length(); i++){
        int j=i;
        while(j<input.length()&&Character.isDigit(input.charAt(j)))
            j++;
        ops.add(input.substring(i, j));
        if(j!=input.length())   ops.add(input.substring(j, j+1));
        i=j;
    }
    int N=(ops.size()+1)/2; //num of integers
    ArrayList<Integer>[][] dp=(ArrayList<Integer>[][]) new ArrayList[N][N];
    for(int d=0; d<N; d++){
        if(d==0){
            for(int i=0; i<N; i++){
                dp[i][i]=new ArrayList<>();
                dp[i][i].add(Integer.valueOf(ops.get(i*2)));
            }
            continue;
        }
        for(int i=0; i<N-d; i++){
            dp[i][i+d]=new ArrayList<>();
            for(int j=i; j<i+d; j++){
                ArrayList<Integer> left=dp[i][j], right=dp[j+1][i+d];
                String operator=ops.get(j*2+1);
                for(int leftNum:left)
                    for(int rightNum:right){
                        if(operator.equals("+"))
                            dp[i][i+d].add(leftNum+rightNum);
                        else if(operator.equals("-"))
                            dp[i][i+d].add(leftNum-rightNum);
                        else
                            dp[i][i+d].add(leftNum*rightNum);
                    }
            }
        }
    }
    return dp[0][N-1];
}
```

T: O(n^4)

