from typing import List 
import random

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)
        
        while True:
            key = self.generateRandom(length)
            if key in nums:
                continue
            else:
                return key
                
    def generateRandom(self, length):
        key = ""
        for i in range(length):
            temp = str(random.randint(0, 1))
            key += temp  
            
        return key

# Driver Code
sn = Solution()
print(sn.findDifferentBinaryString(["111","011","001"]))
