# Count Good Nodes in Binary Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a binary tree `root`, a node  *X*  in the tree is named  **good**  if in the path from root to  *X*  there are no nodes with a value  *greater than*  X.

Return the number of  **good**  nodes in the binary tree.

 

 **Example 1:** 

```
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```

 **Example 2:** 

```
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
```

 **Example 3:** 

```
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
```

 

 **Constraints:** 

- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].

## Solution

**Language:** Python  
**Runtime:** 133 ms (beats 38.77%)  
**Memory:** 32 MB (beats 38.14%)  
**Submitted:** 2026-08-28T16:25:32.973Z  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if root is None:
            return 0
        self.count = 1
        

        def count_good(node, maximum_on_path):
            if not node:
                return
            if node.val >= maximum_on_path:
                self.count += 1
                maximum_on_path = node.val
            count_good(node.left, maximum_on_path)
            count_good(node.right, maximum_on_path)


        count_good(root.left, root.val)
        count_good(root.right, root.val)
        return self.count

        

        
        
```

---

[View on LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)