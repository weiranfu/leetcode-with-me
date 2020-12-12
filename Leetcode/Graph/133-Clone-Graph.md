---
title: Medium | Clone Graph 133
tags:
  - tricky
categories:
  - Leetcode
  - Graph
date: 2020-05-27 23:25:13
---

Given a reference of a node in a **connected** undirected graph.

Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph.

Each node in the graph contains a val (`int`) and a list (`List[Node]`) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

[Leetcode](https://leetcode.com/problems/clone-graph/)

<!--more-->

**Test case format:**

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with `val = 1`, the second node with `val = 2`, and so on. The graph is represented in the test case using an adjacency list.

**Adjacency list** is a collection of unordered **lists** used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the **copy of the given node** as a reference to the cloned graph.

**Example:**

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

**Constraints:**

- `1 <= Node.val <= 100`
- `Node.val` is unique for each node.
- Number of Nodes will not exceed 100.
- There is no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

---

#### Tricky 

**How to do a deep copy? The key is to keep track of new copied Node, such as saving them into map or `Node[]`.**

Since when we do DFS/BFS, we could not copy its neighbor right away, so we need to refer to it by map later.

---

#### DFS

Use `Node[]` to save copied nodes.

```java
class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return node;
        Node[] visited = new Node[101];
        return deepCopy(node, visited);
    }
    
    private Node deepCopy(Node node, Node[] visited) {
        Node res = new Node(node.val);
        List<Node> neighbors = res.neighbors;
        visited[node.val] = res;
        for (Node n : node.neighbors) {
            Node copied;
            if (visited[n.val] == null) {       // if haven't create copied node.
                copied = deepCopy(n, visited);
                
            } else {
                copied = visited[n.val];       // retrieve copied node.
            }
            neighbors.add(copied);
        }
        return res;
    }
}
```

T: O(N + E)		S: O(N)

---

#### BFS

```java
class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return node;
        Node[] visited = new Node[101];
        Queue<Node> queue = new LinkedList<>();
        queue.add(node);
        Node root = new Node(node.val);
        visited[node.val] = root;
        while (!queue.isEmpty()) {
            Node n = queue.poll();
            Node copied = visited[n.val];
            for (Node neighbor : n.neighbors) {
                Node newNode;
                if (visited[neighbor.val] == null) {
                    newNode = new Node(neighbor.val);
                    visited[neighbor.val] = newNode;
                    queue.add(neighbor);
                } else {
                    newNode = visited[neighbor.val];
                }
                copied.neighbors.add(newNode);
            }
        }
        return root;
    }
}
```

T: O(N + E)		S: O(N)

