# Path Sum III

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `root` of a binary tree and an integer `targetSum`, return  *the number of paths where the sum of the values along the path equals*  `targetSum`.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

 **Example 1:** 

```
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

```

 **Example 2:** 

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 1000].
- -109 <= Node.val <= 109
- -1000 <= targetSum <= 1000

## Solution

**Language:** Python  
**Runtime:** 423 ms (beats 21.14%)  
**Memory:** 19.6 MB (beats 99.74%)  
**Submitted:** 2026-08-31T13:46:30.834Z  

```py
class Solution:

    def pathSum(self, root, targetSum):

        self.ans = 0

        # Counts all valid paths starting from the current node.
        def dfs(node, cur):

            if not node:
                return

            cur += node.val

            if cur == targetSum:
                self.ans += 1

            dfs(node.left, cur)
            dfs(node.right, cur)

        if not root:
            return 0

        stack = [root]

        # Every node becomes a starting point.
        while stack:

            node = stack.pop()

            dfs(node, 0)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return self.ans
```

---

[View on LeetCode](https://leetcode.com/problems/path-sum-iii/)