# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root: 
            return True 
        return abs(self.checkheight(root.left)-self.checkheight(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    def checkheight(self, node):
            if not node: 
                return -1 
            return 1+max(self.checkheight(node.left), self.checkheight(node.right))
         
            
            
        
        
        