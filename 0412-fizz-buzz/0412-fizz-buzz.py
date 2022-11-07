class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #         check_l 
        check_l =[0]*10000
        if check_l[n]!=0: 
            return check_l[1:n+1]
        
        for i in range(1,n+1):
            if i % 15 == 0: 
                check_l[i] = 'FizzBuzz'
            elif i%3 ==0: 
                check_l[i] = 'Fizz'
            elif i%5 == 0 : 
                check_l[i] = 'Buzz'
            else: 
                check_l[i] = str(i)
                
        return check_l[1:n+1]
            
            

#  check conditions 
#  add to check_l 
        
        