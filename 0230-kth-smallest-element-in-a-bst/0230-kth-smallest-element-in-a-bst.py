# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        number_l = []
        def dfs(node): 
            
            if node.left: 
                dfs(node.left)
            number_l.append(node.val)
            if node.right: 
                dfs(node.right)
                
            
            
        
        dfs(root)
        number_l = number_l[::-1]
        target_loc = len(number_l) -k
        
        return number_l[target_loc]
        