---
title: Medium | Consecutive Numbers 180
tags:
  - tricky
categories:
  - Leetcode
  - SQL
date: 2020-06-04 18:21:29
---

Write a SQL query to find all numbers that appear at least three times consecutively.

[Leetcode](https://leetcode.com/problems/consecutive-numbers/)

<!--more-->

```
+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
```

For example, given the above `Logs` table, `1` is the only number that appears consecutively for at least three times.

```
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
```

---

#### Standard solution  

```sql
# Write your MySQL query statement below
SELECT DISTINCT log1.Num AS ConsecutiveNums
FROM Logs log1, Logs log2, Logs log3
WHERE log1.Id = log2.Id - 1
      and log2.Id = log3.Id - 1
      and log3.Num = log2.Num
      and log2.Num = log1.Num
```

