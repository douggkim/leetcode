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
        ctr = 1 
        while ptr.next != None: 
            ptr = ptr.next 
            ctr += 1 
        
        ptr = head 
        new_ctr = 1 
        st = [] 
        
        if ctr % 2 ==0 : 
            while ptr != None : 
                if new_ctr >= (ctr//2+1): 
                    if ptr.val == st.pop():
                        ptr = ptr.next 
                        
                    else: 
                        return False
                else: 
                    st.append(ptr.val)
                    ptr = ptr.next 
                    new_ctr += 1
        
        else : 
            while ptr != None: 
                if new_ctr == (ctr//2 +1):
                    ptr = ptr.next
                    new_ctr += 1 
                elif new_ctr > (ctr//2 + 1): 
                    if ptr.val == st.pop():
                        ptr = ptr.next 
                        
                    else: 
                        return False 
                else:
                    st.append(ptr.val)
                    ptr = ptr.next
                    new_ctr += 1
        
        if len(st) == 0: 
            return True
        else: 
            return False
        
        
        # if even 
        # start popping at n//2 
        
        
        # if odd 
        # pop at n//2 
        # start popping 