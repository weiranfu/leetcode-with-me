---
title: Medium | Department Highest Salary 184
tags:
  - common
categories:
  - Leetcode
  - SQL
date: 2020-06-04 19:04:53
---

The `Employee` table holds all employees. Every employee has an Id, a salary, and there is also a column for the department Id.

[Leetcode](https://leetcode.com/problems/department-highest-salary/)

<!--more-->

```
+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
```

The `Department` table holds all departments of the company.

```
+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
```

Write a SQL query to find employees who have the highest salary in each of the departments. For the above tables, your SQL query should return the following rows (order of rows does not matter).

```
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+
```

---

#### Tricky 

There may be multiple employees in a same department have largest salary.

---

#### WHERE 

```sql
# Write your MySQL query statement below
SELECT D.Name AS 'Department', E.Name AS 'Employee', E.Salary
FROM Employee E, Department D
WHERE E.DepartmentId = D.Id
AND E.Salary = (SELECT max(E2.Salary) 
                FROM Employee E2
                WHERE E2.DepartmentId = D.Id)
```

---

#### Optimized

```sql
# Write your MySQL query statement below
SELECT
    Department.name AS 'Department',
    Employee.name AS 'Employee',
    Salary
FROM
    Employee
        JOIN
    Department ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId , Salary) IN
    (   SELECT
            DepartmentId, MAX(Salary)
        FROM
            Employee
        GROUP BY DepartmentId
	)
;
```

