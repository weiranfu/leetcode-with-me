---
title: Medium | Get Watched Videos by Your Friends 1311
tags:
  - common
  - Oh-shit
  - implement
categories:
  - Leetcode
  - Graph
date: 2020-01-05 10:21:39
---

There are `n` people, each person has a unique *id* between `0` and `n-1`. Given the arrays `watchedVideos` and `friends`, where `watchedVideos[i]` and `friends[i]` contain the list of watched videos and the list of friends respectively for the person with `id = i`.

Level **1** of videos are all watched videos by your friends, level **2** of videos are all watched videos by the friends of your friends and so on. In general, the level **k** of videos are all watched videos by people with the shortest path equal to **k** with you. Given your `id`and the `level` of videos, return the list of videos ordered by their frequencies (increasing). For videos with the same frequency order them alphabetically from least to greatest. 

[Leetcode](https://leetcode.com/problems/get-watched-videos-by-your-friends/)

<!--more-->

**Example 1:**

**![img](https://assets.leetcode.com/uploads/2020/01/02/leetcode_friends_1.png)**

```
Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
Output: ["B","C"] 
Explanation: 
You have id = 0 (green color in the figure) and your friends are (yellow color in the figure):
Person with id = 1 -> watchedVideos = ["C"] 
Person with id = 2 -> watchedVideos = ["B","C"] 
The frequencies of watchedVideos by your friends are: 
B -> 1 
C -> 2
```

**Example 2:**

**![img](https://assets.leetcode.com/uploads/2020/01/02/leetcode_friends_2.png)**

```
Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
Output: ["D"]
Explanation: 
You have id = 0 (green color in the figure) and the only friend of your friends is the person with id = 3 (yellow color in the figure).
```

**Constraints:**

- `n == watchedVideos.length == friends.length`
- `2 <= n <= 100`
- `1 <= watchedVideos[i].length <= 100`
- `1 <= watchedVideos[i][j].length <= 8`
- `0 <= friends[i].length < n`
- `0 <= friends[i][j] < n`
- `0 <= id < n`
- `1 <= level < n`
- if `friends[i]` contains `j`, then `friends[j]` contains `i`

---

#### Implement

Use `(a, b) -> {}` to create a new Comparator() for priority queue or sort.

```java
Collections.sort(res, (a, b) -> {           
    if (count.get(a) != count.get(b)) {
        return count.get(a) - count.get(b);
    } else {
        return a.compareTo(b);
    }
});
```

#### Oh-Shit

We must mark a friend as visited before he is added into queue rather than he is polled out from a queue.

Because if a level of friends have a common unvisited friend A, then A will be added into queue multiple times.

---

#### My thoughts 

BFS to get N'th level friends, then get their movies, and store them into frequency map.

Sort these movies by its frequency.

---

#### First solution 

```java
class Solution {
    public List<String> watchedVideosByFriends(List<List<String>> watchedVideos, int[][] friends, int id, int level) {
        boolean[] visited = new boolean[friends.length];
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(id);
        visited[id] = true;
        while (level != 0 && !queue.isEmpty()) {
            int size = queue.size();
            while (size-- != 0) {
                int curr = queue.poll();
                // visited[i] = true;     Attention! we can't set visited[] here!
                for (int i : friends[curr]) { // Otherwise if a level of friends have a 
                    if (!visited[i]) {  // common unvisited friend A, then friend A will 
                        queue.add(i);   // be added into queue multiple times.
                        visited[i] = true;
                    }               
                }
            }
            level--;
        }
        List<String> res = new ArrayList<>();
        if (queue.isEmpty()) {
            return res;
        }
        Map<String, Integer> count = new HashMap<>();
        while (!queue.isEmpty()) {
            int friend = queue.poll();
            for (String movie : watchedVideos.get(friend)) {
                count.put(movie, count.getOrDefault(movie, 0) + 1);
            }
        }
        for (String movie : count.keySet()) {
            res.add(movie);
        }
        Collections.sort(res, (a, b) -> {           
            if (count.get(a) != count.get(b)) {
                return count.get(a) - count.get(b);
            } else {
                return a.compareTo(b);
            }
        });
        return res;
    }
}
```

T: O(E + V + mlogm)

S: O(V + m)

---

#### Summary 

Use `(a, b) -> {}` to create a new Comparator() for priority queue or sort.

```java
Collections.sort(res, (a, b) -> {           
    if (count.get(a) != count.get(b)) {
        return count.get(a) - count.get(b);
    } else {
        return a.compareTo(b);
    }

```

