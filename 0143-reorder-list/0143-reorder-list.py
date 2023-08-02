# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            pass
        else: 
            # Create a list of nodes 
            node_l = [] 
            curr = head 

            while curr != None:
                node_l.append(curr)
                curr = curr.next

            left = 0 
            right = len(node_l)-1 

            tmp = head 
            # create a new ordering 
            while left <= right:
                if left == right: 
                    tmp.next = node_l[left]
                    tmp = tmp.next
                    left += 1 
                    right -= 1 
                    
                elif left == 0: 
                    tmp.next = node_l[right]
                    tmp = tmp.next 
                    left += 1 
                    right -= 1 
                else: 
                    tmp.next = node_l[left]
                    tmp = tmp.next 
                    tmp.next = node_l[right]
                    tmp = tmp.next 
                    left += 1
                    right -= 1
            tmp.next = None 
                    
