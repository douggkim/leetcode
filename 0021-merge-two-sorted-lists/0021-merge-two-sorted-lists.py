# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge cases 
        if list1 == None and list2 == None: 
            return None 
        elif list1 == None and list2 != None: 
            return list2
        
        elif list1 != None and list2 == None: 
            return list1 
        
        # start with list 1 if smaller 
        if list1.val <= list2.val: 
            head = list1 
            curr_1 = list1.next 
            curr_2 = list2
            # head = head.next 
            # head.next = None 
        # start with list 2 if smaller 
        else: 
            head = list2 
            curr_2 = list2.next 
            curr_1 = list1
            # head = head.next 
            # head.next = None 
            print(head)
        
        start = head 
        
        
        while curr_1 != None and curr_2 != None: 
            if curr_1.val <= curr_2.val: 
                head.next = curr_1
                head = head.next 
                curr_1 = curr_1.next 
                
                # head.next = None
                
            else:
                head.next = curr_2 
                head = head.next 
                curr_2 = curr_2.next 

                # head.next = None 
            # print(head) 
            
        if curr_1 != None: 
            head.next = curr_1 
            head = head.next 
        if curr_2 != None: 
            head.next = curr_2 
            head = head.next 
        
        return start 
        
    
        
        
        
        