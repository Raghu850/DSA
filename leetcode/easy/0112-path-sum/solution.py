# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def find(node, hap):
            if not node:
                return False
            if not node.left and not node.right:
                return hap + node.val == targetSum

            if find(node.left, hap + node.val):
                return True
                
            if find(node.right, hap + node.val):
                return True

            return False
        return find(root, 0)