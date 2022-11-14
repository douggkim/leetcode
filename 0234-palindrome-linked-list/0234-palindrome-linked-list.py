# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # dict apporach -> no, cases like 1234123 
        # get a list -> split in the middle -> flip -> compare : n^2 
        # count -> even, odd -> cases -> pop stack 
        # Get the length 
        ptr = head 
        l = [head.val] 
        while ptr.next != None:
            ptr = ptr.next 
            l.append(ptr.val)
        
        if l == l[::-1]: 
            return True 
        else:
            return False
            
        
        
        
        
        # if even 
        # start popping at n//2 
        
        
        # if odd 
        # pop at n//2 
        # start popping 