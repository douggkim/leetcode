# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None: 
            return 0 
        
        max_depth, curr_depth = self.searchDepth(root, 0, 0)
        
        return max_depth
     
    def searchDepth(self, node:TreeNode, maxDepth:int, currDepth:int) -> Tuple[int, int]: 
        maxDepth_l, currDepth_l, maxDepth_r, currDepth_r = 0,0,0,0 
        if node.left != None: 
            maxDepth_l, currDepth_l = self.searchDepth(node.left, maxDepth, currDepth+1)
        if node.right != None: 
            maxDepth_r, currDepth_r = self.searchDepth(node.right, maxDepth, currDepth+1)
        
        current_maxDepth = (currDepth_l-currDepth) + (currDepth_r - currDepth)
        tmp_maxDepth = max(maxDepth_l, maxDepth_r)
        tmp_maxDepth_2 = max(maxDepth, current_maxDepth)
        
        maxDepth = max(tmp_maxDepth, tmp_maxDepth_2)
        print(f"max {maxDepth}")
        tmp_currDepth = max(currDepth_l, currDepth_r)
        currDepth = max(currDepth, tmp_currDepth)
        print(f"curr {currDepth}")
        
        return maxDepth, currDepth 
        
    