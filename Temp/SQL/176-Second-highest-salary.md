---
title: Easy | Second Highest Salary 176
tags:
  - tricky
categories:
  - Leetcode
  - SQL
date: 2020-06-04 16:59:27
---

Write a SQL query to get the second highest salary from the `Employee` table.

[Leetcode](https://leetcode.com/problems/second-highest-salary/)

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

For example, given the above Employee table, the query should return `200` as the second highest salary. If there is no second highest salary, then the query should return `null`.

```
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```

**Follow up:** [Nth Highest Salary](https://aranne.github.io/2020/06/04/177-Nth-highest-salary/#more)

---

#### Tricky 

How to deal with null if there is no such second highest salary since there might be only one record in this table?

We could wrap another SELECT around it.

---

#### Standard solution  

```sql
SELECT (
    SELECT DISTINCT Salary 
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary
```



