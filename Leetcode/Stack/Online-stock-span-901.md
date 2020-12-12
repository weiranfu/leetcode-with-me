---
title: Medium | Online Stock Span 901
tags:
  - common
  - tricky
categories:
  - Leetcode
  - Stack
date: 2020-07-27 18:48:44
---

Write a class `StockSpanner` which collects daily price quotes for some stock, and returns the *span* of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were `[100, 80, 60, 70, 60, 75, 85]`, then the stock spans would be `[1, 1, 1, 2, 1, 4, 6]`.

![Click to enlarge](https://media.geeksforgeeks.org/wp-content/uploads/Stock_span.png)

[Leetcode](https://leetcode.com/problems/online-stock-span/)

<!--more-->

**Example 1:**

```
Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.
```

**Note:**

1. Calls to `StockSpanner.next(int price)` will have `1 <= price <= 10^5`.
2. There will be at most `10000` calls to `StockSpanner.next` per test case.
3. There will be at most `150000` calls to `StockSpanner.next` across all test cases.

**Follow up:** 

[Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

---

#### Stack 

We use `day` to count `ith` day.

We need to find the previous larger day `j`, which is same as *finding previous larger element*. And this can be solved by using a decreasing stack.

Then the span for day `i` will be `i - j`.

```java
class StockSpanner {
    
    Stack<int[]> stack;
    int day;

    public StockSpanner() {
        day = 0;
        stack = new Stack<>();
    }
    
    public int next(int price) {
        int today = day++;
        while (!stack.isEmpty() && stack.peek()[0] <= price) {
            stack.pop();
        }
        int preday = stack.isEmpty() ? -1 : stack.peek()[1];
        int len = today - preday;
        stack.push(new int[]{price, today});
        return len;
    }
}
```

T: O(n)			S: O(n)

---

#### Stack II

We could push every pair of `<price, result>` to a stack.
Pop lower price from the stack and accumulate the count.

```java
class StockSpanner {
    
    Stack<int[]> stack;

    public StockSpanner() {
        stack = new Stack<>();
    }
    
    public int next(int price) {
        int cnt = 1;
        while (!stack.isEmpty() && stack.peek()[0] <= price) {
            cnt += stack.pop()[1];
        }
        stack.push(new int[]{price, cnt});
        return cnt;
    }
}
```

T: O(n)			S: O(n)

