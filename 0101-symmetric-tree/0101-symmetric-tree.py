# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(l, r):
            if not l and not r: 
                return True 
            if not l or not r: 
                return False 
            
            if l.val == r.val: 
                return dfs(l.left, r.right) and dfs(l.right, r.left)
            
            return False 
        
        return dfs(root.left, root.right)
                
        
        
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if root == None or (root.left==None and root.right == None): 
#             return True 
#         if root.left == None or root.right==None: 
#             return False 
        
#         l_curr = root.left 
#         r_curr = root.right 
        
#         def left_trav(head, track):
#             if head.left != None and head.left not in track: 
#                 track = left_trav(head.left, track) 
            
#             track.append(head.val)
            
#             if head.right != None and head.right not in track: 
#                 track = left_trav(head.right, track)
            
#             return track
        
#         def right_trav(head, track):
#             if head.right != None and head.right not in track: 
#                 track = right_trav(head.right, track)
            
#             track.append(head.val)
            
#             if head.left != None and head.left not in track: 
#                 track = right_trav(head.left, track) 
            
        
#             return track
    
#         l_track = left_trav(l_curr, [])
#         r_track = right_trav(r_curr, [])
        
#         print(l_track)
#         print(r_track)
        
#         if l_track == r_track: 
#             return True
#         else: 
#             return False 