# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_list = []
        pointer = head
        while pointer is not None: 
            node_list.append(pointer)
            pointer = pointer.next 
        if len(node_list) <=1: 
            node_list.append(head)
            return None
        print(node_list)
        print(node_list[len(node_list)-n-1])
        if node_list[len(node_list)-n-1].next: 
            node_list[len(node_list)-n-1].next = node_list[len(node_list)-n-1].next.next 
        elif node_list[len(node_list)-n-1] == node_list[len(node_list)-1]:
            head = head.next
        else:
            return None 
        return head 