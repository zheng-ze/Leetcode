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
        def evaluate(mem: List[List[int]], node: Optional[TreeNode], level: int = 0):
            if not node:
                return
            
            while len(mem) <= level:
                mem.append([])
            
            mem[level].append(node.val)
            
            evaluate(mem, node.left, level + 1)
            evaluate(mem, node.right, level + 1)
        out = []
        evaluate(out, root)
        return out
            
            