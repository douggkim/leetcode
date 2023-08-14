class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        current_l = [] 
        
        def helper(left:int, right:int, paren:str) : 
            if left==right and left+right == 2*n : 
                current_l.append(paren)
            
            if left < n: 
                helper(left+1, right, paren+"(")
            if right < left: 
                helper(left, right+1, paren+")")
        
        helper(1,0,"(")
        
        return current_l 
            
            
        
        
        