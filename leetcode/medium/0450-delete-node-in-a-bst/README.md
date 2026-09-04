# Delete Node in a BST

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return  *the  **root node reference**  (possibly updated) of the BST*.

Basically, the deletion can be divided into two stages:

- Search for a node to remove.
- If the node is found, delete the node.

 

 **Example 1:** 

```
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

```

 **Example 2:** 

```
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

```

 **Example 3:** 

```
Input: root = [], key = 0
Output: []

```

 

 **Constraints:** 

- The number of nodes in the tree is in the range [0, 104].
- -105 <= Node.val <= 105
- Each node has a unique value.
- root is a valid binary search tree.
- -105 <= key <= 105

 

 **Follow up:**  Could you solve it with time complexity `O(height of tree)`?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 22.1 MB (beats 17.87%)  
**Submitted:** 2026-09-04T18:14:48.490Z  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None 
        if root.val == key:
            return self.helper(root)
        
        dummy = root
        while root is not None:
            if root.val > key:
                if root.left is not None and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right is not None and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
        return dummy
    
    def helper(self, root):
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        rightChild = root.right
        lastRight = self.flr(root.left)  # rightmost node in left subtree
        lastRight.right = rightChild
        return root.left
    
    def flr(self, root):
        if root.right is None:
            return root
        return self.flr(root.right)
```

---

[View on LeetCode](https://leetcode.com/problems/delete-node-in-a-bst/)