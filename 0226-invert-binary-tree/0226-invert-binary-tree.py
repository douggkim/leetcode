# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: 
            return None
        copy_root = TreeNode(val=root.val)
        copy_root = self.traverseInvert(root, copy_root)
        return copy_root
    
    def traverseInvert(self, origin:TreeNode, copy:TreeNode): 
        if origin.left != None: 
            copy.right = TreeNode(val=origin.left.val)
            copy.right = self.traverseInvert(origin.left, copy.right)
        
        if origin.right != None: 
            copy.left = TreeNode(val=origin.right.val)
            copy.left = self.traverseInvert(origin.right, copy.left)
            
        
        return copy
        