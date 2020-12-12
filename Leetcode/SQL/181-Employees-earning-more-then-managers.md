---
title: Easy | Employees Earning More Than Their Managers 181
tags:
  - common
categories:
  - Leetcode
  - SQL
date: 2020-06-04 18:30:23
---

The `Employee` table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

[Leetcode](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

<!--more-->

```
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
```

Given the `Employee` table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

```
+----------+
| Employee |
+----------+
| Joe      |
+----------+
```

---

#### WHERE clause 

```sql
# Write your MySQL query statement below
SELECT 
    E1.Name AS 'Employee'
FROM 
    Employee E1,
    Employee E2
WHERE E1.ManagerId = E2.Id
      AND E1.Salary > E2.Salary
```

---

#### JOIN clause

```sql
# Write your MySQL query statement below
SELECT E1.Name AS 'Employee'
FROM Employee E1 JOIN Employee E2
     ON E1.ManagerId = E2.Id
     AND E1.Salary > E2.Salary
```



