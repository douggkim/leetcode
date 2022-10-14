# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: 
            return -1 
        return abs(self.checkheight(root.left)-self.checkheight(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right) 
    def checkheight(self, root: Optional[TreeNode]) -> int: 
        if root is None: 
            return -1 
        return 1+max(self.checkheight(root.left),self.checkheight(root.right))

         
            
            
        
        
        