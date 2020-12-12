---
title: Math 
tags:
  - tricky
categories:
  - Summary
date: 2020-06-07 20:41:49
---

Something about math.

<!--more-->

---

#### Median

```java
int median = (A[n/2] + A[(n-1)/2])/2
```

---

#### Count primes in range(1, n)

```java
class Solution {
    public int countPrimes(int n) {
       boolean[] isPrime = new boolean[n];
       Arrays.fill(isPrime, true);
       // Loop's ending condition is i * i < n instead of i < sqrt(n)
       // to avoid repeatedly calling an expensive function sqrt().
       for (int i = 2; i * i < n; i++) {
          if (!isPrime[i]) continue;
          for (int j = i * i; j < n; j += i) {
             isPrime[j] = false;
          }
       }
       int count = 0;
       for (int i = 2; i < n; i++) {
          if (isPrime[i]) count++;
       }
       return count;
    }
}
```

---

#### Shuffle Algorithm

Shuffle an array

```java
class Solution {
	public int shuffle(int[] array) {
    int n = array.length;
    Random random = new Random();
    for (int i = 0; i < n; i++) {
  		int rand = i + random.nextInt(n - i);      // get rand in [i, n]
      exchange(nums, i, rand);                   // exchange nums[i] with nums[rand]
    }
  }
  
  private void exchange(int[] nums, int i, int j) {
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
  }
}
```

---

`int a = (int) 1e9` means 10^9