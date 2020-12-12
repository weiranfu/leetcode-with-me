---
title: Easy | Rising Temperature 197
tags:
  - common
categories:
  - Leetcode
  - SQL
date: 2020-06-06 00:21:17
---

Given a `Weather` table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

[Leetcode](https://leetcode.com/problems/rising-temperature/)

<!--more-->

```
+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
```

For example, return the following Ids for the above `Weather` table:

```
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
```

---

#### First solution  

```sql
# Write your MySQL query statement below
select w1.Id
from Weather w1, Weather w2
where w1.Temperature > w2.Temperature
      and TO_DAYS(w1.RecordDate) - TO_DAYS(w2.RecordDate) = 1
```

---

#### Optimized

```sql
# Write your MySQL query statement below
select w1.Id
from weather w1
       join
     weather w2 on DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
where w1.Temperature > w2.Temperature
```

