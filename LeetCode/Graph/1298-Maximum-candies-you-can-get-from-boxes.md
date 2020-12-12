---
title: Hard | Maximum Candies You Can Get from Boxes 1298
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2019-12-22 23:44:46
---

Given `n` boxes, each box is given in the format `[status, candies, keys, containedBoxes]` where:

- `status[i]`: an integer which is **1** if `box[i]` is open and **0** if `box[i]` is closed.
- `candies[i]`: an integer representing the number of candies in `box[i]`.
- `keys[i]`: an array contains the indices of the boxes you can open with the key in `box[i]`.
- `containedBoxes[i]`: an array contains the indices of the boxes found in `box[i]`.

You will start with some boxes given in `initialBoxes` array. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return *the maximum number of candies* you can get following the rules above.

[Leetcode](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/)

<!--more-->

**Example 1:**

```
Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
Output: 16
Explanation: You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2. Box 1 is closed and you don't have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
Total number of candies collected = 7 + 4 + 5 = 16 candy.
```

**Example 2:**

```
Input: status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
Output: 6
Explanation: You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys. The total number of candies will be 6.
```

**Example 3:**

```
Input: status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1]
Output: 1
```

**Example 4:**

```
Input: status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = []
Output: 0
```

**Example 5:**

```
Input: status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0]
Output: 7
```

**Constraints:**

- `1 <= status.length <= 1000`
- `status.length == candies.length == keys.length == containedBoxes.length == n`
- `status[i]` is `0` or `1`.
- `1 <= candies[i] <= 1000`
- `0 <= keys[i].length <= status.length`
- `0 <= keys[i][j] < status.length`
- All values in `keys[i]` are unique.
- `0 <= containedBoxes[i].length <= status.length`
- `0 <= containedBoxes[i][j] < status.length`
- All values in `containedBoxes[i]` are unique.
- Each box is contained in one box at most.
- `0 <= initialBoxes.length <= status.length`
- `0 <= initialBoxes[i] < status.length`

---

#### Tricky 

These problem is actually a directed graph problem. `containedBoxes` means neighbors of a parent node.

---

#### My thoughts 

Using DFS. 

1. Find all posible keys. DFS all boxes to find keys, if we find a key and corresponding box is closed, we open that box and marked visited. Then find all keys its contained boxes have.
2. Find all candies.

---

#### DFS 

We must mark openned boxes as visited, because we might visite a box twice when we find a duplicate key in contained boxes.

```java
class Solution {
    public int maxCandies(int[] status, int[] candies, int[][] keys, int[][] containedBoxes, int[] initialBoxes) {
        int sum = 0;
        boolean[] visited = new boolean[status.length];
        for (int i : initialBoxes) {
            findKeys(i, containedBoxes, keys, status, visited);
        }
        for (int i : initialBoxes) {
            sum += findCandies(i, containedBoxes, candies, status);
        }
        return sum;
    }
    private void findKeys(int i, int[][] containedBoxes, int[][] keys, int[] status, boolean[] visited) {
        if (status[i] == 1 && !visited[i]) {
            visited[i] = true;
            for (int key : keys[i]) {
                if (status[key] == 0) {
                    status[key] = 1;
                    findKeys(key, containedBoxes, keys, status, visited);
                }
            }
            for (int n : containedBoxes[i]) {
                findKeys(n, containedBoxes, keys, status, visited);
            }
        }
    }
    private int findCandies(int i, int[][] containedBoxes, int[] candies, int[] status) {
        int sum = 0;
        if (status[i] == 1) {
            sum += candies[i];
            for (int n : containedBoxes[i]) {
                sum += findCandies(n, containedBoxes, candies, status);
            }
        }
        return sum;
    }
}
```

T: O(n^2) S: O(n)

---

#### BFS + Bellman Ford 

We continue open possible boxes and find keys until all left boxes are closed and no keys can used for them.

```java
class Solution {
    public int maxCandies(int[] status, int[] candies, int[][] keys, int[][] containedBoxes, int[] initialBoxes) {
        int sum = 0;
        List<Integer> list = new ArrayList<>();
        Queue<Integer> unopennedBoxes = new LinkedList<>();
        for (int i : initialBoxes) {
            unopennedBoxes.offer(i);
        }
        while (!unopennedBoxes.isEmpty()) {
            boolean open = false;
            int size = unopennedBoxes.size();
            for (int i = 0; i < size; i += 1) {
                int box = unopennedBoxes.poll();
                if (status[box] == 1) {
                    open = true;
                    sum += candies[box];
                    for (int key : keys[box]) {
                        status[key] = 1;
                    }
                    for (int c : containedBoxes[box]) {
                        unopennedBoxes.offer(c);
                    }
                } else {
                    unopennedBoxes.offer(box);
                }
            }
            if (!open) break;
        }
        return sum;
    }
}
```

T: O(n^2) S: O(n)

---

#### Summary 

* DFS: find all keys then open boxes and get candies.
* BFS: find keys and open boxes at the same time until no more change.