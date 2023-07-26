class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = "" 
        
        for s in strs: 
            encoded_str += s.replace('/','//') + "/:"
        
        return encoded_str 

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_str = [] 
        
        decoded_word = "" 
        i = 0 
        
        while i < len(s): 
            if s[i:i+2] == '//': 
                decoded_word += '/'
                i += 2 
                
            elif s[i:i+2] == '/:': 
                decoded_str.append(decoded_word) 
                decoded_word = ""
                i += 2                 
                
            else: 
                decoded_word += s[i] 
                i += 1 
        
        return decoded_str
            
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))