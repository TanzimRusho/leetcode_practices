from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0 
        
        # length = len(operations)
        
        for elem in operations:
            if "--" in elem:
                x -= 1 
            else:
                x += 1 
        
        return x 
        
        
s = Solution()
print(s.finalValueAfterOperations(["--X","X++","X++"]))
