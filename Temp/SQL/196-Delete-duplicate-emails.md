---
title: Easy | Delete Duplicate Emails 196
tags:
  - common
categories:
  - Leetcode
  - SQL
date: 2020-06-06 00:12:59
---

Write a SQL query to **delete** all duplicate email entries in a table named `Person`, keeping only unique emails based on its *smallest* **Id**.

[Leetcode](https://leetcode.com/problems/delete-duplicate-emails/)

<!--more-->

```
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
```

For example, after running your query, the above `Person` table should have the following rows:

```
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
```

**Note:**

Your output is the whole `Person` table after executing your sql. Use `delete` statement.

---

#### Tricky 

**where we try this clause :**

```sql
delete from Person where id not in(select min(id) as id from Person group by email)
```

you will be noted " **You can't specify target table 'Person' for update in FROM clause** ",
The solution is using a middle table with select clause:

```sql
# Write your MySQL query statement below
DELETE 
FROM Person
WHERE Id NOT IN (SELECT * FROM
                     (SELECT MIN(P.Id) 
                      FROM Person P 
                      GROUP BY P.Email) AS TMP
                 )
```

