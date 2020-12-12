---
title: Cycle Detect 
tags:
  - tricky
categories:
  - Summary
date: 2020-06-07 18:58:05
---

Detecting cycle is an interesting topic in graph or linked list.

<!--more-->

---

#### Graph (Directed)

1. Tarjan Algorithm

   Keep a stack to dfs all nodes, we when meet a node which is on Stack, then we find a cycle.

   ```java
   class Solution {
       public boolean canFinish(int n, List<Integer>[] graph) {
           boolean[] marked = new boolean[n];
           boolean[] onStack = new boolean[n];
           
           for (int i = 0; i < n; i++) {
               if (!marked[i]) {
                   if (dfs(i, marked, onStack, graph)) {
                       return false;
                   }
               }
           }
           return true;
       }
       
       private boolean dfs(int v, boolean[] marked, boolean[] onStack, List<Integer>[] graph) {
           marked[v] = true;
           onStack[v] = true;
           
           for (int w : graph[v]) {
               if (!marked[w]) {
                   if (dfs(w, marked, onStack, graph)) {
                       return true;
                   }
               }
               if (onStack[w]) {     // find a cycle
                   return true;
               }
           }
           onStack[v] = false;      // pop off from a stack. Finish finding a SCC.
           return false;
       }
   }
   ```

   T: O(V + E)		S: O(V)

2. BFS Topological sort

   We could do a BFS topological sort. If there's no cycle, we will end up visiting all nodes. If there's a cycle, the nodes in the cycle all have 1 indegree edge left. (*Just like dead lock*).

   **So if there exist cycle, the topological sort won't collect the nodes on cycle.**
   
   ```java
   class Solution {
       public boolean canFinish(int n, List<Integer>[] graph) {
           int[] indegrees = new int[n];
           for (int v = 0; v < n; v++) {
             for (int w : graph[v]) {
               indegrees[w]++;
             }
           }
           Queue<Integer> start = new LinkedList<>();
           for (int i = 0; i < n; i++) {
               if (indegrees[i] == 0) {
                   start.add(i);
               }
           }
           while (!start.isEmpty()) {
               int v = start.poll();
               for (int w : graph[v]) {
                   indegrees[w]--;
                   if (indegrees[w] == 0) {
                       start.add(w);
                   }
               }
           }
           // check whether there exist a cycle.
           for (int i = 0; i < n; i++) {   
               if (indegrees[i] > 0) {
                   return false;
               }
           }
           return true;
       }
}
   ```
   
   T: O(V + E)			S: O(V)

---

#### Linked List

Find cycle using `fast` & `slow` pointers.

We could also find meet point by reseting `fast` to head node.

```java
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {       // find cycle
                fast = head;          // reset find to head
                while (slow != fast) { // find meet point
                    slow = slow.next;
                    fast = fast.next;
                }
                return fast;
            }
        }
        return null;
    }
}
```

