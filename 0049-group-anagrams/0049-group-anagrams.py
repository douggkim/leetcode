class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for string in strs: 
            sort_str=''.join(sorted(string))
            if sort_str in dic: 
                dic[sort_str].append(string)
            else: 
                dic[sort_str] = [string]
        
        return list(dic.values()) 

             
                                
        