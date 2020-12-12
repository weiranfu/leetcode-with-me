---
title: Easy | Duplicate Emails
tags:
  - common
categories:
  - Leetcode
  - SQL
date: 2020-06-04 18:37:49
---

Write a SQL query to find all duplicate emails in a table named `Person`.

[Leetcode](https://leetcode.com/problems/duplicate-emails/)

<!--more-->

```
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
```

For example, your query should return the following for the above table:

```
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
```

---

#### GROUP and HAVING

```sql
# Write your MySQL query statement below
SELECT P.Email
FROM Person P
GROUP BY P.Email
HAVING COUNT(EMAIL) > 1;
```

---

#### GROUP with a TMP table

```sql
# Write your MySQL query statement below
SELECT TMP.Email
FROM (SELECT Email, COUNT(*) AS Num
      FROM Person P
      GROUP BY P.Email
     ) as TMP
WHERE TMP.Num > 1
```

