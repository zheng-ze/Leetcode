# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(root, arr, val):
            if not root:
                return False
            
            arr.append(root)
            
            if root == val:
                return True
            
            elif findPath(root.left, arr, val) or findPath(root.right, arr, val):
                return True
            
            arr.pop()
            return False
                
        #find path from root to p
        path_p = []
        findPath(root, path_p, p)
        #find path from root to q
        path_q = []
        findPath(root, path_q, q)
        
        #find common node in paths and return lowest
        return [element for element in path_p if element in path_q][-1]
