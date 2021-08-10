from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        
        length = len(nums)
        
        break_ = False
        
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j) 
                    break_ = True
                    break
                
            if break_:
                break
                
        return res
        
# Driver codee
s = Solution()
print(s.twoSum([2,7,11,15],9))

        
