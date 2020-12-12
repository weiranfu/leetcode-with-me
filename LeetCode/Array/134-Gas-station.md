---
title: Medium | Gas station 134
tags:
  - tricky
  - Oh-shit
categories:
  - Leetcode
  - Array
date: 2019-07-19 14:35:59
---

There are *N* gas stations along a circular route, where the amount of gas at station *i* is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from station *i* to its next station (*i*+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

<!--more-->

**Note:**

- If there exists a solution, it is guaranteed to be **unique**.
- Both input arrays are non-empty and have the same length.
- Each element in the input arrays is a non-negative integer.

**Example 1:**

```
Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
```

**Example 2:**

```
Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
```

---

#### Tricky 

Total means total sum of the array.

Tank means real-time sum of the array.

<span style="color:blue">**If the total sum of an array is not negative, then there must be a start position, where I can circle the array from this start position and the real-time sum should always be not negative.**</span>

So if the total = sum(gas - cost) is not negative, there must be a solution!

Now let's find the start postion.

If the car starts at position `i`, and the tank is not negative. But when it arrives at position `j`, the tank is negative. This indicates the car has a positive tank from position `i` to position `j-1`. The tank becomes negative when car drives from position `j-1` to `j`.

<span style="color:blue">**So We do not need to find start position between position `i` and position `j`, because car starts at any start position between these two points can not arrive position `j`.**</span>

So we can jump to position `j+1` to find start position. 

<span style="color:blue">**If we find a start position `i` where car can drive from `i` to the last position in the array and the total is not negative(which means there must exist a solution), then the car certainly will drive a circle from this start point.**</span>

This is because total is not negative, so the `sum1` of position `i` to last positon is must greater than `sum2` of position `0` to position `i`. 

given: `Sum1` + `sum2` >= 0, `sum1` >= 0 

==>     `sum1` >= |`sum2`|

So the car can make a circle driving, and the solution is unique.

#### Oh-Shit 

In a *for* loop, if we want to restart this loop at i, use

**`i = -1;`**  instead of  `i = 0`;

because after this step, `i += 1` will run in the *for* loop.

---

#### My thoughts 

At any start position, *for* loop the whole array to test whether tank will become negative. If true, then restart *for* loop at a new start position(`start += 1;`)

If *for* loop is over, then return start. (this start is successful)

There must exists a solution (total >= 0), so the *for* loop won't restart forever (dead loop).

---

#### First solution 

```java
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int tank = 0;
        int totalGas = 0;
        int totalCost = 0;
        int start = 0;
        for (int i = 0; i < gas.length; i += 1) {
            totalGas += gas[i];
            totalCost += cost[i];
        }
        if (totalGas < totalCost) {
            return -1;
        }
        for (int i = 0; i < gas.length; i += 1) {
            tank += gas[(start + i) % gas.length] - cost[(start + i) % gas.length];
            if (tank < 0) {
                tank = 0;
                start += 1;
                i = -1;            //restart the loop.
            }
        }
        return start;
    }
}
```

T: O(n*n) S: O(1)

---

#### Standard solution 

```java
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int tank = 0;
        int start = 0;
        int total = 0;
        for (int i = 0; i < gas.length; i += 1) {
            tank += gas[i] - cost[i];
            total += gas[i] - cost[i];
            if (tank < 0) {
                tank = 0;
                start = i + 1;      // start at i+1
            }
        }
        if (total < 0) {
            return -1;
        }
        return start;
    }
}
```

T: O(n) S: O(1)

---

#### Summary 

This is a classical consuming problem.

**If car starts at A and can not reach B, any station between A and B can not reach B.(B is the first station that A can not reach.)**