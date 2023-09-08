class Solution:
    @cache
    def countBits(self, n: int) -> List[int]:
        i = 0 
        result_l = []

        while i <= n:
            cnt = 0 
            tmp = i 
            while tmp >= 1:
                cnt += tmp % 2 
                tmp = tmp//2 
            i += 1 

            result_l.append(cnt)
        
        return result_l 