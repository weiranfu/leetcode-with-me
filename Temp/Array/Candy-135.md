---
title: Hard | Candy 135	
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-05-28 16:30:15
---

There are *N* children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

[Leetcode](https://leetcode.com/problems/candy/)

<!--more-->

**Example 1:**

```
Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
```

**Example 2:**

```
Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
```

---

#### Brute Force 

Keep a track of candies. We scan the array from left to right. When we change candies, we set flag `rescan = true` to rescan once until all is done.

When we find `ratings[i] > ratings[i - 1] && candies[i] <= candies[i - 1]`, we assign `candies[i] = candies[i - 1] + 1`. Set `rescan` true.

When we find `ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1] `, we assign `candies[i] = candies[i + 1] + 1`. Set `rescan` true.

```java
class Solution {
    public int candy(int[] ratings) {
        if (ratings == null || ratings.length == 0) return 0;
        int n = ratings.length;
        boolean rescan = true;
        int[] candies = new int[n];
        Arrays.fill(candies, 1);
        while (rescan) {
            rescan = false;
            for (int i = 0; i < n; i++) {
                if (i < n - 1 && ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1]) {
                    candies[i] = candies[i + 1] + 1;
                    rescan = true;
                }
                if (i > 0 && ratings[i] > ratings[i - 1] && candies[i] <= candies[i - 1]) {
                    candies[i] = candies[i - 1] + 1;
                    rescan = true;
                }  
            }
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            res += candies[i];
        }
        return res;
    }
}
```

**Analysis:**

We can `rescan` the array at most `n` times, cause we can modify each point at most twice.

T: O(n^2)			S: O(n)

---

#### Two Scan

Inspired by brute force method, during we rescanning the array, each point can be modified at most twice.

So we can scan the array twice. Once from left to right and only consider current point and its left one.

Once from right to left and only consider current point and its right one.

**When we increase value of a point from one side, it won't break up the condition that the other side holds.**

When we traverse for the second time, the value assign to the point is the maximum of left and right.

```java
class Solution {
    public int candy(int[] ratings) {
        if (ratings == null || ratings.length == 0) return 0;
        int n = ratings.length;
        boolean rescan = true;
        int[] candies = new int[n];
        Arrays.fill(candies, 1);
        for (int i = 1; i < n; i++) {               // left to right
            if (ratings[i] > ratings[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }
        int res = candies[n - 1];
        for (int i = n - 2; i >= 0; i--) {         // right to left
            if (ratings[i] > ratings[i + 1]) {
              	// maximum of left and right
                candies[i] = Math.max(candies[i], candies[i + 1] + 1); 
            }
            res += candies[i];
        }
        return res;
    }
}
```

T: O(n)		S: O(n)

---

#### Up & Down counters

**We can view the given `ratings` as some rising and falling slopes. Whenever the slope is rising, the distribution takes the form: `1, 2, 3, ..., m`. Similarly, a falling slope takes the form: `k,..., 2, 1`. **

An issue that arises now is that the local peak point can be included in only one of the slopes. Whether to include the local peak point in the rising slope or the falling slope?

we can observe that in order to satisfy both the right neighbour and the left neighbour criteria, the peak point's count needs to be the max. of the counts determined by the rising and the falling slopes. Thus, in order to determine the number of candies required, the peak point needs to be included in the slope which contains more number of points.

We could maintain two counters `up` and `down` to keep a track of the count of elements on the rising slope and on a falling slope. And use `peak` counter to indicate how many elements are in `rising` slope.

If `down > peak`, which means peak point should be included in `falling` slope and candies at peak point should increase more `res += down - peak`.

There're three cases that we need to recalculate the candies at peak point(determine peak point belongs to rising slope or falling slope): 

* at the beginning of another rising slope(end of a mountain)
* at the beginning of a plain `ratings[i] == ratings[i - 1]`.
* When we finish the *for* loop, we need to recheck the last mountain.

The following figure shows the cases that need to be handled for this example:

```
rankings: [1 2 3 4 5 3 2 1 2 6 5 4 3 3 2 1 1 3 3 3 4 2]
```

![Candy_Two_Arrays](https://leetcode.com/problems/candy/Figures/135_Candy_Constant_Space.PNG)

When we scan in regions a, `up` and `peak` counters increase. At `pt.5`, `up == 4 and peak == 4`.

When we scan in regions b, `down` counter increases and we assign value from 1…n (**We assigning  candies from 1 to n equals assigning candies from n to 1**)

At `pt.8`, recalculate candies at `pt.5`, `4 = up > down = 3`

At `pt.10`, `up == 2 and peak == 2`. 

`At pt.13`, recalculate candies at `pt.10`, `2 = up < down = 3`, so candies need to increase `down - peak = 1` more.

```js
rising phase:
1 2 3 4 5
falling phase:
1 2 3 4 5 1 2 3
we assigning candies in region b from 1 2 3 equals 3 2 1
recalculate candies at pt.5 (peak still belongs to rising slope)
1 2 3 4 5 1 2 3
rising phase:
1 2 3 4 5 1 2 3 2 3
falling phase:
1 2 3 4 5 1 2 3 2 3 1 2 3
recalculate candies at pt.10 (down > peak, so we increase (down - peak = 1) more)
1 2 3 4 5 1 2 3 2 4 1 2 3
```

```java
class Solution {
    public int candy(int[] ratings) {
        if (ratings == null || ratings.length == 0) return 0;
        int n = ratings.length;
        int res = 1;                            // base is 1.
        int up = 0, down = 0;
        int peak = 0;
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                if (down > peak) {            // one mountain is over, recheck peak value.
                    res += down - peak; 
                }
                peak = 0;            // clear peak & down count
                down = 0;            
                up++;
                peak = up;           // peak is at "up" side.
                res += up + 1;      // assign this point (up + base) candies.
            } else if (ratings[i] == ratings[i - 1]) {
                if (down > peak) {           // one mountain is over, recheck peak value.
                    res += down - peak; 
                }
                peak = 0;          // clear peak & down count.
                down = 0;
                up = 0;            
                res += 1;          // assign base 1.
            } else {
                up = 0;            // clear up count
                down++;
                res += down;      // assign value from 1->2->...n
            }
        }
        if (down > peak) {          // last mountain is over, recheck peak value.
            res += down - peak; 
        }
        return res;
    }
}
```

T: O(n)		S: O(1)



