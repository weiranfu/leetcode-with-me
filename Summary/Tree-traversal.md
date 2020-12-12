---
title: Tree Traversal
tags:
  - tricky
categories:
  - Summary
date: 2020-01-11 18:38:01
---

Preorder Traversal, Inorder Traversal, Postorder Traversal and Levelorder Traversal. 

<!--more-->

---

#### Preorder Traversal

##### 1. Recursion

```java
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        preorderHelper(root, res);
        return res;
    }
    
    private void preorderHelper(TreeNode node, List<Integer> list) {
        if (node == null) return;
        list.add(node.val);
        preorderHelper(node.left, list);
        preorderHelper(node.right, list);
    }
}
```

##### 2. Iteration

```java
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Stack<TreeNode> stack = new Stack<>();
        stack.add(root);
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            res.add(n.val);
            if (n.right != null) stack.push(n.right);
            if (n.left != null) stack.push(n.left);
        }
        return res;
    }
}
```

##### 3. Node traversal

```java
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            if (curr != null) {
                res.add(curr.val);
                stack.push(curr);
                curr = curr.left;
            } else {
                TreeNode n = stack.pop();
                curr = n.right;
            }
        }
        return res;
    }
}
```

##### 4. Morris traversal

Space complexity will be optimized to O(1).

**Algorithm**

