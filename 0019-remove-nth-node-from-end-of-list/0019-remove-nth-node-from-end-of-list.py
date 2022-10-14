# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_list = []
        pointer = head 
        
        while pointer: 
            node_list.append(pointer)
            pointer = pointer.next 
        
        if len(node_list) == 0 or len(node_list) == 1: 
            return None 
        elif node_list[len(node_list)-n]==head: 
            head=head.next
        elif node_list[len(node_list)-n]==node_list[len(node_list)-1]:
            node_list[len(node_list)-2].next= None 
        else: 
            node_list[len(node_list)-n-1].next = node_list[len(node_list)-n-1].next.next
        
        return head