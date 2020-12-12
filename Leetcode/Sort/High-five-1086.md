---
title: Easy | High Five 1086
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Sort
date: 2020-08-26 15:04:42
---

Given a list of scores of different students, return the average score of each student's **top five scores** in **the order of each student's id**.

Each entry `items[i]` has `items[i][0]` the student's id, and `items[i][1]` the student's score.  The average score is calculated using integer division.

[Leetcode](https://leetcode.com/problems/high-five/)

<!--more-->

**Example 1:**

```
Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
```

**Note:**

1. `1 <= items.length <= 1000`
2. `items[i].length == 2`
3. The IDs of the students is between `1` to `1000`
4. The score of the students is between `1` to `100`
5. For each student, there are at least 5 scores

---

#### Priority Queue

We need to figure out how many students there are.

So we need to sort `items[][]` by `id`.

Then we could create a priority queue for each id and select top five scores.

```java
class Solution {
    public int[][] highFive(int[][] items) {
        Arrays.sort(items, (a, b) -> a[0] - b[0]);
        int n = items.length;
        int N = items[n - 1][0];
        PriorityQueue<Integer>[] pqs = new PriorityQueue[N];
        for (int i = 0; i < N; i++) pqs[i] = new PriorityQueue<>();
        for (int[] item : items) {
            int id = item[0] - 1, score = item[1];
            pqs[id].add(score);
            if (pqs[id].size() > 5) pqs[id].poll();
        }
        int[][] res = new int[N][2];
        for (int i = 0; i < N; i++) {
            int sum = 0;
            while (!pqs[i].isEmpty()) {
                sum += pqs[i].poll();
            }
            res[i] = new int[]{i + 1, sum / 5};
        }
        return res;
    }
}
```

T: O(nlogn)			S: O(n)

2. Sort

   However, we could do better!

   Since we need to sort `items[][]`, we can sort it by `id` and `score`, then we only need to pick up the top five scores from the sorted array.

   ```java
   class Solution {
       public int[][] highFive(int[][] items) {
           Arrays.sort(items, (a, b) -> {
               if (a[0] == b[0]) return b[1] - a[1];
               else return a[0] - b[0];
           });
           int n = items.length;
           int N = items[n - 1][0];
           int[][] res = new int[N][2];
           int id = 1, count = 0, sum = 0;
           for (int i = 0; i < n && id <= N; i++) {
               if (items[i][0] == id) {
                   sum += items[i][1];
                   count++;
                   if (count == 5) {
                       res[id - 1] = new int[]{id, sum / 5};
                       sum = 0;
                       count = 0;
                       id++;
                   }
               }
           }
           return res;
       }
   }
   ```

   T: O(nlogn)			S: O(1)

