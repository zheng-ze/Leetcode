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
        out = []
        q = deque([])
        q.append((root, 0))
        
        while q:
            node, level = q.popleft()
            
            if not node:
                continue
            
            try:
                out[level].append(node.val)
            except:
                out.append([node.val])
            
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        
        return out
            
            