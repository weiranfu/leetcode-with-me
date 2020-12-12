---
title: Medium | Nth Highest Salary 177
tags:
  - common
categories:
  - Leetcode
  - SQL
date: 2020-06-04 17:06:43
---

Write a SQL query to get the *n*th highest salary from the `Employee` table.

[Leetcode](https://leetcode.com/problems/nth-highest-salary/)

<!--more-->

```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

For example, given the above Employee table, the *n*th highest salary where *n* = 2 is `200`. If there is no *n*th highest salary, then the query should return `null`.

```
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```

---

#### Tricky 

`SET N = N - 1`

---

#### Standard solution  

```sql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT (
          SELECT DISTINCT Salary
          FROM Employee
          ORDER BY Salary DESC
          LIMIT 1 OFFSET N
      )
  );
END
```

