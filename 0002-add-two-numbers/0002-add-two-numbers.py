# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Set cursors 
        l1_curr = l1
        l2_curr = l2
        
        # define a return node 
        return_n = ListNode() 
        return_start = return_n
        
        # define a number to contain digits of ten from result 
        pass_num = 0 
        
        
        
        while l1_curr != None and l2_curr != None: 
            #add the two digits 
            result_num = l1_curr.val + l2_curr.val
            result_num += pass_num 
            
            return_n.val = result_num%10
            pass_num = result_num//10
            
            # move to next 
            l1_curr = l1_curr.next 
            l2_curr = l2_curr.next
            if l1_curr != None or l2_curr != None: 
                return_n.next  = ListNode()
                return_n = return_n.next
            
            
        while l1_curr != None: 
            result_num = l1_curr.val + pass_num 
            
            return_n.val = result_num%10 
            pass_num = result_num//10 
            
            # move to next 
            l1_curr = l1_curr.next 
            if l1_curr != None: 
                return_n.next  = ListNode()
                return_n = return_n.next
            
        while l2_curr != None: 
            result_num = l2_curr.val + pass_num 
             
            return_n.val = result_num%10 
            pass_num = result_num//10 
            
            # move to next 
            l2_curr = l2_curr.next 
            if l2_curr != None: 
                return_n.next  = ListNode()
                return_n = return_n.next
            
    
        if pass_num != 0: 
            return_n.next = ListNode() 
            return_n = return_n.next 
            return_n.val = pass_num
        
        return return_start
            
        