# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None: 
            return TreeNode(val)
        else: 
            if val > root.val: 
                if root.right == None: 
                    root.right = TreeNode(val)
                    return root 
                else: 
                    self.searchInsert(root.right, val)
            
            else: 
                if root.left == None: 
                    root.left = TreeNode(val)
                    return root 
                else: 
                    self.searchInsert(root.left, val)
        return root 
    
    
    
    def searchInsert(self, node:TreeNode, val:int): 
        if val > node.val: 
            if node.right == None: 
                node.right = TreeNode(val)
            else: 
                self.searchInsert(node.right, val)
        
        else: 
            if node.left == None: 
                node.left = TreeNode(val)
            else: 
                self.searchInsert(node.left, val)