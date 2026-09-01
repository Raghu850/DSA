# Longest ZigZag Path in a Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given the `root` of a binary tree.

A ZigZag path for a binary tree is defined as follow:

- Choose any node in the binary tree and a direction (right or left).
- If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
- Change the direction from right to left or from left to right.
- Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return  *the longest  **ZigZag**  path contained in that tree*.

 

 **Example 1:** 

```
Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

```

 **Example 2:** 

```
Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

```

 **Example 3:** 

```
Input: root = [1]
Output: 0

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [1, 5 * 104].
- 1 <= Node.val <= 100

## Solution

**Language:** Python  
**Runtime:** 32 ms (beats 95.21%)  
**Memory:** 38.2 MB (beats 74.03%)  
**Submitted:** 2026-09-01T17:35:25.887Z  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftvalue =  self.longestfromcur(root.left,1,1) if root.left else 0
        rightvalue = self.longestfromcur(root.right,0,1) if root.right else 0
       
        return max(leftvalue,rightvalue)



    def longestfromcur(self,cur,handiness,depth):
        '''
        longest length from the cur node, when the current node takes the handiness action. there s already depth number consecutive 
        '''
        if (not cur.left) and (not cur.right):
            return depth
        if handiness ==0:
            leftvalue =depth
            rightvalue =depth
            if cur.left:
                leftvalue = self.longestfromcur(cur.left,1,depth+1)
            if cur.right :
                rightvalue =  self.longestfromcur(cur.right,0,1)
            return max(leftvalue,rightvalue)
        else:
        
            leftvalue =depth
            rightvalue =depth
            if cur.left:
                leftvalue = self.longestfromcur(cur.left,1,1)
            if cur.right :
                rightvalue = self.longestfromcur(cur.right,0,depth+1)
            return max(leftvalue,rightvalue)
```

---

[View on LeetCode](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/)