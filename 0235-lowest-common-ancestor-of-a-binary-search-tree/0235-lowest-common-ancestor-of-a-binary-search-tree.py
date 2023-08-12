# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l,r, result = self.search(root, p, q)
        return result 
    
    def search(self, node, p, q): 
        l,r, result = False, False, None 
        l_l, l_r, l_result = False, False, None 
        r_l, r_r, r_result = False, False, None 
        
        if node == p: 
            l = True 
        elif node == q: 
            r = True 
        
        if node.left != None: 
            l_l, l_r, l_result = self.search(node.left, p, q)
            # print(l_l, l_r,l_result)
        
        if node.right != None: 
            # print(node.right)
            r_l, r_r, r_result = self.search(node.right, p, q)
            # print(r_l, r_r, r_result)
        
        if l_result != None: 
            result = l_result 
        elif r_result != None: 
            result = r_result 
        
        
        
        l = l or l_l or r_l 
        r = r or l_r or r_r 
        
        if result!= None: 
            return l, r, result 
        
        if l and r: 
            result = node 
        
        
        return l, r, result 
        
    