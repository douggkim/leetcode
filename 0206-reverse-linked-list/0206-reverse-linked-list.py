# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_l = [] 
        if head == None: 
            return None
        ptr = head 
        # append head 
        node_l.append(ptr)
        
        # move to the end of head 
        while ptr.next != None: 
            ptr = ptr.next
            node_l.append(ptr)
        
        head = ptr
        
        while len(node_l) != 0: 
            ptr.next = node_l.pop()
            ptr = ptr.next
        
        ptr.next = None 
        return head 