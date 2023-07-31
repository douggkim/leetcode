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
        else: 
            cnt = self.countDepth(root, 1)
            return cnt
        
    def countDepth(self, origin:TreeNode, cnt:int) -> int: 
        cnt_l = 0 
        cnt_r = 0 
        
        if origin.left != None: 
            cnt_l = self.countDepth(origin.left, cnt+1)
        if origin.right != None: 
            cnt_r = self.countDepth(origin.right, cnt+1)
            
        higher_cnt = max(cnt_l, cnt_r)
        max_cnt = max(cnt, higher_cnt)
        
        return max_cnt
        
        