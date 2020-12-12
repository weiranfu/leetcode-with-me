---
title: Easy | Customers Who Never Order 183
tags:
  - common
categories:
  - Leetcode
  - SQL
date: 2020-06-04 18:48:29
---

Suppose that a website contains two tables, the `Customers` table and the `Orders` table. Write a SQL query to find all customers who never order anything.

[Leetcode](https://leetcode.com/problems/customers-who-never-order/)

<!--more-->

Table: `Customers`.

```
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
```

Table: `Orders`.

```
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
```

Using the above tables as example, return the following:

```
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
```

---

#### NOT EXISTS 

```sql
# Write your MySQL query statement below
SELECT C.Name AS 'Customers'
FROM Customers C
WHERE NOT EXISTS (SELECT * FROM Orders O WHERE C.Id = O.CustomerId)
```

---

#### NOT IN

```sql
# Write your MySQL query statement below
SELECT C.Name AS 'Customers'
FROM Customers C
WHERE C.Id NOT IN (SELECT O.CustomerId FROM Orders O)
```

---

#### LEFT JOIN

```sql
# Write your MySQL query statement below
SELECT C.Name AS 'Customers'
FROM Customers C LEFT JOIN Orders O
ON C.Id = O.CustomerId
WHERE O.CustomerId IS NULL
```