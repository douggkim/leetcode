# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_carry = "" 
        tmp_l1 = l1 
        
        while tmp_l1 != None: 
            l1_carry += str(tmp_l1.val)
            tmp_l1 = tmp_l1.next 
        
        l1_reverse = l1_carry[::-1]
        l1_carry_int = int(l1_reverse)
        
        l2_carry = "" 
        tmp_l2 = l2
        
        while tmp_l2 != None: 
            l2_carry += str(tmp_l2.val)
            tmp_l2 = tmp_l2.next 
        
        l2_reverse = l2_carry[::-1]
        l2_carry_int = int(l2_reverse)
        
        result = l1_carry_int + l2_carry_int 
        result_str = str(result)
        result_l = [c for c in result_str]
        result_l = result_l[::-1]
        
        head = ListNode(int(result_l[0])) 
        result_tmp = head 
        
        for i in range(1, len(result_l)): 
            result_tmp.next = ListNode(int(result_l[i]))
            result_tmp = result_tmp.next
        
        return head 
        
            