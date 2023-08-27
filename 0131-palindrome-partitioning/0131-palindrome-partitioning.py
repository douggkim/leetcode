class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result_l = [] 
        tmp = [] 
        n = len(s)
        
        def findPalindrome(start:int, tmp_l:List[str]): 
            if start >= n: 
                result_l.append(tmp_l[:])  # Make a copy of tmp_l
                return 
            
            for i in range(start, n): 


                l,r = i,i 
                while l >= start and r < n and s[l] == s[r]: 
                    if l == start: 
                        tmp_l.append(s[l:r+1])
                        findPalindrome(r+1, tmp_l=tmp_l)
                        tmp_l.pop()  # Remove the last element added
                    l -= 1 
                    r += 1 

                l, r = i, i+1 
                while l >= start and r < n and s[l] == s[r]: 
                    if l == start: 
                        tmp_l.append(s[l:r+1])
                        findPalindrome(r+1, tmp_l=tmp_l)
                        tmp_l.pop()  # Remove the last element added
                    l -= 1 
                    r += 1 

        findPalindrome(0, tmp)
        return result_l
