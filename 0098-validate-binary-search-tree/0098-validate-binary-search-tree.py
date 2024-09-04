# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, floor = -float('inf'), ceiling = float('inf')):
            if not node:
                return True
            
            if node.val <= floor or node.val >= ceiling:
                return False
            
            if not isValid(node.left, floor, node.val):
                return False
            
            if not isValid(node.right, node.val, ceiling):
                return False
            
            return True
        
        return isValid(root)