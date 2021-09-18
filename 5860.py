from typing import List
from collections import deque

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
    
        
        new_list = deque()

        sorted_changed = sorted(changed)
        
        length = len(sorted_changed)
        
        count = 0
        for i in range(length):
            if changed[i] == 0:
                count += 1 
                
        if count % 2 == 1:
            return []
        
        for i in range(len(sorted_changed)):
            try:
    
                if sorted_changed[0] * 2 in sorted_changed:
                    new_list.append(sorted_changed[0])
                    elem = sorted_changed[0]
                    #print(sorted_changed[0], sorted_changed[0]*2)
                    sorted_changed.remove(sorted_changed[0])
                    sorted_changed.remove(elem*2)
            except (IndexError, ValueError) as e:
                break 
                        
    
        if len(new_list) != length // 2: 
            return []    
                
        return list(new_list)
        

        
s = Solution()
print(s.findOriginalArray([1,2,3,4,6,2]))
