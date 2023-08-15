# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: 
            return [] 
        
        next_l = deque([root])
        result_l = [] 
        
        while next_l: 
            curr = next_l 
            next_l = deque() 
            
            while curr: 
                node = curr.popleft() 
                
                if node.left:
                    next_l.append(node.left)
                if node.right: 
                    next_l.append(node.right)
            result_l.append(node.val)
        
        return result_l