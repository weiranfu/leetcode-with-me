---
title: Medium | Tweet Counts Per Frequency 1348
tags:
  - tricky
  - implement
categories:
  - Leetcode
  - Tree
date: 2020-03-06 20:28:23
---

Implement the class `TweetCounts` that supports two methods:

1.` recordTweet(string tweetName, int time)`

- Stores the `tweetName` at the recorded `time` (in **seconds**).

2.` getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime)`

- Returns the total number of occurrences for the given `tweetName` per **minute**, **hour**, or **day** (depending on `freq`) starting from the `startTime` (in **seconds**) and ending at the `endTime` (in **seconds**).
- `freq` is always **minute***,* **hour** *or **day***, representing the time interval to get the total number of occurrences for the given `tweetName`.
- The first time interval always starts from the `startTime`, so the time intervals are `[startTime, startTime + delta*1>,  [startTime + delta*1, startTime + delta*2>, [startTime + delta*2, startTime + delta*3>, ... , [startTime + delta*i, **min**(startTime + delta*(i+1), endTime + 1)>` for some non-negative number `i` and `delta`(which depends on `freq`).  

[Leetcode](https://leetcode.com/problems/tweet-counts-per-frequency/)

<!--more-->

**Example:**

```
Input
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

Output
[null,null,null,null,[2],[2,1],null,[4]]

Explanation
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);
tweetCounts.recordTweet("tweet3", 60);
tweetCounts.recordTweet("tweet3", 10);                             // All tweets correspond to "tweet3" with recorded times at 0, 10 and 60.
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // return [2]. The frequency is per minute (60 seconds), so there is one interval of time: 1) [0, 60> - > 2 tweets.
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // return [2, 1]. The frequency is per minute (60 seconds), so there are two intervals of time: 1) [0, 60> - > 2 tweets, and 2) [60,61> - > 1 tweet.
tweetCounts.recordTweet("tweet3", 120);                            // All tweets correspond to "tweet3" with recorded times at 0, 10, 60 and 120.
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // return [4]. The frequency is per hour (3600 seconds), so there is one interval of time: 1) [0, 211> - > 4 tweets.
```

**Constraints:**

- There will be at most `10000` operations considering both `recordTweet` and `getTweetCountsPerFrequency`.
- `0 <= time, startTime, endTime <= 10^9`
- `0 <= endTime - startTime <= 10^4`

---

#### Tricky 

If we want to maintain data in sorted order, do not use sort. Because everytime we add a data, we need sort, which is not efficient. 
Use TreeMap to maintain data in sorted order.

#### Implement

We use ArrayList rather than LinkedList if we use `list.get(i)` more frequently than `list.add(i)`

---

#### My thoughts 

Use an ArrayList to store tweets in sorted order by time.

Do not use sort(), because everytime we add a tweet, we need to sort.

---

#### First solution 

Keep tweets idx, and increase start time value to traverse all time interval.

```java
class TweetCounts {
    Map<String, List<Integer>> map;

    public TweetCounts() {
        map = new HashMap<>();
    }
    
    public void recordTweet(String tweetName, int time) {
        List<Integer> list = map.getOrDefault(tweetName, new ArrayList<Integer>());
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) >= time) {             // Need to use ArrayList rather than LinkedList
                list.add(i, time);                 // Although list.get(i) list.add(i) both used here
                map.put(tweetName, list);          // list.get(i) is used more frequently.
                return;
            }
        }
        list.add(time);
        map.put(tweetName, list);
    }
    
    public List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) {
        List<Integer> list = map.get(tweetName);
        int interval;
        if (freq.equals("minute")) {
            interval = 60;
        } else if (freq.equals("hour")) {
            interval = 3600;
        } else {
            interval = 86400;
        }
        List<Integer> res = new LinkedList<>();
        if (!map.containsKey(tweetName)) return res;
        int idx = 0, st = startTime;
        for (; idx < list.size(); idx++) {
            if (list.get(idx) >= startTime) break;
        }
        while (st <= endTime) {
            int count = 0;
            while (idx < list.size() && list.get(idx) - st < interval && list.get(idx) <= endTime) {
                count++;
                idx++;
            }
            st += interval;
            res.add(count);
        }
        return res;
    }
}
```

Add  					T: O(n)

GetCounts     	 T: O(n)

---

#### TreeMap

We could use treemap to maintain sorted data.

Use `map.subMap(start, end)` to get a submap of sorted map.

`TreeMap<Integer, Integer> times = map.putIfAbsent(tweetName, new TreeMap<Integer, Integer>())`

`Map<Integer, Integer> submap = times.sumMap(startTime, endTime)`

```
for (Map.Entry<Integer, Integer> entry : submap.entrySet()) {
	count += entry.getValue();
}
```

```java
class TweetCounts {
    Map<String, TreeMap<Integer, Integer>> map;

    public TweetCounts() {
        map = new HashMap<>();
    }
    
    public void recordTweet(String tweetName, int time) {
        map.putIfAbsent(tweetName, new TreeMap<Integer, Integer>());
        TreeMap<Integer, Integer> times = map.get(tweetName);
        times.put(time, times.getOrDefault(time, 0) + 1);
    }
    
    public List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) {
        TreeMap<Integer, Integer> times = map.get(tweetName);
        int interval;
        if (freq.equals("minute")) {
            interval = 60;
        } else if (freq.equals("hour")) {
            interval = 3600;
        } else {
            interval = 86400;
        }
        List<Integer> res = new LinkedList<>();
        if (!map.containsKey(tweetName)) return res;
        int st = startTime;
        while (st <= endTime) {
            int end = Math.min(st + interval, endTime + 1);
            int count = 0;
            for (Map.Entry<Integer, Integer> entry : times.subMap(st, end).entrySet()) {
                count += entry.getValue();
            }
            res.add(count);
            st += interval;
        }
        return res;
    }
}

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts obj = new TweetCounts();
 * obj.recordTweet(tweetName,time);
 * List<Integer> param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */
```

Add: 			O(logN)

GetCount:   O(N)

---

#### Optimized 

Use buckets to store these times.

Bucket size is : `int size = (endTime - startTime) / interval + 1`

```java
class TweetCounts {
    Map<String, TreeMap<Integer, Integer>> map;

    public TweetCounts() {
        map = new HashMap<>();
    }
    
    public void recordTweet(String tweetName, int time) {
        map.putIfAbsent(tweetName, new TreeMap<Integer, Integer>());
        TreeMap<Integer, Integer> times = map.get(tweetName);
        times.put(time, times.getOrDefault(time, 0) + 1);
    }
    
    public List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime) {
        TreeMap<Integer, Integer> times = map.get(tweetName);
        int interval;
        if (freq.equals("minute")) {
            interval = 60;
        } else if (freq.equals("hour")) {
            interval = 3600;
        } else {
            interval = 86400;
        }
        List<Integer> res = new LinkedList<>();
        if (!map.containsKey(tweetName)) return res;
      
        int size = (endTime - startTime) / interval + 1;
        int[] buckets = new int[size];
      
        for (Map.Entry<Integer, Integer> entry : times.subMap(startTime, endTime + 1).entrySet()) {
            int idx = (entry.getKey() - startTime) / interval;
            buckets[idx] += entry.getValue();
        }
        for (int n : buckets) {
            res.add(n);
        }
        return res;
    }
}
```

---

#### Summary 

TreeMap usage:

`TreeMap<Integer, Integer> times = map.putIfAbsent(tweetName, new TreeMap<Integer, Integer>())`

`Map<Integer, Integer> submap = times.sumMap(startTime, endTime)`

```
for (Map.Entry<Integer, Integer> entry : submap.entrySet()) {
	count += entry.getValue();
}
```

