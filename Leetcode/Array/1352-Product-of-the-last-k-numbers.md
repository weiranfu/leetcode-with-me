---
title: Medium | Product of the Last K Numbers 1352
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2020-03-08 17:57:51
---

Implement the class `ProductOfNumbers` that supports two methods:

1.` add(int num)`

- Adds the number `num` to the back of the current list of numbers.

2.` getProduct(int k)`

- Returns the product of the last `k` numbers in the current list.
- You can assume that always the current list has **at least** `k` numbers.

At any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

[Leetcode](https://leetcode.com/problems/product-of-the-last-k-numbers/)

<!--more-->

**Example:**

```
Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
```

**Constraints:**

- There will be at most `40000` operations considering both `add` and `getProduct`.
- `0 <= num <= 100`
- `1 <= k <= 40000`

---

#### Tricky 

Use preSum to store the total product from a[:i] into product[i].

When we meet 0, we create a new empty product array to store remaining product.

if k > product.size, which means we meet 0, just return 0.

---

#### My thoughts 

```java
class ProductOfNumbers {
    List<Integer> product;

    public ProductOfNumbers() {
        product = new ArrayList<>();
    }
    
    public void add(int num) {
        int size = product.size();
        if (num == 0) {
            product = new ArrayList<>();
            return;
        }
        if (size == 0) {
            product.add(num);
        } else {
            product.add(product.get(size - 1) * num);
        }
    }
    
    public int getProduct(int k) {
        int size = product.size();
        if (k > size) {
            return 0;
        } else if (k == size) {
            return product.get(size - 1);
        } else {
            return product.get(size - 1) / product.get(size - k - 1);
        }
    }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers obj = new ProductOfNumbers();
 * obj.add(num);
 * int param_2 = obj.getProduct(k);
 */
```

T: O(1)				S: O(n)

---

#### Optimized

We could add 1 into product in the initilization, so that we can simplify query code.

```java
class ProductOfNumbers {
    List<Integer> product;

    public ProductOfNumbers() {
        product = new ArrayList<>();
        product.add(1);
    }
    
    public void add(int num) {
        int size = product.size();
        if (num == 0) {
            product = new ArrayList<>();
            product.add(1);
            return;
        }
        product.add(product.get(size - 1) * num);
    }
    
    public int getProduct(int k) {
        int size = product.size();
        if (k >= size) {       // contains default 1
            return 0;
        } else {
            return product.get(size - 1) / product.get(size - k - 1);
        }
    }
}
```

T: O(1)			S: O(n)

---

#### Summary 

In tricky.