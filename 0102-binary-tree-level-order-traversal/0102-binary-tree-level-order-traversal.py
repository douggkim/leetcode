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
        
        traversal_l = [] 
        traversal_l.append([root.val])
        
        def searchTree( node: TreeNode, depth:int): 
            if node.left != None: 
                if depth+1 > len(traversal_l)-1:
                    traversal_l.append([node.left.val])
                else: 
                    traversal_l[depth+1].append(node.left.val)
                searchTree(node.left, depth+1)
            if node.right != None: 
                if depth+1 > len(traversal_l) -1 : 
                    traversal_l.append([node.right.val])
                else: 
                    traversal_l[depth+1].append(node.right.val)
                searchTree(node.right, depth+1)
        
        searchTree(root, 0)
        
        return traversal_l
        