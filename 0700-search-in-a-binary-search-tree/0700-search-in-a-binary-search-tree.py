# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        result = None 
        if root.val == val: 
            result = root 
        else: 
            if val < root.val: 
                if root.left: 
                    result = self.searchBST(root.left, val)
                else: 
                    result = None 

            else: 
                if root.right: 
                    result = self.searchBST(root.right, val)
                else: 
                    result = None 
        return result 
