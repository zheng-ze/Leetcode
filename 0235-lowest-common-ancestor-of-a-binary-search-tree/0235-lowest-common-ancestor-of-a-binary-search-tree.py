# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        minimum = min(p.val, q.val)
        maximum = max(p.val, q.val)
        
        while root:
            if root.val < minimum:
                root = root.right
            elif root.val > maximum:
                root = root.left
            else:
                break
        
        return root 
