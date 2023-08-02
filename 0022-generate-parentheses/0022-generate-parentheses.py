class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        current_list = []     
        def parenthesis_helper( n:int, left:int, right:int, current_str:str) -> None: 
            if left == right and left + right == n*2: 
                current_list.append(current_str)
            else: 
                if left < n: 
                    parenthesis_helper(n=n, left=left+1, right=right, current_str= current_str+"(")
                if right < left: 
                    parenthesis_helper(n=n, left=left, right=right+1, current_str= current_str+")")
        
        parenthesis_helper(n,left=1,right=0,current_str="(")

        return current_list
            
        
        
        