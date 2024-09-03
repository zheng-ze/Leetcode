# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.mem = []
        self.length = 0
        def evaluate(node: Optional[TreeNode], level: int = 0):
            if not node:
                return
            
            if self.length <= level:
                self.mem.append([])
                self.length += 1
            
            self.mem[level].append(node.val)
            
            evaluate(node.left, level + 1)
            evaluate(node.right, level + 1)
        
        evaluate(root)
        return self.mem
            
            