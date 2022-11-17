# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A_set = set() 
        
        curr = headA 
        
        while curr: 
            A_set.add(curr)
            curr = curr.next
        
        curr = headB
        
        while curr: 
            if curr in A_set:
                return curr 
            else: 
                curr = curr.next
        