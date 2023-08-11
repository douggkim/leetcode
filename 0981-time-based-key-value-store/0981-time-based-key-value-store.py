class TimeMap:

    def __init__(self):
        self.record_dict = {} 
        self.index_dict = {} 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        new_key = key+ "_"+str(timestamp) 
        self.record_dict[new_key] = value 
        self.index_dict[key] = self.index_dict.get(key,[]) + [timestamp]
        
        

    def get(self, key: str, timestamp: int) -> str:
        new_key = key +"_"+str(timestamp) 
        if new_key in self.record_dict: 
            return self.record_dict[new_key]
        if key not in self.index_dict: 
            return "" 
        else: 
            search_l = self.index_dict[key]
            if timestamp < search_l[0]: 
                return ""
            
            l = 0 
            r = len(search_l)-1 
            
            while l <= r: 
                mid = l+(r-l)//2 
                if search_l[mid] < timestamp:
                    closest = search_l[mid]
                    l = mid+ 1 
                else: 
                    r = mid -1 
            return self.record_dict[key+"_"+str(closest)]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)