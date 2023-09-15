class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_len = len(words)
        i = 0
        counter = 0  
        tmp_l = []  
        result_l = [] 
        
        while i < words_len: 
            counter += len(words[i])
            tmp_l.append(words[i])
            if i == words_len-1:
                pad_num = maxWidth - counter - (len(tmp_l)-1)
                input_word = " ".join(tmp_l)
                input_word = input_word + " "*pad_num
                result_l.append(input_word)
            
            elif counter+(len(tmp_l))+len(words[i+1]) > maxWidth: 
                pad_num = maxWidth - counter
                if len(tmp_l) == 1: 
                    input_word = tmp_l[0]+pad_num*" "
                else: 
                    pad_place_num = len(tmp_l)-1
                    padding_per_word = pad_num//pad_place_num
                    leftover_pad = pad_num - padding_per_word*pad_place_num
                    input_word = "" 
                    for order,word in enumerate(tmp_l): 
                        input_word = input_word + word 
                        if order != len(tmp_l)-1: 
                            input_word = input_word + " "*padding_per_word
                            if leftover_pad != 0: 
                                input_word = input_word + " "
                                leftover_pad -= 1 
                
                result_l.append(input_word)
                counter = 0 
                tmp_l = [] 
                
            i += 1 
            
        
        
        return result_l 


                    

        # if more than 2 
        # if 1 word 