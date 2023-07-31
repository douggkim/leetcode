class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = "" 
        
        for s in strs: 
            for i in range(len(s)): 
                if s[i] == '/': 
                    encoded+='//'
                else: 
                    encoded+=s[i]
            encoded += '/:'
        
        return encoded 

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result_l = []
        tmp_word = "" 
        i = 0 
        
        while i < len(s): 
            if s[i:i+2] == '//': 
                tmp_word += '/'
                i += 2 
            elif s[i:i+2] == '/:': 
                result_l.append(tmp_word)
                i += 2 
                tmp_word = "" 
            else: 
                tmp_word += s[i]
                i += 1 
        
        return result_l
            
            
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))