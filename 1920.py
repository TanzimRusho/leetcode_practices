from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
    

def main():
    nums = [0,2,1,5,3,4]
    
    solve = Solution()
    
    ans = solve.buildArray(nums)
    
    print(ans)

if __name__ == "__main__":
    main()
    
