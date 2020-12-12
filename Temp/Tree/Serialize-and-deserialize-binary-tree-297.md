---
title: Hard | Serialize and Deserialize Binary Tree 297
tags:
  - tricky
categories:
  - Leetcode
  - Tree
date: 2019-12-24 19:41:06
---

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

[Leetcode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

<!--more-->

**Example:** 

```
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
```

**Clarification:** The above format is the same as [how LeetCode serializes a binary tree](https://leetcode.com/faq/#binary-tree). You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

**Note:** Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

---

#### Tricky 

Serialize a tree to a string, the key is to delimit each node with a delimiter.

---

#### My thoughts 

BFS: level order traversal.

Serialize tree level by level.

Deserialize: Using a stack to save one level's nodes, and for each node in a level, assign its left and right nodes.

---

#### First solution 

```java
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "";
        StringBuilder sb = new StringBuilder();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- != 0) {
                TreeNode t = queue.poll();
                if (t == null) {
                    sb.append("null" + ",");
                } else {
                    sb.append(t.val + ",");
                    queue.offer(t.left);
                    queue.offer(t.right);
                }
            }
        }
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.equals("")) return null;
        String[] nodes = data.split(",");
        Queue<TreeNode> queue = new LinkedList<>();
        int start = 0;
        TreeNode root = new TreeNode(Integer.parseInt(nodes[start++]));
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- != 0) {
                TreeNode tmp = queue.poll();
                if (tmp == null) continue;
                tmp.left = !nodes[start].equals("null") ? new TreeNode(Integer.parseInt(nodes[start])) : null;
                start++;
                queue.offer(tmp.left);
                tmp.right = !nodes[start].equals("null") ? new TreeNode(Integer.parseInt(nodes[start])) : null;
                start++;
                queue.offer(tmp.right);
            }
        }
        return root;
    }
}
```

T: O(n) S: O(n)

---

#### Preorder + recursion

Use preorder traversal to serialize tree with "," delimiter.

During recursion, we need to keep track of scan position of data string. We use `start[0]` to track it, because we could change `start[0]`'s value out of recursion.

```java
public class Codec {
    
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "null" + ",";
        return root.val + "," + serialize(root.left) + serialize(root.right);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        int[] index = new int[1]; // Initial index[0] is 0.
        return deserializeHelper(data.split(","), index);
    }
    
    private TreeNode deserializeHelper(String[] nodes, int[] index) {
        if (nodes[index[0]].equals("null")) {
            index[0]++; // Change value of index[0] even when we return null.
            return null;
        }
        TreeNode root = new TreeNode(Integer.parseInt(nodes[index[0]++]));
        root.left = deserializeHelper(nodes, start);
        root.right = deserializeHelper(nodes, start);
        return root;
    }
}
```

T: O(n) S: O(n)

---

#### Preorder + iteration 

Use a stack to track unfinished node during preorder.

```java
public class Codec {
    
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "null" + ",";
        StringBuilder sb = new StringBuilder();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode n = root;
        while (!stack.isEmpty() || n != null) {
            if (n != null) {
                stack.push(n);
                sb.append(n.val + ",");
                n = n.left;
            } else {
                sb.append("null" + ",");
                TreeNode tmp = stack.pop();
                n = tmp.right;
            }
        }
        sb.append("null" + ",");  // Append the right null of last child.
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] nodes = data.split(",");
        if (nodes[0].equals("null")) return null;
        Stack<TreeNode> stack = new Stack<>();
        int start = 0;
        TreeNode root = new TreeNode(Integer.parseInt(nodes[start++]));
        TreeNode n = root;
        while (!stack.isEmpty() || n != null) {
            if (n != null) {
                if (nodes[start].equals("null")) {
                    n.left = null;
                } else {
                    n.left = new TreeNode(Integer.parseInt(nodes[start]));
                }
                stack.push(n); // push unfinished node into stack.
                start++;      // Scan next node.
                n = n.left;
            } else {
                TreeNode tmp = stack.pop();
                if (nodes[start].equals("null")) {
                    tmp.right = null;
                } else {
                    tmp.right = new TreeNode(Integer.parseInt(nodes[start]));
                }
                start++;
                n = tmp.right;
            }
        } 
        return root;
    }
}
```

T: O(n) S: O(n)

---

#### Summary 

The key to serialize and deserialize tree into a string is to use a delimiter to delimit nodes.