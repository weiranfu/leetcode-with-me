---
title: Hard | Find Median from Data Stream 295
tags:
  - tricky
categories:
  - Leetcode
  - Array
date: 2019-12-23 23:37:43
---

Design a data structure that supports the following two operations:

- void addNum(int num) - Add a integer number from the data stream to the data structure.
- double findMedian() - Return the median of all elements so far.

[Leetcode](https://leetcode.com/problems/find-median-from-data-stream/)

<!--more-->

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,

```
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
```

**Example:**

```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
```

**Follow up:** 

***1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?***

We can maintain an integer array of length 100 to store the count of each number along with a total count. Then, we can iterate over the array to find the middle value to get our median.

Time and space complexity would be O(100) = O(1).

***2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?***

As 99% is between 0-100. So we need an integer array of length 100 and can keep a counter for less_than_zero and greater_than_hundred.
As we know soluiton will be definately in 0-100 we don't need to know those number which are >100 or < 0, only count of them will be enough.

---

#### Tricky 

Using two Heaps, each Heap stores half data.

Heap is implemented by PriorityQueue.

---

#### My thoughts 

Failed to solve.

---

#### First solution 

```java
class MedianFinder {
    
    PriorityQueue<Integer> maxHeap;
    PriorityQueue<Integer> minHeap;
    int maxCount;
    int minCount;
    double median;
    
    /** initialize your data structure here. */
    public MedianFinder() {
        maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        minHeap = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        median = findMedian();
        if (num > median) {
            minHeap.offer(num);
        } else {
            maxHeap.offer(num);
        }
        if (maxHeap.size() < minHeap.size()) {
            maxHeap.offer(minHeap.poll());
        } else if (maxHeap.size() > minHeap.size()) {
            minHeap.offer(maxHeap.poll());
        }
    }
    
    public double findMedian() {
        if (minHeap.size() == 0 && maxHeap.size() == 0) return 0.0;
        else if (minHeap.size() < maxHeap.size()) return (double) maxHeap.peek();
        else if (minHeap.size() > maxHeap.size()) return (double) minHeap.peek();
        else return (double) (maxHeap.peek() + minHeap.peek()) / 2;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
```

T: O(logN) S: O(n)

---

#### Optimized 

We don't need to compare new item with median when we add an item.

We can always add new item to larger heap, then move smallest item into smaller heap.

If smaller heap size is greater, then add largest item into larger heap.

```java
class MedianFinder {
    
    PriorityQueue<Integer> maxHeap;
    PriorityQueue<Integer> minHeap;
    
    /** initialize your data structure here. */
    public MedianFinder() {
        maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        minHeap = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        // Always add new item to minHeap, then move to maxHeap.
        minHeap.offer(num);
        maxHeap.offer(minHeap.poll());
        if (maxHeap.size() > minHeap.size()) {
            minHeap.offer(maxHeap.poll());
        }
    }
    
    public double findMedian() {
        if (minHeap.size() > maxHeap.size()) {
            return (double) minHeap.peek();
        } else {
            return (double) (minHeap.peek() + maxHeap.peek()) / 2;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
```

T: O(logN) S: O(n)

---

#### Summary 

When we care about the median, we can use two heaps. 

minHeap and maxHeap each store half data.