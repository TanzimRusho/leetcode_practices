from typing import List 
import numpy as np

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        length = len(mat)
        
        for i in range(length):
            mat[i].sort()
            
        arr1 = np.array(mat)
        arr1_transpose = arr1.transpose()
        
        #print(arr1_transpose)
        
        length_ = len(arr1_transpose)
        
        for i in range(length_):
            if sum(arr1_transpose[i]) == target:
                return arr1_transpose

sn = Solution()
print(sn.minimizeTheDifference([[1,2,3],[4,5,6],[7,8,9]], 13))
