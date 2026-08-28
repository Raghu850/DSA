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
**Runtime:** 147 ms (beats 5.94%)  
**Memory:** 31.8 MB (beats 70.64%)  
**Submitted:** 2026-08-28T16:24:12.490Z  

```py
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # helper dfs returns count of good nodes from this node down
        def dfs(node, max_so_far):
            if not node:
                return 0  # base case: null node, 0 good nodes

            # is this node good?
            count = 1 if node.val >= max_so_far else 0

            # update max for children
            new_max = max(max_so_far, node.val)

            # count good nodes in left and right subtrees
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count

        return dfs(root, root.val)
```

---

[View on LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)