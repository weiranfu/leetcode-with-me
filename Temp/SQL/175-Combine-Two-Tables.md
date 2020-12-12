---
title: Easy | Combine Two Tables 175
tags:
  - common
categories:
  - Leetcode
  - SQL
date: 2020-06-04 16:55:10
---

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

```sql
FirstName, LastName, City, State
```

[Leetcode](https://leetcode.com/problems/combine-two-tables/)

<!--more-->

Table: `Person`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
```

Table: `Address`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
```

---

#### Tricky 

Left Join two tables.

---

#### Standard solution  

```sql
SELECT P.FirstName, P.LastName, A.City, A.State
FROM Person P LEFT JOIN Address A
ON P.PersonId = A.PersonId
```



