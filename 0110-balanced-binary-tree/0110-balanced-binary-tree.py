# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None: 
            return True
        depth, isBalanced = self.search(root,0,True)
        
        return isBalanced
    
    def search(self, node:TreeNode, depth:int, isBalanced:bool) -> tuple[int,bool]: 
        depth_l = depth 
        depth_r = depth 
        isBalanced_l = True 
        isBalanced_r = True 
        
        if node.left != None: 
            depth_l, isBalanced_l = self.search(node.left, depth+1, isBalanced)
        if node.right != None: 
            depth_r, isBalanced_r = self.search(node.right, depth+1, isBalanced)
            
        currDepth_l = depth_l - depth
        currDepth_r = depth_r - depth 
        
        if abs(currDepth_l - currDepth_r) > 1: 
            isBalanced = False
        
        isBalanced = isBalanced and isBalanced_r and isBalanced_l 
        
        tmp_depth = max(depth_l, depth_r)
        depth = max(tmp_depth, depth)
        
        return depth, isBalanced