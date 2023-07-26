class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = "" 
        
        for s in strs: 
            encoded += (s.replace("/", "//") +"/:") 
        
        return encoded 
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        tmp_word = "" 
        decoded_l = [] 
        i = 0 
        
        while i < len(s): 
            if s[i:i+2] == '/:':
                decoded_l.append(tmp_word) 
                tmp_word = "" 
                i += 2 
            elif s[i:i+2] == '//': 
                tmp_word += "/"
                i += 2 
            else: 
                tmp_word += s[i]
                i += 1
                
        return decoded_l 
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))