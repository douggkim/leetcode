class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val): 
            if node == None: 
                return True
            
            if not (min_val < node.val < max_val): 
                return False
            
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
            
            
        return dfs(root, -math.inf, math.inf) 
        