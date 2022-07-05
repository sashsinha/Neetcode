# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.get_height(root)