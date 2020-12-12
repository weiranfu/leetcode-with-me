---
title: Be careful about these things
tags:
  - tricky
  - corner case
categories:
  - Summary
date: 2020-06-07 22:08:46
---

Something we need to be careful about when solving Leetcode problems.

<!--more-->

---

#### Get the median of an array

`int a = (l + r) / 2`				**向下取整**

`int b = (l + r + 1) / 2`		**向上取整**

`int median = (a + b) / 2`

---

#### Arrays.sort(a, (a, b) -> a - b)

We cannot perform `Arrays.sort` on `int[] array` with custom comparator because `int` cannot autobox to `Integer`.

We should use `Stream` : `boxed()`, `sorted()`

```java
int median = (arr[(n-1)/2] + arr[n/2])/2;
arr = Arrays.stream(arr)
            .boxed()
            .sorted((a, b) -> {
            int x = Math.abs(a - median);
            int y = Math.abs(b - median);
            if (x != y) return x - y;
            else return a - b;
            })
            .mapToInt(i -> i)
            .toArray();
```

---

#### Create empty int array

`int[] res = new int[0]`

---

#### Random()

```java
Random random = new Random();
int a = random.nextInt(n);			// a in [0, n-1]
```

**Shuffle Algorithm**

```java
public void shuffle(int[] a) {
  for (int i = a.length - 1; i >= 0; i--) {
    int rand = random.nextInt(i + 1);
    swap(a, i, rand);
  }
}
private void swap(int[] a, int l, int r) {
  int tmp = a[l];
  a[l] = a[r];
  a[r] = tmp;
}
```

---

#### TreeMap

The time complexity of `containsKey()` is `O(logn)`

`containsKey()` doesn't use `hashCode` of key instead `equals()` to determine whether the key exists or not.