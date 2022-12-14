# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(root):
            # Base case where root is None
            if not root:
                return True
            
            # Find subtree height: If -1, subtree is not balanced so tree is not balanced
            leftHeight = balanced(root.left)
            if leftHeight == -1:
                return -1
            
            rightHeight = balanced(root.right)
            if rightHeight == -1:
                return -1
            
            # If subtree are both height balanced, whether their heights are similar
            if abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1
        
        balanced = balanced(root)
        return balanced != -1