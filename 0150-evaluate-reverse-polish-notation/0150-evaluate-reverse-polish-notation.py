class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = [] 
        operator = set(["+","-","*","/"])
        
        for tok in tokens: 
            if tok in operator: 
                num2 = numStack.pop() 
                num1 = numStack.pop() 
                if tok == "+": 
                    tmpNum = num1+num2
                
                elif tok == "-": 
                    tmpNum = num1 - num2 

                elif tok == "*": 
                    tmpNum = num1 * num2 
                else: 
                    tmpNum = num1/num2
                    if tmpNum >= 0:
                        tmpNum = math.floor(tmpNum)
                    else:
                        tmpNum = math.ceil(tmpNum)
                numStack.append(tmpNum) 
            else: 
                numStack.append(int(tok))
        
        return numStack[0]