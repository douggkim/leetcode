# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val):
            if not node:
                return True  # An empty tree is a valid BST

            if not (min_val < node.val < max_val):
                return False  # Node's value is not within the valid range

            # Check left subtree with updated max_val
            # Check right subtree with updated min_val
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

        # Call the DFS function with initial min_val and max_val as negative and positive infinity
        return dfs(root, float('-inf'), float('inf'))
