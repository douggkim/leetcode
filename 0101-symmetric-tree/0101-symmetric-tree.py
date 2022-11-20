# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(l, r): 
            if not l and not r: 
                return True 
            if not l or not r: 
                return False 
            
            if l.val == r.val: 
                return dfs(l.left, r.right) and dfs(l.right, r.left)
                
            else: 
                return False 
        
        return dfs(root.left, root.right)
                