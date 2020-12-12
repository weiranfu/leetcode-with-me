---
title: Hard | Maximum Students Taking Exam 1349
tags:
  - tricky
categories:
  - Leetcode
  - DP
date: 2020-02-18 16:09:40
---

Given a `m * n` matrix `seats`  that represent seats distributions in a classroom. If a seat is broken, it is denoted by `'#'` character otherwise it is denoted by a `'.'`character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the **maximum** number of students that can take the exam together without any cheating being possible..

Students must be placed in seats in good condition.

[Leetcode](https://leetcode.com/problems/maximum-students-taking-exam/)

<!--more-->

**Example 1:**

```
Input: seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
Output: 4
Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam. 
```

**Example 2:**

```
Input: seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
Output: 3
Explanation: Place all students in available seats. 
```

**Example 3:**

```
Input: seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
Output: 10
Explanation: Place students in available seats in column 1, 3 and 5.
```

**Constraints:**

- `seats` contains only characters `'.' and``'#'.`
- `m == seats.length`
- `n == seats[i].length`
- `1 <= m <= 8`
- `1 <= n <= 8`

---

#### Tricky 

Bitmask DP.

---

#### My thoughts 

Search with backtrack.

However, notice that the time complexity is 2^64 `(1 <= m <= 8, 1 <= n <= 8)`, we need to reduce the time complexity.

---

#### First solution 

Search with backtrack and pruning ---> **Long Time Error**

```java
class Solution {
    int[][] direct = {{0, 1}, {0, -1}, {-1, -1}, {-1, 1}};
    public int maxStudents(char[][] seats) {
        int m = seats.length;
        int n = seats[0].length;
        int[] res = new int[1];
        int total = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (seats[i][j] == '.') {
                    total++;
                }
            }
        }
        search(seats, 0, 0, res, total, 0);
        return res[0];
    }
    private void search(char[][] seats, int start, int cnt, int[] max, int total, int pass) {
        max[0] = Math.max(max[0], cnt);
        if (total - pass + cnt <= max[0]) return;   // Pruning
        int m = seats.length;
        int n = seats[0].length;
        for (int k = start; k < m * n; k++) {
            int i = k / n;
            int j = k % n;
            if (seats[i][j] == '#') continue;
            boolean find = false;
            for (int[] dir : direct) {
                int x = i + dir[0];
                int y = j + dir[1];
                if (x < 0 || x >= m || y < 0 || y >= n) continue;
                if (seats[x][y] == '!') {
                    find = true;
                    break;
                }
            }
            if (!find) {               // backtracking
                seats[i][j] = '!';
                search(seats, k + 1, cnt + 1, max, total, pass + 1);
                seats[i][j] = '.';
            } else {
                pass++;
            }
        }
    }
}
```

T: O((mn)!) 			S: O(mn) call stack

---

#### Optimized: DP

 When we backtrack, we need to store the max students can seat with the arrangement of seats.

**We could use bitmask to store the arrangement.**

When doing Bitmasking DP, we are always handling problems like "what is the i-th bit in the state" or "what is the number of valid bits in a state". These problems can be very complicated if we do not handle them properly. I will show some coding tricks below which we can make use of and solve this problem.

- We can use **(x >> i) & 1** to get i-th bit in state **x**, where **>>** is the right shift operation. If we are doing this in an if statement (i.e. to check whether the i-th bit is 1), we can also use **x & (1 << i)**, where the **<<** is the left shift operation.
- We can use **(x & y) == x** to check if **x** is a subset of **y**. The subset means every state in **x** could be 1 only if the corresponding state in **y** is 1.
- We can use **(x & (x >> 1)) == 0** to check if there are no adjancent valid states in **x**.

Now we can come to the problem. We can use a bitmask of n bits to represent the validity of each row in the classroom. The i-th bit is 1 if and only if the i-th seat is not broken. For the first example in this problem, the bitmasks will be "010010", "100001" and "010010". When we arrange the students to seat in this row, we can also use n bits to represent the students. The i-th bit is 1 if and only if the i-th seat is occupied by a student. We should notice that n bits representing students must be a subset of n bits representing seats.

1. Subproblems

   Save the arrangement row by row. So if there're row[n] here, 

   subproblem: prefix rows: row[:i] represents max students can seat under **ith** row's arrangement.

   \# of subproblems is n

2. Guess

   consider all possible arrangement for **ith** row, `2^m` possibilities.

   for each one of them, to find max value of all possible valid arrangement of last row.

3. Recurrence

   We denote **dp\[i][mask]** as the maximum number of students for the first **i** rows while the students in the i-th row follow the masking **mask**. There should be no adjancent valid states in **mask**. The transition function is:

   `dp[i][mask] = max(dp[i - 1][mask'] for last row's mask' ) + number of valid bits(mask)`

   where **mask'** is the masking for the (i-1)-th row. To prevent students from cheating, the following equation must hold:

   - **(mask & (mask' >> 1)) == 0**, there should be no students in the **upper left** position for every student.
   - **((mask >> 1) & mask') == 0**, there should be no students in the **upper right** position for every student.

   If these two equation holds and **dp\[i - 1][mask']** itself is valid, we could then transit from **dp\[i - 1][mask']** to **dp\[i][mask]** according to the transition function.

   So time/subproblem is O(2^m * 2^m = 2^2m)

4. Topological order

   From 0 row to n row.

5. Run time

   \# of subproblem * time/subproblem = O(n * 2^2m)

Count num of bits for an integer: `num = Integer.bitCount(n)`

```java
class Solution {
    public int maxStudents(char[][] seats) {
        if (seats == null || seats.length == 0 || seats[0].length == 0) return 0;
        int m = seats.length, n = seats[0].length;
        int[] row = new int[m + 1];
        int[][] dp = new int[m + 1][1 << n];
        for (int i = 0; i < m; i++) {
            int state = 0;
            for (int j = 0; j < n; j++) {
                if (seats[i][j] == '#') {
                    state |= 1 << j;
                }
            }
            row[i + 1] = state;
        }
        for (int i = 1; i <= m; i++) {
            for (int s = 0; s < 1 << n; s++) {
                // cannot overlap with row[] and cannot have neighbors
                if ((s & row[i]) == 0 && ((s & s >> 1) == 0)) { 
                    for (int k = 0; k < 1 << n; k++) {
                // cannot overlap with row[] and cannot have left and right neighbors
                        if ((k & row[i - 1]) == 0 && ((s & k >> 1) == 0) 
                            && ((s & k << 1) == 0)) {
                            dp[i][s] = Math.max(dp[i][s], dp[i - 1][k] + Integer.bitCount(s));
                        }
                    }
                }
            }
        }
        int res = 0;
        for (int i = 0; i < 1 << n; i++) {
            res = Math.max(res, dp[m][i]);
        }
        return res;
    }
}
```

T: O(m*2^2n)

S: O(m*2^n)

---

#### Summary 

Use `Integer.bitCount(n)` to get number of 1 bit in an integer n.

Use bitmask to store the arrangement of row in a graph.