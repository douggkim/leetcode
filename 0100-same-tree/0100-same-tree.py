# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None: 
            return True 
        elif p == None or q == None: 
            return False 
        else:
            return self.compareTree(p, q)
    
    def compareTree(self, p:TreeNode, q:TreeNode): 
        if p.val != q.val: 
            return False
        
        bool_l = False 
        bool_r = False 
        
        if p.left != None and q.left != None: 
            bool_l = self.compareTree(p.left, q.left)
        elif p.left != None or q.left != None: 
            return False
        else: 
            bool_l = True 
        
        if p.right != None and q.right != None: 
            bool_r = self.compareTree(p.right, q.right)
        elif p.right != None or q.right != None: 
            return False
        else: 
            bool_r = True
        
        return bool_l and bool_r 
            
            
        