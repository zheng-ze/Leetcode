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
        def evaluate(node: Optional[TreeNode]) -> List[List[int]]:
            if not node:
                return []
            left, right = evaluate(node.left), evaluate(node.right)
            lenLeft, lenRight = len(left), len(right)
            
            out = [[] for i in range(max(lenLeft, lenRight) + 1)]
            
            for i in range(max(lenLeft, lenRight)):
                if i < lenLeft:
                    out[i + 1].extend(left[i])
                if i < lenRight:
                    out[i + 1].extend(right[i])
            out[0].append(node.val)
            
            return out
        
        return evaluate(root)
            
            