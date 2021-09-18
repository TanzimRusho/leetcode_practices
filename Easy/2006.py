from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        length = len(nums)
        count = 0
        
        for i in range(length):
            for j in range(i+1, length):
                if abs(nums[i] - nums[j]) == k:
                    count += 1 
                    
        return count 
        
s = Solution()
print(s.countKDifference([1,2,2,1], 1))
