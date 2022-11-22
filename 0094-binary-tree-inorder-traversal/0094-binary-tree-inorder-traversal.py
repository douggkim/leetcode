# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result_l = []
        def inorder(root, result_l):
            if root == None: 
                return result_l
            
            reesult_l = inorder(root.left,result_l)
            result_l.append(root.val) 
            result_l = inorder(root.right,result_l)
        
            return result_l
        
        return inorder(root,result_l)