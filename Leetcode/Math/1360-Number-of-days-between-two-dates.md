---
title: Easy | Number of Days Between Two Dates 1360
tags:
  - tricky
categories:
  - Leetcode
  - Math
date: 2020-02-24 13:07:32
---

Write a program to count the number of days between two dates.

The two dates are given as strings, their format is `YYYY-MM-DD` as shown in the examples.

[Leetcode](https://leetcode.com/problems/number-of-days-between-two-dates/)

<!--more-->

**Example 1:**

```
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
```

**Example 2:**

```
Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
```

**Constraints:**

- The given dates are valid dates between the years `1971` and `2100`.

---

#### Tricky 

How to get the days between two dates?

We can calculate all days from `1971` to current year and then subtract them.

---

#### First solution 

We need to consider leap year.

leap Year: `year % 400 == 0 || year % 100 != 0 && year % 4 == 0`.

February has 28 days normally, but 29 days in leap year.

```java
class Solution {
    public int daysBetweenDates(String date1, String date2) {
        return Math.abs(getDays(date1) - getDays(date2));
    }
    private int getDays(String s) {
        String[] date = s.split("-");
        int year = Integer.parseInt(date[0]);
        int month = Integer.parseInt(date[1]);
        int day = Integer.parseInt(date[2]);
        int res = 0;
        for (int i = 1971; i < year; i++) {
            if (i % 400 == 0 || i % 4 == 0 && i % 100 != 0) {
                res += 366;
            } else {
                res += 365;
            }
        }
        for (int m = 1; m < month; m++) {
            if (m == 1 || m == 3 || m == 5 || m == 7 
                || m == 8 || m == 10 || m == 12) {
                res += 31;
            } else if (m == 2) {
                if (year % 400 == 0 || year % 4 == 0 && year % 100 != 0) {
                    res += 29;
                } else {
                    res += 28;
                }
            } else {
                res += 30;
            }
        }
        res += day;
        return res;
    }
}
```

T: O(year) 		S: O(1)

---

#### Summary 

How to determin a leap year?

`year % 400 == 0 || year % 100 != 0 && year % 4 == 0`