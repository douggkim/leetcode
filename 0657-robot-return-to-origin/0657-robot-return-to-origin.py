class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l = 0
        r = 0
        u = 0
        d = 0 
        for i in moves: 
            if i == 'L': 
                l +=1 
            elif i=='R':
                r +=1
            elif i=='U':
                u +=1
            elif i=='D': 
                d +=1
        if d==u and l==r: 
            return True 
        else:
            return False 
        