class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l=0
        r=0
        u=0
        d=0
        
        for _ in moves: 
            if _=='L':
                l+=1
            elif _=='R':
                r+=1
            elif _=='U':
                u+=1
            elif _=='D':
                d+=1
        
        if l==r and u==d: 
            return True
        else:
            return False
        