# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None: 
            return [] 
        
        result_l = [[root.val]] 
        curr_node = deque([root])
        
        while curr_node: 
            next_node = curr_node
            curr_node = deque()
            tmp_l = [] 
            
            while len(next_node)>0: 
                node = next_node.popleft()
                
                if node.left != None: 
                    curr_node.append(node.left)
                    tmp_l.append(node.left.val)
                if node.right != None: 
                    curr_node.append(node.right)
                    tmp_l.append(node.right.val)
            if len(tmp_l) != 0: 
                result_l.append(tmp_l)
        
        return result_l
                    
                
            