Here the idea is to go down from the node to its predecessor, and each predecessor will be visited twice. For this go one step left if possible and then always right till the end. When we visit a leaf (node's predecessor) first time, it has a zero right child, so we update output and establish the pseudo link `predecessor.right = root` to mark the fact the predecessor is visited. When we visit the same predecessor the second time, it already points to the current node, thus we remove pseudo link and move right to the next node.

If the first one step left is impossible, update output and move right to next node.

```java
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        TreeNode curr = root;
        while (curr != null) {
            if (curr.left != null) {  // If has left child, create predecessor.
                TreeNode predecessor = curr.left;
                // Travel to right most node to create a path to current node.
                while (predecessor.right != null && predecessor.right != curr) {
                    predecessor = predecessor.right;
                }
                if (predecessor.right == null) {//If first visit curr node, create path.
                    predecessor.right = curr;
                    res.add(curr.val);
                    curr = curr.left;
                } else {                    // If visit curr node before, destroy path.
                    predecessor.right = null;
                    curr = curr.right;
                }
            } else {                 // If doesn't have left child, use path to go back
                res.add(curr.val);   // to predecessor node.
                curr = curr.right;
            }
        }
        return res;
    }
}
```

T: O(n)			S: O(1)

---

#### Inorder Traversal

##### 1. Recursion

```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        inorderHelper(root, res);
        return res;
    }
    private void inorderHelper(TreeNode node, List<Integer> res){
        if (node == null) return;
        inorderHelper(node.left, res);
        res.add(node.val);
        inorderHelper(node.right, res);
    }
}
```

##### 2. Node traversal

```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            if (curr != null) {
                stack.push(curr);
                curr = curr.left;
            } else {
                TreeNode prev = stack.pop();
                res.add(prev.val);
                curr = prev.right;
            }
        }
        return res;
    }
}
```

##### 3. Morris traversal

```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        TreeNode curr = root;
        while (curr != null) {
            if (curr.left != null) {
                TreeNode predecessor = curr.left;
                while (predecessor.right != null && predecessor.right != curr) {
                    predecessor = predecessor.right;
                }
                if (predecessor.right == null) {
                    predecessor.right = curr;
                    curr = curr.left;
                } else {
                    predecessor.right = null;
                    res.add(curr.val);       // Add curr.val only when we visit this 
                    curr = curr.right;       // node at second times.
                }
            } else {
                res.add(curr.val);       // At the left most leaf to res.
                curr = curr.right;
            }
        }
        return res;
    }
}
```

T: O(n)			S: O(1)

---

#### Postorder Traversal

##### 1. Recursion

```java
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        postorderHelper(root, res);
        return res;
    }
    private void postorderHelper(TreeNode node, List<Integer> list) {
        if (node == null) return;
        postorderHelper(node.left, list);
        postorderHelper(node.right, list);
        list.add(node.val);
    }
}
```

##### 2. Iteration

The reverse of preorder traversal.

```java
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode n = stack.pop();
            res.add(n.val);
            if (n.left != null) stack.push(n.left);
            if (n.right != null) stack.push(n.right);
        }
        Collections.reverse(res);   // reverse!!!
        return res;
    }
}
```

##### 3. Node traversal

The reverse of preorder traversal.

```java
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            if (curr != null) {
                res.add(curr.val);
                stack.push(curr);
                curr = curr.right;
            } else {
                TreeNode prev = stack.pop();
                curr = prev.left;
            }
        }
        Collections.reverse(res);    // reverse!!!
        return res;
    }
}
```

##### 4. Iterative with result

```java
public int countUnivalSubtrees(TreeNode root) {
        if (root == null) return 0;
        Map<TreeNode, Integer> map = new HashMap<>();
        map.put(null, 0);                              // store null for true as result
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;                          // point to root
        int cnt = 0;
        while (curr != null || !stack.isEmpty()) {
            if (!map.containsKey(curr)) {
                stack.push(curr);
                curr = curr.left;
            } else {
                TreeNode n = stack.peek();
                if (!map.containsKey(n.right)) {
                    curr = n.right;                  // point to right node
                } else {
                    curr = stack.pop();
                    int sum = map.get(curr.left + curr.right);
                  	map.put(curr, sum);              // store result
                    curr = null;                     // clear curr = null
                }																		 // so that we can jump up back
            }
        }
        return cnt;
    }
```

##### 5. Morris traversal

```java
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        TreeNode curr = root;
        while (curr != null) {
            if (curr.right != null) {
                TreeNode predecessor = curr.right;
                while (predecessor.left != null && predecessor.left != curr) {
                    predecessor = predecessor.left;
                }
                if (predecessor.left == null) {
                    predecessor.left = curr;
                    res.add(0, curr.val);
                    curr = curr.right;
                } else {
                    predecessor.left = null;
                    curr = curr.left;
                }
            } else {
                res.add(0, curr.val);
                curr = curr.left;
            }
        }
        return res;
    }
}
```

T: O(n) 			S: O(1)

---

#### Levelorder Traversal

##### 1. Recursion

```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        levelorderHelper(res, root, 0);
        return res;
    }
    public void levelorderHelper(List<List<Integer>> result, TreeNode node, int height) {
        if (node == null) return;
        if (height == result.size()) {
            result.add(new ArrayList<Integer>());
        }
        result.get(height).add(node.val);
        levelorderHelper(result, node.left, height + 1);
        levelorderHelper(result, node.right, height + 1);
    }
}
```

##### 2. Iteration

```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            res.add(new ArrayList<Integer>());
            int level = res.size() - 1;
            while (size-- != 0) {
                TreeNode n = queue.poll();
                res.get(level).add(n.val);
                if (n.left != null) queue.offer(n.left);
                if (n.right != null) queue.offer(n.right);
            }
        }
        return res;
    }
}
```

---

#### Zigzag Traversal

**1.  One deque**

Use size to control level traversal with a deque.

When `leftToRight`, we `removeFirst` node from deque, and `addLast` node to deque.

When `rightToLeft`, we `removeLast` node from deque, and `addFirst` node to deque.

```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> deque = new LinkedList<>();
        deque.add(root);
        boolean leftToRight = true;
        while (!deque.isEmpty()) {
            int size = deque.size();
            List<Integer> list = new ArrayList<>();
            while (size-- != 0) {
                if (leftToRight) {
                    TreeNode node = deque.pollFirst();
                    list.add(node.val);
                    if (node.left != null) deque.addLast(node.left);
                    if (node.right != null) deque.addLast(node.right);
                } else {
                    TreeNode node = deque.pollLast();
                    list.add(node.val);
                    if (node.right != null) deque.addFirst(node.right);
                    if (node.left != null) deque.addFirst(node.left);
                }
            }
            leftToRight = !leftToRight;
            res.add(list);
        }
        return res;
    }
}
```

T: O(n)		S:  O(n)

**2. Recursion**

```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        zigzag(root, 0, res);
        return res;
    }
    
    private void zigzag(TreeNode node, int level, List<List<Integer>> res) {
        if (node == null) return;
        if (res.size() <= level) {
            List<Integer> newList = new ArrayList<>();
            res.add(newList);
        }
        List<Integer> list = res.get(level);
        if (level % 2 == 0) {
            list.add(node.val);
        } else {
            list.add(0, node.val);
        }
        zigzag(node.left, level + 1, res);
        zigzag(node.right, level + 1, res);
    }
}
```

T: O(n)		S: O(n)

---

#### Vertical Traversal

Given a binary tree, return the *vertical order* traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from **left to right**.

Use `col` to get the corresponding list.

```java
class Solution {
    int min, max;
    
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        min = 0; max = 0;
        findBorder(root, 0);
       
        for (int i = 0; i < max - min + 1; i++) {
            res.add(new ArrayList<>());
        }
        Queue<TreeNode> q = new LinkedList<>();
        Queue<Integer> cols = new LinkedList<>();
        q.add(root);
        cols.add(0);
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            int col = cols.poll();
            res.get(col - min).add(node.val);  // find corresponding list
            if (node.left != null) {
                q.add(node.left);
                cols.add(col - 1);
            }
            if (node.right != null) {
                q.add(node.right);
                cols.add(col + 1);
            }
        }
        return res;
    }
    
    private void findBorder(TreeNode root, int col) {
        if (root == null) return;
        min = Math.min(min, col);
        max = Math.max(max, col);
        findBorder(root.left, col - 1);
        findBorder(root.right, col + 1);
    }
}
```

T: O(n)		S:  O(n)