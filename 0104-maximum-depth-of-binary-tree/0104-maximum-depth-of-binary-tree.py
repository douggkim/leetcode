# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: 
            return 0
        curr = root 
        l_result = 0 
        r_result = 0
        
        if curr.left == None and curr.right==None: 
            return 1
        else: 
            if curr.left : 
                l_result = self.maxDepth(curr.left)+1
            
            if curr.right : 
                r_result = self.maxDepth(curr.right)+1
        
        final = max(l_result, r_result)
        
        return final
        