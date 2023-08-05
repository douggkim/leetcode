# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None: 
            return True
        elif root == None or subRoot == None: 
            return False
        
        return self.searchRoot(root, subRoot)
        
    def searchRoot(self, node:TreeNode, subRoot:TreeNode) -> bool: 
        result = False
        if node.val == subRoot.val: 
            result = self.compareTree(node, subRoot)
        result_l, result_r = False, False
        if node.left != None: 
            result_l = self.searchRoot(node.left, subRoot)
        if node.right != None: 
            result_r = self.searchRoot(node.right, subRoot)
        
        return result_l or result_r or result
    
    def compareTree(self, origin:TreeNode, compare:TreeNode) -> bool: 
        if origin.val != compare.val: 
            return False 
        left_r, right_r = False, False 
        
        if origin.left == None and compare.left == None: 
            left_r = True 
        elif origin.left == None or compare.left == None: 
            left_r = False 
        else: 
            left_r = self.compareTree(origin.left, compare.left)
        
        if origin.right == None and compare.right == None: 
            right_r = True 
        elif origin.right == None or compare.right == None: 
            right_r = False 
        else: 
            right_r = self.compareTree(origin.right, compare.right)
        
        return left_r and right_r