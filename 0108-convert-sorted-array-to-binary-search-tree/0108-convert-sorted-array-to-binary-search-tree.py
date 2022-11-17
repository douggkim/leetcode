# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # check if new list is null 
        # form tree 
        # get the middle 
        def add_bin(num_l:List[int]) -> Optional[TreeNode]: 
            if len(num_l)==0: 
                return 
            mid = len(num_l)//2 
            start=TreeNode(num_l[mid])
            start.left = add_bin(num_l[:mid])
            start.right = add_bin(num_l[mid+1:])
            
            return start
        
        start = add_bin(nums)
        return start
        
            
            
                
            
        # lower = mid -1 
        # higher = len(nums)
        # while lower <= 0 
        # if curr < nums[lower]  add to left 
        # curr = curr.left 
        # elif curr > nums[lower] add to right 
        # curr = curr.right 
        
        # while higher < mid
        
        