# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle_set = set() 
        curr = head 
        
        while curr: 
            if curr not in cycle_set: 
                cycle_set.add(curr)
            else: 
                return True
            curr = curr.next 
        
        return False